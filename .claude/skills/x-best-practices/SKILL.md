---
name: x-best-practices
description: X (Twitter) formatting rules plus deterministic scripts — check_x_post.py (weighted length) and export_thread.py (assembles gate-approved posts into ready/). Load for every X writer and the compliance gate.
---
# X best practices
- Hard limit: **280 weighted characters** per post (standard account).
- Weighting (X's counting rules): most Latin text = 1; URLs = 23 regardless of length;
  emoji and CJK/most non-Latin characters = 2. **Never count by eye — run the script.**
- Threads: 3–8 posts; hook first; numbered "1/" style optional (counts toward length).
- Put links in the last post (reach), max 1 link per thread.
- Images: annotated TradingView screenshot from `chart-annotation-writer`.

## Scripts
```
printf '%s' "text" | python3 .claude/skills/x-best-practices/scripts/check_x_post.py --stdin
python3 .claude/skills/x-best-practices/scripts/check_x_post.py --file drafts/2026-10-14_thread.md
python3 .claude/skills/x-best-practices/scripts/export_thread.py --file drafts/X.md --gate-report drafts/X_gate.md
```
Files are split into posts on lines containing only `---`. Lines starting with `#` or `>` before the first post
and HTML comments are ignored. Exit code 0 = all posts valid; 1 = violation; 2 = usage error.
See `references/x-rules.md`.
