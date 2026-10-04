---
doc_id: SKG-DEC-001
title: SinkGrab design decisions register
project: SinkGrab
doc_type: Design decisions register
version: "0.3"
status: Draft
date: '2026-10-04'
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
  change: "Amish's round-2 decisions 27A, 28B and 29B of 2026-10-03 moved to Decisions made (SKG-DDR-003); one new decision posed: the scraper sleeve's travel"
- version: "0.3"
  date: '2026-10-04'
  author: Amish Chadha
  change: "Amish's round-3 decision 5A of 2026-10-04 (scraper sleeve travel) moved to Decisions made (SKG-DDR-004); no open decisions"
---

# SinkGrab design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/` or in `docs/REVIEW.md`; this register is the index Amish works from. The build plan (`docs/05-build-plan.md`) describes the design as it stands and does not list decisions.

> **Safety:** Several decisions below set SinkGrab's safety case (overload limits, lowering on a brake that is on when let go, the doors over the shaft, no entry). Each took the conservative option; the evidence that would relax it is in SKG-DDR-001, Table 1. None of the requirement decisions of 2026-10-03 and 2026-10-04 changes the safety case.

## Open decisions

None. Every decision posed so far has been made by Amish: R4, R3 and R1 on 2026-10-03 and the scraper sleeve's travel (R2) on 2026-10-04 (below). Requirements that are not met or at risk on paper are posed to Amish as a state, options and a recommendation (Amish, 2026-10-03: "A simple statement doesn't add value - ensure you are identifying a state and posing it as a clear recommendation for me to decide on"); what remains of R4 and R1 is settled by the timed trial and the first well trial, as already decided.

## To confirm when parts are bought

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | Release load of the link pins from the coil bought, by breaking three pins | The link must release between 1.20 and 1.47 kN; the pin diameter (about 1.9 mm) is chosen from these breaks | SKG-CAL-001, C |
| 2 | Release of the 3 mm crank shear pins from the bar bought | Sized on 240 MPa shear; a stronger bar lets the line pass the tripod's proof load | SKG-CAL-001, C |
| 3 | Breaking strength and splice of the 8 mm rope bought | Factors assume 12 kN and 90 % at the splice | SKG-CAL-001, E |
| 4 | Sheave groove, bore and width fit the HatchSide cheeks and 20 mm axle, and the grab head's cheeks 30 mm apart | The head sheave is swapped while SinkGrab works; the upper sheave of the 3:1 tackle uses the same sheave | SKG-DDR-002, item 2; SKG-DDR-003 |
| 5 | HatchSide foot plate size and thickness on the tripod as built | The cradle rim and clamp bars are sized on 140 x 280 mm | SKG-DWG-107 |
| 6 | Brake lining friction on the steel drum | Holding torque assumes 0.35 | SKG-CAL-001, F |
| 7 | Bearing centre heights and bolt pitches | Pads and top plates are drilled to UCP206 and UCP205 catalogue sizes | SKG-DWG-101 |
| 8 | Ring size and wall thickness at the trial well | Toe position, skid holes and saddle slot are set for a 1.0 m ring with a 75 mm wall | SKG-DWG-112, 113, 117 |
| 9 | The sleeve slides the full 300 mm of its slots on the cross pin, and the arms fold to inside an 800 mm circle | The head must pass a 0.8 m ring when lifted | SKG-DDR-004; SKG-DWG-113 |

## Value engineering

Value-engineering target: USD 4,000 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 2,566 (USD 1,434 under the target). Main cost drivers and savings worth trying:

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
| 2026-10-03 | R4 (item 27A): a third person on the cranks during the hoist, on a 240 mm two-hand handle on the +X crank; R4 restated for three people at the hoist; cycle 3.17 min, about 0.2 min over, the timed trial decides | Amish: "i agree with all the 46 recommendations you provided. please proceed." | SKG-DDR-003, item 1 |
| 2026-10-03 | R3 (item 28B): a 3:1 closing tackle, with an upper sheave under the head and the dead end and shear link on the crosshead; lip force about 685 N (+50 %); USD 35, 3.1 kg | Amish, as above | SKG-DDR-003, item 2 |
| 2026-10-03 | R1 (item 29B): toe blades cutting 40 mm past the ring's outer face; USD 10, 0.4 kg; friction measured in the first trial | Amish, as above | SKG-DDR-003, item 3 |
| 2026-10-04 | Scraper sleeve travel (R2, item 5A): a 340 mm sleeve with a 13 x 312 mm slot each side and a 12 mm cross pin through the pole running in the slots, in place of the stop collar; sleeve travel 300 mm, arms fold to 389 mm radius; USD 5, 0.9 kg (head with arms unpinned 20.1 kg) | Amish: "For round 3, I agree with all your proposed recommendations" | SKG-DDR-004 |
