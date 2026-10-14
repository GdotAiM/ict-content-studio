# Template: ICT Term of the Day (single post)
Series for `x-single-post-writer` (mode: `term-of-the-day`). One term per post.
Definition must come from `.claude/skills/ict-glossary/references/glossary.md` — do not invent terms.

```
ICT term of the day: <Term> (<ABBR>)

<Plain-English definition, 1–2 short sentences, from ict-glossary.>

Past example: <what happened on a PAST NQ session, past tense>, <level> (TradingView CAPITALCOM:US100, YYYY-MM-DD HH:MM ET / HH:MM SAST).

Educational, paper only. Not advice.
```

Rules
- The example is a past session only, never today's or an upcoming move.
- Every level carries source + ET/SAST timestamp (use `scripts/et_to_sast.py`).
- Check repeats first: `python3 scripts/log_post.py check --concepts <term> --days 14`.
- Validate: `check_x_post.py --stdin` and `scan_banned.py --stdin` must exit 0. 0–1 hashtags.
- Attach a chart via `chart-annotation-writer` (optional).
