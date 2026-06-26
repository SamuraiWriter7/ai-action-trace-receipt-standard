# AI Action Trace Receipt Standard

**AI Action Trace Receipt Standard** is a minimal open standard for recording AI-driven UI actions, intent, screen state, consent gates, risk boundaries, rollback policies, trace links, and attribution / royalty bridge metadata for agentic computer use.

> Search-based AI needs citations.
> Action-based AI needs receipts.

## Current Status

**Current status:** `v0.5.0-candidate`

This candidate release adds the **Trace and Royalty Bridge** layer, connecting AI-driven action traces to search trace receipts, synchronization audit records, origin structures, attribution policies, usage logging, and future royalty systems.

The standard currently includes five core layers:

* `Action Trace Receipt` — records the overall AI-driven action.
* `UI Action Event` — records individual UI events such as clicks, typing, scrolling, navigation, and submission.
* `Consent Gate Policy` — defines human review boundaries for risky, irreversible, sensitive, or externally impactful actions.
* `Risk and Rollback Policy` — defines risk levels, rollback rules, stop conditions, fallback behavior, and audit requirements.
* `Trace and Royalty Bridge` — links action traces to source traces, origin structures, attribution policies, audit boundaries, and future allocation systems.

This repository is still experimental.

`v0.5.0-candidate` is intended for:

* early discussion
* validation
* implementation experiments
* agentic computer-use auditing
* trace interoperability
* future attribution and royalty-system integration

It is not yet a final or stable standard.

## Why This Exists

AI systems are moving from text generation into direct interaction with software interfaces.

An AI agent may now:

* view a screen,
* interpret UI elements,
* click buttons,
* type into forms,
* navigate pages,
* submit data,
* save files,
* trigger workflows,
* modify local or external state,
* and generate outputs through real software environments.

Once AI agents can act, simple output logging is no longer enough.

We need a structured way to record:

* what the agent saw,
* what it intended,
* what action it selected,
* what changed afterward,
* whether human consent was required,
* whether the action was reversible,
* how risk was classified,
* how rollback or fallback should work,
* and how the action connects to source traces, audits, attribution, and future royalty layers.

This repository defines that minimal record.

## Core Principle

> If an AI agent can act on a screen, its action should be traceable.

The basic flow is:

```text
Human Intent
  ↓
AI Perception
  ↓
UI Action
  ↓
State Change
  ↓
Action Trace Receipt
  ↓
Trace / Audit / Attribution / Royalty Bridge
```

## Purpose

The purpose of this repository is to define a minimal, implementation-neutral receipt format for AI-driven actions.

An **Action Trace Receipt** is not:

* a full browser automation framework,
* a universal agent runtime,
* a complete security log,
* a platform-specific telemetry format,
* a smart contract system,
* or a legal compliance framework.

Instead, it is a compact trace structure for recording meaningful AI actions in a way that can be validated, shared, audited, and connected to other trace systems.

## Repository Structure

```text
ai-action-trace-receipt-standard/
  README.md
  CHANGELOG.md

  schemas/
    action-trace-receipt.schema.json
    ui-action-event.schema.json
    consent-gate-policy.schema.json
    risk-rollback-policy.schema.json
    trace-royalty-bridge.schema.json

  examples/
    action-trace-receipt.example.yaml
    ui-action-event.example.yaml
    consent-gate-policy.example.yaml
    risk-rollback-policy.example.yaml
    trace-royalty-bridge.example.yaml

  scripts/
    validate_examples.py

  .github/
    workflows/
      validate.yml
```

## Specification Layers

The standard is currently organized into five layers.

```text
Action Trace Receipt
  └── UI Action Event
        ├── Consent Gate Policy
        ├── Risk and Rollback Policy
        └── Trace and Royalty Bridge
```

Each layer can be used independently, but they are designed to work together.

## v0.1 Scope — Action Trace Receipt

Version `v0.1.0-candidate` introduced the **Action Trace Receipt**.

This is the high-level receipt that records the overall AI-driven action.

It records:

* receipt identity
* specification version
* human origin intent
* optional knowledge context
* action environment
* screen or interface state before action
* AI action and action intent
* human consent gate
* screen or interface state after action
* risk boundary
* related trace links
* optional royalty bridge metadata

The first schema is located at:

```text
schemas/action-trace-receipt.schema.json
```

A minimal example is located at:

```text
examples/action-trace-receipt.example.yaml
```

Example:

```yaml
action_trace_receipt:
  receipt_id: atr-2026-0001
  version: "0.1.0"

  origin_intent:
    human_prompt: "Review the form and prepare it for submission."
    intent_hash: "sha256:example-intent-hash"

  knowledge_context:
    source_trace_receipts:
      - "astr-2026-0007"
    okf_bundle_id: "okf-demo-bundle-0001"

  environment:
    type: "browser"
    surface: "local_demo_ui"
    external_side_effect: false

  state_before:
    screenshot_hash: "sha256:example-before-screen"
    ui_elements:
      - type: "input"
        label: "Name"
      - type: "button"
        label: "Submit"

  action:
    type: "click"
    target: "Submit button"
    intent: "Prepare the completed form for human-confirmed submission."

  consent_gate:
    required: true
    approved: false
    reason: "Submission may create an external state change."

  state_after:
    screenshot_hash: "sha256:example-after-screen"
    outcome: "submission_confirmation_visible"

  risk:
    level: "medium"
    reversible: true

  trace_links:
    related_receipts:
      - "astr-2026-0007"

  royalty_bridge:
    attribution_required: true
    allocation_required: false
```

## v0.2 Scope — UI Action Event

Version `v0.2.0-candidate` introduced the **UI Action Event** layer.

While `v0.1.0-candidate` defines the high-level Action Trace Receipt, `v0.2.0-candidate` adds a more granular event structure for recording individual UI actions.

A UI Action Event can represent actions such as:

* click
* type
* scroll
* navigate
* submit
* save
* delete
* confirm
* cancel
* read
* wait

The basic relationship is:

```text
Action Trace Receipt
  └── UI Action Event 0
  └── UI Action Event 1
  └── UI Action Event 2
```

Each event can include:

* event identity
* parent receipt link
* sequence index
* actor
* environment
* event type
* event intent
* target UI element
* optional input payload
* before and after state hashes
* consent information
* result status
* risk boundary

The schema is located at:

```text
schemas/ui-action-event.schema.json
```

The example is located at:

```text
examples/ui-action-event.example.yaml
```

## v0.3 Scope — Consent Gate Policy

Version `v0.3.0-candidate` introduced the **Consent Gate Policy** layer.

While `v0.1.0-candidate` defines the high-level Action Trace Receipt and `v0.2.0-candidate` defines granular UI Action Events, `v0.3.0-candidate` defines when an AI-driven action should pause for human approval.

A consent gate may be required for actions such as:

* external submission
* payment
* message sending
* file modification
* file deletion
* credential entry
* personal data use
* account setting changes
* public publication
* irreversible actions
* high-risk actions

The basic relationship is:

```text
Action Trace Receipt
  └── UI Action Event
        └── Consent Gate Policy
```

Each Consent Gate Policy can include:

* policy identity
* scope
* consent triggers
* allowed approval states
* human review boundary
* default behavior when uncertain
* default behavior when denied
* default behavior when approval expires
* audit metadata

The schema is located at:

```text
schemas/consent-gate-policy.schema.json
```

The example is located at:

```text
examples/consent-gate-policy.example.yaml
```

## v0.4 Scope — Risk and Rollback Policy

Version `v0.4.0-candidate` introduced the **Risk and Rollback Policy** layer.

While `v0.3.0-candidate` defines when an AI-driven action should pause for human approval, `v0.4.0-candidate` defines how to classify action risk, determine rollback availability, identify stop conditions, and choose fallback behavior.

The Risk and Rollback Policy layer is designed to answer questions such as:

* How risky is this AI-driven action?
* Is the action reversible?
* Is rollback available?
* What should happen if the screen state is uncertain?
* What should happen if consent is missing?
* What should happen if the action fails?
* What should happen if the action cannot be safely rolled back?

The basic relationship is:

```text
Action Trace Receipt
  └── UI Action Event
        ├── Consent Gate Policy
        └── Risk and Rollback Policy
```

Each Risk and Rollback Policy can include:

* policy identity
* scope
* risk levels
* rollback rules
* stop conditions
* fallback behavior
* audit requirements

The schema is located at:

```text
schemas/risk-rollback-policy.schema.json
```

The example is located at:

```text
examples/risk-rollback-policy.example.yaml
```

## v0.5 Scope — Trace and Royalty Bridge

Version `v0.5.0-candidate` introduces the **Trace and Royalty Bridge** layer.

While the earlier versions define how AI-driven actions are recorded, evented, consent-gated, and risk-bounded, `v0.5.0-candidate` defines how those action traces can be connected to broader trace, attribution, audit, and royalty architectures.

The Trace and Royalty Bridge does not implement royalty allocation directly.

Instead, it provides bridge metadata for connecting an action trace to:

* search trace receipts
* UI action events
* synchronization audit records
* origin structure assets
* attribution policies
* allocation hints
* usage logging
* audit boundaries

The basic relationship is:

```text
Action Trace Receipt
  └── UI Action Event
        ├── Consent Gate Policy
        ├── Risk and Rollback Policy
        └── Trace and Royalty Bridge
```

## v0.6 Scope — Agent Session Trace

Version `v0.6.0-candidate` introduces the **Agent Session Trace** layer.

While earlier versions define individual action receipts, UI events, consent gates, risk boundaries, rollback policies, and trace bridges, `v0.6.0-candidate` groups those records into a single AI agent execution session.

The Agent Session Trace layer is designed to answer questions such as:

- Which agent performed the session?
- What runtime or harness was used?
- What isolation boundary protected the session?
- When did the session start and end?
- Which action receipts and UI events were included?
- Which consent and risk policies governed the session?
- Which trace and royalty bridges were linked?
- What was the final outcome?
- Were any risks unresolved?
- Was sensitive data redacted?

The basic relationship is:

```text
Agent Session Trace
  ├── Action Trace Receipt
  ├── UI Action Event
  ├── Consent Gate Policy
  ├── Risk and Rollback Policy
  └── Trace and Royalty Bridge

This allows an AI-driven action to be linked not only to what happened, but also to what prior knowledge, origin structure, or trace context contributed to the action.

Each Trace and Royalty Bridge can include:

* bridge identity
* scope
* trace links
* origin binding
* contribution context
* attribution policy
* allocation hint
* usage logging policy
* audit boundary

The schema is located at:

```text
schemas/trace-royalty-bridge.schema.json
```

The example is located at:

```text
examples/trace-royalty-bridge.example.yaml
```

## Validation

Examples can be validated with:

```bash
python scripts/validate_examples.py
```

The validator checks each example YAML file against its corresponding JSON Schema.

Expected output:

```text
[validate] AI Action Trace Receipt
  schema : schemas/action-trace-receipt.schema.json
  example: examples/action-trace-receipt.example.yaml
[ok] action-trace-receipt.example.yaml is valid
[validate] UI Action Event
  schema : schemas/ui-action-event.schema.json
  example: examples/ui-action-event.example.yaml
[ok] ui-action-event.example.yaml is valid
[validate] Consent Gate Policy
  schema : schemas/consent-gate-policy.schema.json
  example: examples/consent-gate-policy.example.yaml
[ok] consent-gate-policy.example.yaml is valid
[validate] Risk and Rollback Policy
  schema : schemas/risk-rollback-policy.schema.json
  example: examples/risk-rollback-policy.example.yaml
[ok] risk-rollback-policy.example.yaml is valid
[validate] Trace and Royalty Bridge
  schema : schemas/trace-royalty-bridge.schema.json
  example: examples/trace-royalty-bridge.example.yaml
[ok] trace-royalty-bridge.example.yaml is valid
```

## GitHub Actions

This repository includes a GitHub Actions workflow:

```text
.github/workflows/validate.yml
```

The workflow runs validation automatically on:

* push
* pull request

## Conceptual Position

This standard begins from a simple distinction:

```text
Search Trace = what the AI read
Action Trace = what the AI did
Output Trace = what the AI produced
```

`AI Action Trace Receipt Standard` focuses on the second layer:

```text
Action Trace = what the AI did
```

However, by `v0.5.0-candidate`, the standard also provides a bridge for connecting action traces to:

* search traces,
* synchronization audits,
* origin structures,
* attribution policies,
* and future royalty allocation layers.

## Relationship to Other Layers

This standard is designed to connect with broader trace, audit, and royalty architectures.

```text
AI Search Trace Receipt Standard
  ↓
AI Action Trace Receipt Standard
  ↓
Synchronization Audit Protocol
  ↓
Origin Structure Market
  ↓
Royalty OS
```

In this architecture:

* **AI Search Trace Receipt Standard** records what an AI system read, referenced, or searched.
* **AI Action Trace Receipt Standard** records what an AI system did.
* **Synchronization Audit Protocol** evaluates similarity, influence, origin ambiguity, and structural synchronization.
* **Origin Structure Market** treats origin structures as traceable assets.
* **Royalty OS** connects traceable contribution to future value allocation.

## Consent and Risk Boundary

AI-driven action requires explicit boundaries.

This standard includes consent and risk layers because some actions may:

* submit external data,
* send messages,
* modify files,
* trigger payments,
* delete information,
* change account settings,
* expose sensitive data,
* publish public content,
* or create irreversible state changes.

The standard is designed so that AI actions can be paused, reviewed, blocked, or escalated when risk becomes uncertain or unsafe.

## Trace and Royalty Bridge

The `Trace and Royalty Bridge` section does not implement value allocation directly.

Instead, it provides lightweight metadata indicating whether an action may require:

* attribution,
* allocation review,
* usage logging,
* audit review,
* origin binding,
* later connection to a royalty system,
* or linkage to a broader contribution graph.

This keeps the standard lightweight while allowing future connection to larger attribution and value-allocation systems.

## Design Philosophy

This standard follows five principles.

### 1. Minimality

The receipt should be small enough to implement easily.

### 2. Neutrality

The format should not depend on a specific AI model, platform, browser, or agent runtime.

### 3. Traceability

Actions should record intent, state, outcome, risk, and relevant links.

### 4. Human Boundary

Consent gates should be explicit when actions may affect external systems, sensitive data, money, public content, or irreversible state.

### 5. Future Linkability

Receipts should be able to connect with search traces, audit protocols, attribution systems, and royalty layers.

## Candidate Release Summary

`v0.5.0-candidate` includes:

* `Action Trace Receipt`
* `UI Action Event`
* `Consent Gate Policy`
* `Risk and Rollback Policy`
* `Trace and Royalty Bridge`
* JSON Schema validation
* YAML examples
* Python validation script
* GitHub Actions workflow

This candidate release is suitable for early experimentation and discussion.

## Possible Future Versions

Potential future versions may include:

```text
v0.6 — Agent Session Trace
```

A session-level structure for grouping multiple receipts and UI events into a longer AI agent workflow.

```text
v0.7 — Output Artifact Trace
```

A layer for recording what output, file, message, form, or artifact was produced by AI-driven action.

```text
v0.8 — Computer Use Adapter
```

Adapter-oriented mapping for browser, desktop, mobile, and tool-use runtimes.

```text
v0.9 — Unified Trace Kernel
```

A unified structure connecting search traces, action traces, output traces, audit records, and allocation metadata.

## Summary

AI systems are no longer only generating text.

They are beginning to act.

When AI acts, its actions need receipts.

This repository defines a candidate standard for recording those actions, reviewing their safety boundaries, and connecting them to broader trace, audit, attribution, and royalty systems.

```text
Search-based AI needs citations.
Action-based AI needs receipts.
```

## License

To be determined.
