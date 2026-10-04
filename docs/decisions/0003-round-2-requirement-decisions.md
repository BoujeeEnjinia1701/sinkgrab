---
doc_id: SKG-DDR-003
title: SinkGrab requirement decisions of 2026-10-03 (R4, R3, R1)
project: SinkGrab
doc_type: Design decision record
version: "0.1"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: "Amish's decisions 27A, 28B and 29B of 2026-10-03 recorded and carried out in the model, calculations, drawings and build plan"
---

# 0003: Requirement decisions of 2026-10-03 (R4, R3, R1)

- **Date:** 2026-10-03
- **Status:** accepted

## Context

The TRL 3 calculations (SKG-CAL-001 v0.1) left one requirement not met on paper and two at risk, each posed to Amish with options and a recommendation in the design decisions register (SKG-DEC-001, open decisions 1 to 3) and `docs/REVIEW.md`:

- **R4, cycle time:** about 3.7 min at 10 m against 3 min, because two people at the cranks give about 100 W and the hoist took 111 s.
- **R3, bite per cycle:** 21.2 L at an assumed 75 % fill but 14.1 L at 50 %, because the 2:1 tackle closed the lips with only 0.71 of the line pull, capped by the grab's submerged weight.
- **R1, depth gained:** the 8-ring string keeps sinking to 3 m only while skin friction stays below 1.66 kPa, against an estimate of 1 to 3 kPa.

These were items 27, 28 and 29 of the portfolio's round-2 list. Amish Chadha (owner), 2026-10-03: "i agree with all the 46 recommendations you provided. please proceed."

## Options considered

| Item | Option A | Option B | Option C |
| --- | --- | --- | --- |
| 27, R4 | **A third person at the cranks during the hoist, on a 240 mm two-hand handle (chosen)** | Narrower 240 mm shells: 3.4 min but a 15 L bite, so R3 missed | Keep two people and make 4 min the trial target |
| 28, R3 | Keep the 2:1 tackle and settle the fill in trials | **A 3:1 tackle with a second sheave in the head (chosen)** | 10 kg more head ballast: 14 % more lip force, shear link margin down to 1.08 |
| 29, R1 | Toes 15 mm past the ring as drawn; measure in the trial | **Toe blades cutting 40 mm past the ring's outer face (chosen)** | Sixteen saddles: limit 1.81 kPa for 165 kg more kit and USD 340 |

## Decision

All three as recommended:

1. **27A.** The +X crank carries a 32 x 240 mm handle on a longer M12 bolt so two people can work it side by side; a third person joins the hoist and the crew is two at other times. R4 is restated: "3 min or less per grab cycle at 10 m depth with three people at the cranks during the hoist and two otherwise" (SKG-REQ-001 v0.4).
2. **28B.** The closing line now runs down through the head's guide tube, under the crosshead sheave, up over a fourth bought sheave (the upper sheave) hung on two 6 mm cheeks under the head, and down to the shear link on a dead-end arm and lug welded to the crosshead. The upper sheave stands across the hinge direction so the line comes up into it on the grab's centre plane and leaves 130 mm to one side. The dead-end arm stays above 140 mm from the hinge so the open shells clear it.
3. **29B.** A 10 mm wear-resistant blade, 100 x 35 mm, is welded under the end of each scraper arm at the cutting level, lapped on the toe plate and standing 25 mm beyond it, so the blades cut 40 mm past a 1.0 m ring's outer face (first design 15 mm). The arm and its linkage are unchanged, so the fold is unchanged apart from the blade.

## Consequences

From SKG-CAL-001 v0.2 and `cad/src/model.py` (no overlaps, no parts adrift, folded scraper inside the smallest bore):

| Requirement | Before | After | Target | Status |
| --- | --- | --- | --- | --- |
| R4 cycle at 10 m | 3.7 min (two people) | 3.17 min with three at the hoist (3.8 min with two) | 3 min or less | Not met on paper by about 0.2 min (6 %); the timed trial decides |
| R3 bite | 21.2 L at 75 %, lips closing with about 437 N | 21.2 L at 75 %, lips closing with about 685 N (1.06 of the line pull, 50 % more) | At least 20 L | Met on paper at the assumed fill; the test-pit trial confirms the fill |
| R1 depth | Sinks while friction is below 1.66 kPa | Unchanged limit; blades cut 40 mm past the ring to keep friction low | At least 3 m | At risk; friction measured in the first trial |

- **Mass.** The grab rises from 47.9 to 51.0 kg (upper sheave 2.2 kg, axle, cheeks and dead-end arm), about 0.6 kg more than the 2.5 kg estimated when the option was posed. The cranks gain about 0.8 kg (the handle is modelled solid; a tube is lighter). The toe blades add about 0.4 kg, which takes the scraper head with its arms on to 25.2 kg, over the 25 kg limit of R9: it is carried with the arms unpinned (19.2 and 6.0 kg), and the heaviest piece is then the capstan frame at 22.9 kg. The kit is about 456 kg.
- **Overload limits.** Every part of the line carries the same tension, so the shear link still sees the line pull. Its lowest release is now 1.15 times the working pull (1.19 before), and the proof load at twice the working load is 193 kg, inside HatchSide's 225 kg. The crank pin limits are unchanged.
- **Cycle.** The 3:1 tackle takes 426 mm of line to close (284 before), about 1.5 s more a cycle, and its 3.1 kg slows the hoist by about 4 s; the third person saves about 39 s.
- **Scraper.** The T-bar force rises 4 % (142 N each for two people). Folded, the blades reach 389 mm radius, inside the 400 mm bore of a 0.8 m ring with 11 mm to spare. The soil to remove for 3 m of sinking rises from 3.28 to 3.56 m3.
- **Cost.** Value-engineering target: USD 4,000. Estimated cost of the constructable design: USD 2,561 (USD 1,439 under the target). The changes add USD 55: upper sheave USD 30 and cheeks, axle and dead-end arm USD 5 (USD 35 for the tackle), the long handle USD 10, the toe blades USD 10.
- **Safety.** Three people now stand at the capstan during the hoist. The briefing card and safety stop 4 say that all three let go together on the stop call, the pawl holds the drum, and nobody stands between the capstan and the lead sheave. The crank shear pin matters more with a third person, not less.
- **Finding while checking the fold.** The scraper's arms fold only if the sleeve can slide 300 mm down the pole, but the stop collar is drawn 40 mm below the sleeve, so as drawn the toes fold only to about 604 mm radius. This was true of the first design too. It is posed to Amish in SKG-DEC-001 and `docs/REVIEW.md`.
- **Changed files.** `cad/src/model.py`, `docs/04-calcs/sizing.py` and `01-sizing.md` (v0.2), `docs/03-requirements.md` (v0.4), `docs/02-concept.md` (v0.4), `docs/05-build-plan.md` (v0.2), `bom/bom.csv` (lines 4, 10, 13, 14, 15, 25), SKG-DWG-001 and 002 (Rev P3), SKG-DWG-103, 110, 111, 113, joints 9 and 14, steps 9, 13 and 20, the overview, concept media and `cad/src/product_model.py`.
