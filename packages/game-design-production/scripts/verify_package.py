#!/usr/bin/env python3
"""Read-only integrity check. Python 3.10+, standard library only; no network."""
from pathlib import Path
from urllib.parse import unquote
import hashlib
import json
import re
import sys

def verify(root):
    errors = []
    manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    entries = manifest["files"]
    listed = [item["path"] for item in entries]
    if len(listed) != len(set(listed)):
        errors.append("Duplicate manifest path")
    actual = {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()}
    if actual != set(listed) | {"manifest.json"}:
        errors.append("Manifest file list differs from directory contents")
    links = 0
    json_count = 0
    for item in entries:
        path = root / item["path"]
        if not path.resolve().is_relative_to(root.resolve()) or path.is_symlink():
            errors.append("Unsafe path: " + item["path"])
            continue
        if not path.is_file():
            errors.append("Missing file: " + item["path"])
            continue
        raw = path.read_bytes()
        if len(raw) != item["bytes"] or hashlib.sha256(raw).hexdigest() != item["sha256"]:
            errors.append("Content mismatch: " + item["path"])
        if path.suffix == ".json":
            json.loads(raw.decode("utf-8"))
            json_count += 1
        if path.suffix == ".md":
            for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", raw.decode("utf-8")):
                link = link.strip().strip("<>")
                if link.startswith(("https://", "http://", "#")):
                    continue
                target = (path.parent / unquote(link.split("#", 1)[0])).resolve()
                links += 1
                if not target.is_relative_to(root.resolve()) or not target.exists():
                    errors.append("Broken/outside link: " + item["path"] + " -> " + link)
    skill_root = root / ".agents/skills/game-design-handoff"
    skill = (skill_root / "SKILL.md").read_text(encoding="utf-8")
    if not skill.startswith("---\nname: game-design-handoff\n") or "\ndescription:" not in skill:
        errors.append("Invalid Skill frontmatter")
    templates = skill_root / "assets/templates"
    for name, count in [("art-contract.json", 14), ("audio-contract.json", 13)]:
        contract = json.loads((templates / name).read_text(encoding="utf-8"))
        cols = contract["columns"]
        if len(cols) != count or [c["column"] for c in cols] != list(range(1, count + 1)):
            errors.append("Invalid columns: " + name)
    config = json.loads((templates / "configuration-contract.json").read_text(encoding="utf-8"))
    if [r["row"] for r in config["header_rows"]] != [1, 2, 3] or config["data_start_row"] != 4:
        errors.append("Invalid configuration row structure")
    report = {"status": "FAIL" if errors else "PASS", "files": len(entries) + 1,
              "json_files": json_count + 1, "local_links": links, "errors": errors,
              "scope": "Package integrity only; not production-document or game acceptance."}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if errors else 0

if __name__ == "__main__":
    try:
        sys.exit(verify(Path(__file__).resolve().parents[1]))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False))
        sys.exit(1)
