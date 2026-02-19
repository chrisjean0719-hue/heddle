"""Yarns this planner knows. Sett ranges are for plain weave."""

YARNS = {
    "8/2 cotton": {"yards_per_pound": 3360, "plain_min": 18, "plain_max": 24},
    "5/2 cotton": {"yards_per_pound": 2100, "plain_min": 12, "plain_max": 16},
    "10/2 cotton": {"yards_per_pound": 4200, "plain_min": 24, "plain_max": 30},
    "8/4 cotton": {"yards_per_pound": 1680, "plain_min": 10, "plain_max": 15},
}


def yarn_names():
    return sorted(YARNS)


def lookup_yarn(name):
    if not isinstance(name, str):
        return None
    key = name.strip().lower()
    for yarn_name, yarn in YARNS.items():
        if yarn_name.lower() == key:
            return {"name": yarn_name, **yarn}
    return None
