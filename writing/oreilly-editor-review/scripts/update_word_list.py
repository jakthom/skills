#!/usr/bin/env python3
"""Regenerate references/word-list.md from an audited official index.md."""

from __future__ import annotations

import argparse
import re
from html import unescape
from html.parser import HTMLParser
from pathlib import Path

OFFICIAL_SOURCE = "https://oreillymedia.github.io/production-resources/styleguide/"


class WordListParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_word_list = False
        self.in_h2 = False
        self.heading_parts: list[str] = []
        self.current_letter = ""
        self.ul_depth = 0
        self.li_depth = 0
        self.current_parts: list[str] = []
        self.nested_parts: list[str] = []
        self.entries: dict[str, list[tuple[str, list[str]]]] = {}
        self.inline_stack: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "section" and attributes.get("id") == "word-list":
            self.in_word_list = True
        if not self.in_word_list:
            return
        if tag == "h2":
            self.in_h2 = True
            self.heading_parts = []
        elif tag == "ul":
            self.ul_depth += 1
        elif tag == "li":
            self.li_depth += 1
            if self.li_depth == 1:
                self.current_parts = []
                self.nested_parts = []
            elif self.li_depth == 2:
                self.nested_parts.append("")
        elif tag in {"em", "i"}:
            self._append("*")
            self.inline_stack.append("*")
        elif tag == "code":
            self._append("`")
            self.inline_stack.append("`")
        elif tag in {"sub", "subscript"}:
            self._append("<sub>")
            self.inline_stack.append("</sub>")

    def handle_endtag(self, tag: str) -> None:
        if not self.in_word_list:
            return
        if tag == "h2" and self.in_h2:
            letter = clean("".join(self.heading_parts))
            if len(letter) == 1 and letter.isalpha():
                self.current_letter = letter.upper()
                self.entries.setdefault(self.current_letter, [])
            self.in_h2 = False
        elif tag == "li":
            if self.li_depth == 1 and self.current_letter:
                entry = clean("".join(self.current_parts))
                nested = [clean(item) for item in self.nested_parts if clean(item)]
                self.entries[self.current_letter].append((entry, nested))
            self.li_depth -= 1
        elif tag == "ul":
            self.ul_depth -= 1
        elif tag in {"em", "i", "code", "sub", "subscript"} and self.inline_stack:
            self._append(self.inline_stack.pop())

    def handle_data(self, data: str) -> None:
        if self.in_h2:
            self.heading_parts.append(data)
        elif self.in_word_list and self.li_depth:
            self._append(data)

    def handle_entityref(self, name: str) -> None:
        self._append(unescape(f"&{name};"))

    def handle_charref(self, name: str) -> None:
        self._append(unescape(f"&#{name};"))

    def _append(self, value: str) -> None:
        if self.li_depth >= 2 and self.nested_parts:
            self.nested_parts[-1] += value
        elif self.li_depth == 1:
            self.current_parts.append(value)


def clean(value: str) -> str:
    value = unescape(value)
    value = value.replace("<sub>", "\u0000SUBOPEN\u0000")
    value = value.replace("</sub>", "\u0000SUBCLOSE\u0000")
    value = value.replace("<", "&lt;").replace(">", "&gt;")
    value = value.replace("\u0000SUBOPEN\u0000", "<sub>")
    value = value.replace("\u0000SUBCLOSE\u0000", "</sub>")
    return re.sub(r"\s+", " ", value).strip()


def render(entries: dict[str, list[tuple[str, list[str]]]], source: str) -> str:
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    missing = [letter for letter in letters if letter not in entries]
    if missing:
        raise ValueError(f"Missing letter sections: {', '.join(missing)}")
    count = sum(len(entries[letter]) for letter in letters)
    if count != 600:
        raise ValueError(f"Expected 600 top-level entries, found {count}")
    lines = [
        "# O'Reilly Word List: Complete Snapshot",
        "",
        f"Generated from the audited official source `{source}`. This snapshot contains all {count} top-level entries under all 26 letter headings. Preserve spellings, casing, spacing, hyphenation, typography, and usage notes exactly when applying a listed form.",
        "",
        "Use the O'Reilly list first and Merriam-Webster's Collegiate Dictionary when a term is absent. Parenthetical abbreviations in the source include `a` (adjective), `n` (noun), `v` (verb), `s` (singular), `p` (plural), `lc` (lowercase), and `prep. phrase` (prepositional phrase). A note to “be consistent” requires a document-wide consistency check rather than an arbitrary replacement.",
        "",
        "## Contents",
        "",
        " | ".join(f"[{letter}](#{letter.lower()})" for letter in letters),
        "",
    ]
    for letter in letters:
        lines.extend([f"## {letter}", ""])
        for entry, nested in entries[letter]:
            lines.append(f"- {entry}")
            for child in nested:
                lines.append(f"  - {child}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", help="Audited official styleguide/index.md")
    parser.add_argument("output", help="Destination word-list Markdown file")
    parser.add_argument(
        "--source-label",
        default=OFFICIAL_SOURCE,
        help="Provenance label written into the generated reference",
    )
    args = parser.parse_args()

    source = Path(args.source)
    extractor = WordListParser()
    extractor.feed(source.read_text(encoding="utf-8"))
    Path(args.output).write_text(render(extractor.entries, args.source_label), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
