# Changelog

All notable changes to this project will be documented in this file.

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
