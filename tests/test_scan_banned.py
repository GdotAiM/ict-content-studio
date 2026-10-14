import subprocess
import sys
from pathlib import Path

import pytest
from scan_banned import load_patterns, scan_text

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / ".claude/skills/compliance-rules/scripts/scan_banned.py"
PATS = load_patterns()


@pytest.mark.parametrize("text", [
    "This setup is GUARANTEED to work", "risk-free entries", "Buy now before the open",
    "go long at the open", "entry at 20100", "TP: 20500", "join my VIP group",
    "easy money on NQ", "100% win rate", "free signals daily",
    "85% winrate this month", "72.5% win rate", "win rate of 90", "BUY @ 21000", "SELL NQ now",
    "another banger trade", "+120 handles today", "caught 45 handles", "use my code GDOT for 20% off",
    "prop firm discount code inside", "affiliate code in bio",
])
def test_banned_detected(text):
    assert scan_text(text, PATS)


@pytest.mark.parametrize("text", [
    "Price swept buy-side liquidity, then displaced lower.",
    "Educational only. Paper-traded. Not financial advice.",
    "The FVG formed at 10:01 ET / 17:01 SAST.",
    "BUY-side liquidity rested above the high.", "Sell-side liquidity was swept first.",
    "I wrote code to check post length.", "Win or lose, I log every paper trade.",
])
def test_clean_text(text):
    assert scan_text(text, PATS) == []


def test_cli(tmp_path):
    f = tmp_path / "x.md"
    f.write_text("fine line\nguaranteed profits\n", encoding="utf-8")
    r = subprocess.run([sys.executable, str(SCRIPT), "--file", str(f)], capture_output=True, text=True)
    assert r.returncode == 1 and "line 2" in r.stdout
    r = subprocess.run([sys.executable, str(SCRIPT), "--stdin"], input="clean", capture_output=True, text=True)
    assert r.returncode == 0


def test_example_thread_clean():
    r = subprocess.run([sys.executable, str(SCRIPT), "--file", str(ROOT / "examples/thread_2026-01-15.md")],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout


def test_signal_ban_unchanged():
    assert r"\bsignal(s)?\b" in [p.pattern for p in PATS]
