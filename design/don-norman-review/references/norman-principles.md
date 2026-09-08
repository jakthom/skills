# The Design of Everyday Things: Review Reference

This is an applied synthesis of the revised and expanded 2013 edition and Norman's related explanations. The examples are illustrative review scenarios, not quotations or cases attributed to the book. Use the concepts as diagnostic tools and test recommendations against the intended users and setting.

## Interaction principles

### Affordances: possible actions

An affordance is a relationship between an actor's capabilities and an object's properties that makes an action possible. It need not be perceived, intended, or desirable. A handle can afford grasping to someone who can reach and grip it; another person may be unable to use it.

Determine whether the action is possible before diagnosing how it is communicated. A drawn button's appearance is a signifier; the system's ability to respond is a separate question. Changing its decoration does not by itself change the available action.

James J. Gibson introduced affordances. Norman popularized their use in design and later clarified the confusion around perceived affordances. [Norman: Affordances and Design](https://jnd.org/affordances-and-design/).

### Signifiers: perceivable clues

Signifiers indicate where or how to act, or communicate meaningful state. They can be visual, auditory, or tactile, and deliberate or incidental. Their interpretation may depend on learned conventions.

Inspect labels, shapes, placement, sounds, motion, and tactile cues for the action they suggest. Look for missing cues, misleading cues, and competing cues. A hidden gesture can be supported without offering newcomers a way to discover it; a handle can suggest pulling even when pushing is required.

Choose cues that the intended audience can perceive and interpret. Adding an icon or label is useful only if it resolves the actual ambiguity. [Norman: Signifiers, not affordances](https://jnd.org/signifiers-not-affordances/).

### Mapping: controls and effects

Mapping is the relationship between controls, actions, and their effects. Spatial correspondence can reduce the need to translate or memorize: a control arrangement can follow the arrangement of the things controlled.

Check which object an action affects, its direction, and its scope. In a multi-item editor, determine whether a command applies to one item, the selection, or everything. A clear label may still leave the target ambiguous. For a slider, examine whether movement and resulting change correspond in an understandable way.

Prefer direct correspondence where practical. Do not assume a mapping that feels natural to one audience is universal. The book addresses cultural variation in natural mappings. [Book contents: mapping and culture](https://jnd.org/books/the-design-of-everyday-things-revised-and-expanded-edition/).

### Feedback: perceiving the result

Feedback communicates that an input was received, what the system is doing, and the resulting state. It must be timely, interpretable, and relevant to the action.

Separate acknowledgment from completion. A pressed-button animation does not establish that an upload finished. Inspect progress, success, failure, and partial completion where those states matter. Assess whether someone can tell what remains to be done and whether repeating the action could cause an unwanted duplicate.

Avoid flooding people with undifferentiated notifications. Match the cue to the event's importance and the environment. State timing concerns as hypotheses unless timing was observed or established. [Norman: feedback in interacting systems](https://jnd.org/opportunities-and-challenges-for-touch-and-gesture-based-systems/).

### Constraints: limiting or guiding actions

Constraints reduce the range of possible or plausible actions. They differ in strength:

| Kind | Basis | Review application |
| --- | --- | --- |
| Physical | Structure or mechanics restrict action. | A keyed part blocks incorrect assembly. |
| Cultural | A shared convention guides behavior. | Familiar symbols suggest expected actions to a particular audience. |
| Semantic | The situation's meaning narrows interpretation. | A model vehicle's windshield belongs in front of its driver. |
| Logical | Relationships allow alternatives to be deduced. | One remaining compatible part and opening suggest the final placement. |

Do not treat a warning as equivalent to an enforced restriction. Cultural and logical constraints can be ignored or misunderstood. In software, an unavailable action should have a discoverable explanation and path forward when the reason is not apparent.

Forcing functions make a necessary condition a prerequisite to action. An **interlock** enforces a dependency or sequence; a **lock-in** prevents premature interruption or exit; a **lock-out** prevents entry into an inappropriate operation or state. Use these selectively: a restriction that blocks legitimate activity can create workarounds and new errors.

[Norman: constraints and conventions](https://jnd.org/affordance-conventions-and-design-part-2/), [book contents: constraints and forcing functions](https://jnd.org/books/the-design-of-everyday-things-revised-and-expanded-edition/).

### Conceptual models: explanations that support prediction

A conceptual model provides a useful explanation of how a system works. A person's mental model is the understanding they form; it may be incomplete or incorrect.

Distinguish the designer's model, the **system image** through which the product communicates, and the user's model. The system image includes appearance, behavior, instructions, and supporting information. Users cannot read the designer's intentions.

Inspect whether names, grouping, states, and behavior tell a coherent story. For example, "Save," "Publish," and "Share" need understandable relationships. Ask what someone would predict about visibility, ownership, persistence, or reversibility before acting. Do not assume the internal implementation is the best explanation for users.

Look for situations in which people could follow instructions correctly while holding a false belief about the result. Correct that explanation as well as the individual control. [Norman: Design as Communication](https://jnd.org/design-as-communication/).

### Discoverability: finding actions and understanding state

Discoverability concerns whether people can determine what actions are available and the current state of the system. It depends on the other principles working together.

Check how a newcomer finds the next action at the moment it is needed. Hidden gestures, unlabeled modes, and controls revealed only by an unexplained action deserve investigation. A feature's existence in a menu or help page does not establish that people will find it during the task.

Balance discovery with attention: showing every control at once can make the relevant action harder to identify. Progressive disclosure should provide a meaningful path to additional controls. Treat visibility as a contributor to discovery, with equivalent consideration for nonvisual interaction. [Norman: revision and discoverable possibilities](https://jnd.org/preface-design-of-everyday-things-revised-edition/).

## Action cycle and the two gulfs

The seven stages are **goal, plan, specify, perform, perceive, interpret, compare**. Use them to locate a breakdown; do not require conscious, linear execution of every stage.

- **Gulf of execution:** translating an intention into available actions.
- **Gulf of evaluation:** interpreting the resulting state and comparing it with the goal.

A visible "Share" command can help execution while an ambiguous completion message leaves evaluation unresolved. Ask both how someone acts and how they know the task succeeded.

**Feedforward** helps anticipate an action and its consequences; **feedback** helps understand the response. For example, "Delete 12 selected files" describes the forthcoming operation, while "12 files moved to Trash" reports its outcome.

[Book contents: action cycle](https://jnd.org/books/the-design-of-everyday-things-revised-and-expanded-edition/), [NN/g: the two gulfs and mistaken plans](https://www.nngroup.com/articles/user-mistakes/).

## Knowledge, conventions, and capability

**Knowledge in the head** includes remembered procedures and expertise. **Knowledge in the world** includes labels, visible selections, spatial relationships, checklists, and reminders. Check whether the task needlessly depends on remembering information the product could present at the point of decision.

For example, display the selected delivery address when asking someone to confirm it. "Use previous address" leaves them to recall which address was used. Preserve efficient learned shortcuts while providing an understandable path for occasional users.

External aids must also be usable: excessive instruction can bury the relevant information. Place reminders where the action occurs and make them specific to the current state. [Norman: knowledge in the head and the world](https://jnd.org/chapter-16-coffee-cups-in-the-cockpit/).

Evaluate conventions for the audience and setting. Expertise, language, sensory and motor capabilities, interruptions, gloves, noise, and lighting can change what is perceivable or operable. Do not treat a familiar interaction as universally intuitive. Use observation to resolve uncertain assumptions about convention and behavior. [Norman: conventions and observation](https://jnd.org/affordance-conventions-and-design-part-2/).

## Error and recovery

Distinguish error mechanisms before prescribing a remedy:

| Mechanism | Example | Candidate response |
| --- | --- | --- |
| Slip: execution diverges from an appropriate intention. | Selecting the adjacent file by accident. | Clarify selection, distinguish targets, allow correction. |
| Mistake: the goal or plan rests on an incorrect understanding. | Deleting a shared file believing only a personal shortcut is removed. | Explain scope and ownership before the decision. |
| Memory lapse: necessary information or an intention is forgotten. | Losing track of an unfinished step after interruption. | Preserve progress and show the next required action. |
| Mode error: acting under the wrong assumption about the active state. | Typing while an unexpected text-entry mode is active. | Make the mode apparent or reduce dependence on it. |

Memory lapses can contribute to slips or mistakes; mode errors are treated as slips in the book. These rows identify useful mechanisms rather than four mutually exclusive error classes.

Support prevention, detection, and recovery. Consider reversible operations, clear scope, preserved work, and understandable failure states. A generic confirmation may not correct a mistaken belief: someone can confidently confirm the wrong plan. Do not replace a necessary constraint with undo if the consequence cannot actually be reversed.

[NN/g: slips](https://www.nngroup.com/articles/slips/), [NN/g: mistakes](https://www.nngroup.com/articles/user-mistakes/), [Norman: revised error classification](https://jnd.org/preface-design-of-everyday-things-revised-edition/).

Look beyond the immediate action when procedures or incentives make errors predictable. Trace a recurring failure to its contributing conditions; do not stop at blaming the operator or assume training repairs misleading controls. Conversely, do not claim design is the cause of every error. [Norman: Human Error? No, Bad Design](https://jnd.org/human-error-no-bad-design/).

## Iteration, emotion, and practical constraints

Human-centered design investigates the underlying problem, observes activities, develops alternatives, prototypes, and tests. Treat a requested solution as a hypothesis about the need, while preserving the user's agreed scope. A hard-to-find export command might call for better placement or a different task model; observing the intended activity distinguishes those possibilities.

Choose a verification task that tests the diagnosis. Functional checks establish behavior; observing whether someone predicts and interprets the result tests understanding. Do not claim that either alone proves broad usability. [Norman: human-centered design principles](https://jnd.org/human-centered-versus-humanity-centered-design/).

When relevant, consider **visceral** immediate reactions, **behavioral** experience during use, and **reflective** meaning afterward. These help assess confidence, comfort, and interpretation without reducing the review to attractiveness. A pleasing appearance does not establish successful task completion. [Norman: Emotional Design](https://jnd.org/emotional-design-people-and-things/).

Account for necessary complexity, expert performance, cost, schedules, and organizational dependencies. Recommend changes proportionate to the task and identify tradeoffs. The book's later chapters address design in practice and business; a local interaction fix may not resolve a workflow or organizational problem. [Norman: the revised book's practical scope](https://jnd.org/books/the-design-of-everyday-things-1st-ed/).

## Worked example

**Artifact:** A supplied screenshot shows a document editor with a "Share" button and a notice reading "Done." No interaction has been observed.

**Finding:** The notice does not state whether the document was sent, access was granted, or a link was created. This is an observed ambiguity in feedback; confusion about completion is a hypothesis until checked. It may leave a gulf of evaluation even if the sharing action succeeds.

**Correction:** First establish the operation's actual result. Then communicate that result and its scope, such as "Link created; people with the link can view," if that is the implemented behavior. Do not invent delivery or permission guarantees to make the message sound reassuring.

**Verification:** Check the action and access state. Ask an intended user what happened and who can access the document after seeing the revised result. Successful execution and correct interpretation answer different questions.
