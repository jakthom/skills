# O'Reilly Formatting and Production Rules

Bundled snapshot: official O'Reilly Style Guide `gh-pages` commit `5b601621124fc7ae8f32f69dfaeae348bc8c2ac2`, dated 2026-04-14. Source: <https://oreillymedia.github.io/production-resources/styleguide/>. Use this reference with [house-style.md](house-style.md) and [word-list.md](word-list.md).

## Contents

- [Formatting audit sequence](#formatting-audit-sequence)
- [Inline typography and semantic styles](#inline-typography-and-semantic-styles)
- [Headings, sidebars, and admonitions](#headings-sidebars-and-admonitions)
- [Lists](#lists)
- [Links and cross-references](#links-and-cross-references)
- [Figures, tables, and examples](#figures-tables-and-examples)
- [Code formatting](#code-formatting)
- [Generative AI material](#generative-ai-material)
- [Footnotes and punctuation-sensitive formatting](#footnotes-and-punctuation-sensitive-formatting)
- [Format-specific production checks](#format-specific-production-checks)
- [Implementation references](#implementation-references)
- [Cover-copy formatting](#cover-copy-formatting)

## Formatting Audit Sequence

Inspect source markup or semantic styles when available; visual appearance alone cannot distinguish correct tagging from manual imitation.

1. Inventory every inline role: emphasis, technical term, code element, user input, placeholder, filename/path, URL/email/domain, key or menu label, package/library, and annotation.
2. Inventory every block role: heading level, paragraph, list type and nesting, code block, generated-AI exchange, admonition, sidebar, figure, table, example, caption/title, and footnote.
3. Verify navigation: live xrefs, descriptive links, numbered-element introductions, and print/ebook-safe language.
4. Apply the authoring-format checks for AsciiDoc, DocBook, Word/Google Docs, HTMLBook, InDesign, or plain text/Markdown.
5. Check code widths against both series and placement. Verify indentation, lexer use, and block introductions.
6. Report missing semantic information as **Conditional** or **Query** rather than claiming visual conformity.

## Inline Typography and Semantic Styles

Use semantic tagging appropriate to the source format. Ask the editor before deviating from a fixed convention or styling a new element. URLs remain italic; a project may vary some other conventions only with approval.

| Element | Required final treatment |
|---|---|
| Filenames, file extensions such as `.jpeg`, and directory paths | Italic body font |
| URLs, URIs, email addresses, and domain names | Italic body font |
| Emphasis | Italic, not bold |
| First occurrence of a technical term | Italic body font |
| Code blocks | Constant width |
| Registry keys | Constant width |
| Classes, types, namespaces, attributes, methods, variables, keywords, functions, modules, commands, properties, parameters, values, objects, events, XML/HTML tags, and comparable language or script elements | Constant width |
| SQL commands such as `SELECT`, `INSERT`, `ALTER TABLE`, and `CREATE INDEX` | Constant-width capitals |
| Replaceable syntax items and placeholders | Constant-width italic |
| Commands or text the user must type | Constant-width bold |
| Line annotations | Smaller italic body font |
| A placeholder inside an already italic path, URL, or similar string | Keep the surrounding italic treatment and distinguish the placeholder with the source format's semantic convention |
| Keyboard accelerators/keys such as `Ctrl` and `Shift`; menu titles, options, and buttons | Roman body text |
| Packages and libraries such as NumPy, scikit-learn, TensorFlow, and rJava | Roman body text with conventional casing |

Use straight quotation marks in constant-width text and code. Preserve literal Unix-command backticks. Match the casing of on-screen labels. Quote a multiword lowercase or mixed-case label only when needed to distinguish it from surrounding prose. Omit a UI menu item's displayed trailing ellipsis when naming it in running text.

## Headings, Sidebars, and Admonitions

- Do not put inline code, bold, italics, or other style markup in a heading.
- Expand an acronym unless it is common and familiar to the audience.
- Put body text immediately after every heading. Do not follow one heading directly with another heading or an admonition.
- Do not stack headings, sidebars, or admonitions.
- Use title case for A- and B-level headings in most templates. Capitalize main words; lowercase articles, conjunctions, and technical/program names whose conventional spelling is lowercase.
- Use sentence case for C-level headings. Capitalize proper nouns and the first word after a colon unless that item is code whose spelling is lowercase.
- Run rare D-level headings into the following paragraph, apply the C-level capitalization rules, and end the heading with a period.
- Use title case for sidebar titles.
- Admonition titles are optional; when present, use title case.
- In title case, capitalize both halves of a hyphenated term when the second half is a main word (`Big-Endian`), but only the first when the second is minor (`Built-in`). Apply Chicago judgment.
- Lowercase a preposition of four letters or fewer unless it belongs to a phrasal verb: `Set Up Your Operating System`.
- Capitalize subordinating conjunctions such as *As*, *If*, *That*, and *Because* regardless of length.

## Lists

- Use numbered lists for ordered or chronological steps, variable/definition lists for terms and explanations, and bullets for unordered series.
- Sentence-cap every list item.
- Treat items as independent. Do not string them together with commas, semicolons, or conjunctions.
- When all items are fragments, omit periods. When any item is a full sentence, put periods on every item, including fragments.
- Use em dashes as bullets for a bulleted list nested inside another bulleted list.
- Convert bullets built from a short term plus its definition into variable-list entries.
- Sentence-case variable-list terms.
- Use a numbered list for step-by-step instructions.
- For back-cover bullets only, begin with a capitalized word and omit punctuation even when an item is a full sentence.

## Links and Cross-References

Write for a single source that becomes both print and reflowable electronic output:

- Do not use *above* or *below* for figures, tables, examples, unnumbered code, equations, or similar elements. Prefer a live numbered xref; otherwise use *preceding* or *following*.
- In Atlas, anchor a URL to specific, descriptive text. Avoid generic anchors such as *here* or *this website*. Ebook output shows the link; print output appends the URL in parentheses.
- Production shortens long URLs for print. Since May 2019, O'Reilly uses its internal `oreil.ly` service rather than bit.ly.
- Do not anchor URLs to text in InDesign books.
- Do not link to product pages on Amazon, Apple, Google, or another sales channel. Link product references only to oreilly.com. An unlinked statement that a book is available on Amazon is allowed; vendors must flag prohibited links to production.
- Link an O'Reilly book title itself to its O'Reilly catalog page; do not leave the catalog URL bare.
- Use live xrefs whenever supported. Preferred prose patterns include `See Chapter 27.`, `See “Treatment” on page xx.`, `…as shown in Figure 1-1.`, and `See “A Note for Mac Users” on page xx.` Atlas page references update dynamically.
- Use documented AsciiDoc xref markup. In DocBook, use the relevant `<xref>` format.

## Figures, Tables, and Examples

- Precede every formally numbered figure, table, and example with a specific in-text reference such as `see Figure 99-1`, `Example 1-99 shows`, or `Table 1-1 lists`.
- Do not introduce a formal element with a colon, *in the following figure*, *as shown in this table*, or a similar positional phrase. A missing xref may cause incorrect placement.
- Reserve unnumbered informal figures, tables, and examples for material that will not receive extended discussion or later references.
- In Word, number these elements as chapter-item (`1-2`) using a hyphen, not an en dash. Production may soft-code the number later.
- In AsciiDoc, use the documented AsciiDoc xref pattern. In DocBook, use `<xref>` for every figure, table, and example.
- Sentence-case word groups inside figures and omit periods in general; preserve proper nouns.
- Sentence-case figure captions. Code styling is allowed. Omit the final period. Discuss a consistent alternate scheme for several long captions with production.
- Sentence-case table titles and column heads. Code styling is allowed. Omit the final period from the table title.
- Sentence-case example titles. Code styling is allowed. Omit the final period.
- In Word, tag every table cell with a cell paragraph style, including empty cells. Tag a bold subheading below the first row as `CellSubheading`, not `CellHeading`.
- In Word, put every figure in a `FigureHolder` paragraph followed immediately by a `FigureTitle` paragraph.

## Code Formatting

### Blocks, indentation, and highlighting

- Introduce an unnumbered code block with a colon.
- Indent with spaces, not tabs.
- In Word, keep code inside template margins and preserve intended line breaks and indentation.
- O'Reilly uses Pygments. Most printed code is black and white; electronic formats, including web PDF, use color.
- Authors must choose an available Pygments lexer and apply the source format's documented syntax-highlighting markup.
- Generated-AI programming interactions are an exception: do not apply syntax highlighting.

### Atlas v2 maximum line lengths

Use the value at the intersection of series and placement:

| Series | Body/top-level | Examples | Lists | Readeraids | Sidebars |
|---|---:|---:|---:|---:|---:|
| Animal (7×9) | 81 | 85 | 73 | 57 | 77 |
| Animal 6×9 | 64 | 68 | 56 | 40 | 60 |
| Report 6×9 | 64 | 68 | 56 | 40 | 60 |
| Trade 6×9 | 76 | 72 | 65 | 80 | 69 |
| Cookbook | 81 | 85 | 73 | 57 | 77 |
| Make 1-column | 89 | 89 | 81 | 66 | 39 |
| Make 2-column | 45 | 46 | 35 | 28 | 40 |
| Make Getting Started | 63 | 67 | 60 | 51 | 60 |
| Nutshell | 71 | 75 | 67 | 60 | 75 |
| Pocket Ref | 51 | 55 | 50 | 42 | 51 |
| Theory in Practice | 81 | 85 | 77 | 51 | 83 |

If series or placement is unknown, label the result conditional rather than inventing a limit.

### Word conversion

Before conversion, globally find code tabs with `^t`. Replace each tab with enough spaces to preserve indentation. Four spaces matches the ORA.dot cleanup macro and is only a starting rule of thumb; correct indentation controls.

## Generative AI Material

Classify AI material as either conversational chatbot/UI content or programming-context content. Ask production when uncertain.

For conversational content:

- Put the exchange in blockquotes.
- Italicize speaker labels so prompts and responses are distinguishable.
- Edit human prompts only very lightly for punctuation or capitalization.
- Keep generated output verbatim. If it must be edited, preserve attribution and make its AI origin explicit.

For programming-context content:

- Put the interaction in a code block; use an ordinary paragraph between prompt and response where needed.
- Keep code substantially verbatim and flag typos for the author or production.
- Do not use syntax highlighting.

## Footnotes and Punctuation-Sensitive Formatting

- Put a running-text footnote marker after punctuation.
- Restart running-text footnote numbers at 1 in each chapter.
- Use letters (`a`, `b`, `c`, …) for table footnotes, put them directly after the table, and keep them to a minimum.
- Keep parentheses roman even when their contents are italic. Use square brackets for a parenthetical nested inside parentheses.
- Close up ellipses and em dashes with no surrounding spaces.
- Use curly quotation marks and apostrophes in prose, but straight quotation marks in code and constant-width text.

## Format-Specific Production Checks

Use the separate authoring guide for implementation details in AsciiDoc, HTMLBook, DocBook, or Word. The style guide defines the treatment; the authoring guide defines the markup or named style.

| Format | Mandatory checks from the style guide |
|---|---|
| AsciiDoc | Apply documented semantic inline styles, lexer markup, live xrefs, figure/table/example xrefs, and footnote markup |
| DocBook | Apply semantic inline elements, documented syntax-highlighting markup, and `<xref>` for referenced figures, tables, examples, sections, and sidebars |
| Word/Google Docs | Keep code within template margins; replace tabs; preserve indentation; apply correct table-cell and figure paragraph tags; use the Word conversion guide |
| InDesign | Do not anchor URLs to descriptive text; follow environment-specific term-tagging instructions |
| HTMLBook/plain text/Markdown | Preserve the required semantic distinction in the available markup and flag any treatment the format cannot express |

Correct term tagging is mandatory and varies among Word/OpenOffice, DocBook XML, and InDesign. Ask the editor or `toolsreq@oreilly.com` for environment-specific instructions. Conventions may vary slightly by project; ask the editor, production editor, or freelance coordinator rather than guessing.

Before submitting a Word copyedit for conversion:

1. Replace code tabs with indentation-preserving spaces.
2. Convert remaining Word comments to blue-highlighted, tagged `Comment` paragraphs.
3. Find manual line breaks with `^l`; delete them or replace them with paragraph breaks as appropriate.
4. Accept all tracked changes.
5. Confirm filenames follow house style.

## Implementation References

The official style guide delegates source-markup details to these resources:

- Pygments [available lexers](https://pygments.org/docs/lexers/)
- O'Reilly [Writing in AsciiDoc](http://docs.atlas.oreilly.com/writing_in_asciidoc.html), including inline styles, syntax highlighting, xrefs, and footnotes
- [HTMLBook](http://oreillymedia.github.io/HTMLBook/)
- [DocBook](https://docbook.org/) and O'Reilly's [DocBook Authoring Guidelines](https://prod.oreilly.com/external/tools/docbook/docs/authoring/); when the latter requests credentials, use username `guest` and leave the password blank
- O'Reilly [Word Template Quickstart Guide](http://oreillymedia.github.io/production-resources/word/), including paragraph/character styles and syntax highlighting

Consult these guides when the review must verify exact source syntax or named styles. Do not treat a link target as a replacement for the O'Reilly house-style treatment in this reference.

## Cover-Copy Formatting

- Use Chicago 18 for uncovered cover-copy issues.
- Back-cover bullets start with a capitalized word and end without punctuation, even when an item is a complete sentence.
- Lowercase job attributions where possible. Formal job titles may use title case; informal roles are lowercase. Mixed casing is acceptable when attributions differ in formality.
- Sentence-case an attribution that begins on its own line.
