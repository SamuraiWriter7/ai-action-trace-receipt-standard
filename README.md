# AI Action Trace Receipt Standard

**AI Action Trace Receipt Standard** is a minimal open standard for recording AI-driven UI actions, intent, screen state, consent gates, risk boundaries, and trace links for agentic computer use.

> Search-based AI needs citations.
> Action-based AI needs receipts.

## Status

**Current status:** `v0.1.0-candidate`

This repository is currently an experimental candidate specification.

Version `v0.1.0-candidate` defines the first minimal structure for an **Action Trace Receipt**: a lightweight record that captures what an AI agent saw, why it acted, what UI action it performed, what changed after the action, and whether human consent or risk boundaries were involved.

This release is intended for:

* early discussion
* validation
* implementation experiments
* agentic computer-use auditing
* future integration with trace, attribution, and royalty systems

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
* or change external system states.

Once AI agents can act, simple output logging is no longer enough.

We need a structured way to record:

* what the agent saw,
* what it intended,
* what action it selected,
* what changed afterward,
* whether a human consent gate was required,
* whether the action was reversible,
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

## v0.1 Scope

Version `v0.1.0-candidate` defines the first minimal schema:

```text
Action Trace Receipt
```

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

## Non-Goals

This repository does not attempt to define:

* a complete AI agent framework
* a complete Computer Use runtime
* a universal UI automation protocol
* a full provenance graph
* a smart contract royalty implementation
* a replacement for browser history
* a replacement for security logs
* a complete legal or regulatory standard

The goal of `v0.1.0-candidate` is intentionally small:

> define the minimum receipt structure required to record AI-driven actions.

## Repository Structure

```text
ai-action-trace-receipt-standard/
  README.md
  CHANGELOG.md

  schemas/
    action-trace-receipt.schema.json

  examples/
    action-trace-receipt.example.yaml

  scripts/
    validate_examples.py

  .github/
    workflows/
      validate.yml
```

## Schema

The initial schema is located at:

```text
schemas/action-trace-receipt.schema.json
```

The schema defines the required structure for an `action_trace_receipt` object.

At minimum, a valid receipt includes:

* `receipt_id`
* `version`
* `origin_intent`
* `environment`
* `state_before`
* `action`
* `consent_gate`
* `state_after`
* `risk`

Optional sections include:

* `knowledge_context`
* `trace_links`
* `royalty_bridge`

## Example

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

## Validation

Examples can be validated with:

```bash
python scripts/validate_examples.py
```

The validator checks the example YAML file against the JSON Schema.

Expected output:

```text
[validate] AI Action Trace Receipt
  schema : schemas/action-trace-receipt.schema.json
  example: examples/action-trace-receipt.example.yaml
[ok] action-trace-receipt.example.yaml is valid
```

## GitHub Actions

This repository includes a GitHub Actions workflow:

```text
.github/workflows/validate.yml
```

The workflow runs validation automatically on:

* push
* pull request

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

## Conceptual Position

The standard begins from a simple distinction:

```text
Search Trace = what the AI read
Action Trace = what the AI did
Output Trace = what the AI produced
```

`v0.1.0-candidate` focuses only on the second layer:

```text
Action Trace = what the AI did
```

Future versions may expand toward a unified trace kernel that connects reading, acting, producing, auditing, and allocating.

## Consent and Risk Boundary

AI-driven action requires explicit boundaries.

This standard includes a `consent_gate` section because some actions may:

* submit external data,
* send messages,
* modify files,
* trigger payments,
* delete information,
* change account settings,
* or create irreversible state changes.

The `risk` section records whether an action is:

* low risk,
* medium risk,
* high risk,
* critical risk,
* reversible,
* or irreversible.

This makes the receipt useful not only for provenance, but also for operational safety and human review.

## Royalty Bridge

The `royalty_bridge` section is optional in `v0.1.0-candidate`.

It does not implement value allocation directly.

Instead, it provides lightweight metadata indicating whether the action may require:

* attribution,
* allocation,
* later connection to a royalty system,
* or linkage to a broader contribution graph.

Example:

```yaml
royalty_bridge:
  attribution_required: true
  allocation_required: false
```

## Design Philosophy

This standard follows five principles:

1. **Minimality**
   The receipt should be small enough to implement easily.

2. **Neutrality**
   The format should not depend on a specific AI model, platform, browser, or agent runtime.

3. **Traceability**
   Actions should record intent, state, outcome, and risk.

4. **Human Boundary**
   Consent gates should be explicit when actions may affect external systems.

5. **Future Linkability**
   Receipts should be able to connect with search traces, audit protocols, attribution systems, and royalty layers.

## Candidate Release Notes

`v0.1.0-candidate` introduces:

* initial Action Trace Receipt concept
* JSON Schema validation
* YAML example receipt
* Python validation script
* GitHub Actions workflow
* minimal bridge fields for trace and royalty systems

This candidate release is suitable for early experimentation and discussion.

## Possible Future Versions

Potential future versions may include:

```text
v0.2 — UI Action Event Layer
```

Detailed event structures for:

* click
* type
* scroll
* navigate
* submit
* save
* delete
* confirm
* cancel

```text
v0.3 — Consent Gate Expansion
```

More detailed human approval, irreversible action, and external side-effect policies.

```text
v0.4 — Risk and Rollback Policy
```

Structured risk classification, rollback availability, and stop conditions.

```text
v0.5 — Trace and Royalty Bridge
```

Stronger integration with search trace receipts, synchronization audit records, contribution graphs, and royalty allocation layers.

## Summary

AI systems are no longer only generating text.

They are beginning to act.

When AI acts, its actions need receipts.

This repository defines the first minimal candidate structure for recording those actions.

```text
Search-based AI needs citations.
Action-based AI needs receipts.
```

## License

To be determined.

