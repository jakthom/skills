---
name: apache-readme-review
description: Review, revise, or draft READMEs for Apache Software Foundation projects and incubating podlings using applicable ASF policies and project conventions. Use for Apache project README guidelines, audits, and onboarding improvements. Apache-2.0 licensing alone does not make a repository an ASF project.
---

# Apache README Review

Make the README a reliable entry point for users and contributors. Distinguish policy requirements, project conventions, and editorial recommendations; support policy findings with the relevant Apache source and its actual scope.

## Establish Scope and Evidence

Infer whether the user wants findings, an edit, or a new README. Perform requested edits directly; a review alone calls for findings.

Identify from the repository and official project information:

- Project identity and status: established ASF project, incubating podling, third-party project, or unverified. Never add ASF affiliation based only on an Apache license or a dependency on Apache software.
- README role: repository entry point, module documentation, release-distribution document, or content also published as a project website. Several roles can apply.
- Intended audience and version: users installing a release, contributors building a checkout, or both.
- Supporting evidence: existing README variants, project instructions, build manifests and workflows, release documentation, contribution and security guidance, and applicable LICENSE, NOTICE, and DISCLAIMER files.

Inspect only the supporting material relevant to the request. Use a module README's links to its parent documentation before proposing duplicated project-wide sections. For a release review, examine the actual distribution when available; repository files alone do not establish what the package contains.

If status or publication context is uncertain, continue with verifiable editorial improvements and mark affected policy checks as unresolved. For a third-party project, apply requested general README improvements without assigning ASF governance, naming, or incubation obligations to it.

## Select Applicable Guidance

Consult the relevant sections of [references/apache-guidance.md](references/apache-guidance.md):

- Identity and official links: branding and project independence.
- Installation, releases, and build instructions: release policy and download guidance.
- Licensing statements or headers: licensing and source headers.
- Community, contribution, and bug-reporting paths: contribution and security guidance.
- Podlings: incubation naming and disclaimers.
- Distribution READMEs involving cryptography: the conditional crypto notice.
- An outline or general quality review: the editorial checklist.

The reference is a dated synthesis. Verify the controlling source before declaring a policy violation or claiming current compliance. If browsing is unavailable, use the recorded guidance date and describe policy findings as provisional. Project instructions establish local conventions and may document approved exceptions; they do not silently override ASF policy. Treat draft documents and other projects' READMEs as supporting context, not Foundation-wide rules.

Apply each rule to its publication surface. Website navigation requirements and distribution-file requirements do not automatically dictate sections in every repository README. Conversely, a README reused as a homepage or shipped in a release can have additional obligations.

## Review or Draft

Use the editorial checklist as coverage prompts, not a mandatory section template. Keep the README short enough to orient readers and link to maintained detail. Preserve a useful existing structure, terminology, and document format.

Check the user's path from understanding the project to a first successful use. Verify technical claims, prerequisites, package names, versions, commands, and example output against repository evidence and authoritative documentation. Clearly label instructions for building development code. Do not invent a successful command, performance claim, support commitment, mailing-list address, or release URL.

Check relative links, heading anchors, images, badges, and destinations in the relevant rendering context. A live link can still lead to the wrong version or an unofficial resource. Keep package coordinates, executable names, and literal code unchanged when correcting prose branding.

When editing, preserve established legal headers, notices, and disclaimers unless a verified correction is in scope. Check the source-header exceptions before adding boilerplate. Report missing companion files separately; a README sentence cannot repair a deficient release package. Leave unknown project facts in a short follow-up list rather than filling the document with plausible guesses.

Run an existing documentation check when appropriate. Execute a documented quickstart only when its effects fit the authorized task and environment; otherwise validate it from source and identify it as unexecuted. Keep a README task focused on documentation rather than changing release configuration or project governance.

## Report Findings and Verification

Classify findings by authority, separately from their impact:

- **Required:** a verified, applicable ASF requirement conflicts with the artifact. Cite the exact policy section and explain why it applies here.
- **Project convention:** an explicit rule from this project's maintained guidance.
- **Recommendation:** an ASF recommendation or an editorial improvement; distinguish which basis applies.
- **Needs verification:** missing evidence about status, version, applicability, an exception, or technical behavior.

Lead with the changes or findings that most affect a reader's ability to identify, obtain, use, or contribute to the project. Give each finding a location, concrete correction, rationale, and source when policy is involved. Consolidate repeated issues.

For a requested draft or revision, provide the edited file or replacement text and summarize material changes. State which files and publication contexts were reviewed, which checks ran, and what remains unverified. Limit conclusions to that scope; README review does not establish complete ASF project or release compliance.
