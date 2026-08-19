---
name: asd-ste100-review
description: Review, edit, or rewrite technical documentation for ASD-STE100 Simplified Technical English compliance. Use for STE audits, controlled-language checks, aerospace or defense documentation, maintenance and operating procedures, descriptive technical text, warnings and cautions, notes, terminology and approved-word review, sentence and paragraph limits, word counting, punctuation, multi-word nouns, technical nouns and verbs, translation-readiness, or a rule-linked compliant revision.
---

# ASD-STE100 Review

Review technical content against the applicable issue of ASD-STE100 without changing its technical meaning. Treat STE as a controlled natural language for technical documentation, not as a general readability style or an automatic certification.

## Load the Standard Model

Read both references completely for every review:

- [references/rules-reference.md](references/rules-reference.md) contains all 53 Issue 9 writing rules, the eight general recommendations, exceptions, and cross-rule checks.
- [references/standard-and-dictionary.md](references/standard-and-dictionary.md) contains scope, edition control, official-source handling, dictionary mechanics, technical-term categories, lexical decision logic, and formatting boundaries.

Use the official standard, not these paraphrased references, as the authority for a disputed interpretation or a complete lexical audit. Obtain the current official copy from the ASD STEMG website when it is not available with the task. Do not redistribute or add the official PDF to a repository.

## Establish the Review Contract

Infer what is available and state material assumptions. Do not block a useful review only because one input is missing.

- Applicable ASD-STE100 issue; default to Issue 9 only when the user gives no contractual issue
- Requested outcome: audit, annotated findings, clean revision, side-by-side revision, terminology queries, or compliance report
- Content boundaries and location identifiers
- Document type and each block's class: procedural, descriptive, safety instruction, note, quoted/immutable text, title or heading, table, or list
- Company, project, or industry specifications that govern formatting, abbreviations, units, safety labels, and official terminology
- Approved company glossary or terminology database for technical nouns and technical verbs
- Text that must remain exact, including screen labels, placards, identifiers, formulas, quotations, legal language, and controlled part names

Do not infer company-approved terminology from familiarity alone. If the termbase or official dictionary is unavailable, mark the affected checks as unverified and do not claim full compliance.

## Preserve Meaning First

Before changing language:

1. Identify the actor, action, object, condition, sequence, limit, tolerance, result, and risk in each passage.
2. Record identifiers, quantities, units, negation, modality, cross-references, and defined terms that must survive unchanged.
3. Query any ambiguous or technically incomplete source. Do not choose a technical meaning merely to produce fluent STE.
4. Put safety-critical ambiguity, missing conditions, contradictory limits, and incorrect risk levels ahead of language findings.

Never make a sentence lexically compliant by changing its engineering meaning. A technically correct query is better than a confident but unsafe rewrite.

## Review in Passes

Keep the passes separate so a clean sentence does not conceal a classification or safety problem.

1. **Scope and classification**: Divide mixed content into its correct classes. Apply procedural rules to instructions, descriptive rules to information and notes, and safety rules to hazards.
2. **Technical fidelity**: Compare the source and proposed meaning. Preserve all actions, conditions, sequences, limits, tolerances, causal relations, and risks.
3. **Safety instructions**: Verify risk level, label, command or condition first, consequence, sentence length, and the boundary between warnings, cautions, notes, and ordinary work steps.
4. **Vocabulary**: Check every lexical item against the official Part 2 dictionary. Verify approval, part of speech, approved meaning, permitted form, help restriction, and context. Check unlisted words through the technical-noun or technical-verb decision process.
5. **Terminology**: Check company approval, category eligibility, shortness, clarity, domain fit, and one-term-per-concept consistency. Do not silently rename parts or processes.
6. **Verbs and voice**: Check permitted tenses and forms, active voice, imperative instructions, passive-voice exceptions, “-ing” forms, auxiliary constructions, direct action verbs, and phrasal verbs.
7. **Sentences and information flow**: Check completeness, articles, contractions, one topic or instruction, condition placement, vertical lists, connectors, gradual information, and sentence construction.
8. **Length and word count**: Apply the 20-word procedural limit, 25-word descriptive and note limit, six-sentence paragraph limit, and every special count rule in Section 8.
9. **Punctuation and presentation**: Reject semicolons; check hyphens, parentheses, colons, and list punctuation. Separate STE requirements from external formatting, abbreviation, numbering, unit, typography, and safety-symbol rules.
10. **Consistency and recommendations**: Check repeated terminology and wording, pronoun clarity, “that,” ambiguous “with,” false friends, Latin abbreviations, inclusive language, and possessives.
11. **Regression**: Recheck the revised passage from the first pass. A vocabulary replacement can create a new voice, length, article, syntax, or meaning violation.

## Revise Safely

- Make the smallest revision that resolves the rule violation and keeps the full technical meaning.
- Use a different sentence construction when direct substitution changes meaning, part of speech, grammar, or technical logic.
- Split instructions into ordered work steps unless actions truly occur at the same time.
- Put a necessary condition before its command and separate them with a comma.
- Keep information out of notes when the reader needs it to complete the task, meet a limit, or avoid harm.
- Retain immutable quoted text and official identifiers. Review the surrounding sentence and apply the special word-count treatment.
- Preserve an approved long technical noun on first use; then use its authorized short form or abbreviation when appropriate.
- Do not “fix” an authorized technical noun or verb merely because it is absent from the STE dictionary.
- Do not use a checker, word list, readability score, or language model as a substitute for human technical and lexical judgment.

When a requested rewrite cannot be verified against the official dictionary and termbase, call it an **STE-oriented revision**, not an **ASD-STE100-compliant revision**.

## Report the Review

Lead with the edition, scope, content classes, and verification status. Use one of these conclusions:

- **Compliant in reviewed scope**: all applicable checks were completed with the official issue and necessary termbase; no unresolved violations remain.
- **Not compliant**: one or more mandatory violations remain.
- **Compliance not fully verifiable**: the official dictionary, termbase, source context, or external directive needed for a required check was unavailable.

List findings in reader-risk order. For each finding, give:

1. Severity: **Safety-critical**, **Mandatory**, **Terminology query**, **General recommendation**, or **External directive**
2. Location and a short identifying excerpt
3. Applicable ASD-STE100 rule or recommendation
4. Problem and why it matters
5. Proposed revision or author query
6. Verification note when dictionary, terminology, or technical approval is unresolved

Group repeated instances only when the proposed fix is genuinely the same. Do not hide the number or locations of occurrences.

End with:

- A clean revised passage when requested
- Technical-fidelity checks completed
- Quantitative checks completed, including sentence and paragraph counts
- Vocabulary and terminology verification status
- External formatting or publication checks that remain
- Strengths worth preserving and unresolved author decisions

## Handle Conflicts

ASD-STE100 controls expression. The applicable publication specification, contract, regulator, or house guide can separately control typography, numbering, abbreviations, units, labels, and layout. Identify each source of authority and do not present an external formatting rule as an STE rule.

If an external directive requires an STE exception, preserve the directive and document the conflict. If two requirements can both be satisfied, satisfy both.
