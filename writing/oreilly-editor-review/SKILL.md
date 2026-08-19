---
name: oreilly-editor-review
description: Review, copyedit, format, or revise manuscripts, chapters, articles, captions, code-heavy technical prose, cover copy, and other book content against the complete O'Reilly Style Guide and Word List. Use for O'Reilly house-style checks, style-guide compliance audits, editorial QA, line edits, copyedits, proofreading, terminology normalization, inclusive-language review, or formatting audits covering inline typography, semantic styles, headings, lists, code blocks, figures, tables, examples, captions, cross-references, links, footnotes, generated-AI output, and Word/AsciiDoc/DocBook/InDesign production conventions.
---

# O'Reilly Editor Review

Apply O'Reilly house style without flattening the author's voice. Return actionable findings grounded in the bundled guide snapshot and distinguish definite violations from judgment calls.

## Establish the Review Contract

Infer the deliverable from the request. If it is not stated, default to a findings-only review rather than silently rewriting the manuscript.

Identify, when available:

- Review mode: findings only, annotated edit, clean revision, or answer to a style question
- Scope: excerpt, chapter, full manuscript, cover copy, or production-ready Word content
- Authoring format: AsciiDoc, HTMLBook, DocBook, Word/Google Docs, InDesign, or plain text/Markdown
- Book series and placement context for code line limits
- Book-specific word list or project exceptions

Do not block on missing metadata. Mark format- or series-dependent checks as conditional and state the assumption used.

## Load the Rules

Read [references/house-style.md](references/house-style.md) completely for every review. It contains the editorial and prose rules plus the precedence hierarchy.

Read [references/formatting.md](references/formatting.md) completely for every review. It contains the complete element-treatment matrix and production-format checks. A findings-only prose review still needs the inline typography, heading, list, punctuation, and link checks.

Use [references/word-list.md](references/word-list.md) for spelling, casing, hyphenation, spacing, acronym, and part-of-speech decisions. For focused work, search it with `rg -ni '^[- ]*.*TERM' references/word-list.md`. For an exhaustive manuscript audit, inspect every suspect technical term against it; do not rely on memory.

The official guide changes over time. When the user requests current, latest, authoritative, exhaustive, or publication-ready compliance and network access is available, run:

```bash
python scripts/check_upstream.py
```

If it reports a changed snapshot, consult the official guide before finalizing findings and disclose that the bundled reference needs synchronization. Never allow an unavailable network check to prevent a review; identify the bundled snapshot date instead.

## Review in Passes

Keep separate passes so one category does not hide another.

1. Preserve meaning and voice. Flag factual or technical changes instead of making them under the guise of style.
2. Check the project's explicit exceptions, then the O'Reilly guide, then Chicago 18, then Merriam-Webster's Collegiate. Do not override a higher-precedence decision with a lower-precedence source.
3. Check inclusive, precise, conversational language and company/person agreement.
4. Run the complete formatting audit in `references/formatting.md`: inline styles, block structures, navigation, media/data elements, code, generated-AI material, and source-format production requirements. Report categories that were not inspectable.
5. Check mechanics: spelling, preferred forms, capitalization, acronyms, numbers, dates, punctuation, quotation marks, dashes, ellipses, articles, and hyphenation.
6. Check technical typography without inferring treatment from appearance alone: code versus prose, filenames/paths/URLs, user input, placeholders, SQL, UI labels, packages/libraries, and first-use terms must use the correct semantic role.
7. Check production constraints for the actual authoring format: electronic-format language, live xrefs, code widths, spaces instead of tabs, syntax highlighting, Word tags/comments/line breaks, and filename conventions.
8. Search the word list for each distinctive product name, protocol, platform, technical compound, unit, key name, and common variant. Check nearby entries when a compound's part of speech changes.
9. Re-read every proposed correction in context. Remove false positives inside verbatim quotations, code, generated-AI output, literal UI strings, formal names, intentional voice, and documented exceptions.

## Classify Findings

Use these labels consistently:

- **Required**: direct conflict with an unambiguous O'Reilly rule
- **Conditional**: depends on authoring format, series, placement, project convention, or first/subsequent mention
- **Query**: needs author, editor, or production-editor judgment
- **Suggestion**: improves clarity or tone but is not a house-style requirement

Do not present a Chicago or Merriam-Webster fallback as an explicit O'Reilly rule. Do not invent a correction when the guide says to be consistent; first test the document's internal consistency.

## Report the Review

Lead with the overall result and the highest-risk patterns. For each finding, include:

1. Severity label
2. Location or a short identifying excerpt
3. Current form
4. Proposed form or action
5. Concise rationale and the bundled reference section

Group repeated instances into one pattern finding and give representative locations plus an occurrence count when possible. Keep quoted manuscript text short.

After the findings, include:

- Checks completed, including categories with no findings
- Formatting coverage: inline, block, navigational, figure/table/example, code, AI-output, and format-specific checks; explicitly mark any category not present or not inspectable
- Assumptions and conditional checks not resolved
- Project-level decisions to add to the book-specific word list
- Snapshot status when an upstream check was requested or materially relevant

If asked to revise, apply only high-confidence corrections automatically. Preserve code, commands, URLs, AI-generated output, literal UI labels, quotations, and intentional technical casing unless the relevant rule explicitly requires a change. Surface ambiguous changes as queries.

## Handle Conflicts and Exceptions

- Follow a person's stated language preference.
- Honor verbatim quotations, historical names, code, APIs, literal UI, trademarks, and author-approved terminology; explain unavoidable exceptions.
- Ask the production editor about new element styling, unclear generative-AI categories, deviations from fixed typography, long-caption punctuation schemes, and book-specific questions.
- Record any consistent choice allowed by the guide in the project's word-list document.
- Treat the official online guide as authoritative when it is newer than the bundled snapshot.

## Maintain the Snapshot

Use `scripts/check_upstream.py` to detect upstream changes. After deliberately auditing a new official revision, regenerate the word list with:

```bash
python scripts/update_word_list.py /path/to/production-resources/styleguide/index.md references/word-list.md
```

Then update the prose and formatting references, snapshot metadata in all references and scripts, validate the 26 letter headings and entry counts, and rerun the skill validator. Do not regenerate blindly: upstream prose or formatting changes require human comparison and paraphrase.
