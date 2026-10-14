# ICT creators on X — research snapshot (2026-10-14)

Collected 2026-10-14 ~17:55 SAST via the X API (x MCP: get_users_by_usernames, get_users_posts with retweets/replies excluded, search_posts_all since 2026-08-01) plus WebSearch for well-known accounts. 17 X calls in total.
Metrics are as returned at collection time. Impressions = X impression_count. Times are converted to **SAST (UTC+2)**. Sample = the last ~25 original posts per account, so the medians are a snapshot, not long-run averages.
Raw data: `research/x-ict-creators-2026-10-14.json`.

## 1. Creator table
| Account | Followers | Posts sampled (SAST span) | Median likes | Median impr. | Main format | Peak hours SAST | Content type |
|---|---|---|---|---|---|---|---|
| @I_Am_The_ICT | 841,318 | 25 (Oct 2–12) | 1,424 | 112,769 | short text (18/25) | 13–15 | mindset, market commentary, the source of the concepts |
| @Ali_Khan_ICT | 115,747 | 25 (Sep 23–Oct 13) | 335 | 13,862 | text (23/25) | 11–12, 16 | "ICT Tip 💡" concept posts, aphorisms, own DRT model |
| @TritonTrades | 34,211 | 25 (Oct 7–14) | 29 | 3,168 | image (15/25) | 20, 23 | stat hooks ("X% winrate"), drama, prop-firm codes |
| @IamMavion | 26,073 | 25 (Oct 10–14) | 91 | 6,304 | video/image | 08–10 | CRT×ICT "bookmark this" explainers |
| @JeRRyMMXM | 21,150 | 25 (Oct 12–14) | 23 | 1,418 | video (10/25) | 14, 20, 23 | ICT clip curation, setup lists, very high frequency |
| @Jacobtradesz | 14,349 | 21 (Oct 2–14) | 42 | 1,980 | text/image | 16–18 | payouts, discipline posts, affiliate codes |
| @Ed_tradess | 10,468 | 24 (Sep 30–Oct 14) | 3 | 570 | image (16/24) | 14 (14/24) | concept infographics ("Masterclass💡") |
| @NQTimmy | 6,831 | 25 (Oct 1–14) | 110 | 3,713 | image (17/25) | 16–18 | NQ trade-win screenshots, lifestyle, giveaways |
| @PIPMUNCH | 5,448 | 25 (Sep 7–Oct 14) | 51 | 2,751 | image (17/25) | 15–19 | NQ handle tallies, ICT Spaces recaps |
| @AGIRAFX | 4,800 | 23 (Oct 4–14) | 6 | 231 | image (19/23) | 16–18 | giveaways, prop-firm promos |
| @Josephfgjr | 1,457 | 25 (Sep 27–Oct 14) | 12 | 982 | image (21/25) | 11, 13 | cheat sheets, daily plans, hashtag-heavy |
| @petar_trades | 1,374 | 23 (Oct 1–14) | 4 | 630 | text (16/23) | 13–14, 22 | testing ICT with AI, skeptical/analytical |
| @ICTSBTrader | 681 | 25 (Oct 8–14) | 0 | 64 | image | 20 | NQ/ES Silver Bullet "play of the day" |
| @TradeZella (journal tool, ICT-adjacent) | 59,417 | 24 (Oct 9–14) | 5 | 1,204 | text | 18 | journaling stats, brand content |

Also found in search (not profiled): @Z3uS_Trading, @Quantumalgo, @AtlasOnChain2, @sarani_trader, @Shanict1, @tdatadriven, @Minkjer_ICT. These are small accounts (<5k followers) posting Silver Bullet/FVG setups, often on XAUUSD and often written as BUY/SELL calls.

## 2. Top posts and patterns (with examples)
**Short, plain mindset text gets the most reach at the top.** ICT's top posts in the sample have no image:
- https://x.com/I_Am_The_ICT/status/2107435296551805216 (5,360 likes, 472 RTs, 223,898 impr.): "When markets are at all time highs… Same rules"
- https://x.com/I_Am_The_ICT/status/2107805761686340057 (4,147 likes, 180,218 impr.): "I am still not interested in this market"
- https://x.com/Ali_Khan_ICT/status/2107420541707600223 (780 likes) and https://x.com/Ali_Khan_ICT/status/2103128522583621919 (559 likes): "Master one asset. Master one setup…"

**Recurring series of concept tips.** Ali Khan's "ICT Tip 💡:" is the clearest example, e.g. https://x.com/Ali_Khan_ICT/status/2104137685866512706 (645 likes, 29,846 impr.) on the 1st-presentation FVG. Ed_tradess runs a "…Explained💡 / Masterclass💡" infographic series, e.g. https://x.com/Ed_tradess/status/2107777657790505164 and https://x.com/Ed_tradess/status/2108867639003201985.

**Stat-hook plus chart.** https://x.com/TritonTrades/status/2108304238686401000 ("the 8 AM range has a 99.6% winrate on NQ 🤯", 476 likes, 58,758 impr.) and https://x.com/TritonTrades/status/2108889540933145001. These perform well, but the win-rate wording breaks our rule 3.

**Bookmark-bait video.** https://x.com/IamMavion/status/2109249305244746168 ("This video should cost more than $50,000 but it's here for free… Bookmark", 413 likes, 73 RTs). The reposts-to-likes ratio is high, so people save and share these.

**Lists / taxonomies.** https://x.com/JeRRyMMXM/status/2109620392516272549 ("The algorithm keeps delivering the same 4 setups…", 242 likes, 14,484 impr.), compared with a median of 23 likes for that account.

**Community curation.** https://x.com/PIPMUNCH/status/2098135033949176269 links to ICT's Spaces on NQ (150 likes, 30 RTs; this account's top post).

**P&L / lifestyle flexing works for engagement but brings in a different audience.** https://x.com/NQTimmy/status/2106572565124698233 (dream car, 594 likes), https://x.com/NQTimmy/status/2110005351970136305 ("BANGER TRADE!"), https://x.com/PIPMUNCH/status/2107953848593657942 ("210 Handles"), https://x.com/Jacobtradesz/status/2109848016874311933 (payout thank-you).

**"No trade today" discipline posts do well.** https://x.com/Jacobtradesz/status/2108209247204880555 got 82 likes, about twice that account's median. ICT's "not interested in this market" post (above) is a similar case.

**Signals and giveaways do poorly.** AGIRAFX (median 231 impr.) and ICTSBTrader (median 64 impr.) post daily setups and calls with little explanation and get the least reach in the sample.

**Contrarian / "testing ICT" angle.** https://x.com/petar_trades/status/2109059872289366324 got 45 replies and 27,950 impressions on a 1.4k-follower account, so debate drives replies.

### Format, length, hashtags, CTAs
- Images are the default for mid-size accounts. The biggest accounts mostly post text.
- Posts are short. Average length is 75–260 characters, with heavy line breaks and one idea per line.
- Hashtags are almost absent among the top performers (ICT, Ali, Triton, Mavion: 0 in the sample). Only small accounts use #ICT/#NQ heavily, and that brings no visible reach benefit.
- Common CTAs: "Bookmark", "Which one did you take?", Discord/Telegram links, prop-firm discount codes. Only PIPMUNCH puts "Not a financial advisor | Educational" in the bio.
- Posting times (SAST): ICT posts 13:00–15:00 SAST (07:00–09:00 ET, before the NY open). Ali posts late morning SAST. Recap and P&L accounts post 16:00–23:00 SAST, after the NY AM session.

## 3. What works
1. One clear idea in under ~200 characters, mindset or concept, no image needed when the account has authority.
2. A named recurring series (ICT Tip 💡, Explained💡) so people know what to expect.
3. Saveable reference material: cheat sheets, lists of N setups, explainer videos. Reposts and bookmarks are high on these.
4. Showing discipline ("no trade today") gets more engagement than an account's average post.
5. Curating ICT's own material (Spaces/video links with context) borrows his reach.

## 4. Gaps (opportunities for GdotAiM)
- **No sourced or timestamped levels.** None of the sampled posts give a price source plus an ET/SAST timestamp. Our rule 6 is a real point of difference.
- **No transparent paper journal.** Posts are P&L wins or nothing. Nobody publishes losses or rule breaks as a series.
- **No SAST/Africa framing.** No account in the sample translates ICT time windows (Silver Bullet, NY open, macros) into SAST, even though the NY open falls in the African afternoon.
- **NQ CFD (CAPITALCOM US100) specifically.** Nearly all NQ accounts talk futures/prop firms. Nobody covers CFD price differences or session hours.
- **Compliance-clean education.** Win-rate claims, "BUY/SELL" labels and affiliate codes are common, so a clean, no-hype account would stand out.
- **Glossary-grade definitions.** Terms like IFVG, CISD and CRT are used everywhere but rarely defined in plain English.

## 5. Ten recommendations mapped to repo changes
1. **New series template `templates/ict-term-of-the-day.md`** (+ `x-single-post-writer` option): plain-English definition from `ict-glossary` plus one annotated *past* NQ example. Modeled on Ali's ICT Tip series.
2. **New agent `.claude/agents/paper-journal-writer.md`**: turns `journal/` into a weekly "Paper Journal Wk N" thread with losses and rule breaks, every trade labelled PAPER. This fills the transparency gap.
3. **New agent `.claude/agents/no-trade-day-writer.md`**: a short discipline post when the journal shows no qualifying setup, based on the "no trade today" pattern.
4. **Posting schedule `state/schedule.yaml` + README section**: concept post at ~13:00–14:00 SAST (before the NY open, matching ICT's window); session review at ~19:00–20:00 SAST, after the 09:30–11:00 ET session. Weekly journal thread on Saturday. Times are suggestions only; Ntloso posts by hand.
5. **SAST time-translation helper `scripts/et_to_sast.py`** (deterministic, DST-aware), used by writers for "Silver Bullet in SAST" posts. Add a test in `tests/`.
6. **Compliance additions in `banned_phrases.txt`**: add win-rate patterns (`\d+(\.\d+)?% winrate`), "BUY/SELL" labels, "banger trade", "handles" tallies and prop-firm/affiliate "code". These are the patterns competitors rely on.
7. **Hashtag rule in `x-best-practices/references/x-rules.md`**: 0–1 hashtags per post (top performers use none). Have `check_x_post.py` warn when there are more than 2.
8. **Bookmarkable cheat-sheet template `templates/cheat-sheet.md`** + `chart-annotation-writer` mode for one-image checklists (FVG, liquidity sweep, Silver Bullet). Use "Bookmark for your replay sessions" as the CTA.
9. **Curation agent `.claude/agents/ict-source-curator.md`**: drafts "what ICT said about X" posts that link the original ICT video or Space (link in the last post, per the existing rule) with a timestamp.
10. **Research refresh `.claude/agents/x-research-scout.md`** + `research/` convention: monthly re-run of this snapshot (read-only X calls), storing JSON metrics so performance claims stay sourced. Log own post metrics manually in `state/posted.jsonl` (extend `log_post.py` with optional likes/impressions fields).

## 6. Ten hook ideas (validated)
All ten pass `check_x_post.py` (110–175/280) and `scan_banned.py` (CLEAN) as of 2026-10-14. Any real level added later still needs a source and an ET+SAST timestamp.

 1. Most ICT posts show the win. This is my paper-trade journal for the day, losses included. NQ / US100 CFD, process only, not advice. 🧵
 2. Silver Bullet window, translated for Johannesburg: 10:00-11:00 ET = 16:00-17:00 SAST (EDT). Here is what that hour looked like in yesterday's replay, with every level sourced.
 3. I marked every fair value gap on NQ yesterday and logged which ones were respected. Educational review of past price action, paper only.
 4. A liquidity sweep is not a reversal by itself. Here is the 3-step checklist I use to study one after the fact.
 5. Week 1 of my public ICT paper journal: setups studied, rules followed, rules broken. No P&L screenshots, just the process.
 6. "Where is the draw on liquidity?" is the first question I ask in replay. Here is how I answer it on a past NQ session, step by step.
 7. Trading from South Africa means the NY open lands at 15:30 SAST. This is my study routine around that hour, and why I review instead of chase.
 8. Every level in this post has a source and a timestamp in ET and SAST. If a chart claim cannot be checked, treat it as unverified.
 9. ICT term of the day: Inversion FVG. Plain-English definition, one annotated past NQ example, one common misread.
10. Day off from the charts. A no-setup day is still a journal entry: here is what I watched for and why nothing qualified.
