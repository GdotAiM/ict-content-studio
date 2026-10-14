#!/usr/bin/env python3
"""Assemble gate-approved posts into ready/YYYY-MM-DD_HHMM_thread.md.

Refuses to export unless:
  * the LAST line of the gate report matching ^VERDICT:\s*(SHIPS|DOES NOT SHIP)\s*$
    is 'VERDICT: SHIPS' (template text / quoted earlier verdicts are ignored;
    no such line = blocked),
  * every post passes check_x_post length rules,
  * scan_banned finds no banned phrases.
This script only writes a file. It never posts anywhere.
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[1] / "compliance-rules" / "scripts"))
from xtext import MAX_WEIGHTED, split_posts, weighted_length  # noqa: E402
from scan_banned import load_patterns, scan_text  # noqa: E402

SAST = ZoneInfo("Africa/Johannesburg")


VERDICT_RE = re.compile(r"^VERDICT:\s*(SHIPS|DOES NOT SHIP)\s*$")


def final_verdict(report: str) -> str | None:
    """Return the verdict from the last strictly-formatted VERDICT line, or None."""
    verdict = None
    for line in report.splitlines():
        m = VERDICT_RE.match(line)
        if m:
            verdict = m.group(1)
    return verdict


def gate_ships(report: str) -> bool:
    return final_verdict(report) == "SHIPS"


def build(posts: list[str], stamp: datetime, source: str) -> str:
    n = len(posts)
    out = [f"# Ready thread — {stamp:%Y-%m-%d %H:%M} SAST",
           f"<!-- source: {source}; {n} posts; human posts manually — no automation -->", ""]
    for i, p in enumerate(posts, 1):
        out += [f"## Post {i}/{n} ({weighted_length(p)}/{MAX_WEIGHTED})", "", p, ""]
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--file", required=True, help="draft file, posts split on '---'")
    ap.add_argument("--gate-report", required=True, help="compliance-gate report file")
    ap.add_argument("--out-dir", default="ready")
    ap.add_argument("--timestamp", help="override time, 'YYYY-MM-DD HH:MM' SAST (for tests)")
    args = ap.parse_args(argv)

    draft, report = Path(args.file), Path(args.gate_report)
    for p in (draft, report):
        if not p.is_file():
            print(f"error: file not found: {p}", file=sys.stderr)
            return 2
    if not gate_ships(report.read_text(encoding="utf-8")):
        print("BLOCKED: gate verdict is not SHIPS", file=sys.stderr)
        return 1
    posts = split_posts(draft.read_text(encoding="utf-8"))
    if not posts:
        print("BLOCKED: no posts in draft", file=sys.stderr)
        return 1
    bad = [i for i, p in enumerate(posts, 1) if weighted_length(p) > MAX_WEIGHTED]
    if bad:
        print(f"BLOCKED: posts over {MAX_WEIGHTED}: {bad}", file=sys.stderr)
        return 1
    hits = scan_text("\n".join(posts), load_patterns())
    if hits:
        print(f"BLOCKED: banned phrases: {sorted({h['match'] for h in hits})}", file=sys.stderr)
        return 1

    stamp = (datetime.strptime(args.timestamp, "%Y-%m-%d %H:%M").replace(tzinfo=SAST)
             if args.timestamp else datetime.now(SAST))
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"{stamp:%Y-%m-%d_%H%M}_thread.md"
    out.write_text(build(posts, stamp, str(draft)), encoding="utf-8")
    print(f"WROTE {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
