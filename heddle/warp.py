"""Warp ends and yarn length. Length is the cloth on the loom, plus tying-on waste."""

import math


def round_half_up(value):
    return int(math.floor(value + 0.5))


def end_count(width_in, epi):
    return round_half_up(width_in * epi)


def inches_per_end(length_in, loom_waste_in):
    return length_in + loom_waste_in


def warp_yards(ends, length_in, loom_waste_in):
    return ends * inches_per_end(length_in, loom_waste_in) / 36


def pounds(yards, yards_per_pound):
    return yards / yards_per_pound


def sett_warning(yarn, epi):
    if yarn["plain_min"] <= epi <= yarn["plain_max"]:
        return None
    return (
        f"epi {epi} is outside the plain-weave range "
        f"{yarn['plain_min']}-{yarn['plain_max']} for {yarn['name']}"
    )


def odd_end_warning(ends):
    if ends % 2 == 0:
        return None
    return f"{ends} ends is odd, so a plain weave will not close evenly"
