import json

import log_post

NOW = "2026-10-14T16:00+02:00"


def _add(state, topic, concepts, now=NOW):
    return log_post.main(["--state", str(state), "--now", now, "add", "--topic", topic,
                          "--concepts", concepts, "--format", "thread"])


def test_add_and_schema(tmp_path):
    s = tmp_path / "posted.jsonl"
    assert _add(s, "FVG after PDH sweep", "FVG, PDH,displacement") == 0
    rec = json.loads(s.read_text().strip())
    assert rec["concepts"] == ["displacement", "fvg", "pdh"]
    assert rec["platform"] == "x" and rec["posted_at"].startswith("2026-10-14T16:00")
    assert set(rec) == {"posted_at", "platform", "format", "topic", "concepts", "ready_file", "url"}


def test_check_repeat_and_fresh(tmp_path):
    s = tmp_path / "posted.jsonl"
    _add(s, "old", "ob", now="2026-09-01T10:00+02:00")
    _add(s, "recent", "fvg")
    chk = lambda c: log_post.main(["--state", str(s), "--now", "2026-10-15T10:00+02:00",
                                   "check", "--concepts", c, "--days", "7"])
    assert chk("FVG") == 1
    assert chk("ob") == 0
    assert chk("smt") == 0


def test_bad_format(tmp_path):
    s = tmp_path / "p.jsonl"
    assert log_post.main(["--state", str(s), "--now", NOW, "add", "--topic", "t",
                          "--concepts", "fvg", "--format", "tiktok"]) == 2
    assert not s.exists()


def test_check_empty_state(tmp_path):
    assert log_post.main(["--state", str(tmp_path / "none.jsonl"), "check", "--concepts", "fvg"]) == 0


def test_optional_metrics(tmp_path):
    s = tmp_path / "p.jsonl"
    assert log_post.main(["--state", str(s), "--now", NOW, "add", "--topic", "t", "--concepts", "fvg",
                          "--likes", "12", "--impressions", "900"]) == 0
    rec = json.loads(s.read_text().strip())
    assert rec["likes"] == 12 and rec["impressions"] == 900


def test_metrics_omitted_by_default(tmp_path):
    s = tmp_path / "p.jsonl"
    _add(s, "t", "fvg")
    rec = json.loads(s.read_text().strip())
    assert "likes" not in rec and "impressions" not in rec


def test_negative_metrics_rejected(tmp_path):
    s = tmp_path / "p.jsonl"
    assert log_post.main(["--state", str(s), "--now", NOW, "add", "--topic", "t", "--concepts", "fvg",
                          "--likes", "-1"]) == 2
    assert not s.exists()
