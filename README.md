# AI Action Trace Receipt Standard

**AI Action Trace Receipt Standard** is a minimal open standard for recording AI-driven UI actions, intent, screen state, consent gates, risk boundaries, and trace links for agentic computer use.

As AI agents move from reading and generating text into operating real interfaces, a new layer of accountability becomes necessary.

Search-based AI needs citations.
Action-based AI needs receipts.

This standard defines a lightweight receipt format for recording:

* what an AI agent saw,
* why it acted,
* what UI action it performed,
* what changed after the action,
* whether human consent was required,
* whether the action was reversible,
* and how the action connects to source traces, attribution, audit, and royalty layers.

## Purpose

The purpose of this repository is to define a minimal, implementation-neutral record for AI-driven actions.

An **Action Trace Receipt** is not a full automation log, browser history, or platform-specific telemetry format.

It is a structured receipt for one or more meaningful AI actions, designed to support:

* AI action accountability
* human consent boundaries
* UI state transition records
* agentic computer-use auditing
* source and action trace linkage
* future attribution and royalty systems

## Core Principle

> If an AI agent can act on a screen, its action should be traceable.

The standard begins with a simple idea:

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

## v0.1 Scope

Version `v0.1` defines the first minimal receipt schema:

```text
Action Trace Receipt
```

It records:

* receipt identity
* origin intent
* knowledge context
* action environment
* screen state before action
* AI action
* human consent gate
* screen state after action
* risk boundary
* trace links
* royalty bridge metadata

## Non-Goals

This repository does not attempt to define:

* a complete browser automation framework
* a universal agent runtime
* a smart contract royalty system
* platform-specific telemetry
* a replacement for security logs
* a complete legal compliance framework

Instead, it defines the minimum trace structure required for interoperable AI action receipts.

## Relationship to Other Layers

This standard is designed to connect with:

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

* **Search Trace Receipt** records what an AI read or referenced.
* **Action Trace Receipt** records what an AI did.
* **Synchronization Audit** evaluates similarity, influence, and origin ambiguity.
* **Royalty OS** allocates value back to origin structures when appropriate.

## Example

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

## Status

This repository is experimental.

The current version is a candidate specification for discussion, validation, and small-scale implementation examples.

## License

To be determined.
