# Apache Guidance for README Work

Source review date: 2026-09-06. This file synthesizes guidance for README work; the linked ASF documents remain authoritative. Recheck an applicable source before making a current policy finding. The editorial checklist below is this skill's recommendation, not a prescribed ASF README format.

## Branding and Official Identity

The [Apache Project Branding Policy](https://www.apache.org/foundation/marks/pmcs), particularly “Project Naming Policy” and “Project Branding And Descriptions Policy,” requires the Apache prefix in primary project branding. Use the confirmed project name in the title and first prominent reference; preserve literal executable and package names.

Recommend a concrete sentence explaining the software and a link to the project's verified official homepage. Homepage-specific description, navigation, attribution, and logo requirements become applicable when the README also serves that website role. Inspect the rendered page and shared navigation before reporting a missing element. Their absence from a repository README alone does not establish a website-policy violation. Do not guess trademark registration symbols or replace an approved logo.

The policy's “Website Navigation Links Policy” identifies the required website links, including licensing, sponsorship, sponsors, security, privacy, and the ASF homepage. Consult that section for exact destinations when website publication is in scope.

## Project Independence

[Apache Project Independence](https://community.apache.org/projectIndependence.html), especially “Apache products may be used independently” and “Apache projects are branded as Apache projects,” distinguishes ASF projects from third-party software using the Apache license. Confirm affiliation before applying ASF-specific requirements.

Make the community's own software, documentation, and support discoverable. Check for language implying that a vendor owns the Apache project or that a commercial offering is necessary for ordinary use. Third-party services can be identified accurately without turning them into the default or exclusive path. Preserve useful integrations and factual acknowledgments; their presence alone is not evidence of improper influence.

## Releases and Installation

The [ASF Release Policy](https://www.apache.org/legal/release-policy.html), under “Publication” and “Artifacts,” directs the public to approved releases and distinguishes them from development materials. In a README, separate the released-software quickstart from contributor checkout instructions. Do not present a default-branch archive, snapshot, nightly build, or release candidate as the official release. Development build instructions remain useful when addressed to contributors.

Recommend linking to the maintained project download page rather than reconstructing artifact URLs. Check that package-manager or container instructions correspond to a documented release and correctly describe their provenance. Do not assume all redistributions are prohibited: “Release Distribution” permits other channels after canonical publication.

The [release download page guidance](https://infra.apache.org/release-download-pages.html), under “Download links” and “Your Apache project's download page,” governs download pages. A README linking to such a page need not reproduce it. If the README itself acts as the download page, check source availability and the required signature, checksum, and key links. Follow the project's current distribution mechanism, including Apache Trusted Releases where applicable; recheck Infra guidance before hard-coding download infrastructure. Do not replace source-release links with GitHub-generated archives.

## Licensing and Source Headers

The [ASF Release Policy](https://www.apache.org/legal/release-policy.html), under “Licensing Documentation,” requires LICENSE and NOTICE files appropriate to each distributed package. A README license summary or badge does not substitute for those files. Link to existing files using their real paths, and report package omissions as release findings rather than missing README sections.

The [ASF Source Header and Copyright Notice Policy](https://www.apache.org/legal/src-headers.html) applies to ASF-developed documentation included in distributions, with exceptions. Its FAQ “What files in an Apache release do not require a license header?” allows judgment for short informational README and INSTALL files whose product identity is clear. This is not an exemption for every file named README.

Preserve a valid existing header. For substantial release documentation, check the applicable header form and project audit conventions. The current policy also allows an equivalent SPDX form with the required provenance and NOTICE information; a lone license identifier is insufficient. Do not replace it merely because it differs from the long form. “Treatment of Third-Party Works” prohibits replacing third-party notices with an ASF contribution header. Clarify provenance before proposing such changes.

## Community and Contributions

The [ASF contributor guide](https://community.apache.org/contributors/), under “Where is everything?” and “Communication,” explains the roles of project documentation, contribution paths, and mailing lists. These are useful README destinations, not mandatory heading names.

Link to the actual contributing guide, ordinary issue tracker, support channel, development discussion, and applicable code of conduct when available. Confirm list names and subscription/archive URLs from the project; conventions such as `users` and `dev` are not proof that an address exists. Recognize documentation and other non-code contributions. Avoid inventing an ICLA requirement for every drive-by contribution; preserve the project's documented process.

## Vulnerability Reporting

The [ASF Security Team's “Reporting a vulnerability” guidance](https://www.apache.org/security/) strongly encourages private reporting of undisclosed vulnerabilities. Keep this distinct from the public tracker used for ordinary bugs. Prefer the project's verified SECURITY file or security page; the ASF security page is a fallback when a project contact cannot be found.

Recommend an explicit security-reporting link when a generic invitation to report issues could misdirect reporters. Classify the ASF's encouragement accurately rather than inventing a universal requirement for a section titled “Security.” Do not invent a project security address or route routine support questions to the security team.

## Incubating Podlings

The [Incubator Branding Guide](https://incubator.apache.org/guides/branding.html), under “Naming,” explicitly requires each podling repository's README to use the Apache project name and identify incubation status at the first reference. Verify the podling's current status and approved name before changing either. A typical form is `Apache ProjectName (Incubating)`.

The guide recommends a README link to the disclaimer. Its “Disclaimers” section requires a clear incubation disclaimer in websites and documentation, including releases; alternative disclaimer wording requires Incubator PMC approval. Preserve approved wording and verify any project-specific substitutions rather than writing a new assurance about endorsement or maturity. For releases, a separate DISCLAIMER file beside LICENSE and NOTICE is the recommended placement.

Do not attach incubation language to a graduated or unaffiliated project. Confirm which version of the documentation is being edited: historical release documentation may correctly retain the status at release time.

## Conditional Cryptography Notice

[Handling cryptography within an ASF release](https://infra.apache.org/crypto.html), under “Inform users by including a crypto notice in the distribution's README file,” calls for a notice in each qualifying distribution's README and information about the cryptographic components.

Check this when the artifact is a distribution README and project records establish that the crypto process applies. Preserve an existing notice while verifying its accuracy against release records. The guidance records a 2019 regulatory update; confirm current ASF guidance and the project's established classification before proposing replacement text. A dependency name alone does not establish an export classification. If applicability is unknown, identify the missing evidence rather than assigning an ECCN or claiming legal compliance. Keep export filings and classification decisions outside a README edit.

## Source Authority Caveat

The page titled [Apache Project Minimum Requirements](https://www.apache.org/dev/project-requirements.html) is explicitly marked as a draft, not official policy, at the source review date. Follow its links to the adopted policies when establishing a requirement. Similarly, a particular project's writing guide or README can establish a local convention or illustrate an approach; it cannot establish a rule for all ASF projects.

## Editorial Checklist

These are coverage prompts for README quality. Adapt their order and depth to the audience; satisfy a topic with a useful link when detailed documentation already exists.

| Reader need | Check |
| --- | --- |
| Understand the project | Identify what the software does, its intended use, and the relevant project or module. Give prose priority over a wall of badges. |
| Find maintained information | Link to the official homepage and documentation for the appropriate version. Make development documentation distinguishable from release documentation. |
| Get started | Provide verified prerequisites and a short installation/use example, or link to the maintained quickstart. State enough expected behavior to recognize success. |
| Build and test | Identify the working directory, toolchain, and relevant build/test commands or contributor instructions. Keep development setup distinct from installation for users. |
| Get help and contribute | Provide confirmed destinations for support, ordinary bugs, contributions, and private vulnerability reporting. Avoid making chat or a vendor account the only documented entry point. |
| Understand licensing and status | Use an accurate license summary and existing companion-file links. Include conditional notices only when they apply. |
| Navigate the document | Check headings, local anchors, relative links, image alternatives, badge targets, and code-fence languages. Check release-relative links against the actual archive when reviewing a distribution. |

Use the repository's supported document format and renderer. Avoid adding a table of contents to a short README, duplicating long manuals, or turning preferred headings and stylistic choices into compliance failures.
