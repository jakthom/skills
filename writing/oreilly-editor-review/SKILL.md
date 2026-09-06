---
name: oreilly-editor-review
description: Review or revise O'Reilly book content for house style, word-list terminology, semantic formatting, and production readiness. Use for O'Reilly-specific style questions, copyedits, proofreading, manuscript audits, and source-format QA; use a general writing workflow when O'Reilly conventions are not requested or relevant.
---

# O'Reilly Editor Review

Apply O'Reilly house style without flattening the author's voice. Ground findings in the bundled guide snapshot, distinguish definite violations from judgment calls, and state what the available artifact does and does not let you inspect.

## Route the Request

Load only the rules needed for the requested work:

- **Focused style question:** read the relevant section of [references/house-style.md](references/house-style.md) or [references/formatting.md](references/formatting.md), then search [references/word-list.md](references/word-list.md) when a term is involved.
- **Prose copyedit or proofread:** read `house-style.md` completely. Read the relevant formatting sections for headings, lists, punctuation, links, and any structured elements present. Search the word list for every suspect technical term.
- **Formatting or production audit:** read `formatting.md` completely and the applicable section of [references/authoring-formats.md](references/authoring-formats.md). Add `house-style.md` when prose is also in scope.
- **Cover copy:** read “Cover-copy formatting” in `formatting.md`, the relevant prose rules in `house-style.md`, and any applicable word-list entries.
- **Exhaustive or publication-ready audit:** read all three bundled guide references completely, use `authoring-formats.md` for the actual source format, and verify the upstream snapshot.
- **Full manuscript, multiple files, annotated edit, clean revision, or document artifact:** also read [references/review-workflows.md](references/review-workflows.md).

For focused word-list work, search case-insensitively and inspect nearby entries and part-of-speech variants:

```bash
rg -ni -- 'search term' references/word-list.md
```

Do not treat absence from the word list as permission to guess. Apply rules in this order:

1. Documented book-specific decision or production-editor instruction
2. O'Reilly Style Guide and Word List
3. *The Chicago Manual of Style*, 18th edition
4. *Merriam-Webster's Collegiate Dictionary*

Identify lower-precedence decisions as fallbacks rather than explicit O'Reilly rules.

## Establish the Review Contract

Infer the deliverable from the request. If it is not stated, return findings only and leave the source unchanged.

Identify, when available:

- Review mode: findings only, annotated edit, clean revision, or answer to a style question
- Scope: excerpt, chapter, full manuscript, cover copy, or conversion-ready content
- Authoring format: AsciiDoc, HTMLBook, DocBook, Word/Google Docs, IDML/InDesign, or plain text/Markdown
- Book series and element placement for code line limits
- Book-specific word list and project exceptions

Do not block on missing metadata. Mark format-, series-, or project-dependent checks as conditional and state the assumption used. Do not claim semantic-format compliance from a rendered view alone.

## Verify Currency When It Matters

The bundled references snapshot the official guide at the commit and date recorded in each file. When the user requests current, latest, authoritative, exhaustive, or publication-ready compliance and network access is available, run from the skill directory:

```bash
python scripts/check_upstream.py
```

If it reports `CHANGED`, consult the official guide before finalizing affected findings and disclose that the bundle needs synchronization. If the network is unavailable, continue with the bundled snapshot and report its date. Never imply that a successful snapshot check validates book-specific instructions or separate authoring guides.

## Review in Distinct Passes

1. Preserve meaning and voice. Flag factual or technical changes instead of making them as style edits.
2. Apply project exceptions and the source hierarchy before proposing corrections.
3. Check inclusive, precise, conversational language and singular agreement for companies and collective entities.
4. Audit every inspectable element category in `formatting.md`: inline roles, blocks, navigation, media and data elements, code, generated-AI material, and format-specific production requirements.
5. Check mechanics: spelling, preferred forms, capitalization, acronyms, numbers, dates, punctuation, quotation marks, dashes, ellipses, articles, and hyphenation.
6. Check technical typography from semantic markup or styles: code versus prose, filenames and paths, links, user input, placeholders, SQL, UI labels, packages and libraries, and first-use terms.
7. Search the word list for distinctive product names, protocols, platforms, technical compounds, units, key names, and common variants.
8. Re-read every proposed correction in context. Remove false positives in quotations, code, generated-AI output, literal UI strings, formal names, intentional voice, and documented exceptions.

For large or multi-file work, use the coverage ledger and aggregation procedure in `review-workflows.md`. A sample, partial scan, or unreviewed file cannot support a “complete manuscript” conclusion.

## Classify and Report Findings

Use these labels consistently:

- **Required:** direct conflict with an unambiguous O'Reilly rule
- **Conditional:** depends on source format, series, placement, project convention, or first/subsequent mention
- **Query:** needs author, editor, or production-editor judgment
- **Suggestion:** improves clarity or tone but is not a house-style requirement

When the guide permits multiple forms, first test document-wide consistency. Do not invent a preferred form.

Lead with the overall result and highest-risk patterns. For each finding, give the label, stable location or short excerpt, current form, proposed form or action, concise rationale, and bundled reference section. Consolidate repeated instances and give a reproducible occurrence count when possible.

End with:

- Checks completed, including categories with no findings
- Formatting coverage: inline, block, navigation, figures/tables/examples, code, AI output, and source-format checks
- Categories absent, uninspectable, or only partially inspected
- Assumptions and unresolved conditional checks
- Decisions to record in the project word list
- Snapshot status when checked or materially relevant

Do not call a review exhaustive, complete, or publication-ready unless every in-scope source file appears in the coverage ledger and every applicable category has a recorded result.

## Revise Safely

Edit only when the user requests a revision. Apply high-confidence corrections automatically and surface ambiguous changes as queries. Preserve code, commands, URLs, AI-generated output, literal UI labels, quotations, and intentional technical casing unless a controlling rule explicitly requires a change.

For an annotated edit, preserve comments and tracked changes. Accepting changes and converting comments into production paragraphs belongs only to a specifically requested, final conversion-ready deliverable after editorial decisions have been resolved. Create a separate output artifact unless the user explicitly requests in-place editing. Follow the artifact verification and delivery rules in `review-workflows.md`.

Honor a person's stated language preference, historical names, APIs, trademarks, literal UI, verbatim material, and approved terminology. Record unclear styling, AI categories, caption schemes, and project-specific choices as queries for the editor or production editor; do not contact anyone without user authorization.

## Maintain the Snapshot

Use `scripts/check_upstream.py` to detect source changes. After deliberately auditing a new official revision, regenerate the word list with:

```bash
python scripts/update_word_list.py /path/to/production-resources/styleguide/index.md references/word-list.md
```

Use `--expected-count N` only when independently verifying a known inventory. Then update the prose and formatting references, source commit, snapshot dates and hashes, expected inventory in `check_upstream.py`, and the provenance in `authoring-formats.md` if source-format guidance changed. Run the skill validator, script checks, word-list round-trip test, and `python scripts/check_links.py`. Do not regenerate blindly: prose and formatting changes require comparison and careful paraphrase.
