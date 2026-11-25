# The World in One Day — Wednesday 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/melatim80186/makefun-news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/melatim80186/makefun-news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

Entry for the make.fun competition
**"Sum up 25 November's world news in one image"**
(`news-image-20261125`, $100 USDC, top 50 share).

## What the image shows

A one-page newspaper front page for **Wednesday 25 November 2026**.
Every story on it either happened — or was first reported — on
25 November 2026, in any time zone. The masthead names the day, and a
red **DATE CHECK** box at the bottom lists the big stories from
19–23 November that are *not* today's news, so they cannot be mistaken
for it.

### Lead story (25 Nov)

**CIA and spy chief's office hit by cyber breach** — CNN reports the
CIA and the Office of the Director of National Intelligence were hit
by a cyberattack affecting classified information, the latest in a run
of breaches hitting US government systems.

### The three hero stories (25 Nov)

1. **Zelenskyy: Ukraine hit the Russian ship** — President Zelenskyy
   confirms Ukraine's drone strike on the cargo ship Sparta II in the
   Gulf of Finland, and a Russian warship sunk off Benghazi, Libya.
   Putin warns of retaliation. Sources: Reuters, Bloomberg.
2. **Houthi drone hits Riyadh's tallest tower** — at least 11 people
   wounded in the Saudi capital, the second strike on the tower in
   under a week, as Houthi fighters press to within 60 km of Aden.
   Sources: Reuters, Saudi Civil Defense.
3. **Huawei guilty in US criminal trial** — a New York jury convicts
   the Chinese telecom giant on 10 of 12 counts: trade-secret theft
   and bank fraud over its business in Iran. Huawei says it will
   appeal. Sources: Reuters, US Department of Justice.

### Also pictured (25 Nov)

- WHO pulls staff from an Ebola hospital in DR Congo after three days
  sheltering from fighting (5,775 Ebola deaths in the outbreak).
- Iran says more oil tankers hit mines in the Strait of Hormuz.
- Houthis advance to within 60 km of Aden; Yemen's army says the city
  will not fall.
- Trump awards the Medal of Freedom to Rudy Giuliani.
- Sarkozy and Carla Bruni ordered to stand trial over alleged witness
  tampering.
- China launches a space mission carrying a Pakistani astronaut.
- NATO to deploy early-warning aircraft in Poland.
- EU to cap hybrid-car imports from 1 December, aimed chiefly at China.
- Russian strikes kill 11 in a Kyiv-region apartment block.
- Today is the International Day for the Elimination of Violence
  against Women.

### Stat strip (25 Nov)

700,000 Russian soldiers killed in the Ukraine war (new analysis) ·
11 wounded in Riyadh · 10 of 12 Huawei counts guilty · 25 hostages
in a Cartagena supermarket · 5 crew killed in a Turkish helicopter
crash · 5,775 Ebola deaths in DR Congo.

### Date-checked — NOT 25 November (red box on the image)

GTA VI launch (19 Nov) · COP31 talks end with no deal (22 Nov) ·
ICJ: Myanmar committed genocide (19 Nov) · Democrats clinch the US
House (23 Nov) · Nvidia reinstates Jensen Huang (23 Nov) ·
Trump–Xi–Putin summit in Shenzhen (19 Nov).

## How it was built

The hero triptych (burning Sparta II, Riyadh tower at night, courtroom
gavel) was generated as an illustration with no text; the front page —
masthead, headlines, stat strip, lists and DATE CHECK box — was then
composed with PIL so every word is spelled exactly and stays legible.
The render went through three visual review rounds: the first caught
the bottom of the page overflowing past the DATE CHECK box and footer,
the second caught a deck line touching a rule and the DATE CHECK text
crowding its border, and the third confirmed a clean page — no
overflow, no clipping, no garbled text.
`main.py` (Python 3.13, stdlib only) simply copies the finished
1024×1024 PNG to the output directory; two runs write identical bytes.

## Run it

```sh
python3 main.py   # writes entry.png to /output (or $MAKEFUN_OUTPUT_DIR)
```

Entered on [make.fun](https://make.fun/bounty/news-image-20261125).
