"""Plain-weave and 2/2 twill tie-ups. Each treadle lists the shafts that rise."""


def plain_tie_up(shafts):
    odds = [shaft for shaft in range(1, shafts + 1) if shaft % 2 == 1]
    evens = [shaft for shaft in range(1, shafts + 1) if shaft % 2 == 0]
    return [odds, evens]


def twill_tie_up(shafts):
    """Each treadle lifts two neighboring shafts, stepping one shaft each pick.

    On four shafts the lifts are 1 2, then 2 3, then 3 4, then 4 1.
    """
    rows = []
    for index in range(shafts):
        first = index + 1
        second = (index + 1) % shafts + 1
        rows.append([first, second])
    return rows


def draft(shafts, weave):
    tie_up = plain_tie_up(shafts) if weave == "plain" else twill_tie_up(shafts)
    treadling = list(range(1, len(tie_up) + 1))
    return {
        "weave": weave,
        "tie_up": tie_up,
        "treadling": treadling,
        "lifts": [list(tie_up[treadle - 1]) for treadle in treadling],
    }


def odd_plain_warning(shafts, weave):
    if weave == "plain" and shafts % 2 == 1:
        return "plain weave on an odd number of shafts lifts two neighboring ends together"
    return None
