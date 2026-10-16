#!/usr/bin/env python3
"""标题合规校验（Shopee / Mercado Livre / Amazon）—— 字符数是实测值，不是估算。

  python title_lint.py "标题文本" --platform shopee
  python title_lint.py 标题.txt --platform mercadolivre --forbidden iPhone,Samsung
  python title_lint.py "标题" --platform shopee --keywords carregador,20000mah,45w

检查项（阈值来自 references/platform-title-rules.md 规则卡）：
  length        : 字符数（非字节数）是否在平台上限内；<90% 建议补词（Shopee）
  first30       : 前 30 字符内容（Shopee 权重最高段，供人工确认主关键词是否前置）
  forbidden     : 禁用词命中（未授权品牌词、绝对化用语等）
  keywords      : 核心关键词覆盖（缺了哪些词）
  emoji         : 表情/非常规符号（Shopee 禁）
  all_caps      : 全大写单词（Shopee 禁堆砌大写）
  promo_words   : 促销词（Shopee 谨慎 / ML 明确不建议）
  duplicates    : 重复词堆砌（≥3 次）
  locale        : 中文字符混入（PT-BR 站点应为母语）
"""
import argparse
import json
import re
import sys

PLATFORMS = {
    "shopee": dict(limit=120, first_n=30, rec_fill=0.80, promo="warn"),
    "mercadolivre": dict(limit=60, first_n=None, rec_fill=None, promo="warn"),
    "amazon": dict(limit=200, first_n=None, rec_fill=None, promo="warn"),
}

PROMO_WORDS = [
    "frete grátis", "frete gratis", "promoção", "promocao", "oferta", "imperdível",
    "imperdivel", "brinde", "desconto", "promo", "sale", "免费", "促销", "特价",
]

EMOJI_RE = re.compile("[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U0001F900-\U0001F9FF]")
CJK_RE = re.compile(r"[\u4e00-\u9fff]")


def analyse(title, platform, args):
    p = PLATFORMS[platform]
    res = []   # (级别, 检查项, 说明)
    t = title.strip()
    n = len(t)   # Python 字符串长度 = 字符数（非字节）

    # 1) 长度
    if n > p["limit"]:
        res.append(("FAIL", "length", f"{n} 字符 > 平台上限 {p['limit']} —— 超出部分会被截断"))
    elif p["rec_fill"] and n < p["limit"] * p["rec_fill"]:
        res.append(("WARN", "length", f"{n}/{p['limit']} 字符（利用率 {n / p['limit']:.0%}），"
                                      f"建议补关键词到 90%+"))
    else:
        res.append(("PASS", "length", f"{n}/{p['limit']} 字符"))

    # 2) 前 30 字符（Shopee 权重最高段）
    if p["first_n"]:
        head = t[:p["first_n"]]
        res.append(("INFO", "first30", f"「{head}」← 前 30 字符，主关键词必须在这里"))

    # 3) 禁用词
    forbidden = args.forbidden or []
    if isinstance(forbidden, str):
        forbidden = [w.strip() for w in forbidden.split(",") if w.strip()]
    if args.forbidden_file:
        try:
            with open(args.forbidden_file, encoding="utf-8") as f:
                forbidden += [ln.strip() for ln in f if ln.strip()]
        except OSError as e:
            res.append(("WARN", "forbidden", f"禁用词文件读不了：{e}"))
    hits = [w for w in forbidden if w and w.lower() in t.lower()]
    if hits:
        res.append(("FAIL", "forbidden", f"命中禁用词：{'、'.join(hits)}（未授权品牌词/绝对化用语会有下架风险）"))
    elif forbidden:
        res.append(("PASS", "forbidden", f"0 命中（查了 {len(forbidden)} 个词）"))

    # 4) 关键词覆盖
    if args.keywords:
        kws = [k.strip() for k in args.keywords.split(",") if k.strip()]
        missing = [k for k in kws if k.lower() not in t.lower()]
        if missing:
            res.append(("WARN", "keywords", f"核心词未覆盖：{'、'.join(missing)}"))
        else:
            res.append(("PASS", "keywords", f"{len(kws)} 个核心词全覆盖"))

    # 5) 表情符号（Shopee 禁）
    if EMOJI_RE.search(t):
        res.append(("FAIL" if platform == "shopee" else "WARN", "emoji",
                    f"发现表情/符号：{EMOJI_RE.findall(t)[:5]}"))

    # 6) 全大写单词（Shopee 禁堆砌大写）
    caps = [w for w in re.findall(r"[A-Za-z]{4,}", t) if w.isupper()]
    if caps:
        res.append(("WARN", "all_caps", f"全大写词：{'、'.join(caps[:6])}（Shopee 禁堆砌大写，仅品牌缩写可接受）"))

    # 7) 促销词
    promos = [w for w in PROMO_WORDS if w in t.lower()]
    if promos:
        lv = "FAIL" if p["promo"] == "fail" else "WARN"
        res.append((lv, "promo_words", f"促销词：{'、'.join(promos)}（ML 明确不建议；Shopee 谨慎，属促销信息应放图/描述）"))

    # 8) 重复词堆砌
    words = re.findall(r"[A-Za-zÀ-ÿ0-9]+", t.lower())
    dup = [w for w in set(words) if words.count(w) >= 3 and len(w) > 2]
    if dup:
        res.append(("FAIL", "duplicates", f"重复 ≥3 次：{'、'.join(dup)}（关键词堆砌降权）"))

    # 9) 语言混入（PT-BR 站点出现中文）
    if CJK_RE.search(t):
        res.append(("FAIL", "locale", "标题含中文字符 —— 巴西站买家可见文本必须是 PT-BR"))

    ok = not any(lv == "FAIL" for lv, _, _ in res)
    return dict(platform=platform, chars=n, limit=p["limit"], ok=ok, checks=res,
                first_30=t[:30])


def main():
    ap = argparse.ArgumentParser(description="标题合规校验（字符数实测，非估算）")
    ap.add_argument("title", nargs="?", help="标题文本；或用 --file 传入")
    ap.add_argument("--file", help="从文件读标题（一行一个，逐条校验）")
    ap.add_argument("--platform", required=True, choices=list(PLATFORMS))
    ap.add_argument("--forbidden", help="禁用词，逗号分隔（品牌词/绝对化用语）")
    ap.add_argument("--forbidden-file", help="禁用词文件（每行一个）")
    ap.add_argument("--keywords", help="核心关键词，逗号分隔（查覆盖）")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    titles = []
    if args.file:
        try:
            with open(args.file, encoding="utf-8") as f:
                titles = [ln.strip() for ln in f if ln.strip()]
        except OSError as e:
            sys.exit(f"[ERROR] 读不了文件：{e}")
    elif args.title:
        titles = [args.title]
    else:
        sys.exit("[ERROR] 给标题文本或 --file")

    reports = [analyse(t, args.platform, args) for t in titles]
    all_ok = all(r["ok"] for r in reports)

    if args.json:
        print(json.dumps(reports if len(reports) > 1 else reports[0],
                         ensure_ascii=False, indent=2))
    else:
        for r in reports:
            icon = {"PASS": "✅", "WARN": "⚠️ ", "FAIL": "❌", "INFO": "ℹ️ "}
            print(f"\n「{r['first_30']}{'…' if r['chars'] > 30 else ''}」"
                  f"  [{r['platform']}  {r['chars']}/{r['limit']} 字符]"
                  f"  总判定: {'✅ 通过' if r['ok'] else '❌ 未通过'}")
            for lv, name, detail in r["checks"]:
                print(f"  {icon[lv]} {name:<12} {detail}")
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
