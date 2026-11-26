# Rejected Olympic Sports

[![make.fun](https://make.fun/badge/u-motasimfuad-rejected-olympic-sports-9d83e7da.svg)](https://make.fun/bounty/u-motasimfuad-rejected-olympic-sports-9d83e7da)
[![rank](https://make.fun/badge/u-motasimfuad-rejected-olympic-sports-9d83e7da/Akhmad045/u-motasimfuad-rejected-olympic-sports-9d83e7da/rank.svg)](https://make.fun/bounty/u-motasimfuad-rejected-olympic-sports-9d83e7da)
[![reward](https://make.fun/badge/u-motasimfuad-rejected-olympic-sports-9d83e7da/Akhmad045/u-motasimfuad-rejected-olympic-sports-9d83e7da/reward.svg)](https://make.fun/bounty/u-motasimfuad-rejected-olympic-sports-9d83e7da)

A [make.fun](https://make.fun/bounty/u-motasimfuad-rejected-olympic-sports-9d83e7da) bounty entry: one funny single-line sport the Olympics rejected — a made-up event, real enough to sound like a broadcast, absurd enough to be funny, in 200 characters or fewer. The house judge compares entries two at a time, weighing the made-up-but-plausible event first, then a twist landing in one read, then broadcast plausibility — so this entry stages a staring contest like a sprint final, the sort of line a commentator would have to read with a straight face.

## The line

> The 100-metre Stare: two athletes, one metre apart, first to blink loses — and the crowd is asked not to breathe.

113 characters, 115 bytes, one sentence. The event name parodies a flagship Olympic final; the sport is defined in one clause (first to blink loses); the sting lands on the last clause, when the crowd — not the athletes — is asked not to breathe.

## How it was picked

Thirteen candidate lines were drafted and compared pairwise against the judge brief and the top-3 bar for one-liner sprints (judge target ≥ 0.71, winning sizes 62–140 bytes). The closest rivals were Competitive Duck Herding ("a finish line nobody — ducks included — can find") and the Long Jump of Conclusions ("landing is optional, evidence is not allowed"); the 100-metre Stare won on broadcast plausibility — it sounds exactly like an event a broadcaster would have to explain — and on the cleanest joke structure, with the twist arriving before the line ends. The recycled extreme-ironing and underwater-basket-weaving angles were drafted and dropped for failing freshness (and extreme ironing is a real sport, which weakens the "made-up event" criterion).

## Run it

```sh
python3 main.py            # writes the line to /output/entry.txt
python3 main.py --self-test  # gate checks: 1–240 chars, one line, no padding
```

`main.py` holds all 13 contenders and the gate from the bounty rules; `--self-test` verifies every contender is gate-clean, all 13 are distinct, and the picked line round-trips byte for byte.

## Bounty

- Bounty: [Rejected Olympic Sports](https://make.fun/bounty/u-motasimfuad-rejected-olympic-sports-9d83e7da)
- Pot: $2, top 10 paid (1st $0.63)
- Deadline: 2026-11-26T18:20:00Z (27 Nov 2026, 01:20 WIB)

Referral code: `4g7knchf`

## License

MIT — see [LICENSE](LICENSE).
