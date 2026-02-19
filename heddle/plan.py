"""Build a warp plan from a project object."""

from heddle.reed import reed_choices
from heddle.validate import validate_project
from heddle.warp import end_count, inches_per_end, odd_end_warning, pounds, sett_warning, warp_yards
from heddle.yarns import lookup_yarn


class PlanError(Exception):
    def __init__(self, errors):
        self.errors = errors
        super().__init__("\n".join(errors))


def plan_warp(project):
    errors = validate_project(project)
    if errors:
        raise PlanError(errors)

    yarn = lookup_yarn(project["yarn"])
    ends = end_count(project["widthIn"], project["epi"])
    yards = warp_yards(ends, project["lengthIn"], project["loomWasteIn"])
    warnings = []
    sett = sett_warning(yarn, project["epi"])
    if sett:
        warnings.append(sett)
    odd = odd_end_warning(ends)
    if odd:
        warnings.append(odd)

    return {
        "name": project["name"].strip(),
        "yarn": yarn["name"],
        "width_in": project["widthIn"],
        "length_in": project["lengthIn"],
        "loom_waste_in": project["loomWasteIn"],
        "epi": project["epi"],
        "ends": ends,
        "inches_per_end": inches_per_end(project["lengthIn"], project["loomWasteIn"]),
        "yards": yards,
        "pounds": pounds(yards, yarn["yards_per_pound"]),
        "reeds": reed_choices(project["epi"]),
        "shafts": project["shafts"],
        "warnings": warnings,
    }
