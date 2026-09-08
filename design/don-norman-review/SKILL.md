---
name: don-norman-review
description: Review products, interfaces, physical controls, and service workflows using Don Norman's The Design of Everyday Things. Use for a Don Norman review or a usability diagnosis focused on affordances, signifiers, mappings, feedback, constraints, conceptual models, discoverability, and error recovery. Pure visual styling and biographical questions are outside this review workflow.
---

# Don Norman Review

Evaluate whether people can discover what to do, carry out their intentions, understand the result, and recover from problems. Turn observed friction into specific explanations and practical design changes.

Use the revised and expanded 2013 edition as the default lens. These are design principles, not a formal compliance standard, a numeric scoring system, or claims about what Norman personally would say.

## Establish the Task and Evidence

Infer the following from the request and available artifacts. State consequential assumptions and continue with the evidence available; ask only when missing information prevents a useful review.

- The person's goal and what successful completion means.
- Intended users, relevant experience and capabilities, and the setting in which they act.
- The product or workflow boundary, including important states and handoffs.
- Available evidence: a running product, source, prototype, screenshots, physical observations, or a written proposal.
- Requested deliverable: findings, proposed redesign, or implemented changes.

A review request calls for findings and concrete suggestions. When the user requests fixes or a redesign, carry out the authorized changes and verify them where possible.

Distinguish evidence types. A screenshot can reveal a label or spatial relationship; it cannot establish response timing, keyboard behavior, hidden states, or whether an action succeeds. Source inspection can establish implemented logic without demonstrating how users understand it. Mark unobserved behavior as a hypothesis or a check to perform. Do not invent user testing or attribute intentions to users without evidence.

## Apply the Book's Framework

Read **Interaction principles** in [references/norman-principles.md](references/norman-principles.md) for every review. Use the remaining sections when relevant:

- **Action cycle and the two gulfs** to trace task breakdowns.
- **Knowledge, conventions, and capability** to assess memory demands and audience fit.
- **Error and recovery** for slips, mistaken plans, modes, and consequential actions.
- **Iteration, emotion, and practical constraints** for redesign choices and validation.
- **Worked example** for the expected connection between evidence, diagnosis, and correction.

Follow a representative task through its actual states, rather than reviewing isolated controls alone. Examine entry, action selection, execution, response, interpretation, completion, and relevant recovery paths. Scale the depth to the requested scope.

Check all seven interaction principles, but report problems only where the evidence supports them. Trace confusion to its cause: a missing signifier, unclear mapping, misleading model, or missing feedback may all produce poor discoverability. Consolidate a shared cause into one finding instead of counting each principle as a separate defect.

For each proposed change, connect it to the user's goal and the specific breakdown. Prefer a coherent explanation and a clear interaction over added labels, warnings, or controls that leave the underlying problem intact. Preserve useful conventions, expert workflows, and necessary complexity. Consider the cost of a constraint as well as the error it prevents.

When reviewing physical products or accessibility, evaluate the action in relation to the person's capabilities and environment. A visible cue does not establish that a control is reachable, operable, or perceivable through another sensory channel. Make only the accessibility claims the evidence supports.

## Report Actionable Findings

Lead with the task reviewed, the scope of the evidence, and the most consequential breakdowns. For each finding, provide enough detail to act on it:

- **Location or state:** the control, step, screen, physical arrangement, or source location.
- **Evidence and confidence:** what was observed or established, and what remains a hypothesis.
- **Diagnosis:** the applicable Norman concept and the gap between the person's intention and the system's behavior or communication.
- **Consequence:** the likely task failure, wrong interpretation, repeated action, memory burden, or recovery cost.
- **Correction:** a concrete change, including proposed wording or behavior when useful.
- **Verification:** an observable result or focused task to check after the change.

Prioritize by consequence and evidence. Distinguish task blockers or consequential errors from recoverable confusion and minor friction. Do not manufacture frequency estimates, arbitrary scores, or high severity from an untested possibility. If findings are sparse, say so instead of filling a quota.

Briefly identify strengths to preserve, areas actually checked, and material unknowns. For implemented changes, report what changed, how it was checked, and any unresolved behavior. A successful functional check is not evidence that users understand the design; propose a focused observation when that remains uncertain.

## Preserve the Lens and Scope

Use the principles to explain behavior, not to enforce a visual style. Do not equate minimalism with usability, demand labels on every object, eliminate every mode, or assume familiar conventions are universal. Typography, color, motion, and sound matter here when they affect perception, meaning, action, feedback, or recovery.

Keep broader organizational or workflow findings when they explain the observed problem. Avoid turning a focused review into an unsolicited product overhaul. Attribute extensions and contemporary examples as applications of the framework; the source basis in the reference distinguishes Norman's synthesis from concepts he popularized.
