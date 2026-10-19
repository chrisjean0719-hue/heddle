# Heddle

A command-line planner for a handloom warp. It counts the ends in a cloth width, turns the on-loom length and tying-on waste into yards and pounds, lists common reeds that divide the sett evenly, threads those ends in a straight draw or a point draw, ties the shafts for plain weave or a 2/2 twill, turns the on-loom size into a finished size, draws two repeats of the cloth as an SVG, and compares two plans.

It is for someone winding a warp at home. The sample cloths are made up. The tool does not store names, addresses, or customer orders.

Written in Python 3.11 or newer, with no dependencies. Tests use the built-in `unittest` runner.

## Run

```bash
python -m heddle plan examples/scarf.json
python -m heddle draw examples/scarf.json --out draw
python -m heddle compare examples/scarf.json examples/towel.json
python -m unittest discover -s tests
```

A project looks like this:

```json
{
  "name": "Sample scarf",
  "yarn": "8/2 cotton",
  "widthIn": 10,
  "epi": 24,
  "lengthIn": 72,
  "loomWasteIn": 27,
  "shafts": 4,
  "threading": "straight",
  "weave": "plain",
  "takeUp": { "width": 10, "length": 10 },
  "shrinkage": { "width": 10, "length": 10 }
}
```

`widthIn` and `lengthIn` are the cloth on the loom, in inches. `epi` is ends per inch. `loomWasteIn` is the extra length for tying on. Yarn choices are `8/2 cotton`, `5/2 cotton`, `10/2 cotton`, and `8/4 cotton`. The plan warns when the sett sits outside that yarn's plain-weave range, and when the end count is odd. Reeds are 5, 6, 8, 10, 12, and 15 dents per inch, using 1 to 4 ends in each dent. `shafts` is how many shafts the loom has, from 2 to 16. `threading` is `straight` or `point`. Leave it out to keep a straight draw, which repeats shafts 1 through the last shaft. A point draw rises to the last shaft and falls back to shaft 2 without threading the turning shaft twice, so four shafts repeat as 1 2 3 4 3 2. The plan prints that repeat, how many times it fits, and any leftover ends. It does not yet reject a warp that ends in the middle of a repeat. `weave` is `plain` or `twill`. Leave it out to keep plain weave, which lifts the odd shafts against the even shafts. A 2/2 twill needs at least 4 shafts. Each treadle lifts two neighboring shafts and the next pick steps one shaft forward, so four shafts lift 1 2, then 2 3, then 3 4, then 4 1. The plan prints the tie-up and the shafts that rise for each pick in the treadling repeat. An odd shaft count warns that plain weave lifts two neighboring ends together. `takeUp` is the percent lost when the cloth comes off the loom, and `shrinkage` is the further percent lost in washing. Each has `width` and `length`. Leave either out to keep that loss at zero. Finished size is the on-loom measure times what remains after take-up, then times what remains after shrinkage. The plan warns when a finished side is less than half the on-loom side. `heddle draw` writes an SVG of two threading repeats and two treadling repeats. A black cell is a warp end on top, and a white cell is weft on top. The first row is the first pick. Leftover ends at the end of the warp are not in the picture. `--out <directory>` saves `drawdown.svg`. `heddle compare` prints the two plans' end counts, warp yards, and finished widths.

## Layout

```
heddle/     yarn table, checks, warp math, reed, threading, tie-up, shrinkage, drawdown, compare, text plan
examples/   fictional cloths
tests/      unit tests
```

## Next

The six updates are complete. About 38 hours of later work stay in [ROADMAP.md](ROADMAP.md).

## License

MIT
