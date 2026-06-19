"""Build a warp plan from a project object."""

from heddle.draft import draft, odd_plain_warning
from heddle.reed import reed_choices
from heddle.shrink import finished_cloth, half_size_warning
from heddle.threading import thread_ends
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
    weave = project.get("weave", "plain")
    shed = odd_plain_warning(project["shafts"], weave)
    if shed:
        warnings.append(shed)
    take_up = _rates(project, "takeUp")
    shrinkage = _rates(project, "shrinkage")
    finished = finished_cloth(project["widthIn"], project["lengthIn"], take_up, shrinkage)
    for axis, on_loom, done in (
        ("width", project["widthIn"], finished["width_in"]),
        ("length", project["lengthIn"], finished["length_in"]),
    ):
        small = half_size_warning(on_loom, done, axis)
        if small:
            warnings.append(small)

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
        "threading": thread_ends(ends, project["shafts"], project.get("threading", "straight")),
        "draft": draft(project["shafts"], weave),
        "finished": finished,
        "warnings": warnings,
    }


def _rates(project, field):
    value = project.get(field, {})
    return {"width": value.get("width", 0), "length": value.get("length", 0)}
