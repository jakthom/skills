#!/usr/bin/env python3
"""Check whether the bundled O'Reilly style-guide snapshot is still current."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

RAW_URL = (
    "https://raw.githubusercontent.com/oreillymedia/production-resources/"
    "gh-pages/styleguide/index.md"
)
EXPECTED_SHA256 = "03bda3ddca167a65e31f6e019723e8fb6a03c7e932a7ebcd09fd589b82ae8383"
EXPECTED_COMMIT = "5b601621124fc7ae8f32f69dfaeae348bc8c2ac2"
EXPECTED_WORD_ENTRIES = 600
EXPECTED_LETTERS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


class InventoryParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_word_list = False
        self.in_heading = False
        self.heading_tag = ""
        self.heading_text: list[str] = []
        self.headings: list[str] = []
        self.letters: list[str] = []
        self.current_letter = ""
        self.ul_depth = 0
        self.li_depth = 0
        self.word_entries = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "section" and attributes.get("id") == "word-list":
            self.in_word_list = True
        if tag in {"h1", "h2", "h3", "h4"}:
            self.in_heading = True
            self.heading_tag = tag
            self.heading_text = []
        if self.in_word_list and tag == "ul":
            self.ul_depth += 1
        elif self.in_word_list and tag == "li":
            self.li_depth += 1
            if self.ul_depth == 1 and self.li_depth == 1:
                self.word_entries += 1

    def handle_endtag(self, tag: str) -> None:
        if self.in_heading and tag == self.heading_tag:
            heading = " ".join("".join(self.heading_text).split())
            if heading:
                self.headings.append(heading)
                if self.in_word_list and tag == "h2" and len(heading) == 1:
                    self.letters.append(heading)
                    self.current_letter = heading
            self.in_heading = False
        if self.in_word_list and tag == "li":
            self.li_depth -= 1
        elif self.in_word_list and tag == "ul":
            self.ul_depth -= 1

    def handle_data(self, data: str) -> None:
        if self.in_heading:
            self.heading_text.append(data)


def load_source(source: str | None) -> bytes:
    if source:
        return Path(source).read_bytes()
    request = urllib.request.Request(RAW_URL, headers={"User-Agent": "oreilly-styleguide-review"})
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", help="Check a local upstream index.md instead of the network")
    parser.add_argument("--json", action="store_true", help="Print machine-readable output")
    args = parser.parse_args()

    try:
        payload = load_source(args.source)
    except (OSError, urllib.error.URLError) as exc:
        print(f"Unable to read upstream guide: {exc}", file=sys.stderr)
        return 2

    digest = hashlib.sha256(payload).hexdigest()
    inventory = InventoryParser()
    inventory.feed(payload.decode("utf-8"))
    result = {
        "current": digest == EXPECTED_SHA256,
        "expected_commit": EXPECTED_COMMIT,
        "expected_sha256": EXPECTED_SHA256,
        "actual_sha256": digest,
        "word_entries": inventory.word_entries,
        "expected_word_entries": EXPECTED_WORD_ENTRIES,
        "letter_headings": inventory.letters,
        "letter_inventory_complete": inventory.letters == EXPECTED_LETTERS,
        "headings": inventory.headings,
        "source": args.source or RAW_URL,
    }
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        status = "CURRENT" if result["current"] else "CHANGED"
        print(f"Snapshot status: {status}")
        print(f"Expected commit: {EXPECTED_COMMIT}")
        print(f"Expected SHA-256: {EXPECTED_SHA256}")
        print(f"Actual SHA-256:   {digest}")
        print(f"Word-list entries: {inventory.word_entries} (expected {EXPECTED_WORD_ENTRIES})")
        print(f"Letter headings: {''.join(inventory.letters)}")
        if not result["current"]:
            print("Audit upstream changes before relying on the bundled snapshot.")
    return 0 if result["current"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
