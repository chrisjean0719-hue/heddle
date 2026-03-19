"""Text plan for a warp."""


def _trim(number):
    text = f"{number:.2f}"
    if text.endswith("0"):
        text = text[:-1]
    if text.endswith(".0"):
        text = text[:-2]
    return text


def _format_threading(threading):
    repeat = " ".join(str(shaft) for shaft in threading["repeat"])
    if threading["remainder"]:
        remainder = " ".join(str(shaft) for shaft in threading["remainder"])
    else:
        remainder = "none"
    return [
        f"threading: {threading['kind']}",
        f"repeat: {repeat}",
        f"repeats: {threading['repeats']}",
        f"remainder: {remainder}",
    ]


def _shafts(numbers):
    return " ".join(str(number) for number in numbers)


def _format_draft(draft):
    lines = [f"weave: {draft['weave']}", "tie-up:"]
    for index, row in enumerate(draft["tie_up"], start=1):
        lines.append(f"  treadle {index}: {_shafts(row)}")
    lines.append(f"treadling: {_shafts(draft['treadling'])}")
    lines.append("lifts:")
    for index, lift in enumerate(draft["lifts"], start=1):
        lines.append(f"  pick {index}: {_shafts(lift)}")
    return lines


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
    lines.extend(_format_threading(plan["threading"]))
    lines.extend(_format_draft(plan["draft"]))
    for warning in plan["warnings"]:
        lines.append(f"warning: {warning}")
    return "\n".join(lines)
