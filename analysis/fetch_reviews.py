"""Download the most recent US App Store reviews of Words With Friends (app id 1196764367).

Uses Apple's public customer-reviews RSS feed (10 pages, up to 500 reviews).
Writes reviews/all_reviews.json, which code_reviews.py reads.
Run: py fetch_reviews.py
"""
import json, os, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
URL = "https://itunes.apple.com/us/rss/customerreviews/page={}/id=1196764367/sortby=mostrecent/json"

rows = []
for page in range(1, 11):
    with urllib.request.urlopen(URL.format(page)) as r:
        feed = json.load(r).get("feed", {})
    for e in feed.get("entry", []):
        if "im:rating" not in e:
            continue
        rows.append({
            "rating": int(e["im:rating"]["label"]),
            "title": e["title"]["label"],
            "text": e["content"]["label"],
            "version": e["im:version"]["label"],
            "date": e["updated"]["label"],
        })

os.makedirs(os.path.join(HERE, "reviews"), exist_ok=True)
with open(os.path.join(HERE, "reviews", "all_reviews.json"), "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False)
print(f"saved {len(rows)} reviews")
