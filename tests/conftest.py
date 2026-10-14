import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for p in (ROOT / ".claude/skills/x-best-practices/scripts",
          ROOT / ".claude/skills/compliance-rules/scripts",
          ROOT / "scripts"):
    sys.path.insert(0, str(p))
