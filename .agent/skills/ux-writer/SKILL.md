---
name: ux-writer
description: Skill for designing microcopy, interface strings, and optimizing user flows through text. Apply when creating UI components, error handling, onboarding, and transactional messaging.
---

# UX Writer Skill

## Objective
Maximize product ROI by reducing user cognitive load and eliminating friction points in the interface.

## Execution Rules (No Fluff)
1. **Conciseness**: Delete every word that doesn't carry functional weight. Minimum adjectives, maximum action verbs.
2. **Clarity**: Eliminate technical jargon (unless it's a dev-tool). Terminology must be consistent across the entire product.
3. **Action-Oriented**: Every text element must answer "What do I do next?" or "What just happened?".
4. **Hierarchy**: Crucial info in the header. Context in the subheader. Expected result in the CTA.

## Interface Analysis Protocol
1. **Context Audit**: Where is the user? (Screen, system state, previous action).
2. **User Goal Identification**: What target action is expected on this step?
3. **Edge Case Validation**: Ensure error messages, empty states, and loading states are addressed.

## Components & Patterns

### Buttons (CTA)
- Format: [Verb] + [Object].
- *Example*: Use "Save Changes" instead of "Click here to save".
- Avoid ambiguity: No "OK" or "Next" if the action can be specified.

### Error Messages
1. **Problem**: Clear statement of fact without blaming the user.
2. **Reason**: Brief cause (if helpful for the solution).
3. **Solution**: Direct instruction or a "recovery" button.
- *Strictly Prohibited*: "An unknown error occurred", "Error 500".

### Onboarding & Tooltips
- Describe **Value**, not the feature.
- Limit: Maximum 2-3 sentences per screen/tooltip.

## Performance Metrics (KPIs)
- **Task Success Rate**: Did the user complete the task after reading the text?
- **Time on Task**: Was decision-making time reduced?
- **Support Volume**: Did tickets decrease for this specific flow?

## Agent Instructions
When asked to "write app text," "fix a button," or "perform UX editing":
1. Apply this skill to analyze the provided UI/flow.
2. Provide 2-3 variants (Concise, Standard, Direct) with rationale based on cognitive load.
3. Validate text against technical constraints (character limits, container size).