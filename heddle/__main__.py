"""Command-line entry. Run from the project root: python -m heddle plan examples/scarf.json"""

import json
import sys
from pathlib import Path

from heddle.format import format_plan
from heddle.plan import PlanError, plan_warp


def main(argv=None):
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) != 2 or args[0] != "plan":
        print("Usage: python -m heddle plan <project.json>", file=sys.stderr)
        return 2

    path = Path(args[1])
    try:
        project = json.loads(path.read_text(encoding="utf-8"))
    except OSError as error:
        print(f"Could not read {path}: {error}", file=sys.stderr)
        return 1
    except json.JSONDecodeError as error:
        print(f"Invalid JSON in {path}: {error}", file=sys.stderr)
        return 1

    try:
        plan = plan_warp(project)
    except PlanError as error:
        print(error, file=sys.stderr)
        return 1

    print(format_plan(plan))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
