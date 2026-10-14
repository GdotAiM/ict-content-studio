# state/posted.jsonl schema
One JSON object per line, appended by `scripts/log_post.py add` **after Ntloso has posted manually**.
Compact on purpose — agents load this file for memory, so no full post text.

| Field | Type | Example |
|-------|------|---------|
| posted_at | ISO-8601 with offset (SAST) | `"2026-10-14T16:05+02:00"` |
| platform | string | `"x"` |
| format | `thread` \| `single` \| `recap` \| `alert` | `"thread"` |
| topic | string (≤ 80 chars) | `"FVG after PDH sweep"` |
| concepts | lowercase string[] (glossary terms) | `["fvg","pdh","displacement"]` |
| ready_file | string \| null | `"ready/2026-10-14_1600_thread.md"` |
| url | string \| null | link to the post, pasted by Ntloso |
| likes | int (optional, omitted if unknown) | copied manually from X: `--likes 12` |
| impressions | int (optional, omitted if unknown) | copied manually from X: `--impressions 900` |

Repeat check: `python3 scripts/log_post.py check --concepts fvg,pdh --days 7` (exit 1 = recently covered).
