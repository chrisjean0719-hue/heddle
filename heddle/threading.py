"""Straight and point threadings. Shaft 1 is the first shaft in the repeat."""


def straight_repeat(shafts):
    return list(range(1, shafts + 1))


def point_repeat(shafts):
    """Rise to the last shaft, then fall back to shaft 2, and repeat.

    The turning shafts are not threaded twice, so a 4-shaft point is 1 2 3 4 3 2.
    """
    return list(range(1, shafts + 1)) + list(range(shafts - 1, 1, -1))


def thread_ends(ends, shafts, kind):
    repeat = straight_repeat(shafts) if kind == "straight" else point_repeat(shafts)
    full, extra = divmod(ends, len(repeat))
    return {
        "kind": kind,
        "repeat": repeat,
        "repeats": full,
        "remainder": repeat[:extra],
    }
