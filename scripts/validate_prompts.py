"""
Validates that all prompt files follow the required format.

Expected format per file:
  # [Title]
  **Model:** ...
  **Category:** ...
  **Variables:** ...
  ---
  [Prompt body — at least 50 chars]

Exit 0 if all pass, exit 1 with details if any fail.
"""

import os
import sys
import re

REQUIRED_FIELDS = ["**Model:**", "**Category:**", "**Variables:**"]
PROMPTS_DIR = os.path.join(os.path.dirname(__file__), "..", "prompts")


def validate_file(path: str) -> list[str]:
    errors = []
    with open(path, encoding="utf-8") as f:
        content = f.read()

    if not content.startswith("# "):
        errors.append("Missing title (must start with '# ')")

    for field in REQUIRED_FIELDS:
        if field not in content:
            errors.append(f"Missing required field: {field}")

    if "---" not in content:
        errors.append("Missing '---' separator between header and prompt body")

    parts = content.split("---", 1)
    if len(parts) > 1:
        body = parts[1].strip()
        if len(body) < 50:
            errors.append(f"Prompt body too short ({len(body)} chars, min 50)")

    return errors


def main():
    all_passed = True
    checked = 0

    for root, _, files in os.walk(PROMPTS_DIR):
        for fname in files:
            if fname.endswith(".md") and fname != ".gitkeep":
                fpath = os.path.join(root, fname)
                rel = os.path.relpath(fpath, PROMPTS_DIR)
                errors = validate_file(fpath)
                checked += 1
                if errors:
                    all_passed = False
                    print(f"FAIL  {rel}")
                    for e in errors:
                        print(f"      - {e}")
                else:
                    print(f"PASS  {rel}")

    print(f"\n{checked} prompt(s) checked.")
    if not all_passed:
        print("Validation FAILED.")
        sys.exit(1)
    else:
        print("All prompts valid.")


if __name__ == "__main__":
    main()
