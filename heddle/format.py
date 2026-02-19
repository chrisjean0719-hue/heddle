"""Text plan for a warp."""


def _trim(number):
    text = f"{number:.2f}"
    if text.endswith("0"):
        text = text[:-1]
    if text.endswith(".0"):
        text = text[:-2]
    return text


def format_plan(plan):
    lines = [
        plan["name"],
        f"yarn: {plan['yarn']}",
        (
            f"cloth: {_trim(plan['width_in'])} in wide, "
            f"{_trim(plan['length_in'])} in long, {plan['epi']} epi"
        ),
        f"ends: {plan['ends']}",
        (
            f"warp: {_trim(plan['inches_per_end'])} in per end, "
            f"{_trim(plan['yards'])} yd, {_trim(plan['pounds'])} lb"
        ),
    ]
    if plan["reeds"]:
        reed_text = "; ".join(
            f"{reed['dents_per_inch']} dents/in, {reed['ends_per_dent']} "
            f"{'end' if reed['ends_per_dent'] == 1 else 'ends'} per dent"
            for reed in plan["reeds"]
        )
        lines.append(f"reed: {reed_text}")
    else:
        lines.append("reed: none of the common reeds divide this sett evenly")
    lines.append(f"shafts: {plan['shafts']}")
    for warning in plan["warnings"]:
        lines.append(f"warning: {warning}")
    return "\n".join(lines)
