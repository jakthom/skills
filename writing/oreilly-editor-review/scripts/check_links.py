#!/usr/bin/env python3
"""Check local and external links used by the O'Reilly editor-review skill."""

from __future__ import annotations

import argparse
import base64
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

URL_PATTERN = re.compile(r"https?://[^\s<>\[\]()'\"`]+")
MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
HEADING_PATTERN = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)
SKIP_HOSTS = {"example.com"}


def default_inputs() -> list[Path]:
    skill_dir = Path(__file__).resolve().parent.parent
    return [skill_dir / "SKILL.md", *sorted((skill_dir / "references").glob("*.md"))]


def extract_urls(paths: list[Path]) -> list[str]:
    urls: set[str] = set()
    for path in paths:
        for match in URL_PATTERN.findall(path.read_text(encoding="utf-8")):
            url = match.rstrip(".,;:!?")
            if urllib.parse.urlparse(url).hostname not in SKIP_HOSTS:
                urls.add(url)
    return sorted(urls)


def heading_anchors(path: Path) -> set[str]:
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    for heading in HEADING_PATTERN.findall(path.read_text(encoding="utf-8")):
        text = re.sub(r"[*_`]", "", heading).strip().lower()
        base = re.sub(r"[^\w\s-]", "", text)
        base = re.sub(r"[\s-]+", "-", base).strip("-")
        count = counts.get(base, 0)
        counts[base] = count + 1
        anchors.add(base if count == 0 else f"{base}-{count}")
    return anchors


def check_local_links(paths: list[Path]) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for source in paths:
        for target in MARKDOWN_LINK_PATTERN.findall(source.read_text(encoding="utf-8")):
            if urllib.parse.urlparse(target).scheme in {"http", "https", "mailto"}:
                continue
            path_text, separator, fragment = target.partition("#")
            destination = source if not path_text else (source.parent / path_text).resolve()
            ok = destination.is_file()
            detail = str(destination)
            if ok and separator and destination.suffix.lower() == ".md":
                ok = fragment in heading_anchors(destination)
                detail = f"{destination}#{fragment}"
            results.append(
                {
                    "kind": "local",
                    "source": str(source),
                    "target": target,
                    "destination": detail,
                    "ok": ok,
                }
            )
    return results


def check_url(url: str, timeout: float) -> tuple[int | None, str]:
    headers = {"User-Agent": "oreilly-editor-review-link-check/1.0"}
    if urllib.parse.urlparse(url).hostname == "prod.oreilly.com":
        token = base64.b64encode(b"guest:").decode("ascii")
        headers["Authorization"] = f"Basic {token}"
    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.status, response.geturl()
    except urllib.error.HTTPError as exc:
        return exc.code, exc.geturl()
    except (OSError, urllib.error.URLError) as exc:
        return None, str(exc)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path, help="Markdown files to scan")
    parser.add_argument("--timeout", type=float, default=20, help="Per-link timeout in seconds")
    parser.add_argument("--json", action="store_true", help="Print machine-readable output")
    args = parser.parse_args()

    paths = args.paths or default_inputs()
    missing = [str(path) for path in paths if not path.is_file()]
    if missing:
        print(f"Missing input files: {', '.join(missing)}", file=sys.stderr)
        return 2

    results = check_local_links(paths)
    for url in extract_urls(paths):
        status, destination = check_url(url, args.timeout)
        results.append(
            {
                "kind": "external",
                "url": url,
                "status": status,
                "destination": destination,
                "ok": status is not None and 200 <= status < 400,
            }
        )

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        for result in results:
            if result["kind"] == "local":
                status = "OK" if result["ok"] else "BROKEN"
                print(f"{status} {result['source']} -> {result['target']}")
                continue
            status = result["status"] if result["status"] is not None else "ERROR"
            print(f"{status} {result['url']}")
            if result["destination"] != result["url"]:
                print(f"  -> {result['destination']}")

    return 0 if results and all(result["ok"] for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
