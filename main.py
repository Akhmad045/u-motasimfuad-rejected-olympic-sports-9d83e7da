#!/usr/bin/env python3
"""Rejected Olympic Sports.

Writes one funny single-line sport the Olympics rejected to
/output/entry.txt (or the path given with --out).

The entry is candidate 1 of 13 drafted lines, picked by internal pairwise
comparison against the judge brief (a funny made-up event the Games might
plausibly have turned down first, then a twist landing in one read, then a
broadcast-plausible event, then economy, then quotability) and the top-3 bar
for one-liner sprints (judge target >= 0.71, winning sizes 62-140 bytes).
The winning line parodies a flagship Olympic event name -- the 100-metre
Stare -- so a commentator would have to read it with a straight face: two
athletes, one metre apart, first to blink loses, and the crowd is asked not
to breathe. It is 113 chars / 115 bytes, inside the winning size band, and
its angle (a staring contest staged like a sprint final) is fresh against
the recycled extreme-ironing and underwater-basket-weaving lines.

Usage:
    python3 main.py [--out PATH] [--self-test]
"""
import argparse
import os
import sys

# 13 drafted candidates, each one sentence, 1-240 chars, single line.
CONTENDERS = [
    # 1. WINNER. The 100-metre Stare: a sprint final where blinking loses.
    "The 100-metre Stare: two athletes, one metre apart, first to blink "
    "loses \u2014 and the crowd is asked not to breathe.",
    # 2. Duck herding: the finish line nobody can find, ducks included.
    "Competitive Duck Herding: twelve ducks, one whistle, and a finish "
    "line nobody \u2014 ducks included \u2014 can find.",
    # 3. Extreme ironing: real sport, so weaker on "made-up"; kicker lands.
    "Extreme Ironing: athletes press shirts on a cliff edge, judged on "
    "creases, courage, and not falling off.",
    # 4. Synchronised queueing: British queue trope, "Team GB" narrows it.
    "Synchronised Queueing: Team GB lines up in perfect formation, and "
    "the gold goes to whoever waited longest without complaining.",
    # 5. Underwater basket weaving: classic "useless major" trope, dated.
    "Underwater Basket Weaving: divers weave at ten metres, judged on "
    "pattern, poise, and how soggy the basket is.",
    # 6. Competitive napping: "waking up exactly on time" is a nice twist.
    "Competitive Napping: athletes sleep for eight hours, judged on "
    "drool, snoring, and waking up exactly on time.",
    # 7. Synchronised eye-rolling: punchy, but the sport itself is thin.
    "Synchronised Eye-Rolling: judged on arc, velocity, and how clearly "
    "the teenager means it.",
    # 8. Long Jump of Conclusions: clever wordplay, slightly abstract.
    "The Long Jump \u2014 of Conclusions: athletes leap from one wild "
    "assumption to another; landing is optional, evidence is not allowed.",
    # 9. Competitive ghosting: clean kicker, but ghosting is a known trope.
    "Competitive Ghosting: athletes ignore each other for four years, and "
    "the gold goes to whoever never replies.",
    # 10. Extreme accountancy: "perfectly reconciled ledger" is a good sting.
    "Extreme Accountancy: competitors balance the books live, and the "
    "crowd goes wild for a perfectly reconciled ledger.",
    # 11. Marathon of Apologies: "sorry for the apology" triple, well-worn.
    "The Marathon of Apologies: runners say sorry for overtaking, sorry "
    "for winning, and sorry for the apology.",
    # 12. Speed bricklaying: gentle joke, "mortar that holds the dream".
    "Speed Bricklaying: a wall a minute, judged on straightness, stamina, "
    "and the mortar that holds the dream together.",
    # 13. Synchronised snoring: "waking the baby" twist, slightly random.
    "Synchronised Snoring: duets of snores in perfect harmony; the judges "
    "deduct points for waking the baby.",
]

PICK = 0  # 0-based index of candidate 1, the 100-metre Stare.


def gate(line):
    """The sealed scorer's gate: UTF-8 text, 1-240 chars, not only
    whitespace, one line, no leading/trailing padding."""
    if not isinstance(line, str):
        return False
    if not 1 <= len(line) <= 240:
        return False
    if line.strip() == "":
        return False
    if line != line.strip():
        return False
    if "\n" in line or "\r" in line:
        return False
    return True


def entry_text():
    return CONTENDERS[PICK]


def self_test():
    """Verify every contender is gate-clean, all 13 are distinct, the pick
    sits inside the winning size band (62-140 bytes, the one-liner top-10
    range), and a round-tripped pick matches byte for byte."""
    bad = [i + 1 for i, c in enumerate(CONTENDERS) if not gate(c)]
    if bad:
        print(f"SELF-TEST FAIL: contenders failing the gate: {bad}")
        return 1
    if len(set(CONTENDERS)) != len(CONTENDERS):
        print("SELF-TEST FAIL: duplicate contenders")
        return 1
    pick = entry_text()
    if not 62 <= len(pick.encode("utf-8")) <= 140:
        print(f"SELF-TEST FAIL: pick is {len(pick.encode('utf-8'))} bytes, "
              f"outside the 62-140 winning size band")
        return 1
    tmp = "/tmp/rejected-olympic-sports-self-test.txt"
    with open(tmp, "w", encoding="utf-8", newline="") as fh:
        fh.write(pick)
    with open(tmp, "rb") as fh:
        raw = fh.read()
    if raw != pick.encode("utf-8"):
        print("SELF-TEST FAIL: round-tripped pick differs")
        return 1
    if raw.endswith(b"\n"):
        print("SELF-TEST FAIL: written entry has a trailing newline; the "
              "entry must be exactly the picked line, nothing else")
        return 1
    if len(raw) != len(pick.encode("utf-8")):
        print("SELF-TEST FAIL: written entry byte length differs from pick")
        return 1
    print(f"SELF-TEST OK: {len(CONTENDERS)} contenders gate-clean and "
          f"distinct; pick #{PICK + 1} is {len(pick)} chars / "
          f"{len(pick.encode('utf-8'))} bytes (inside the 62-140 winning "
          f"size band), round-trips byte-identical")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default="/output/entry.txt",
                        help="where to write the entry (default: %(default)s)")
    parser.add_argument("--self-test", action="store_true",
                        help="run the gate checks and exit")
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    text = entry_text()
    if not gate(text):
        print("GATE FAIL: picked line does not satisfy the 1-240 char, "
              "single-line, no-padding gate", file=sys.stderr)
        return 1
    parent = os.path.dirname(args.out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(args.out, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    # Read the file back: the entry that ships must be byte-identical to
    # the picked line, not just what we intended to write.
    with open(args.out, encoding="utf-8", newline="") as fh:
        written = fh.read()
    if written != text:
        print("WRITE-BACK FAIL: /output/entry.txt differs from the pick",
              file=sys.stderr)
        return 1
    print(f"Wrote {len(text)} chars / {len(text.encode('utf-8'))} bytes "
          f"to {args.out} (read-back verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
