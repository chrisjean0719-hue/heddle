"""Check a warp project before planning it."""

import math

from heddle.yarns import lookup_yarn, yarn_names


def _positive_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value) and value > 0


def _non_negative_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value) and value >= 0


def validate_project(project):
    """Return a list of problems. An empty list means the project can be planned."""
    if not isinstance(project, dict):
        return ["project: Project must be an object"]

    errors = []
    name = project.get("name")
    if not isinstance(name, str) or name.strip() == "":
        errors.append("name: Project needs a name")

    if lookup_yarn(project.get("yarn")) is None:
        errors.append(f"yarn: Unknown yarn \"{project.get('yarn')}\". Use {', '.join(yarn_names())}")

    if not _positive_number(project.get("widthIn")):
        errors.append("widthIn: widthIn must be a positive number of inches")

    epi = project.get("epi")
    if not isinstance(epi, int) or isinstance(epi, bool) or epi <= 0:
        errors.append("epi: epi must be a positive integer")

    if not _positive_number(project.get("lengthIn")):
        errors.append("lengthIn: lengthIn must be a positive number of inches")

    if not _non_negative_number(project.get("loomWasteIn")):
        errors.append("loomWasteIn: loomWasteIn must be zero or more inches")

    shafts = project.get("shafts")
    if not isinstance(shafts, int) or isinstance(shafts, bool) or shafts < 2 or shafts > 16:
        errors.append("shafts: shafts must be an integer from 2 to 16")

    threading = project.get("threading", "straight")
    if threading not in ("straight", "point"):
        errors.append("threading: threading must be straight or point")

    weave = project.get("weave", "plain")
    if weave not in ("plain", "twill"):
        errors.append("weave: weave must be plain or twill")
    elif weave == "twill" and isinstance(shafts, int) and not isinstance(shafts, bool) and shafts < 4:
        errors.append("weave: a 2/2 twill needs at least 4 shafts")

    return errors
