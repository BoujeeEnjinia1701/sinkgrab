---
doc_id: SKG-DDR-002
title: SinkGrab design for construction
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
  change: Constructability review and changes that make the design buildable, decided under Amish's pre-approvals of 2026-10-03
---

# 0002: Design for construction

- **Date:** 2026-10-03
- **Status:** accepted

## Context

STANDARDS section 18 asks for every part to be makeable by its stated process and to fit and fasten to its neighbours (Amish, 2026-09-30: "fix the design assumptions to match and be physically feasible"). The TRL 2 concept (SKG-PRC-001 v0.2, SKG-DDR-001) was modelled part by part in `cad/src/model.py`: how each part is made, how it joins each neighbour, and build123d checks for overlapping parts, for parts that do not touch what holds them, and for the folded scraper passing the smallest ring. The checks now report no overlaps and no floating parts. Amish pre-approved every recommendation on 2026-10-03 ("start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost.") and extended it the same day to this batch ("Proceed with the remaining 15 scaffolds"). No change alters what SinkGrab does or its pitch; the safety-related changes all take the conservative side.

## Options considered

For each problem the simplest physically sound fix was chosen; alternatives are noted in Table 1.

## Decision

*Table 1. Changes made for construction.*

| # | Part | Problem found | Change | Why |
| --- | --- | --- | --- | --- |
| 1 | Capstan position | A 69 kg capstan cannot hang on the tripod's aluminium leg | Ground capstan 3.0 m from a lead sheave; drawbar of two 48.3 mm halves to a cradle under the leg A foot | Fleet angle 1.9 degrees; the pull closes inside the kit |
| 2 | Head sheave | The HatchSide sheave is grooved for 6 mm wire | A bought 150 mm sheave grooved for 8 mm fibre rope fits the same cheeks and axle | Groove fit; 16 rope diameters |
| 3 | Capstan frame | First model 32 kg in 40 x 40 x 2.6 tube with a solid anchor bar | 40 x 40 x 2 tube, 8 mm pads, anchor bar as tube: 22.9 kg | R9 |
| 4 | Drum | 8 mm solid flanges and webs | 6 mm flanges and brake web with lightening holes: 18.3 kg | R9 |
| 5 | Pawl | A pawl pivoted ahead of the nose ran its body through the tooth tips | Pivot 150 mm from the axis at 75 degrees, behind the nose; bracket hung from the front brace | Clears the teeth; holds the paying-out direction |
| 6 | Brake | Not detailed | Lined band 270 degrees round a 250 mm brake drum; anchor post, link, 650 mm lever with a 6 kg weight; anchor and link moved apart so they cannot touch | Brake on when let go; 314 N m |
| 7 | Stakes and guard | Stake heads clashed with the braces; guard tabs inside the guard wall | Stake tubes 200 mm either side of the axis; frame tabs reach the guard face | Fit |
| 8 | Grab mass | First model 72 kg, too close to the link release with a full bite | 4 mm skin, 6 mm end plates, 4 mm top cover, hollow 6 mm head box, 30 x 10 tie rods: 47.9 kg | Link margin 1.19 |
| 9 | Grab hinge | Both shells' end plates in one plane at the pin | Shell B's end plates outside shell A's; each shell's tie rods outside its own end plates; short pins at the lugs | Interleaved hinge, no clash |
| 10 | Shear link | Not detailed | Two 6 mm plates on a 16 mm pin through the dead-end lug; calibrated pin of about 1.9 mm below | R7; opens the grab if it snags |
| 11 | Scraper arms | Arms fixed open would not pass the bore | Arms pinned to the hub, opened by struts from a sliding sleeve and foot; a 300 mm lift folds the toes to 364 mm radius | R2 |
| 12 | Scraper pole | Pole sections were not defined | 42.4 x 2.6 tube in 2.0 m sections with 36 mm spigots and M12 cross bolts; T-bar socket and eye | R9 (fits a small pickup) |
| 13 | Spoil and cover | A chute over the mouth could not also cover the shaft | Well-head frame in two halves on the collar with two mesh doors, a 64 mm pole hole and four datum brackets | Covers the shaft; pole guide; tilt datum |
| 14 | Ballast | A frame on the top ring needed placing by hand | Eight 20.6 kg U-saddles straddling the ring wall, each on a 6 mm line | Placed from the surface |
| 15 | Clearances | Pins in 1 mm oversize holes left parts unconnected in the checks | Holes 0.25 to 0.5 mm over the pin | Each part rests on what holds it |

## Consequences

- `cad/src/model.py` holds the constructable design; STEP and STL, SKG-DWG-001 and 002 (Rev P2), the concept media and the build plan pictures are generated from it.
- SKG-CAL-001 is run on it; the parts cost is USD 2,506, USD 1,494 under the value-engineering target.
- `design_state: constructable` is set in `project.yaml`.
