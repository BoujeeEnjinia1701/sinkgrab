---
doc_id: SKG-DDR-003
title: SinkGrab requirement decisions, round 2
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
  change: Amish's decisions on R4 (1A), R3 (2B) and R1 (3B) carried into the model, calculations, BOM, drawings and build plan
---

# 0003: Requirement decisions, round 2

- **Date:** 2026-10-03
- **Status:** Decided by Amish Chadha, 2026-10-03: "i approve all of the 47 recommendations provided by you. Execute them." For SinkGrab these are the three requirement decisions of SKG-DEC-001 (portfolio decisions 31, 32 and 33), each decided as recommended.

## Context

At TRL 3 (SKG-CAL-001 v0.1) the constructable design (SKG-DDR-002) missed R4, a 3 min cycle at 10 m, at about 3.7 min, because two people at the cranks give about 100 W and the hoist took 111 s. R3, at least 20 L a bite, was at risk: the lips closed with only about 0.71 of the line pull through the 2:1 tackle, and the line can pull no more than the grab's submerged weight. R1, 3 m of depth gained below the water table, was at risk: the 8-ring string keeps sinking only while skin friction stays below 1.66 kPa, against an estimate of 1 to 3 kPa. The three were put to Amish with options and a recommendation in `docs/REVIEW.md` and SKG-DEC-001.

## Options considered

*Table 1. The three decisions put to Amish and the option chosen.*

| # | Requirement | Options | Chosen |
| --- | --- | --- | --- |
| 1 | R4, cycle time | A: a third person at the cranks during the hoist with a 240 mm two-hand handle. B: narrower 240 mm shells (bite about 15 L, R3 not met). C: keep two people and make 4 min the trial target | **A** |
| 2 | R3, bite per cycle | A: keep the 2:1 tackle and settle the fill in test-pit trials. B: a 3:1 tackle with a second sheave in the head. C: 10 kg more ballast on the head | **B** |
| 3 | R1, depth gained | A: as designed, measure friction in the first trial. B: longer toes cutting 40 mm past the ring's outer face. C: sixteen saddles instead of eight | **B** |

## Decision

*Table 2. Each decision as carried into the design. Figures from SKG-CAL-001 v0.2 (`docs/04-calcs/sizing.py`).*

| # | Requirement | Option chosen | Effect on the design | Condition |
| --- | --- | --- | --- | --- |
| 1 | R4 | A: third person at the cranks for the hoist | The +X crank carries a 32 mm handle 240 mm long for two hands (the -X crank keeps its 120 mm handle). Three people at 50 W hoist the full grab at 8.7 m/min; the hoist takes 77 s and the cycle 3.16 min, 5 % over the 3 min target. With two people it is 3.8 min. BOM line 4, USD 10 more | R4 stays **not met on paper**, within 5 %; the timed trial settles the last 0.16 min. R4 is worded for two operators; restating it is a new question (`docs/REVIEW.md`) |
| 2 | R3 | B: 3:1 closing tackle | A second bought 150 mm sheave hangs under the head box between two 8 mm cheeks on a 20 mm axle, skewed 20 degrees about the vertical so both of its rope parts hang straight; the dead end and the shear link move from the head to a 12 mm lug on the crosshead's -Y plate. The line now runs down the guide tube, under the crosshead sheave, up over the head sheave and down to the shear link. Mean lip force rises from 0.71 to 1.06 of the line pull: about 687 N at the lips, 50 % more. Closing takes 426 mm of line, about 1 s more a cycle. The grab gains 3.3 kg (estimate 2.5 kg) to 51.2 kg; the working pull rises to 1,042 N, the shear link's margin falls from 1.19 to 1.15 and the line factor from 10.7 to 10.4. BOM lines 10, 13, 14 and 25: USD 35 more | R3 stays **at risk**: the fill is still an assumption (21.2 L at 75 %, 14.1 L at 50 %) and is settled in the TRL 4 test-pit bite trial; the stronger close makes the higher fill more likely |
| 3 | R1 | B: toes cutting 40 mm past the ring | Arms 25 mm longer (564 mm pivot to toe); the toes reach 615 mm radius, 40 mm past a 1.0 m ring's outer face (was 15 mm). Two people need 142 N each on the T-bar, 4 % more. The soil removed for 3 m of sinking rises to about 3.56 m³. BOM line 15, USD 10 more | R1 stays **at risk**: the friction limit is still 1.66 kPa and the friction itself is only measured in a trial; the wider cut is meant to keep it toward the low end of the 1 to 3 kPa estimate |

*Table 3. Change made while carrying out decision 3, to keep the design constructable (STANDARDS section 18).*

| # | Change | Why |
| --- | --- | --- |
| 4 | Fold lift 320 mm (was 300 mm) | With the longer arms a 300 mm lift folds the toes to 405.5 mm radius, outside the 400 mm bore of the smallest (0.8 m) ring; a 320 mm lift folds them to 377 mm. The model's constructability check passes again. This does not change what the scraper does |

## Consequences

- `cad/src/model.py` carries the changes (`handle_long`, `tackle_parts`, `head_sheave_skew`, `head_sheave_z`, `toe_r` 615, `fold_lift` 320, new parts `upper_sheave` and `upper_axle`); the checks report no overlaps and no floating parts.
- SKG-CAL-001 v0.2 is re-run: R4 3.16 min (not met on paper, within 5 %); R3 at risk with 687 N at the lips; R1 at risk; R9 now **not met on paper by 0.1 kg**, because the longer arms bring the scraper head to 25.1 kg against the 25 kg limit (a new question in `docs/REVIEW.md`).
- Estimated cost of the constructable design: USD 2,561 (was USD 2,506), USD 1,439 under the USD 4,000 value-engineering target; `budget_usd` unchanged.
- STEP and STL, SKG-DWG-001 and 002 (Rev P3), the concept media, `media/model.glb` and the build plan pictures and making sketches are regenerated from the model. The photoreal renders made on Amish's Mac predate this change.
- New questions raised while carrying out the decisions (scraper fold travel and the 25 kg piece limit, R4 wording, shear link margin) are recorded in `docs/REVIEW.md` and SKG-DEC-001 as **Proposed, awaiting Amish**.
