# Source-Format Review Guide

Read the section for the manuscript's actual source format when semantic formatting or production readiness is in scope. O'Reilly's style guide defines the desired treatment; this reference identifies the source evidence needed to verify that treatment.

## Shared Rules

- Inspect semantic markup, named styles, fields, and IDs. Matching visual appearance is insufficient.
- Preserve book-wide IDs, include relationships, code whitespace, links, and generated material.
- Separate a source defect from an output defect: record both when incorrect markup produces incorrect rendering.
- If a project template or production-editor instruction differs from this snapshot, the project-specific instruction controls.
- Mark a check conditional or uninspectable when the available artifact does not expose the needed semantics.

## AsciiDoc for O'Reilly Atlas

The former O'Reilly “Writing in AsciiDoc” site is no longer live. The conventions below preserve the O'Reilly Atlas forms needed by this style-guide audit. They are based on the [archived O'Reilly authoring guide](https://web.archive.org/web/20221231051337/https://docs.atlas.oreilly.com/writing_in_asciidoc.html) and O'Reilly's current public [AsciiDoc book samples](https://github.com/oreillymedia/orm_book_samples/tree/master/asciidoc_only). Atlas used a customized Asciidoctor implementation, so do not assume every feature in current generic Asciidoctor documentation is supported by an existing O'Reilly project.

### Structure and inline roles

| Meaning | Expected source form |
|---|---|
| Chapter with stable ID | `[[chapter_id]]` followed by `== Chapter Title` |
| A-, B-, and C-level headings within a chapter | `===`, `====`, and `=====` respectively |
| Italic semantic role | `_text_`; use doubled underscores when markup abuts a word character |
| Constant width | `+text+`; use doubled plus signs when markup abuts another character |
| User input, constant-width bold | `*+text+*`; the asterisks remain outside the plus signs |
| Placeholder, constant-width italic | `_++text++_`; the underscores remain outside doubled plus signs |
| External descriptive link | `https://example.com[descriptive text]` |
| Footnote | `footnote:[Text]` closed up immediately after the preceding text or punctuation |

Use the semantic treatment matrix in `formatting.md` to decide which form applies. Escaped or passthrough markup may be needed when delimiters occur literally or roles are nested; inspect the rendered output rather than rewriting uncertain nesting mechanically.

### Blocks and navigation

- Sidebar: optional `.Title`, then content between `****` delimiters.
- Admonition: optional `.Title`, then `[NOTE]`, `[TIP]`, `[WARNING]`, or `[CAUTION]` with content between `====` delimiters.
- Bulleted, ordered, and variable lists use `*`, `.`, and `Term::` forms. A `+` on its own line continues a list item with another block.
- A formal figure needs a book-unique ID, caption, image macro, and alt text: `[[id]]`, `.Caption`, then `image::path["alt text"]`. An untitled image is unnumbered and cannot be a formal xref target.
- A formal table needs a unique ID when referenced, a `.Title`, and a table block. Check consistent cell counts and header options.
- Use `<<target_id>>` for references to titled book components. IDs must be unique across the book, contain no spaces, and not begin with a digit. Plain-text figure or chapter numbers are not live xrefs.
- An unresolved xref may render as `???`; search built output for that marker when output is available.

### Code

- An ordinary listing uses `----` delimiters and spaces for indentation.
- Syntax-highlighted code uses `[source,lexer]` immediately before the listing. Verify the lexer against Pygments.
- A titled, cross-referenceable example wraps the listing in an example block with `[[id]]`, `.Title`, and `====` delimiters.
- An external plain-text code file may be included with `include::path[]` inside a listing block. Follow includes when measuring lines or reviewing callouts.
- Code callout markers such as `<1>` must have a one-to-one matching callout list after the block.
- Generated-AI programming exchanges do not receive syntax highlighting even when they contain code.

When an Atlas build or compatible project command is available, run it and inspect validation messages, unresolved xrefs, includes, and rendered output. If no compatible renderer is available, report syntax checks as source inspection rather than build validation.

## HTMLBook

Use O'Reilly's [HTMLBook specification](https://oreillymedia.github.io/HTMLBook/) for exact elements and content models. Inspect XHTML source and validate against the schema supplied by the project or the specification repository when available.

Check `data-type` values, heading levels, IDs, `href` targets, figures and captions, table structure, footnotes, sidebars/admonitions, code elements, and inline semantic elements. Verify that all IDs are unique and every local link target exists. An HTML rendering cannot prove that the XHTML source follows the HTMLBook content model.

## DocBook

Use the project's declared DocBook version. Consult the [DocBook standard](https://docbook.org/) and O'Reilly's [DocBook Authoring Guidelines](https://prod.oreilly.com/external/tools/docbook/docs/authoring/) when exact project markup is in scope; the latter uses username `guest` with a blank password.

Inspect semantic inline elements, program listings and language attributes, titled formal objects, IDs, entities, includes, and `<xref>` targets. Use `<xref>` for referenced figures, tables, examples, sections, and sidebars rather than typing generated labels into prose. Validate against the project's schema or DTD with network access disabled unless external retrieval is explicitly intended. Resolve every missing entity and broken xref before claiming production readiness.

## Word and Google Docs

Use O'Reilly's [Word Template Quickstart Guide](https://oreillymedia.github.io/production-resources/word/) and the project template. Verify named paragraph and character styles in the document model as well as their visible rendering.

Check code margins, spaces in place of tabs, preserved indentation, syntax-highlight styles, table-cell styles including empty cells, `CellSubheading` below the first row, `FigureHolder` immediately followed by `FigureTitle`, caption and example styles, headings, lists, hyperlinks, comments, fields, tracked changes, and manual line breaks. Follow the deliverable-specific rules in `review-workflows.md`; conversion cleanup must not erase review history from an annotated edit.

## IDML and InDesign

Inspect IDML package XML for paragraph and character style names, stories, anchored objects, links, tables, and cross-reference resources. Confirm that URLs are not anchored to descriptive text in InDesign projects. Rendered PDF evidence can supplement IDML inspection but cannot replace it. Treat a native `.indd` file without InDesign-capable tooling as unavailable source.

## Plain Text and Markdown

Apply prose and word-list rules directly. Record semantic treatments that the format cannot distinguish, such as separate roles for user input and placeholders, as conditional production requirements. Do not claim conversion readiness unless the destination format and its mapping are known.
