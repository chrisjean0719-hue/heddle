# Heddle

A command-line planner for a handloom warp. It counts the ends in a cloth width, turns the on-loom length and tying-on waste into yards and pounds, and lists common reeds that divide the sett evenly.

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
  "shafts": 4
}
```

`widthIn` and `lengthIn` are the cloth on the loom, in inches. `epi` is ends per inch. `loomWasteIn` is the extra length for tying on. Yarn choices are `8/2 cotton`, `5/2 cotton`, `10/2 cotton`, and `8/4 cotton`. The plan warns when the sett sits outside that yarn's plain-weave range, and when the end count is odd. Reeds are 5, 6, 8, 10, 12, and 15 dents per inch, using 1 to 4 ends in each dent. `shafts` is how many shafts the loom has, from 2 to 16. Finished size after shrinkage is later work.

## Layout

```
heddle/     yarn table, checks, warp math, reed, text plan
examples/   fictional cloths
tests/      unit tests
```

## Next

Five updates remain. About 38 hours of later work stay in [ROADMAP.md](ROADMAP.md) after those six.

## License

MIT
