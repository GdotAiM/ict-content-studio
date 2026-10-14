# CLAUDE.md — ict-content-studio project rules

You are working inside Ntloso Ngubeni's (GdotAiM) content studio. Ntloso studies and teaches
ICT (Inner Circle Trader) concepts, charts **NQ / US100 CFD on CAPITALCOM via TradingView**, and
lives in **Africa/Johannesburg (SAST, UTC+2)**. Markets are referenced in **New York time (ET)**.

## Hard rules (never break these)
1. **Educational content only.** Explain concepts, review past price action, show process.
2. **No buy/sell signals.** No "long here", "short now", entries/stops/targets for a live market.
3. **No profit promises.** Never "guaranteed", "risk-free", "easy money", "can't lose", win-rate boasts.
4. **No live-trade calls.** Nothing that reads as an instruction to trade a current or upcoming move.
5. **Paper-trading only.** Every trade referenced is a paper/sim trade and is labelled as such.
6. **Source + timestamp on every market fact.** Any price level, range, event or headline carries
   its source and a timestamp in **both ET and SAST**, e.g. `21,345.25 (TradingView CAPITALCOM:US100, 2026-10-14 09:30 ET / 15:30 SAST)`.
   No source → the claim is UNVERIFIED and cannot ship.
7. **The human posts.** Agents never post, schedule or call any X/Twitter write API. There is no
   posting code in this repo and none may be added. Agents write files; Ntloso reviews and posts by hand.
8. **The gate decides.** Nothing is written to `ready/` unless `compliance-gate` returns **SHIPS** and
   `check_x_post.py` + `scan_banned.py` exit 0 for every post.

## Conventions
- Lengths are **measured by scripts, never counted by the model**:
  `printf '%s' "<text>" | python3 .claude/skills/x-best-practices/scripts/check_x_post.py --stdin`
- Banned language: `python3 .claude/skills/compliance-rules/scripts/scan_banned.py --file <path>`
- Memory of what has been posted lives in `state/posted.jsonl` (compact: topic, concepts, date — not full text).
  Check it before proposing a topic; log with `scripts/log_post.py` only after Ntloso confirms it was posted.
- Dated filenames: `briefs/YYYY-MM-DD.md`, `alerts/YYYY-MM-DD_<event>.md`, `ready/YYYY-MM-DD_HHMM_thread.md`.
- Use `ict-glossary` for terminology and `brand-voice` for tone. Do not invent ICT terms.
- Times: ET is UTC-4 (EDT) / UTC-5 (EST); SAST is fixed UTC+2. So 09:30 ET = 15:30 SAST in EDT, 16:30 SAST in EST.
- Redact account numbers, broker IDs, and personal data before putting journal content into context.
- ET→SAST conversions are **computed, not guessed**: `python3 scripts/et_to_sast.py 09:30 --date YYYY-MM-DD`.
- Hashtags: 0–1 per post (`check_x_post.py` warns above 1).
- Posting slots (suggestions; Ntloso posts by hand): see `docs/posting-schedule.md` — ~13:00–14:00 SAST pre-open concept, ~19:00–20:00 SAST session review, Saturday paper-journal thread (EDT season; +1h in EST).
- Templates live in `templates/` (term of the day, cheat sheet). Research snapshots live in `research/` (refreshed monthly by `x-research-scout`, read-only).
- If a required input is missing (no brief, no journal entry), **stop and say so** — do not fabricate.
