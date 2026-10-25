"""Read-only fund research: FinanceToolkit for US funds, AKShare for China."""
import argparse
from datetime import date, datetime, timezone
from importlib import import_module, metadata
import json
import os
from pathlib import Path
import re
import sys


def iso_date(value):
    try:
        return date.fromisoformat(value).isoformat()
    except ValueError as exc:
        raise argparse.ArgumentTypeError("Use YYYY-MM-DD") from exc


def save_frame(frame, output, source, identifier):
    if frame is None or frame.empty or frame.dropna(how="all").empty:
        raise ValueError("Provider returned no usable data; no output written")
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(output, encoding="utf-8-sig")
    info = {"source": source, "identifier": identifier,
            "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
            "rows": len(frame), "columns": [str(c) for c in frame.columns],
            "versions": {p: metadata.version(p) for p in ("financetoolkit", "akshare")},
            "note": "Historical observations, not a recommendation or expected return."}
    output.with_suffix(output.suffix + ".metadata.json").write_text(
        json.dumps(info, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved {len(frame)} rows to {output}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("doctor", help="Check imports and dependency versions; no data requests")
    us = commands.add_parser("us-history", help="Download one US fund's daily history")
    us.add_argument("ticker")
    us.add_argument("--start", type=iso_date, required=True)
    us.add_argument("--end", type=iso_date, default=date.today().isoformat())
    us.add_argument("--source", choices=["YahooFinance", "FinancialModelingPrep"], default="YahooFinance")
    us.add_argument("--output", default="output/us-history.csv")
    cn = commands.add_parser("cn-history", help="Download one Chinese open-end fund's NAV")
    cn.add_argument("code")
    cn.add_argument("--output", default="output/cn-history.csv")
    args = parser.parse_args(argv)
    if args.command == "doctor":
        for package in ("financetoolkit", "akshare"):
            import_module(package)
            print(f"{package} {metadata.version(package)}: import OK")
        print("FMP_API_KEY: " + ("configured" if os.getenv("FMP_API_KEY") else "not configured (Yahoo history remains available)"))
        return 0
    if args.command == "us-history":
        if args.start >= args.end:
            parser.error("--start must be earlier than --end")
        ticker = args.ticker.upper()
        if not re.fullmatch(r"[A-Z0-9][A-Z0-9.^=\-]{0,19}", ticker):
            parser.error("Invalid ticker")
        key = os.getenv("FMP_API_KEY", "")
        if args.source == "FinancialModelingPrep" and not key:
            parser.error("Set FMP_API_KEY in your environment for the FMP source")
        from financetoolkit import Toolkit
        toolkit = Toolkit([ticker], api_key=key if args.source == "FinancialModelingPrep" else "",
                          start_date=args.start, end_date=args.end, benchmark_ticker=None,
                          enforce_source=args.source, use_cached_data=False, progress_bar=False)
        frame = toolkit.get_historical_data(fill_nan=False)
        save_frame(frame, args.output, f"FinanceToolkit/{args.source}", ticker)
    else:
        if not re.fullmatch(r"\d{6}", args.code):
            parser.error("Chinese fund code must contain exactly six digits")
        import akshare as ak
        frame = ak.fund_open_fund_info_em(symbol=args.code, indicator="单位净值走势")
        save_frame(frame, args.output, "AKShare/Eastmoney unit NAV", args.code)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ImportError, ValueError, OSError) as exc:
        # Avoid echoing request URLs or exception bodies that can contain API keys.
        print(f"Research command failed ({type(exc).__name__}). Check dependencies, source access and input.", file=sys.stderr)
        sys.exit(1)
