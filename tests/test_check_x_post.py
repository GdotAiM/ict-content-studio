import subprocess
import sys
from pathlib import Path

import check_x_post
from xtext import split_posts, weighted_length

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / ".claude/skills/x-best-practices/scripts/check_x_post.py"


def test_plain_ascii():
    assert weighted_length("hello") == 5


def test_url_counts_23():
    assert weighted_length("https://example.com/a/very/long/path/that/keeps/going") == 23
    assert weighted_length("see https://x.co") == 4 + 23


def test_emoji_counts_2():
    assert weighted_length("📊") == 2
    assert weighted_length("a🧠b") == 4


def test_emoji_sequence_counts_2():
    assert weighted_length("👍🏽") == 2
    assert weighted_length("👨\u200d💻") == 2


def test_cjk_counts_2():
    assert weighted_length("日本") == 4


def test_curly_quotes_count_1():
    assert weighted_length("\u201cok\u201d") == 4


def test_limit_boundaries():
    assert check_x_post.check(["a" * 280])[0]["ok"]
    assert not check_x_post.check(["a" * 281])[0]["ok"]
    assert not check_x_post.check(["😀" * 141])[0]["ok"]
    assert check_x_post.check(["😀" * 140])[0]["ok"]


def run(*args, stdin=None):
    return subprocess.run([sys.executable, str(SCRIPT), *args], input=stdin,
                          capture_output=True, text=True)


def test_cli_stdin_ok():
    r = run("--stdin", stdin="short post")
    assert r.returncode == 0 and "OK" in r.stdout


def test_cli_stdin_too_long():
    r = run("--stdin", stdin="x" * 300)
    assert r.returncode == 1 and "over by 20" in r.stdout


def test_cli_empty_fails():
    assert run("--stdin", stdin="  ").returncode == 1


def test_cli_file(tmp_path):
    f = tmp_path / "d.md"
    f.write_text("# Title\n> banner\n\nfirst\n---\nsecond\n", encoding="utf-8")
    assert run("--file", str(f)).returncode == 0
    f.write_text("ok\n---\n" + "y" * 281, encoding="utf-8")
    assert run("--file", str(f)).returncode == 1


def test_cli_missing_file():
    assert run("--file", "/nope/missing.md").returncode == 2


def test_split_posts_strips_headers_and_comments():
    posts = split_posts("# T\n<!-- c -->\nA\n---\n\nB\n---\n")
    assert posts == ["A", "B"]


def test_example_thread_passes():
    assert run("--file", str(ROOT / "examples/thread_2026-01-15.md")).returncode == 0


def test_hashtag_count():
    assert check_x_post.count_hashtags("FVG study #ICT") == 1
    assert check_x_post.count_hashtags("#ICT #NQ #trading") == 3
    assert check_x_post.count_hashtags("no tags, item #1, a&#39;b, x.com/a#frag") == 0


def test_hashtag_warning_not_error(tmp_path):
    r = check_x_post.check(["one #ICT"])[0]
    assert r["ok"] and r["warnings"] == []
    r = check_x_post.check(["many #ICT #NQ"])[0]
    assert r["ok"] and r["hashtags"] == 2 and r["warnings"]
    p = subprocess.run([sys.executable, str(SCRIPT), "--stdin"], input="FVG review #ICT #NQ #US100",
                       capture_output=True, text=True)
    assert p.returncode == 0 and "WARN post 1" in p.stdout
