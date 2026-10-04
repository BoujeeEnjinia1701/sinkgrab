---
doc_id: SKG-DEC-001
title: SinkGrab design decisions register
project: SinkGrab
doc_type: Design decisions register
version: "0.2"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: Register opened; design decisions made under Amish's pre-approvals of 2026-10-03; three requirement decisions (R4, R3, R1) proposed, awaiting Amish
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: Round 2. Amish decided R4 (1A), R3 (2B) and R1 (3B) as recommended (SKG-DDR-003); three new questions raised while carrying them out, proposed, awaiting Amish
---

# SinkGrab design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/` or in `docs/REVIEW.md`; this register is the index Amish works from. The build plan (`docs/05-build-plan.md`) describes the design as it stands and does not list decisions.

> **Safety:** Several decisions below set SinkGrab's safety case (overload limits, lowering on a brake that is on when let go, the doors over the shaft, no entry). Each took the conservative option; the evidence that would relax it is in SKG-DDR-001, Table 1. None of the open decisions below changes the safety case.

## Open decisions

Requirements that are not met or at risk on paper are decided by Amish (2026-10-03: "A simple statement doesn't add value - ensure you are identifying a state and posing it as a clear recommendation for me to decide on"). The three round 1 decisions (R4, R3, R1) were decided on 2026-10-03 and are listed under Decisions made. The questions below were raised while carrying them out; the full state, options and effects are in `docs/REVIEW.md`, session 2026-10-03, round 2. Each is **Proposed, awaiting Amish**.

| # | Decision needed | Options | Recommendation | Affects in the build | Source | Status |
| --- | --- | --- | --- | --- | --- | --- |
| 4 | Scraper fold travel and the 25 kg piece limit (R2, R9): the stop collar sits 30 mm below the sleeve foot, so the pole can lift only 30 mm on the sleeve before it picks the sleeve up, not the 320 mm the arms need to fold; and the longer arms (3B) bring the scraper head to 25.1 kg, 0.1 kg over R9 | A: remove the stop collar and let the struts carry the sleeve once the arms are folded, the folded geometry to be checked in the model (head 24.8 kg, R9 met; USD 0). B: lengthen the spike 320 mm and move the collar down with it (fold works; head about 25.9 kg, R9 not met unless the arms travel unpinned; about USD 5). C: no change (arms cannot fold, so the scraper passes only bores wider than the open toes; R2 not met) | **A** | Bottom pole: stop collar left off | SKG-CAL-001, H5 and K1; SKG-DDR-003 | Proposed, awaiting Amish |
| 5 | R4 wording: R4 is "3 min or less at 10 m with two operators"; the design now hoists with three (1A) | A: restate R4 as "3 min or less at 10 m with three people at the cranks for the hoist" (status unchanged: 3.16 min, not met on paper, within 5 %). B: keep the wording and report R4 against two people (3.8 min) | **A** | None | SKG-CAL-001, J | Proposed, awaiting Amish |
| 6 | Shear link margin: the 3:1 tackle added 3.3 kg to the grab (2.5 kg estimated), so the link's lowest release is 1.15 times the working pull (was 1.19) | A: keep it and watch for releases in the test-pit bite trial (no change). B: thin the ballast plates from 16 to 10 mm to win back 2 kg (margin about 1.18; head weight for opening 14.0 to 12.0 kg) | **A** | None | SKG-CAL-001, C5 | Proposed, awaiting Amish |

## To confirm when parts are bought

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | Release load of the link pins from the coil bought, by breaking three pins | The link must release between 1.20 and 1.47 kN; the pin diameter (about 1.9 mm) is chosen from these breaks | SKG-CAL-001, C |
| 2 | Release of the 3 mm crank shear pins from the bar bought | Sized on 240 MPa shear; a stronger bar lets the line pass the tripod's proof load | SKG-CAL-001, C |
| 3 | Breaking strength and splice of the 8 mm rope bought | Factors assume 12 kN and 90 % at the splice | SKG-CAL-001, E |
| 4 | Sheave groove, bore and width fit the HatchSide cheeks and 20 mm axle | The head sheave is swapped while SinkGrab works | SKG-DDR-002, item 2 |
| 5 | HatchSide foot plate size and thickness on the tripod as built | The cradle rim and clamp bars are sized on 140 x 280 mm | SKG-DWG-107 |
| 6 | Brake lining friction on the steel drum | Holding torque assumes 0.35 | SKG-CAL-001, F |
| 7 | Bearing centre heights and bolt pitches | Pads and top plates are drilled to UCP206 and UCP205 catalogue sizes | SKG-DWG-101 |
| 8 | Ring size and wall thickness at the trial well | Toe position, skid holes and saddle slot are set for a 1.0 m ring with a 75 mm wall | SKG-DWG-112, 113, 117 |

## Value engineering

Value-engineering target: USD 4,000 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 2,561 (USD 1,439 under the target), USD 55 more than before the round 2 decisions (SKG-DDR-003). Main cost drivers and savings worth trying:

- The four-gas detector (USD 550) is the largest line; a crew or partner that already owns a pumped detector saves it.
- The eight ballast saddles (USD 240) and their lines (USD 100): saddles cast in concrete inside a steel strap would cost less, at more bulk.
- The two grab shells (USD 120) need plate rolls; a fabricator with rolls is the cheapest route, a cut-and-fold faceted skin the fallback.
- The pole sections (USD 108 for six) scale with well depth.

## Decisions made

| Date | Decision | Decided by | Record |
| --- | --- | --- | --- |
| 2026-10-03 | Two-shell clamshell grab worked on one closing line, opened by the head's weight | Amish: "I pre-approve the batch runs along with any recommendations you come up with." and "Proceed with the remaining 15 scaffolds" | SKG-DDR-001, items 1, 2 |
| 2026-10-03 | Shear link (1.20 to 1.47 kN) and 3 mm crank shear pin keep the line inside the HatchSide rating and proof load | Amish, as above | SKG-DDR-001, item 3 |
| 2026-10-03 | SinkGrab hand capstan (single drum, 4:1 chain, pawl, band brake) in place of the HatchSide winch | Amish, as above | SKG-DDR-001, item 4 |
| 2026-10-03 | Drawbar to a cradle under the leg A foot; no ground anchors | Amish, as above | SKG-DDR-001, item 5 |
| 2026-10-03 | Lowering on a weighted band brake with the cranks removed | Amish, as above | SKG-DDR-001, item 6 |
| 2026-10-03 | Centred scraper pole with centralizer and weight-opened arms | Amish, as above | SKG-DDR-001, item 7 |
| 2026-10-03 | No de-watering; sump at most 330 mm below the cutting edge | Amish, as above | SKG-DDR-001, item 8 |
| 2026-10-03 | Tilt read every cycle; correct from 1 in 160; stop undercutting at 1 in 80 | Amish, as above | SKG-DDR-001, item 9 |
| 2026-10-03 | Ballast saddles on their own lines in place of a ballast frame | Amish, as above | SKG-DDR-001, item 10 |
| 2026-10-03 | Well-head frame with folding doors and spoil tubs in place of a chute and tipping hook | Amish, as above | SKG-DDR-001, item 11 |
| 2026-10-03 | First co-design candidate to approach: Kerala Ground Water Department (not agreed); second, a rural water NGO in the Ethiopian highlands | Amish, as above | SKG-DDR-001, item 12 |
| 2026-10-03 | HatchSide tripod used with a swapped 8 mm head sheave; SinkGrab capstan recorded as the single-drum variant of the common capstan block; CalRig as first candidate proof-load rig | Amish, as above | SKG-DDR-001, item 13 |
| 2026-10-03 | Targeted patent search for under-curb scraper claims before public release | Amish, as above | SKG-DDR-001, item 14 |
| 2026-10-03 | `budget_usd` kept at 4,000 as a value-engineering target | Amish: "I also accept any cost overruns or variations from the assumed scope cost." | SKG-DDR-001, item 15 |
| 2026-10-03 | Design for construction: the fifteen changes of SKG-DDR-002 | Amish, as for item 1 | SKG-DDR-002 |
| 2026-10-03 | Scraper working limit 25 m (12 pole sections) | Amish, as for item 1 | SKG-CAL-001, H |
| 2026-10-03 | Appearance model additions for renders: wound rope, context collar, ground, tub, ring pieces and mannequin | Amish, as for item 1 | docs/REVIEW.md, TRL 3 |
| 2026-10-03 | R4 cycle time (open decision 1): option A, a third person at the cranks for the hoist on a 240 mm two-hand handle; 3.16 min, not met on paper, within 5 % | Amish: "i approve all of the 47 recommendations provided by you. Execute them." | SKG-DDR-003, item 1 |
| 2026-10-03 | R3 bite (open decision 2): option B, a 3:1 tackle with a second sheave in the head; lips about 687 N; R3 still at risk on the fill | Amish, as above | SKG-DDR-003, item 2 |
| 2026-10-03 | R1 depth gained (open decision 3): option B, toes cutting 40 mm past the ring's outer face; R1 still at risk on the friction | Amish, as above | SKG-DDR-003, item 3 |
| 2026-10-03 | Fold lift 320 mm so the longer arms fold inside a 400 mm bore (made to keep 3B constructable) | Amish, as above | SKG-DDR-003, Table 3 |

## Change log

- 2026-10-03, v0.2: open decisions 1 to 3 decided as recommended (1A, 2B, 3B) and carried into the design (SKG-DDR-003); new questions 4 to 6 opened.
