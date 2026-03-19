# Heddle

A command-line planner for a handloom warp. It counts the ends in a cloth width, turns the on-loom length and tying-on waste into yards and pounds, lists common reeds that divide the sett evenly, threads those ends in a straight draw or a point draw, and ties the shafts for plain weave or a 2/2 twill.

It is for someone winding a warp at home. The sample cloths are made up. The tool does not store names, addresses, or customer orders.

Written in Python 3.11 or newer, with no dependencies. Tests use the built-in `unittest` runner.

## Run

```bash
python -m heddle plan examples/scarf.json
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
  "weave": "plain"
}
```

`widthIn` and `lengthIn` are the cloth on the loom, in inches. `epi` is ends per inch. `loomWasteIn` is the extra length for tying on. Yarn choices are `8/2 cotton`, `5/2 cotton`, `10/2 cotton`, and `8/4 cotton`. The plan warns when the sett sits outside that yarn's plain-weave range, and when the end count is odd. Reeds are 5, 6, 8, 10, 12, and 15 dents per inch, using 1 to 4 ends in each dent. `shafts` is how many shafts the loom has, from 2 to 16. `threading` is `straight` or `point`. Leave it out to keep a straight draw, which repeats shafts 1 through the last shaft. A point draw rises to the last shaft and falls back to shaft 2 without threading the turning shaft twice, so four shafts repeat as 1 2 3 4 3 2. The plan prints that repeat, how many times it fits, and any leftover ends. It does not yet reject a warp that ends in the middle of a repeat. `weave` is `plain` or `twill`. Leave it out to keep plain weave, which lifts the odd shafts against the even shafts. A 2/2 twill needs at least 4 shafts. Each treadle lifts two neighboring shafts and the next pick steps one shaft forward, so four shafts lift 1 2, then 2 3, then 3 4, then 4 1. The plan prints the tie-up and the shafts that rise for each pick in the treadling repeat. An odd shaft count warns that plain weave lifts two neighboring ends together. Finished size after shrinkage is later work.

## Layout

```
heddle/     yarn table, checks, warp math, reed, threading, tie-up, text plan
examples/   fictional cloths
tests/      unit tests
```

## Next

Three updates remain. About 38 hours of later work stay in [ROADMAP.md](ROADMAP.md) after those six.

## License

MIT
