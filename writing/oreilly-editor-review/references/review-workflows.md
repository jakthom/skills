# Review and Artifact Workflows

Read this reference for full manuscripts, multiple files, annotated edits, clean revisions, or document artifacts. The aim is to make review coverage reproducible and to preserve the user's source and editorial history.

## Choose the Deliverable

| Requested result | Source handling | Deliverable |
|---|---|---|
| Style answer | Read only the cited passage and relevant rules | Direct answer with rule source and any dependency |
| Findings-only review | Do not modify source | Findings plus coverage and assumptions |
| Annotated edit | Preserve original text, comments, and revision history | Separate annotated artifact plus unresolved queries |
| Clean revision | Apply accepted, high-confidence edits | Separate clean artifact plus a concise change summary |
| Conversion-ready Word content | Work only after editorial decisions are resolved | Verified conversion copy with changes accepted and comments converted as required |

If the request names no deliverable, use findings only. Do not turn a review request into an edited artifact.

## Inventory the Source

Before reviewing more than one file, create a coverage ledger containing:

- Stable relative path or artifact name
- Format and role, such as chapter, appendix, figure list, or project word list
- Size measure suitable for the source, such as lines and words or document pages
- Review status for prose, word-list terms, inline semantics, blocks, navigation, code, and format-specific production checks
- Assumptions, exclusions, and the reason for every exclusion

Use one row per source and these states: `complete`, `not applicable`, `uninspectable`, or `pending`.

| Source | Role/size | Prose | Terms | Inline | Blocks | Navigation | Code | Format-specific | Notes |
|---|---|---|---|---|---|---|---|---|---|
| `relative/path` | chapter; lines/words | pending | pending | pending | pending | pending | pending | pending | |

Use `rg --files` or the format's package manifest to enumerate text sources. Include book-level files, appendixes, captions, tables, sidebars, and front or back matter when they are in scope. Treat included AsciiDoc files and XML entities as source files, even when a chapter references them indirectly. Record binary or unavailable dependencies rather than silently omitting them.

For a large manuscript, review in bounded units while keeping shared ledgers for:

- Repeated findings and exact occurrence counts
- Project terminology and allowed variants
- Acronym first-use state
- Figure, table, example, and cross-reference targets
- Code-series and placement assumptions
- Queries and book-specific decisions

After all units are reviewed, run a cross-file consistency pass, resolve duplicate findings, and reconcile the coverage ledger with the original inventory. A search hit count is evidence only when the searched file set and pattern are recorded and literal contexts such as code or quotations have been excluded or reviewed.

## Preserve Locations

Use locations a reviewer can reproduce:

- Text source: relative path and line number; add a heading or element ID when useful
- Word document: filename, heading or named style, paragraph-identifying excerpt, and table/figure number when applicable
- PDF or rendered proof: filename and page number; say that semantic tagging was not inspectable
- XML/HTML/IDML: relative path plus line number and element ID or XPath-like element description

Keep quoted manuscript text short. When edits change line numbers, retain an original-location field in the finding ledger.

## Handle Each Artifact Type

### Plain text, Markdown, AsciiDoc, HTMLBook, DocBook, XML, and IDML

Inspect source markup rather than rendered appearance. Preserve IDs, attributes, entities, includes, whitespace-sensitive code, and generated content. Parse or validate structured files with an appropriate tool when available; do not use global replacements across markup boundaries without inspecting each change.

For a revision, write to a separate output tree unless the user requests in-place edits. Re-run available validation and compare the inventory before and after so no source file or included fragment disappears.

### Word and Google Docs exports

When a `.docx` file is involved, use the environment's document-specific workflow or skill when available. Inspect both rendered pages and the underlying OOXML or document model for paragraph styles, character styles, fields, comments, tracked revisions, tables, figure holders, captions, code tabs, and manual line breaks. A visual review alone cannot prove correct semantic tagging.

For annotated review, leave tracked changes and comments intact. For a clean revision, preserve an untouched original and render the result to verify pagination, tables, figures, headings, lists, and code. Accept all revisions and transform comments into O'Reilly `Comment` paragraphs only for a final conversion-ready copy explicitly requested after queries are resolved.

For a live Google Doc, do not infer access or permission to edit. If only an export is available, report that live comments, suggestion history, or named styles may differ from the source document.

### InDesign

Use IDML for semantic and structural inspection. A native `.indd` file requires InDesign-capable tooling; a PDF export supports visual proofreading but cannot establish paragraph/character style correctness, anchored-object structure, or live cross-references. Mark those checks uninspectable unless IDML or equivalent source is available.

### PDF proofs

Use page rendering for visual QA and text extraction for searches, then verify findings against the rendered page. Hyphenation, ligatures, headers, and line wraps in extracted text may be artifacts. PDF review can establish visible output but not source semantics.

## Validate a Revised Artifact

Use checks proportional to the format:

1. Confirm every input file or package part is represented in the output inventory.
2. Re-run structural validation or package opening checks.
3. Render document formats and inspect affected pages plus representative unchanged pages.
4. Re-run searches for corrected patterns and review remaining hits in context.
5. Verify code, commands, links, IDs, xrefs, captions, tables, comments, and tracked changes according to the chosen deliverable.
6. Report the output path, checks performed, unresolved queries, and any check the available tools could not perform.

Do not describe a revision as conversion-ready when validation fails, tracked editorial decisions remain unresolved, or required semantic checks were unavailable.
