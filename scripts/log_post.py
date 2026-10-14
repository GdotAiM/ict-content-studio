#!/usr/bin/env python3
"""Append a compact record of a post Ntloso has MANUALLY published to state/posted.jsonl,
and check for recent repeats. Does not post anything.

  log_post.py add --topic "FVG after PDH sweep" --concepts FVG,PDH,displacement \
      --format thread --ready-file ready/2026-10-14_1600_thread.md [--url https://x.com/...] [--likes 12 --impressions 900]
  log_post.py check --concepts FVG,PDH [--days 7]     # exit 1 if any concept used recently
  log_post.py list [--days 30]
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

SAST = ZoneInfo("Africa/Johannesburg")
DEFAULT_STATE = Path(__file__).resolve().parents[1] / "state" / "posted.jsonl"
FORMATS = {"thread", "single", "recap", "alert"}


def read_records(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


def _norm(concepts: str | list[str]) -> list[str]:
    items = concepts.split(",") if isinstance(concepts, str) else concepts
    return sorted({c.strip().lower() for c in items if c.strip()})


def recent_overlap(records: list[dict], concepts: list[str], days: int, now: datetime) -> list[dict]:
    cutoff = now - timedelta(days=days)
    out = []
    for r in records:
        when = datetime.fromisoformat(r["posted_at"])
        if when >= cutoff and set(r["concepts"]) & set(concepts):
            out.append(r)
    return out


def make_record(topic: str, concepts: list[str], fmt: str, now: datetime,
                ready_file: str | None = None, url: str | None = None,
                likes: int | None = None, impressions: int | None = None) -> dict:
    if not topic.strip():
        raise ValueError("topic required")
    if fmt not in FORMATS:
        raise ValueError(f"format must be one of {sorted(FORMATS)}")
    if not concepts:
        raise ValueError("at least one concept required")
    rec = {"posted_at": now.isoformat(timespec="minutes"), "platform": "x", "format": fmt,
           "topic": topic.strip(), "concepts": concepts, "ready_file": ready_file, "url": url}
    for k, v in (("likes", likes), ("impressions", impressions)):
        if v is not None:
            if v < 0:
                raise ValueError(f"{k} must be >= 0")
            rec[k] = v  # optional, entered manually by Ntloso
    return rec


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--state", default=str(DEFAULT_STATE))
    ap.add_argument("--now", help="ISO timestamp override (tests)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add")
    a.add_argument("--topic", required=True)
    a.add_argument("--concepts", required=True)
    a.add_argument("--format", default="thread")
    a.add_argument("--ready-file")
    a.add_argument("--url")
    a.add_argument("--likes", type=int, help="optional, copied manually from X")
    a.add_argument("--impressions", type=int, help="optional, copied manually from X")
    c = sub.add_parser("check")
    c.add_argument("--concepts", required=True)
    c.add_argument("--days", type=int, default=7)
    l = sub.add_parser("list")
    l.add_argument("--days", type=int, default=30)
    args = ap.parse_args(argv)

    state = Path(args.state)
    now = datetime.fromisoformat(args.now) if args.now else datetime.now(SAST)
    if now.tzinfo is None:
        now = now.replace(tzinfo=SAST)
    records = read_records(state)

    if args.cmd == "add":
        try:
            rec = make_record(args.topic, _norm(args.concepts), args.format, now, args.ready_file, args.url,
                              args.likes, args.impressions)
        except ValueError as e:
            print(f"error: {e}", file=sys.stderr)
            return 2
        state.parent.mkdir(parents=True, exist_ok=True)
        with state.open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(f"LOGGED {rec['topic']} {rec['concepts']}")
        return 0
    if args.cmd == "check":
        hits = recent_overlap(records, _norm(args.concepts), args.days, now)
        for h in hits:
            print(f"REPEAT {h['posted_at']} {h['topic']} {h['concepts']}")
        if not hits:
            print(f"FRESH: none of these concepts posted in last {args.days} days")
        return 1 if hits else 0
    cutoff = now - timedelta(days=args.days)
    for r in records:
        if datetime.fromisoformat(r["posted_at"]) >= cutoff:
            print(json.dumps(r, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
