"""Compare two warp plans by ends, yards, and finished width."""


def compare_plans(left, right):
    return {
        "ends": (left["ends"], right["ends"]),
        "yards": (left["yards"], right["yards"]),
        "finished_width_in": (left["finished"]["width_in"], right["finished"]["width_in"]),
    }


def format_compare(left, right, diff):
    return "\n".join(
        [
            f"{left['name']} vs {right['name']}",
            f"ends: {diff['ends'][0]} vs {diff['ends'][1]}",
            f"yards: {_trim(diff['yards'][0])} vs {_trim(diff['yards'][1])}",
            (
                f"finished width: {_trim(diff['finished_width_in'][0])} in vs "
                f"{_trim(diff['finished_width_in'][1])} in"
            ),
        ]
    )


def _trim(number):
    text = f"{number:.2f}"
    if text.endswith("0"):
        text = text[:-1]
    if text.endswith(".0"):
        text = text[:-2]
    return text
