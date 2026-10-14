# X post rules used by this studio
| Rule | Value |
|------|-------|
| Max weighted length | 280 |
| URL weight | 23 (any http/https URL) |
| Weight 1 ranges | U+0000–U+10FF, U+2000–U+200D, U+2010–U+201F, U+2032–U+2037 |
| Everything else (emoji, CJK, …) | 2 |
| Emoji sequences (ZWJ, skin tones, VS16) | 2 total |
| Text normalisation | Unicode NFC before counting |
| Hashtags | 0–1 per post (top ICT performers use none). `check_x_post.py` prints a WARN above 1; it does not fail the post. |
| Links | In the last post of a thread only. |
