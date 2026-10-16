#!/usr/bin/env python3
"""SKU 定价算术脚本 —— 只算，不猜，不定价（定价决策由人）。

  python sku_pricing.py calc --cost 935 --price 2199 --commission 14 --return 2 \
      --ad 5 --tax 0 --target-margin 32
  python sku_pricing.py matrix --file examples/sample-skus.csv --commission 14 \
      --return 2 --ad 5 --tax 0 --target-margin 32

公式（含巴西税费项）：
  广告前毛利 = 售价 − 到岸成本 − 售价×佣金% − 售价×退货损耗% − 售价×税率%
  净利率     = (广告前毛利 − 售价×广告%) ÷ 售价
  盈亏平衡价 = 到岸成本 ÷ (1 − 佣金% − 退货% − 税率%)          ← 毛利=0
  目标价     = 到岸成本 ÷ (1 − 佣金% − 退货% − 广告% − 目标毛利%)  ← 反算
  优惠券余量 = 售价 × (实际净利率 − 目标毛利%)                 ← 发多少券不破目标
"""
import argparse
import csv
import json
import sys

PARAM_KEYS = {"commission", "return_rate", "ad", "tax", "target_margin"}


def margins(price, cost, comm, ret, ad, tax):
    pre = price - cost - price * comm / 100 - price * ret / 100 - price * tax / 100
    net = pre - price * ad / 100
    return dict(pre_ad_margin=round(pre, 2),
                pre_ad_rate=round(pre / price, 4) if price else 0,
                net_margin=round(net, 2),
                net_rate=round(net / price, 4) if price else 0)


def cmd_calc(args):
    p = dict(comm=args.commission / 100, ret=args.return_rate / 100,
             ad=args.ad / 100, tax=args.tax / 100, tm=args.target_margin / 100)
    m = margins(args.price, args.cost, args.commission, args.return_rate, args.ad, args.tax)
    denom_be = 1 - p["comm"] - p["ret"] - p["tax"]
    denom_tg = denom_be - p["ad"] - p["tm"]
    out = dict(mode="calc", price=args.price, cost=args.cost, **m,
               break_even_price=round(args.cost / denom_be, 2) if denom_be > 0 else None,
               target_price=round(args.cost / denom_tg, 2) if denom_tg > 0 else None,
               target_margin=args.target_margin,
               coupon_headroom=round((m["net_rate"] - p["tm"]) * args.price, 2)
               if m["net_rate"] > p["tm"] else 0,
               break_even_roas=round(1 / (denom_be - 0), 2))
    # 盈亏线 ROAS（广告预算占售价 p% 时）：ROAS = (1-...)/p 的倒数口径见 metrics
    if p["ad"] > 0:
        out["break_even_roas_at_this_ad"] = round((denom_be) / p["ad"], 2)
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


def cmd_matrix(args):
    try:
        with open(args.file, encoding="utf-8-sig") as f:
            rows = list(csv.DictReader(f))
    except OSError as e:
        sys.exit(f"[ERROR] 读不了文件：{e}")
    if not rows:
        sys.exit("[ERROR] CSV 里没有数据行")
    header = list(rows[0].keys())
    low = [h.strip().lower() for h in header]

    def col(*cands):
        for c in cands:
            if c in low:
                return header[low.index(c)]
        return None

    c_name = col("角色", "名称", "sku", "role", "name") or header[0]
    c_price = col("售价", "价格", "price")
    c_cost = col("到岸成本", "成本", "cost")
    if not c_price or not c_cost:
        sys.exit(f"[ERROR] 认不出售价/成本列（表头：{header}）")

    results = []
    for r in rows:
        name = (r.get(c_name) or "?").strip()
        price = _num(r.get(c_price), kind="dec")
        cost = _num(r.get(c_cost), kind="dec")
        if price <= 0 or cost <= 0:
            results.append(dict(sku=name, error="价格或成本非正数，跳过"))
            continue
        m = margins(price, cost, args.commission, args.return_rate, args.ad, args.tax)
        tm = args.target_margin / 100
        headroom = round((m["net_rate"] - tm) * price, 2)
        results.append(dict(
            sku=name, price=price, cost=cost,
            pre_ad_margin=m["pre_ad_margin"], net_rate=m["net_rate"],
            vs_target=round(m["net_rate"] - tm, 4),
            verdict=("达标" if m["net_rate"] >= tm else
                     f"低于目标 {(tm - m['net_rate']) * 100:.1f} 个点"),
            coupon_headroom=max(headroom, 0),
            break_even_price=round(cost / (1 - args.commission / 100 - args.return_rate / 100
                                           - args.tax / 100), 2)))

    # 价格阶梯（按售价排序）
    ladder = []
    sorted_skus = sorted([r for r in results if "price" in r], key=lambda x: x["price"])
    for a, b in zip(sorted_skus, sorted_skus[1:]):
        gap = b["price"] - a["price"]
        ladder.append(dict(frm=a["sku"], to=b["sku"], gap=round(gap, 2),
                           gap_pct=round(gap / a["price"], 4)))

    # 一致性检查：低价 SKU 净利率反而更高 = 引流款策略（正常）；高配净利率低于主推 = 提醒
    notes = []
    by_net = sorted([r for r in results if "net_rate" in r], key=lambda x: -x["net_rate"])
    if len(by_net) >= 2 and by_net[0]["price"] < by_net[-1]["price"]:
        notes.append("最高净利率不是最高价 SKU —— 若是引流款策略属正常；若非刻意设计，检查高配成本")
    under = [r["sku"] for r in results if "net_rate" in r and r["net_rate"] < args.target_margin / 100]
    if under:
        notes.append(f"低于目标毛利 {args.target_margin}% 的 SKU：{('、'.join(under))} —— 确认是否刻意（引流款可低于目标，但须在盈亏价之上）")

    out = dict(mode="matrix", target_margin=args.target_margin, skus=results,
               price_ladder=ladder, notes=notes)
    print(json.dumps(out, ensure_ascii=False, indent=2))

    if not args.json:
        print(f"\n目标毛利 {args.target_margin}% ｜ 佣金 {args.commission}% ｜ 广告 {args.ad}% ｜ "
              f"退货 {args.return_rate}% ｜ 税 {args.tax}%\n")
        print(f"{'SKU':<34}{'售价':>10}{'净利率':>8}{'对目标':>9}{'券余量':>9}")
        for r in results:
            if "error" in r:
                print(f"{r['sku']:<34}  ⚠️ {r['error']}")
                continue
            mark = "✅" if r["vs_target"] >= 0 else "⚠️ "
            print(f"{r['sku']:<34}{r['price']:>10,.2f}{r['net_rate']:>8.1%}"
                  f"{r['vs_target']:>+9.1%}{r['coupon_headroom']:>9,.2f} {mark}")
        print()
        for l in ladder:
            print(f"  阶梯 {l['frm']} → {l['to']}：差 R$ {l['gap']:,.2f}（{l['gap_pct']:.0%}）")
        for n in notes:
            print(f"  ℹ️  {n}")
    return 0


def _num(v, default=0.0, kind="dec"):
    if v is None:
        return default
    s = str(v).strip().replace("R$", "").replace("%", "").replace(" ", "")
    if s in ("", "-", "—", "暂无", "N/A", "nan"):
        return default
    neg = s.startswith("-")
    s = s.lstrip("-")
    if kind == "int":
        digits = "".join(ch for ch in s if ch.isdigit())
        return (-1 if neg else 1) * int(digits) if digits else default
    if "," in s and "." in s:
        s = s.replace(".", "").replace(",", ".") if s.rfind(",") > s.rfind(".") else s.replace(",", "")
    elif "," in s:
        head, _, tail = s.rpartition(",")
        s = f"{head}.{tail}" if len(tail) <= 2 else head + tail
    elif "." in s:
        head, _, tail = s.rpartition(".")
        s = s if len(tail) <= 2 else head + tail
    try:
        return (-1 if neg else 1) * float(s)
    except ValueError:
        return default


def _add_common(p, need_cost=False):
    p.add_argument("--commission", type=float, default=14, help="平台佣金 %%")
    p.add_argument("--return", dest="return_rate", type=float, default=2, help="退货损耗 %%")
    p.add_argument("--ad", type=float, default=5, help="广告预算占售价 %%")
    p.add_argument("--tax", type=float, default=0, help="综合有效税率 %%")
    p.add_argument("--target-margin", type=float, default=32, help="目标净利 %%")
    if need_cost:
        p.add_argument("--cost", type=float, required=True, help="到岸成本 R$")
        p.add_argument("--price", type=float, required=True, help="售价 R$")


def main():
    ap = argparse.ArgumentParser(description="SKU 定价算术（只算不定价）")
    sub = ap.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("calc", help="单 SKU：净利率 / 盈亏价 / 目标价 / 优惠券余量")
    _add_common(c, need_cost=True)

    m = sub.add_parser("matrix", help="多 SKU 矩阵：读 CSV 出净利率表 + 价格阶梯 + 券余量")
    m.add_argument("--file", required=True)
    _add_common(m)
    m.add_argument("--json", action="store_true")

    args = ap.parse_args()
    sys.exit(cmd_calc(args) if args.cmd == "calc" else cmd_matrix(args))


if __name__ == "__main__":
    main()
