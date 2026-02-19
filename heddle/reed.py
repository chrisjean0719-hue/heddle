"""Common reed densities that divide a sett into a whole number of ends per dent."""

COMMON_DENTS = (5, 6, 8, 10, 12, 15)
MAX_ENDS_PER_DENT = 4


def reed_choices(epi):
    choices = []
    for dents in COMMON_DENTS:
        if epi % dents == 0:
            per_dent = epi // dents
            if 1 <= per_dent <= MAX_ENDS_PER_DENT:
                choices.append({"dents_per_inch": dents, "ends_per_dent": per_dent})
    return choices
