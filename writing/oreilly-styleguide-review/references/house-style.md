# O'Reilly House Style: Complete Review Reference

Bundled snapshot: official O'Reilly Style Guide `gh-pages` commit `5b601621124fc7ae8f32f69dfaeae348bc8c2ac2`, dated 2026-04-14. Source: <https://oreillymedia.github.io/production-resources/styleguide/>. This reference paraphrases the complete prose guidance; the companion [word-list.md](word-list.md) preserves all 600 preferred-form entries.

## Contents

- [Authority and editorial principles](#authority-and-editorial-principles)
- [Electronic and multi-format publishing](#electronic-and-multi-format-publishing)
- [Abbreviations and acronyms](#abbreviations-and-acronyms)
- [Bibliographies, citations, and book references](#bibliographies-citations-and-book-references)
- [Code](#code)
- [Cross-references](#cross-references)
- [Dates and numbers](#dates-and-numbers)
- [Figures, tables, and examples](#figures-tables-and-examples)
- [Generative AI content](#generative-ai-content)
- [Headings](#headings)
- [Links](#links)
- [Lists](#lists)
- [Punctuation](#punctuation)
- [Typography and font conventions](#typography-and-font-conventions)
- [Miscellaneous prose rules](#miscellaneous-prose-rules)
- [Cover copy](#cover-copy)
- [Review completeness map](#review-completeness-map)

## Authority and Editorial Principles

Apply rules in this order:

1. A documented, book-specific decision or production-editor instruction
2. O'Reilly Style Guide and Word List
3. *The Chicago Manual of Style*, 18th edition
4. *Merriam-Webster's Collegiate Dictionary*

Record uncovered or intentionally different choices in the book-specific Word List Doc. Ask the editor or production editor about assignment-specific issues. Authors must also follow the authoring documentation for their source format: AsciiDoc, HTMLBook, DocBook, or Word. Sponsored work remains subject to O'Reilly's editorial-independence statement.

The guide covers authors, copyeditors, and proofreaders across formats and changes over time. Bold entries on the live page may be recent additions.

For people and groups:

- Consult the group's advocacy organization for preferred language and follow a person's stated preference.
- Avoid needlessly gendered language such as *middleman* or *man hours*.
- Avoid violent terms such as *hit* and *kill* where they are not precise and necessary.
- Avoid exclusionary, incendiary, or imprecise terms such as *crazy*, *dummy*, *master/slave*, and *tribe*.
- Avoid mapping value judgments to human-associated colors in compounds such as *blackbox*, *black hat*, or *white list*.
- Note legitimate exceptions, including faithful discussion of old research or obsolete technology.
- Useful external resources include the Conscious Style Guide, University of Washington IT Inclusive Language Guide, and Disability Language Style Guide.

## Electronic and Multi-Format Publishing

One source produces print and electronic editions, so review for reflow and print rendering:

- Do not locate figures, tables, examples, unnumbered code, equations, or similar elements with *above* or *below*. Prefer a live numbered cross-reference; otherwise use *preceding* or *following*.
- Anchor links to descriptive text whenever the production format supports it. Avoid generic anchors such as *here* or *this website* because print editions expose the URL after the anchor.
- Production shortens long URLs so print readers can type them.
- Never link to product pages on Apple, Google, Amazon, or other sales channels. Product links may point to oreilly.com. An unlinked statement that a book is available on Amazon is acceptable. Vendors must flag prohibited sales-channel links to production.
- In Word or Google Docs, use O'Reilly's dedicated code-formatting instructions so conversion preserves code.

## Abbreviations and Acronyms

- Choose either `A.M.`/`P.M.` or `a.m.`/`p.m.` and stay consistent.
- Capitalize an expanded acronym only when the expansion is itself a proper noun and the owner spells it that way: *key performance indicator (KPI)* but *Amazon Web Services (AWS)*.
- Expand acronyms in headings unless they are familiar to the intended audience.
- Do not hyphenate a numeral plus abbreviated unit used attributively: `32 MB hard drive`. Hyphenate the spelled-out unit: `32-megabyte hard drive`.
- `K` means 1,024; `k` means 1,000. Thus 64 K is 65,536, while 56 kbps is 56,000 bps.
- Common audience-appropriate acronyms may appear without expansion. The guide explicitly includes AI for artificial intelligence, API, CLI, CPU, HTML, IP, UI, and UX as typical examples.
- Spell out *United States* and *United Kingdom* on first mention; subsequently use `US` and `UK`, without periods.
- Academic degrees may retain or omit periods (`B.A.` or `BA`, for example); be consistent.
- Use Chicago 18 for cases not covered.

## Bibliographies, Citations, and Book References

- Prefer Chicago 18's Notes and Bibliography system for bibliographies, reference lists, and footnotes. Chicago Author-Date is also acceptable when consistently chosen. If the manuscript has no coherent system, suggest Notes for footnotes and Bibliography for endnotes/back matter.
- Record the chosen Chicago system in the project's Word List Doc and tell the production editor.
- In prose references to a book, give up to two authors. With three or more, name the first author and add `et al.` with its period.
- On first prose mention, include author and publisher; later mentions may use only the book title.
- For an O'Reilly book's publisher parenthetical, use `O'Reilly`, not `O'Reilly Media, Inc.`
- Link an O'Reilly book title itself to its O'Reilly catalog page. Do not leave the catalog URL standing alone, and do not link to a retailer product page.
- A footnote cannot consist only of a URL. Give context for the destination or a complete citation.

## Code

### Line lengths

Use spaces, never tabs, for indentation. In Word, keep code within the template margins and explicitly preserve intended line breaks and indentation. Atlas v2 maximum characters by series and placement are:

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

Count against the smallest applicable limit when placement is uncertain and label the result conditional.

### Syntax highlighting

O'Reilly uses Pygments. Most print code is black and white; electronic formats, including the web PDF, use color. Authors should choose an available Pygments lexer and apply the correct source-format markup. Consult the separate AsciiDoc, DocBook, or Word instructions for implementation.

### Code in Word

Before conversion, globally find tabs in code with `^t` and replace each with enough spaces to preserve the actual indentation. Four spaces is only a starting rule of thumb and matches the ORA.dot cleanup macro; visual/semantic indentation is controlling.

## Cross-References

Use live xrefs where the source format supports them. Preferred forms include:

- Chapter: `See Chapter 27.`
- Section: `See “Treatment” on page xx.` In Atlas, the page text updates dynamically.
- Figure: `…as shown in Figure 1-1.`
- Sidebar: `See “A Note for Mac Users” on page xx.` The page text is dynamic.

AsciiDoc has dedicated xref markup. DocBook exposes equivalent `<xref>` formats. Apply the link rules in this reference to URLs and hyperlinks.

## Dates and Numbers

- With a numeral, use `%`, closed up: `0.05%`. A percentage beginning a sentence or title/caption may need spelling out.
- Apply the general zero-through-nine treatment to centuries; typical modern examples are `20th century` and `21st century`.
- In most numbers of 1,000 or more, separate groups of three digits with commas (`32,904`). Do not add grouping commas to page numbers, addresses, port numbers, and comparable identifiers.
- Spell out zero through nine and certain round multiples. If the same kind of object is counted elsewhere in the sentence with 10 or more, use numerals for both: `5 apples and 110 oranges`. Different construction may retain `five apples and one hundred oranges`.
- Spell out ordinals first through ninth; use unsuperscripted numerals for 10th and higher.
- Use numerals for versions: `version 5` or `v5`.
- Use a numeral for an actual measured or monetary value, such as `5%`, `7″`, or `$6.00`.
- Whole one-through-nine numbers followed by *hundred*, *thousand*, *million*, *billion*, and similar magnitudes are usually spelled out, except in scientific contexts or money.
- Decades: `1980s` or `’80s`, with no apostrophe before the `s`.
- Use `32-bit integer`.
- A phone number may use `xxx-xxx-xxxx`.
- Use an en dash, not a hyphen, as a minus sign or before a negative number.
- Use the multiplication sign `×`, not the word *by*, for dimensions: `8.5 × 11`.
- Put spaces around inline operators: `1 + 1 = 2`.

## Figures, Tables, and Examples

- Precede every formally numbered figure, table, and example with a specific in-text reference such as `see Figure 99-1`, `Example 1-99 shows`, or `Table 1-1 lists`.
- Do not introduce formal elements with a colon, *in the following figure*, *as shown in this table*, or another vague positional phrase. Missing xrefs can cause bad placement.
- Reserve unnumbered informal figures, tables, and examples for content that will not receive extended discussion or later references.
- In Word, use chapter-item numbering such as `1-2`, with a hyphen rather than an en dash. Production may soft-code it later.
- In AsciiDoc, use the documented AsciiDoc xref pattern. In DocBook, use `<xref>` for each figure, table, and example.
- In figure-internal word groups, capitalize only the first word and proper nouns; generally omit terminal periods.
- Figure captions use sentence case, may contain code styling, and have no final period. Discuss an intentional alternate punctuation scheme for multiple long captions with production.
- Table titles and column headings use sentence case, allow code styling, and have no final period.
- Example titles use sentence case, allow code styling, and have no final period.
- In Word, tag every table cell with a cell paragraph style, including empty cells. A bold subheading below the first table row is `CellSubheading`, not `CellHeading`.
- In Word, place every figure in a `FigureHolder` paragraph followed immediately by a `FigureTitle` paragraph.

## Generative AI Content

First decide whether the material is conversational chatbot/UI output or programming-context output; ask production when the category is unclear.

For conversational AI:

- Put the exchange in blockquotes.
- Italicize speaker labels so the human prompt and system response are unmistakable.
- Make only very light punctuation/capitalization edits to human prompts.
- Keep generated output verbatim. If it must be edited, continue to credit the AI and make the generated status explicit.

For programming-context AI:

- Put the programming interaction in a code block, with ordinary prose separating prompt and response as needed.
- Keep code content substantially verbatim; flag typos for author or production attention.
- Do not apply syntax highlighting.

## Headings

- Do not use inline code, bold, italic, or other style markup in headings.
- Expand acronyms unless a common acronym is well known to the audience.
- Follow every heading immediately with body text. Do not place another heading or an admonition directly after it without introductory or descriptive prose.
- A- and B-level headings are title case in most templates. Capitalize main words, but not articles, conjunctions, or technical/program names whose conventional form is lowercase.
- C-level headings use sentence case; capitalize proper nouns and the first word after a colon, unless that word is code whose correct form is lowercase.
- Rare D-level headings are run into the following paragraph, use the same sentence-case rules as C heads, and end with a period.
- Sidebar titles use title case.
- Optional note/tip/warning titles use title case.
- In title case, capitalize both parts of a hyphenated compound when the second is a main word (`Big-Endian`); capitalize only the first when the second is minor (`Built-in`). Use judgment and Chicago.
- Lowercase prepositions of four letters or fewer unless they form part of a verb: `Set Up Your Operating System`.
- Capitalize subordinating conjunctions such as *As*, *If*, *That*, and *Because*, regardless of length.

## Links

- In Atlas books, anchor URLs to descriptive text when possible. Ebook output shows the linked phrase; print output appends the URL in parentheses.
- Production shortens long and complex links. Since May 2019, O'Reilly's internal `oreil.ly` service replaces bit.ly for shortened links.
- Do not anchor URLs to text in InDesign-produced books.
- Also apply the electronic-format restrictions on retailer links and generic anchor text.

## Lists

- Use numbered lists for ordered or chronological steps, variable/definition lists for terms plus explanations, and bullets for unordered series.
- Start each item with sentence-style capitalization.
- Treat items as independent; do not chain them with commas, semicolons, *and*, or *or*.
- If every item is a fragment, omit terminal periods. If any item is a complete sentence, end every item in that list with a period, including fragments.
- Use em dashes as bullets for a bulleted list nested inside another bulleted list.
- Convert bullets of the form “short term: definition” or “short term—definition” to variable-list entries.
- Variable-list terms use sentence case.
- Use a numbered list for step-by-step instructions.

## Punctuation

- Put commas and periods inside quotation marks.
- Use curly quotation marks and apostrophes in normal prose.
- Close up ellipses: no surrounding spaces.
- Close up em dashes: no surrounding spaces.
- O'Reilly does not ban or discourage em dashes merely because some consider frequent em dashes an AI tell. Judge AI-generated writing from multiple signals, not this punctuation alone.
- Place footnote markers after punctuation in running text.
- Number running-text footnotes from 1 again in each chapter.
- Omit a menu item's displayed trailing ellipsis when naming that item in prose.
- Lowercase the first word after a colon in running prose. Heading capitalization is an exception.
- Apply the list-period rule from the Lists section.
- Keep parentheses roman even around italic content. Use square brackets for a parenthetical nested inside parentheses.
- Use the serial comma.
- Use straight quotation marks in constant-width text and all code. Preserve Unix-command backticks.
- Use letters (`a`, `b`, `c`, …) for table footnotes, place them directly after the table, and keep them rare.
- Use Chicago 18 when the guide is silent.

## Typography and Font Conventions

Apply the source format's correct semantic tags, not merely a visual imitation. Ask the editor before deviating. URLs cannot be restyled away from italic. Ask about any new element type.

| Element | Final treatment |
|---|---|
| Filenames, file extensions, directory paths | Italic body font |
| URLs, URIs, email addresses, domain names | Italic body font |
| Emphasis | Italic, not bold |
| First occurrence of a technical term | Italic body font |
| Code blocks | Constant width |
| Registry keys | Constant width |
| Classes, types, namespaces, attributes, methods, variables, keywords, functions, modules, commands, properties, parameters, values, objects, events, XML/HTML tags, and comparable language/script elements | Constant width |
| SQL commands such as `SELECT`, `INSERT`, `ALTER TABLE`, `CREATE INDEX` | Constant-width capitals |
| Replaceable syntax items/placeholders | Constant-width italic |
| Commands or text the user must type | Constant-width bold |
| Line annotations | Smaller italic body font |
| Placeholders inside material already italic, such as paths or URLs | Preserve the italic context and distinguish the placeholder per source-format convention |
| Key names/accelerators (`Ctrl`, `Shift`), menu titles/options/buttons | Roman body text |
| Packages and libraries such as NumPy, scikit-learn, TensorFlow, rJava | Roman body text with official casing |

Conventions can vary slightly by project; consult the editor, production editor, or freelance coordinator. Word and DocBook authors must use their separate implementation guides. Correct tagging is mandatory and varies among Word/OpenOffice, DocBook XML, and InDesign; ask the editor or `toolsreq@oreilly.com` when needed.

Before sending a Word copyedit for conversion:

1. Replace code tabs with indentation-preserving spaces.
2. Convert remaining Word comments to blue-highlighted, tagged `Comment` paragraphs.
3. Find manual line breaks with `^l`; delete them or replace them with paragraph breaks as appropriate.
4. Accept all tracked changes.
5. Confirm filenames follow house style.

## Miscellaneous Prose Rules

- Avoid obscenities and slurs. If retained, obscure them with a grawlix, two-em dash, or similar treatment.
- When possible, avoid the possessive of a singular noun ending in `s`: prefer `the Windows Start menu` to `Windows's Start menu`.
- Do not globally rewrite the author's point of view or voice, such as changing royal *we* to *I* or *you*. Do maintain reasonable local consistency within a sentence or paragraph.
- Close up the prefixes *micro*, *meta*, *multi*, *pseudo*, *re*, *non*, *sub*, and *co* unless the result is a proper noun or a word-list exception. Explicit exceptions include *re-create* and *re-identification*.
- Keep common foreign expressions such as *en masse* roman.
- Treat a company as singular: `Apple emphasizes … its … it`. The same singular agreement applies to generic *organization*, *team*, *group*, and similar collective entities.
- Do not stack admonitions, sidebars, or headings.
- Do not hyphenate an adverb to the word it modifies: `incredibly wide table`.
- Treat a filename's leading dot as silent when choosing an article: `a .pdf file`, but `an .env file`.
- Introduce an unnumbered code block with a colon.
- Use *between* and *each other* for two; use *among* and *one another* for three or more.
- Prefer American spellings.
- Aim for a conversational, user-friendly voice addressed to an intelligent reader who lacks this specific knowledge—an experienced colleague onboarding a new hire. First-person pronouns, contractions, and active verbs are welcome. Copyeditors should ask production before proposing global tone changes.
- Match the capitalization of on-screen software labels. Put quotation marks around a multiword label that appears lowercase or mixed case on screen only when needed to distinguish it from surrounding prose.

## Cover Copy

Use Chicago 18 for uncovered cover-copy issues.

- Back-cover bullet items begin with a capitalized word and never take terminal punctuation, even when an item is a full sentence. This intentionally overrides the normal list-period rule.
- Lowercase job attributions as much as possible. Formal job titles may use title case; informal roles are lowercase. Mixed casing across multiple attributions is acceptable when their formality differs.
- When an attribution begins on a line by itself, sentence-case it.

## Review Completeness Map

The bundled audit covers every official top-level prose area and its nested subsections:

| Official area | Covered here |
|---|---|
| About O'Reilly Style | Authority and editorial principles |
| Considering Electronic Formats | Electronic and multi-format publishing |
| Abbreviations & Acronyms | Abbreviations and acronyms |
| Bibliographical Entries and Citations | Bibliographies, citations, and book references |
| Code: Line Length, Syntax Highlighting, Formatting Code in Word | Code |
| Cross References | Cross-references |
| Dates and Numbers | Dates and numbers |
| Figures, Tables, and Examples | Figures, tables, and examples |
| Generative AI | Generative AI content |
| Headings | Headings |
| Links | Links |
| Lists: Bulleted, Numbered, Variable | Lists |
| Punctuation | Punctuation |
| Typography and Font Conventions | Typography and font conventions |
| Miscellaneous | Miscellaneous prose rules |
| O'Reilly Cover Copy | Cover copy |
| O'Reilly Word List A–Z | Companion `word-list.md`, 26 letters, 600 top-level entries |

Snapshot source SHA-256: `03bda3ddca167a65e31f6e019723e8fb6a03c7e932a7ebcd09fd589b82ae8383`.
