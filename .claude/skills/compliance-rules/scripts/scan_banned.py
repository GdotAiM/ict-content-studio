#!/usr/bin/env python3
"""Scan text for banned trading-content phrases.

Usage: scan_banned.py --file PATH | --stdin  [--patterns PATH]
Exit: 0 clean, 1 banned phrase found, 2 usage error.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

DEFAULT_PATTERNS = Path(__file__).resolve().parents[1] / "references" / "banned_phrases.txt"


def load_patterns(path: Path = DEFAULT_PATTERNS) -> list[re.Pattern]:
    pats = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            pats.append(re.compile(line, re.IGNORECASE))
    return pats


def scan_text(text: str, patterns: list[re.Pattern]) -> list[dict]:
    hits = []
    for lineno, line in enumerate(text.splitlines(), 1):
        for pat in patterns:
            for m in pat.finditer(line):
                hits.append({"line": lineno, "match": m.group(0), "pattern": pat.pattern})
    return hits


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--file")
    src.add_argument("--stdin", action="store_true")
    ap.add_argument("--patterns", default=str(DEFAULT_PATTERNS))
    args = ap.parse_args(argv)
    if args.file:
        p = Path(args.file)
        if not p.is_file():
            print(f"error: file not found: {p}", file=sys.stderr)
            return 2
        text = p.read_text(encoding="utf-8")
    else:
        text = sys.stdin.read()
    hits = scan_text(text, load_patterns(Path(args.patterns)))
    for h in hits:
        print(f"BANNED line {h['line']}: '{h['match']}' (pattern: {h['pattern']})")
    if not hits:
        print("CLEAN: no banned phrases")
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
