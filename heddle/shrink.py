"""Finished cloth size. Take-up is the loss off the loom, then shrinkage is the loss in washing."""


def _percent_left(percent):
    return 1 - percent / 100


def finished_measure(on_loom, take_up_percent, shrink_percent):
    return on_loom * _percent_left(take_up_percent) * _percent_left(shrink_percent)


def finished_cloth(width_in, length_in, take_up, shrinkage):
    return {
        "take_up": {"width": take_up["width"], "length": take_up["length"]},
        "shrinkage": {"width": shrinkage["width"], "length": shrinkage["length"]},
        "width_in": finished_measure(width_in, take_up["width"], shrinkage["width"]),
        "length_in": finished_measure(length_in, take_up["length"], shrinkage["length"]),
    }


def half_size_warning(on_loom, finished, axis):
    if finished < on_loom / 2:
        return f"finished {axis} is less than half the on-loom {axis}"
    return None
