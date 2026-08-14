# Standard Scope and Dictionary Review

Use this reference to control edition, scope, source handling, lexical verification, domain terminology, and the boundary between ASD-STE100 and external publication rules.

## Contents

- Authority and edition control
- What STE does and does not control
- Content classification
- Official dictionary model
- Lexical verification procedure
- Technical noun categories
- Technical verb categories
- Recurring lexical traps
- Formatting and external directives
- Compliance limitations
- Official sources

## Authority and Edition Control

ASD-STE100 is maintained by the ASD Simplified Technical English Maintenance Group (STEMG). Issue 9, dated 2025-01-15, is the current issue at the creation of this skill. It presents STE as an international standard for technical documentation and contains:

- Part 1: nine sections with 53 writing rules
- Part 2: a controlled dictionary

Contractual projects can require an older issue. Record the required issue before review and do not silently apply Issue 9 changes to older controlled content. If no issue is specified, use the latest official issue available at review time and identify it.

The official PDF is free to obtain from the STEMG website, but its distribution notice prohibits unauthorized redistribution. Download it from the official site when necessary; do not commit, attach, mirror, or package it with this skill.

## What STE Does and Does Not Control

STE controls how technical content is expressed so international readers can understand it clearly and consistently. Its controlled vocabulary generally assigns one approved meaning and one approved part of speech to a word, while allowing qualified domain terms.

STE is not:

- A complete grammar or technical-writing textbook
- An English-language course
- A substitute for technical expertise or source validation
- A complete publication or formatting specification
- A rule set for abbreviations
- A rule set for units of measurement
- A certification delivered by an automated checker

Use it with the applicable publication specification, house style, contract, regulator requirements, terminology database, safety standard, and general English reference.

## Content Classification

Classify each block before applying type-specific rules.

### Procedural writing

Text that directs the reader to do a task. Use imperative commands, one instruction per sentence unless actions are simultaneous, a 20-word maximum, and ordered work steps.

### Descriptive writing

Text that explains an item, system, function, operation, or general subject. Notes in procedures are descriptive. Do not use imperative commands. Use a 25-word maximum, one topic per sentence and paragraph, gradual information, and no more than six sentences per paragraph.

### Safety instructions

Text that prevents injury, death, or damage. Apply the procedural sentence limit plus Section 7. A warning covers injury or death; a caution covers object damage in the aerospace and defense convention. When both risks exist, use a warning. Other domains can mandate different labels or symbols.

### Notes

Optional information that helps the reader. A note must not contain a required action, requirement, limit, result needed for the work step, or safety precaution. The procedure must remain complete and safe without its notes.

### Protected or externally controlled text

Quoted screen text, placards, labels, formulas, official titles, identifiers, and proper names can be unchangeable. Preserve the protected content, review the surrounding sentence, and apply the special word-count rules. Typography, numbering, and publication layout remain externally controlled.

### Mixed content

Do not apply one class to an entire file by default. A maintenance document can contain descriptions, prerequisites, work steps, notes, cautions, tables, and quoted labels. Mark and review each block separately.

## Official Dictionary Model

Issue 9 states that Part 2 contains 875 approved words and 1,274 selected unapproved words with suggested alternatives. These counts identify that issue, not a universal fixed inventory.

The dictionary has four columns:

1. **Word and part of speech**
2. **Approved meaning or approved alternatives**
3. **STE example**
4. **Non-STE example**

An uppercase headword is approved. A lowercase headword is not approved. Case in the dictionary is a status convention, not an instruction to write all approved words in uppercase in normal documentation.

The eight dictionary parts of speech are noun, verb, adjective, adverb, pronoun, article, preposition, and conjunction.

### Approved entries

For an approved entry, verify:

- The assigned part of speech
- The stated approved meaning
- The listed form
- Any contextual restriction or help note
- The construction shown by the STE example

If a standard-English meaning is absent, that meaning is not approved. Do not infer approval from familiarity.

### Unapproved entries

The alternatives are suggestions, not automatic replacements. They can:

- Have the same part of speech and permit a direct substitution
- Have a different part of speech and require reconstruction
- Be a multi-word phrase
- Point to a technical noun, marked TN
- Point to a technical verb, marked TV

Select the alternative that preserves the intended technical meaning. If none does, reconstruct with other approved words or query the source.

### Forms by part of speech

- **Nouns**: entries show singular; a countable plural is normally permitted unless a help note says otherwise.
- **Verbs**: use only the forms printed in the entry. The inventory includes regular, irregular, irregular auxiliary, and defective modal verbs. Do not generate an absent tense or participle.
- **Adjectives**: use the base and listed comparative or superlative forms. Constructions with approved *more* or *most* can apply where standard grammar requires them.
- **Adverbs**: do not assume an “-ly” form is approved because its adjective is approved. Verify it as a separate entry.
- **Other parts**: use only the assigned function and approved meaning.

### Help notes

Treat a help note as part of the entry. Issue 9 uses help to provide four kinds of guidance:

1. Additional instructions for correct use
2. Alternatives for meanings outside an approved word's restriction
3. A limitation to a specified context, such as safety instructions
4. Other important information about the listed word or its alternatives

## Lexical Verification Procedure

Perform this process for every potentially changeable word. Do not audit only “difficult” vocabulary.

1. **Protect exact content**: Mark quoted labels, formulas, identifiers, titles, proper names, and other immutable strings.
2. **Look up the spelling**: Search the official dictionary for the exact word or base form.
3. **If approved**: Verify part of speech, meaning, form, help, and context. Passing only the headword check is insufficient.
4. **If listed as unapproved**: Evaluate its alternatives and examples. Use direct replacement only when meaning, part of speech, grammar, and context remain correct.
5. **If absent or unsuitable**: Decide whether it is a technical noun or technical verb under the categories below.
6. **Verify authorization**: Check the company, project, industry, or subject-field termbase. Category eligibility does not prove that a particular term is authorized.
7. **Reconstruct when necessary**: Use approved words and a clear construction while preserving the actor, action, condition, result, quantity, and risk.
8. **Record uncertainty**: Mark `dictionary unverified`, `technical noun pending approval`, `technical verb pending approval`, or an equivalent explicit status.
9. **Recheck the result**: Verify every new word and all affected writing rules.

If the official dictionary is unavailable, review structure and obvious rule violations but label the lexical pass incomplete.

## Technical Noun Categories

A technical noun is a noun term for a defined concept in a subject field. It must fit at least one category and must be appropriate to the context. Issue 9 has 22 categories:

1. **Official parts information**: Design items identified in parts catalogs, drawings, or equivalent official sources.
2. **Vehicles, machines, and their locations**: Types of vehicles or machines and named locations within them.
3. **Tools and support equipment**: Tools, test or support equipment, their parts, and locations on them.
4. **Materials and unwanted substances**: Materials, consumables, contamination, waste, and substances that can cause malfunction.
5. **Facilities, infrastructure, and logistics**: Physical sites, utility or transport infrastructure, storage, distribution, handling, and logistic workflows.
6. **Systems, components, and circuits**: Their structures, functions, configurations, operating states, and parts.
7. **Mathematics, science, and engineering**: Concepts, properties, methods, calculations, formulas, measurements, processes, and technical phenomena.
8. **Navigation and geography**: Positions, directions, mapping, routing, orientation, and geographic locations.
9. **Numbers, measurement, and time**: Numbers, units, symbols, dates, periods, seasons, and time quantities.
10. **Quoted text**: Immutable wording on displays, buttons, placards, signs, labels, markings, and similar sources.
11. **People and organizations**: Professional roles, named individuals, groups, companies, authorities, organizations, states, and other geopolitical entities.
12. **Body parts**: Anatomical features and functions used in applicable technical contexts.
13. **Personal effects, food, and beverages**: Common personal items, clothing, food, and drink.
14. **Medical terminology**: Conditions, procedures, functions, and other medical concepts.
15. **Documents and document structure**: Official document types, standards, specifications, regulatory material, records, manuals, headings, sections, and other document components.
16. **Environmental and operating conditions**: Weather, atmosphere, light, contamination, and external or operational conditions.
17. **Colors**: Color terms are treated as technical nouns in STE even though ordinary grammar treats them as adjectives. Do not use comparative or superlative color forms.
18. **Damage**: Defects, degradation, deformation, wear, contamination signs, and malfunction indications.
19. **Computing and communications technology**: Hardware, software, interfaces, networks, data, security, AI, and information or communication technology.
20. **Civil and military operations**: Activities, organizations, equipment, support, lifecycle, deployment, mission, and service concepts.
21. **Law and regulation**: Legal, contractual, compliance, standards, specification, and regulatory concepts.
22. **Animals, plants, and other life forms**: Biological entities in technical or environmental contexts.

These categories are open classification aids, not preapproved word lists. A word can qualify in one meaning and fail in another. Record the category and authoritative termbase source for each non-dictionary term when the review must be auditable.

## Technical Verb Categories

A technical verb is a verb term for a defined process in a subject field. Prefer an approved dictionary verb when it gives the action accurately. Issue 9 has four principal categories with subcategories.

### 1. Manufacturing processes

- Removing material
- Adding material
- Attaching material
- Changing mechanical strength, structure, or physical properties
- Changing a surface finish
- Changing a material's shape

### 2. Computer processes and applications

- Input and output actions
- User-interface and application actions
- System operations

### 3. Subject-field instructions and information

- Engineering, mathematics, and science
- Medicine
- Civil and military operations
- Navigation
- Automotive and railway work
- Energy, oil, and gas

### 4. Law and regulation

Legal and regulatory actions used in contracts, warranties, certificates, standards, specifications, and legal documents.

Apply these controls:

- The official examples are illustrative, not exhaustive.
- A spelling can qualify as a technical verb in one context and be unapproved in another.
- Use the most precise process verb; do not use a vague umbrella verb when the operation is known.
- Do not convert an available technical noun into a verb merely for brevity.
- Apply all permitted-form, tense, “-ing,” active-voice, and action-expression rules.
- Verify the term in the governing glossary or terminology database.

## Recurring Lexical Traps

The Issue 9 dictionary introduction identifies recurring errors. Use the official entries to select the contextually correct construction; the shorthand below is a triage list, not an independent dictionary.

| Candidate | Review direction |
|---|---|
| acceptable | Usually use the approved adjective *permitted*. |
| alternate | Distinguish from the approved adjective *alternative*. |
| any | Often omit it or reconstruct. |
| avoid | Usually express the action with *prevent*. |
| both | Usually express the concept as *the two*. |
| check as a verb | *Check* is approved as a noun; use a permitted verb construction. |
| cover as a verb | Treat *cover* as a technical noun where applicable and reconstruct the action. |
| complete as an adjective | Distinguish the approved adjective *completed*. |
| damage as a verb | *Damage* is approved as a noun; reconstruct with *cause damage*. |
| ensure | Use the approved construction *make sure* where meaning agrees. |
| fit as a verb | Often use *install*, subject to meaning. |
| follow | For instructions, use *obey*; retain *follow* only with its approved sequence or movement meaning. |
| further | Usually use approved *more* in the applicable part of speech. |
| have to | Use the action verb in imperative form for an instruction. |
| however | Usually use the approved conjunction *but*. |
| insert | Usually use approved *put* when meaning agrees. |
| main | Usually use *primary*, except inside an authorized technical noun. |
| may | Usually use approved modal *can* for its permitted meanings. |
| need | Reconstruct with approved *necessary* where meaning agrees. |
| now | Use *at this time* when the time reference is necessary. |
| old | Select the precise approved idea, such as remaining, used, or expired. |
| over | Select the physical or relational meaning, such as above, on, or along. |
| people | Use the applicable approved noun, such as person or personnel. |
| perform | Usually use approved *do*. |
| portion | Usually use approved *part*. |
| press as a verb | Usually use approved *push* for a physical control action; verify technical UI usage separately. |
| reach | Often use approved *get*, but reconstruct for the exact meaning. |
| repeat | Express the action as *do ... again*. |
| required | Reconstruct with approved *necessary* where meaning agrees. |
| rotate | Usually use approved *turn*. |
| secure as a verb | Select the precise action, commonly *attach* or *safety*. |
| shall / should | The dictionary points to *must*; procedures often need a direct imperative instead. Preserve legal force and check external directives. |
| since as a conjunction | Use approved *because* for cause; do not confuse it with time. |
| test as a verb | *Test* is approved as a noun; use a permitted construction such as *do a test*. |
| therefore | Use approved *thus* or the phrase *as a result*. |
| under | Select the physical or numerical meaning, such as below, in, or less than. |
| using / “-ing” action | Use an approved finite verb or *with* when accurate; also apply Rule 3.5. |

Never copy a suggested replacement without checking the complete dictionary entry, approved meaning, part of speech, source context, and resulting sentence.

## Formatting and External Directives

ASD-STE100 explicitly does not regulate general text formatting. It does not independently set:

- Typeface, point size, emphasis, capitalization scheme, or color
- Page layout, margins, columns, spacing, or indentation
- Numbering and lettering systems
- Required abbreviation schemes
- Unit-of-measurement presentation
- Safety-symbol design or signal-word styling
- Table, figure, or illustration design beyond language and punctuation interactions

STE does regulate language-related presentation details, including vertical-list grammar and punctuation, list sentence boundaries, semicolon prohibition, parentheses uses, hyphenation relevant to clarity, and word-count treatment.

For every formatting finding, label its source:

- `ASD-STE100` for an actual language, punctuation, list, or count rule
- The named publication specification or house style for layout and typography
- The named safety standard for colors, symbols, panels, and signal-word presentation
- `Author query` when no controlling directive is available

Do not infer that uppercase safety examples create an uppercase mandate. Do not infer that the absence of an STE abbreviation rule authorizes unexplained abbreviations; apply the governing project rules and reader needs.

Use an official project abbreviation only when the intended readers know it. Define a long official technical noun and its approved abbreviation on first use where the governing directive requires or permits that method. Avoid dense abbreviation use when the full term is already short and clear.

## Compliance Limitations

Automated tools can find candidate vocabulary, counts, punctuation, voice, and consistency problems. They cannot reliably determine:

- The intended engineering meaning
- Whether an agent is truly unknown
- Whether simultaneous actions are technically simultaneous
- The correct risk level or consequence
- Whether a domain term is approved by the company or subject field
- Whether a dictionary alternative preserves context
- Whether a protected string is genuinely immutable
- Whether an external directive overrides a default

Human technical and editorial judgment is always necessary. Report what was checked, what source was used, and what remains unverified. Do not promise certification from a language-model review.

## Official Sources

- ASD STEMG home: <https://www.asd-ste100.org/>
- Official downloads: <https://www.asd-ste100.org/STE_downloads.html>
- Official Issue 9 PDF: <https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf>
- Official FAQ: <https://www.asd-ste100.org/STE_faq.html>
- Official background: <https://www.asd-ste100.org/about_STE.html>
- Official software guidance: <https://www.asd-ste100.org/software.html>

Check these pages for a newer issue before a noncontractual review. Use primary ASD STEMG sources for rule and edition claims.
