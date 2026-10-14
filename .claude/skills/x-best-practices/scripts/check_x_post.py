#!/usr/bin/env python3
"""Validate X post length using X's weighted counting.

Usage:
  printf '%s' "text" | check_x_post.py --stdin
  check_x_post.py --file drafts/2026-10-14_thread.md   # posts split on '---'
Exit: 0 ok, 1 violation (too long or empty), 2 usage error.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from xtext import MAX_WEIGHTED, split_posts, weighted_length  # noqa: E402


def check(posts: list[str], limit: int = MAX_WEIGHTED) -> list[dict]:
    results = []
    for i, p in enumerate(posts, 1):
        n = weighted_length(p)
        results.append({"post": i, "weighted_length": n, "limit": limit,
                        "ok": 0 < n <= limit, "over_by": max(0, n - limit)})
    return results


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--stdin", action="store_true", help="read one post from stdin")
    src.add_argument("--file", help="read posts from a file split on '---'")
    ap.add_argument("--limit", type=int, default=MAX_WEIGHTED)
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args(argv)

    if args.stdin:
        raw = sys.stdin.read()
        posts = [raw.strip()] if raw.strip() else []
    else:
        path = Path(args.file)
        if not path.is_file():
            print(f"error: file not found: {path}", file=sys.stderr)
            return 2
        posts = split_posts(path.read_text(encoding="utf-8"))
    if not posts:
        print("FAIL: no post text found", file=sys.stderr)
        return 1

    results = check(posts, args.limit)
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for r in results:
            status = "OK  " if r["ok"] else "FAIL"
            extra = f" (over by {r['over_by']})" if r["over_by"] else ""
            print(f"{status} post {r['post']}: {r['weighted_length']}/{r['limit']}{extra}")
    return 0 if all(r["ok"] for r in results) else 1


if __name__ == "__main__":
    sys.exit(main())
