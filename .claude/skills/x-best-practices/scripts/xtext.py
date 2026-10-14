"""Shared helpers: X weighted length and draft-file parsing (stdlib only)."""
from __future__ import annotations

import re
import unicodedata

MAX_WEIGHTED = 280
URL_WEIGHT = 23
_ONE_RANGES = ((0x0000, 0x10FF), (0x2000, 0x200D), (0x2010, 0x201F), (0x2032, 0x2037))
URL_RE = re.compile(r"https?://[^\s]+", re.IGNORECASE)
# Emoji base + any modifiers / variation selectors / ZWJ-joined parts count as one unit (weight 2).
_EMOJI_BASE = r"[\U0001F000-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF\u2300-\u23FF]"
_EMOJI_SEQ = re.compile(
    rf"{_EMOJI_BASE}[\uFE0F\U0001F3FB-\U0001F3FF]*(?:\u200D{_EMOJI_BASE}[\uFE0F\U0001F3FB-\U0001F3FF]*)*"
)


def _char_weight(ch: str) -> int:
    cp = ord(ch)
    for lo, hi in _ONE_RANGES:
        if lo <= cp <= hi:
            return 1
    return 2


def weighted_length(text: str) -> int:
    text = unicodedata.normalize("NFC", text)
    total = 0
    pos = 0
    for m in URL_RE.finditer(text):
        total += _plain_length(text[pos:m.start()]) + URL_WEIGHT
        pos = m.end()
    return total + _plain_length(text[pos:])


def _plain_length(text: str) -> int:
    total = 0
    pos = 0
    for m in _EMOJI_SEQ.finditer(text):
        total += sum(_char_weight(c) for c in text[pos:m.start()]) + 2
        pos = m.end()
    return total + sum(_char_weight(c) for c in text[pos:])


def split_posts(content: str) -> list[str]:
    """Split a draft into posts on lines that are exactly '---'.

    Drops HTML comments and, in each chunk, leading heading ('#') / quote ('>') lines,
    so a file title or disclaimer banner isn't counted as post text.
    """
    content = re.sub(r"<!--.*?-->", "", content, flags=re.S)
    chunks = re.split(r"^\s*---\s*$", content, flags=re.M)
    posts = []
    for chunk in chunks:
        lines = chunk.strip("\n").splitlines()
        while lines and (not lines[0].strip() or lines[0].lstrip().startswith(("#", ">"))):
            lines.pop(0)
        text = "\n".join(lines).strip()
        if text:
            posts.append(text)
    return posts
