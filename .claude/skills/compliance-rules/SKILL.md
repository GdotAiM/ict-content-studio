---
name: compliance-rules
description: Banned-phrase list and claim-rating rules for educational trading content, plus scripts/scan_banned.py. Load in writers and the compliance gate.
---
# Compliance rules
1. Run `python3 .claude/skills/compliance-rules/scripts/scan_banned.py --file <draft>` (or `--stdin`). Exit 1 = hits.
2. Banned phrases: `references/banned_phrases.txt` (case-insensitive; regex allowed). Edit freely.
3. Claim ratings:
   - APPROVED: sourced + timestamped (ET & SAST), traceable to input files.
   - UNVERIFIED: missing source/time, or not in inputs.
   - BANNED: signals, promises, guarantees, live calls, performance marketing, named-person attacks.
4. Required: disclaimer "Educational only" + "Paper" + "Not financial advice" somewhere in the piece.
5. Never mention account size, P&L in currency, or prop-firm payouts.
