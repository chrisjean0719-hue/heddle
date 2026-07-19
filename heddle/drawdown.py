"""A cloth drawdown. Each column is one warp end and each row is one pick.

The first row is the first pick. A black cell means that end's shaft is rising,
so the warp is on top.
"""

CELL = 8
REPEATS = 2


def drawdown_rows(threading_repeat, lifts, repeats=REPEATS):
    ends = list(threading_repeat) * repeats
    rows = []
    for _ in range(repeats):
        for lift in lifts:
            rising = set(lift)
            rows.append([shaft in rising for shaft in ends])
    return rows


def drawdown_svg(name, rows):
    picks = len(rows)
    ends = len(rows[0]) if rows else 0
    width = ends * CELL
    height = picks * CELL
    shapes = []
    for row_index, row in enumerate(rows):
        for column_index, warp_up in enumerate(row):
            x = column_index * CELL
            y = row_index * CELL
            fill = "black" if warp_up else "white"
            shapes.append(
                f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" fill="{fill}" stroke="black"/>'
            )
    body = "\n".join(f"  {shape}" for shape in shapes)
    title = _escape(f"{name} drawdown")
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}">\n'
        f"  <title>{title}</title>\n"
        f"{body}\n"
        "</svg>\n"
    )


def _escape(value):
    return (
        value.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&apos;")
    )
