# Words With Friends FTUE Redesign

**Live case study and playable prototype: https://zackt223.github.io/wwf-ftue-redesign/**

By [Zackariah Telsem](https://www.linkedin.com/in/zackariah-telsem-a8b245246/) · October 2026 · Independent product case study

An onboarding teardown of the Words With Friends first-time user experience (FTUE), checked against real App Store reviews and public benchmarks. It includes a redesigned first match you can play in the browser, a product spec with acceptance criteria, and an A/B test plan.

## What's inside

- **Teardown** of the current first session on iOS (v61, October 2026), with 11 annotated callouts across four screens.
- **Review analysis** of the 450 most recent US App Store reviews (Jul 21 – Oct 3, 2026). Ads come up in 57.6% of the 1–2★ reviews.
- **Four drop-off points** between first open and day-1 return, each with evidence and a fix.
- **Playable prototype** of the redesigned first match, styled as an iPhone screen:
  - real board layout, letter values and scoring
  - an 80,000-word dictionary (ENABLE)
  - an opponent who replies with real words
  - three in-context tips, a free hint, and a save-progress sheet you can swipe away
  - spring physics with velocity handoff, so tiles follow the pointer 1:1 and can be flicked back to the rack
- **Product spec** with 8 acceptance criteria.
- **KPIs and a 3-arm A/B test plan**: hypothesis, guardrails, sample size (about 9,600 installs per arm) and decision rules.

## Repo layout

| Path | What it is |
| --- | --- |
| `index.html` | The full case study and prototype (one page, no build step) |
| `words.txt` | Dictionary used to check words (ENABLE word list, 2–8 letters) |
| `common.txt` | Common English words the opponent and hints choose from |
| `assets/` | Screenshots of the current flow (other players' photos blurred) |
| `analysis/fetch_reviews.py` | Downloads recent App Store reviews from Apple's public RSS feed |
| `analysis/code_reviews.py` | Keyword-codes the 1–2★ reviews into complaint themes |
| `analysis/review_themes.json` | Results used on the page |

## Run it locally

The page loads `words.txt` with `fetch`, so serve the folder rather than opening the file directly:

```bash
python -m http.server 8000
```

Then open http://localhost:8000.

To reproduce the review analysis:

```bash
cd analysis
python fetch_reviews.py
python code_reviews.py
```

New reviews arrive daily, so a fresh run will give slightly different numbers.

## Sources

- Apple App Store, Words With Friends (id 1196764367): rating and rating count via the iTunes Lookup API; reviews via Apple's public customer-reviews RSS feed. Pulled October 4, 2026.
- Sensor Tower, top 5 word puzzle games by revenue, US: [Q2 2025](https://sensortower.com/blog/2025-q2-unified-top-5-word%20puzzle%20games-revenue-us-603697f4241bc16eb8570d37), [Q4 2025](https://sensortower.com/blog/2025-q4-unified-top-5-word-puzzle-games-revenue-us-603697f4241bc16eb8570d37).
- GameAnalytics 2025 Mobile Gaming Benchmarks, via [Game Dev Reports](https://gamedevreports.substack.com/p/gameanalytics-mobile-gaming-benchmarks).

## Disclaimer

Words With Friends is a trademark of Zynga Inc. This project is not affiliated with or endorsed by Zynga. Screenshots are used for commentary and critique. The opponent in the prototype is simulated.
