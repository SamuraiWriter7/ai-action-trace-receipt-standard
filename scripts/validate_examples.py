import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]

VALIDATION_TARGETS = [
    {
        "name": "AI Action Trace Receipt",
        "schema": ROOT / "schemas" / "action-trace-receipt.schema.json",
        "example": ROOT / "examples" / "action-trace-receipt.example.yaml",
    },
    {
        "name": "UI Action Event",
        "schema": ROOT / "schemas" / "ui-action-event.schema.json",
        "example": ROOT / "examples" / "ui-action-event.example.yaml",
    },
    {
        "name": "Consent Gate Policy",
        "schema": ROOT / "schemas" / "consent-gate-policy.schema.json",
        "example": ROOT / "examples" / "consent-gate-policy.example.yaml",
    },
    {
        "name": "Risk and Rollback Policy",
        "schema": ROOT / "schemas" / "risk-rollback-policy.schema.json",
        "example": ROOT / "examples" / "risk-rollback-policy.example.yaml",
    },
]


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main() -> int:
    failed = False

    for target in VALIDATION_TARGETS:
        name = target["name"]
        schema_path = target["schema"]
        example_path = target["example"]

        print(f"[validate] {name}")
        print(f"  schema : {schema_path.relative_to(ROOT)}")
        print(f"  example: {example_path.relative_to(ROOT)}")

        schema = load_json(schema_path)
        example = load_yaml(example_path)

        validator = Draft202012Validator(schema)
        errors = sorted(validator.iter_errors(example), key=lambda e: e.path)

        if errors:
            failed = True
            print(f"[error] {name} validation failed")
            for error in errors:
                path = ".".join(str(p) for p in error.path) or "<root>"
                print(f"  - path: {path}")
                print(f"    message: {error.message}")
        else:
            print(f"[ok] {example_path.name} is valid")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
