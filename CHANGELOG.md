# Changelog

All notable changes to this project will be documented in this file.

## [0.4.0-candidate] - 2026-06-26

### Added

- Added `Risk and Rollback Policy` layer.
- Added `schemas/risk-rollback-policy.schema.json`.
- Added `examples/risk-rollback-policy.example.yaml`.
- Updated validation script to validate:
  - `Action Trace Receipt`
  - `UI Action Event`
  - `Consent Gate Policy`
  - `Risk and Rollback Policy`

### Scope

`v0.4.0-candidate` introduces explicit risk classification, rollback availability, stop conditions, fallback behavior, and audit recording for AI-driven UI actions.

This release defines how an AI action should be evaluated when:

- risk level increases
- rollback may not be available
- the screen state is uncertain
- consent is missing
- sensitive data is detected
- external submission is detected
- payment or credential prompts appear
- an action fails or produces an unexpected result

### Purpose

The purpose of this release is to make AI-driven actions safer and more reviewable.

In this structure:

- `Action Trace Receipt` records the overall AI-driven action.
- `UI Action Event` records each meaningful interface event.
- `Consent Gate Policy` defines when human approval is required.
- `Risk and Rollback Policy` defines how to classify risk, when to stop, and how to recover or escalate when needed.

## [0.3.0-candidate] - 2026-06-26

### Added

- Added `Consent Gate Policy` layer.
- Added `schemas/consent-gate-policy.schema.json`.
- Added `examples/consent-gate-policy.example.yaml`.
- Updated validation script to validate:
  - `Action Trace Receipt`
  - `UI Action Event`
  - `Consent Gate Policy`

### Scope

`v0.3.0-candidate` expands the consent boundary model for AI-driven UI actions.

This release defines when an AI action should require explicit human approval before execution.

Consent triggers include:

- external submission
- payment
- message sending
- file modification
- file deletion
- credential entry
- personal data use
- account setting changes
- public publication
- irreversible actions
- high-risk actions

### Purpose

The purpose of this release is to make human review boundaries explicit.

In this structure:

- `Action Trace Receipt` records the overall action.
- `UI Action Event` records individual interface events.
- `Consent Gate Policy` defines when an event must pause for human approval.

## [0.2.0-candidate] - 2026-06-26

### Added

- Added `UI Action Event` layer.
- Added `schemas/ui-action-event.schema.json`.
- Added `examples/ui-action-event.example.yaml`.
- Updated validation script to validate both:
  - `Action Trace Receipt`
  - `UI Action Event`

### Scope

`v0.2.0-candidate` introduces a detailed event layer for recording individual UI actions inside or alongside an Action Trace Receipt.

The new event layer can represent actions such as:

- click
- type
- scroll
- navigate
- submit
- save
- delete
- confirm
- cancel
- read
- wait

### Purpose

The purpose of this release is to move from a single high-level action receipt toward a more granular event sequence model.

In this structure:

- `Action Trace Receipt` records the overall action context.
- `UI Action Event` records each meaningful interface event.

## [0.1.0-candidate] - 2026-06-26

### Added

- Initial `Action Trace Receipt` concept.
- Added JSON Schema for action trace receipts.
- Added YAML example receipt.
- Added validation script for examples.
- Added GitHub Actions workflow for schema validation.

### Scope

`v0.1.0-candidate` defines the minimum structure required to record:

- human origin intent
- AI action intent
- UI state before and after action
- consent gate
- risk boundary
- trace links
- royalty bridge metadata
