"""Keyword-code real US App Store reviews of Words With Friends (app id 1196764367).

Source: Apple's public customer-reviews RSS feed, 10 pages of most-recent reviews
(fetched 2026-10-04). Each review can match several themes (multi-label).
Run: py code_reviews.py
"""
import json, os, re, collections

HERE = os.path.dirname(__file__)
rows = json.load(open(os.path.join(HERE, "reviews", "all_reviews.json"), encoding="utf-8"))

THEMES = {
    "Ads interrupt play": r"\bads?\b|\badds\b|advert|commercial",
    "Bugs, freezes & slowness": r"bug|glitch|crash|freez|\bslow|lag\b|lagg|not working|won.?t load|doesn.?t work|quit working|stuck",
    "Coins, rewards & paywalls": r"coin|reward|purchase|\bpay\b|paying|money|\$|subscription|spend|token|buy",
    "Unfair tiles / rigged draws": r"rigged|vowels|consonants|tiles|letters (we|i) get|tray|not random",
    "Bots & opponent quality": r"\bbots?\b|fake|\bai\b|computer|real (people|human|player)|opponent|stranger|cheat",
    "Dictionary & word validity": r"not a (real )?word|made.?up|dictionary|slang|acronym|abbreviat|valid word|definition|nonsense word",
    "Sign-in & account": r"sign.?in|log.?in|login|facebook|account|email|password",
    "Learning & onboarding": r"tutorial|instruction|how to play|confus|beginner|new player|learn|explain",
}
neg = [r for r in rows if r["rating"] <= 2]
counts = collections.Counter()
for r in neg:
    text = (r["title"] + " " + r["text"]).lower()
    for theme, pat in THEMES.items():
        if re.search(pat, text):
            counts[theme] += 1

out = {
    "total_reviews": len(rows),
    "rating_counts": dict(sorted(collections.Counter(r["rating"] for r in rows).items())),
    "negative_reviews": len(neg),
    "date_range": [min(r["date"] for r in rows)[:10], max(r["date"] for r in rows)[:10]],
    "themes": [{"theme": t, "reviews": c, "share_pct": round(100 * c / len(neg), 1)} for t, c in counts.most_common()],
}
json.dump(out, open(os.path.join(HERE, "review_themes.json"), "w"), indent=2)
print(json.dumps(out, indent=2))
