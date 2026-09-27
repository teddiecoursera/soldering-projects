#!/usr/bin/env python3
"""Validate, moderate and render the ESP32 project list.

    python scripts/curate.py validate          # offline schema/duplicate checks
    python scripts/curate.py render            # regenerate README.md from projects.yml
    python scripts/curate.py render --check    # fail if README.md is out of date
    python scripts/curate.py audit             # live GitHub checks (set GITHUB_TOKEN)
"""

import argparse
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "projects.yml"
README = ROOT / "README.md"
BEGIN, END = "<!-- BEGIN LIST -->", "<!-- END LIST -->"

# Moderation thresholds; keep in sync with CONTRIBUTING.md.
MIN_STARS = 500
MAX_INACTIVE_DAYS = 730

REQUIRED = {"name", "repo", "category", "description"}
OPTIONAL = {"hardware", "license", "acclaim", "note"}
REPO_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")


def load():
    with DATA.open() as f:
        return yaml.safe_load(f)


def validate(data):
    errors = []
    categories = data.get("categories") or {}
    seen_repos, seen_names = {}, {}
    for i, p in enumerate(data.get("projects") or []):
        where = f"projects[{i}] ({p.get('name', '?')})"
        missing = REQUIRED - p.keys()
        unknown = p.keys() - REQUIRED - OPTIONAL
        if missing:
            errors.append(f"{where}: missing {sorted(missing)}")
        if unknown:
            errors.append(f"{where}: unknown fields {sorted(unknown)}")
        repo = str(p.get("repo", ""))
        if not REPO_RE.match(repo):
            errors.append(f"{where}: repo must be 'owner/name', got {repo!r}")
        if p.get("category") not in categories:
            errors.append(f"{where}: unknown category {p.get('category')!r}")
        desc = str(p.get("description", ""))
        if len(desc) > 120:
            errors.append(f"{where}: description longer than 120 chars")
        if desc.endswith("."):
            errors.append(f"{where}: description should not end with a period")
        if "hardware" in p and not isinstance(p["hardware"], bool):
            errors.append(f"{where}: hardware must be true/false")
        for key, seen in ((repo.lower(), seen_repos), (str(p.get("name", "")).lower(), seen_names)):
            if key in seen:
                errors.append(f"{where}: duplicate of {seen[key]}")
            seen[key] = where
    return errors


def render(data):
    lines = []
    projects = data["projects"]
    for key, title in data["categories"].items():
        entries = sorted((p for p in projects if p["category"] == key), key=lambda p: p["name"].lower())
        if not entries:
            continue
        lines += [f"### {title}", "", "| Project | Description | Stars | Last commit |", "|---|---|---|---|"]
        for p in entries:
            repo = p["repo"]
            name = f"[{p['name']}](https://github.com/{repo})"
            desc = p["description"]
            if p.get("hardware"):
                desc += " 🔧"
            if p.get("note"):
                desc += f" ⚠️ _{p['note']}_"
            stars = f"![stars](https://img.shields.io/github/stars/{repo}?style=flat-square&label=)"
            commit = f"![last commit](https://img.shields.io/github/last-commit/{repo}?style=flat-square&label=)"
            lines.append(f"| {name} | {desc} | {stars} | {commit} |")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def write_readme(body, check):
    text = README.read_text()
    if BEGIN not in text or END not in text:
        sys.exit(f"README.md is missing the {BEGIN} / {END} markers")
    head, rest = text.split(BEGIN, 1)
    _, tail = rest.split(END, 1)
    new = f"{head}{BEGIN}\n{body}{END}{tail}"
    if check:
        if new != text:
            sys.exit("README.md is out of date: run `python scripts/curate.py render`")
        print("README.md is up to date")
    else:
        README.write_text(new)
        print("README.md regenerated")


def github(repo, token):
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}")
    req.add_header("Accept", "application/vnd.github+json")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        return {"_error": f"HTTP {e.code}"}


def audit(data):
    """Check every entry against the live moderation criteria. Returns failure lines."""
    token = os.environ.get("GITHUB_TOKEN")
    now = dt.datetime.now(dt.timezone.utc)
    failures, rows = [], []
    for p in data["projects"]:
        info = github(p["repo"], token)
        problems = []
        if "_error" in info:
            problems.append(f"unreachable ({info['_error']})")
        else:
            if info["full_name"].lower() != p["repo"].lower():
                problems.append(f"moved to {info['full_name']}")
            if info.get("archived"):
                problems.append("archived")
            pushed = dt.datetime.fromisoformat(info["pushed_at"].replace("Z", "+00:00"))
            idle = (now - pushed).days
            if idle > MAX_INACTIVE_DAYS:
                problems.append(f"no push for {idle} days")
            if info["stargazers_count"] < MIN_STARS and not p.get("acclaim"):
                problems.append(f"{info['stargazers_count']} stars < {MIN_STARS} and no `acclaim` link")
            spdx = (info.get("license") or {}).get("spdx_id")
            if (not spdx or spdx == "NOASSERTION") and not p.get("license"):
                problems.append("no license detected by GitHub and no verified `license`")
        stars = info.get("stargazers_count", "?")
        detected = (info.get("license") or {}).get("spdx_id")
        lic = detected if detected and detected != "NOASSERTION" else p.get("license", "?")
        status = "; ".join(problems) or "ok"
        rows.append(f"| {p['name']} | {stars} | {lic} | {status} |")
        if problems:
            failures.append(f"{p['name']} ({p['repo']}): {status}")

    report = "\n".join(["| Project | Stars | License | Status |", "|---|---|---|---|", *rows])
    print(report)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a") as f:
            f.write("## ESP32 list audit\n\n" + report + "\n")
    return failures


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("validate")
    r = sub.add_parser("render")
    r.add_argument("--check", action="store_true")
    sub.add_parser("audit")
    args = ap.parse_args()

    data = load()
    errors = validate(data)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)

    if args.cmd == "validate":
        print(f"{len(data['projects'])} projects OK")
    elif args.cmd == "render":
        write_readme(render(data), args.check)
    elif args.cmd == "audit":
        failures = audit(data)
        if failures:
            print("\nNeeds moderation:\n  " + "\n  ".join(failures), file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
