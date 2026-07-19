"""Command-line entry. Run from the project root: python -m heddle plan examples/scarf.json"""

import json
import sys
from pathlib import Path

from heddle.drawdown import drawdown_svg
from heddle.format import format_plan
from heddle.plan import PlanError, plan_warp

USAGE = "Usage: python -m heddle plan <project.json>\n       python -m heddle draw <project.json> [--out directory]"


def main(argv=None):
    args = list(sys.argv[1:] if argv is None else argv)
    if not args or args[0] not in ("plan", "draw"):
        print(USAGE, file=sys.stderr)
        return 2
    if args[0] == "plan":
        if len(args) != 2:
            print(USAGE, file=sys.stderr)
            return 2
        return _print_plan(args[1])
    return _draw(args[1:])


def _load(path):
    file = Path(path)
    try:
        return json.loads(file.read_text(encoding="utf-8")), None
    except OSError as error:
        return None, f"Could not read {file}: {error}"
    except json.JSONDecodeError as error:
        return None, f"Invalid JSON in {file}: {error}"


def _print_plan(path):
    project, error = _load(path)
    if error:
        print(error, file=sys.stderr)
        return 1
    try:
        plan = plan_warp(project)
    except PlanError as error:
        print(error, file=sys.stderr)
        return 1
    print(format_plan(plan))
    return 0


def _draw(args):
    out = None
    if len(args) == 1:
        path = args[0]
    elif len(args) == 3 and args[1] == "--out":
        path = args[0]
        out = args[2]
    else:
        print(USAGE, file=sys.stderr)
        return 2

    project, error = _load(path)
    if error:
        print(error, file=sys.stderr)
        return 1
    try:
        plan = plan_warp(project)
    except PlanError as error:
        print(error, file=sys.stderr)
        return 1

    svg = drawdown_svg(plan["name"], plan["drawdown"]["rows"])
    if out is None:
        print(svg, end="")
        return 0
    directory = Path(out)
    directory.mkdir(parents=True, exist_ok=True)
    file = directory / "drawdown.svg"
    file.write_text(svg, encoding="utf-8")
    print(file)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
