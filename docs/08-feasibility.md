---
doc_id: SKG-FEA-001
title: SinkGrab feasibility assessment
project: SinkGrab
doc_type: Feasibility assessment
version: "0.2"
status: Draft
date: '2026-10-25'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-24'
  author: Amish Chadha
  change: First feasibility assessment (kit 1.9.1 upgrade)
- version: "0.2"
  date: '2026-10-25'
  author: Amish Chadha
  change: "Amish's decisions of 2026-10-25 (SKG-DEC-001 O2, O4, O5) written in: bentonite annulus, crank slip clutch and load indicator, four people at the T-bar"
---

# SinkGrab feasibility assessment

**SinkGrab is feasible to build, and two parts of its method that did not work on paper as drawn now carry the fixes Amish chose on 2026-10-25, each still to be shown at TRL 4:** the caisson rings sinking 3 m without de-watering (STEM S21, PR-001), where the central unaided friction estimate stops them, now with a bentonite slurry in the overcut annulus (SKG-DEC-001 O2); and the overload device, where no shear pin fitted between the working pull and the tripod's rating (S6, S7, PR-007), now a friction slip clutch on the crank shaft with a load indicator at the dead end, whose 6 % window is shown on CalRig (O4). The mechanism and the lifting gear fit together in the detailed D3 model; the rest can only be settled in a test pit and a partner well. Method: STANDARDS section 23.

Table 1. Feasibility by aspect.

| Aspect | Assessment | Rating | Risks and notes | Evidence |
| --- | --- | --- | --- | --- |
| Design: grab | A one-line clamshell with a 3:1 tackle lifts 21 L a bite at an assumed 75 % fill, inside the tripod's rating | Medium | Closing margin over passive drag in loose sand is about 0.9 to 1.8 after the independent review (S2); fill in denser soil and the head-weight opening (S3) need a bite trial | SKG-STM-001 S1 to S5; SKG-CAL-001 A to C |
| Design: scraper | A pole scraper opened by weight, turned from the surface, folds to pass a 0.8 m ring | Medium | Turning effort of 142 N each for two people exceeded sustained limits (B4); four people now turn it, 71 to 84 N each, since a 2.0 m T-bar does not clear the tripod legs (O5, 2026-10-25); the pivot change of K6 keeps the fold inside the bore (387 mm) | SKG-STM-001 S17 to S20, B4; SKG-CAL-001 H |
| Design: sinking the rings | Self-weight and eight saddles against skin friction, with a 40 mm overcut lubricated by bentonite slurry (O2, 2026-10-25) | Low | Sinks only below 1.66 kPa of friction; the central unaided estimate (2 kPa) exceeds it and soil in full contact would give about 25 kPa; the lubricated friction is unknown until the test pit | SKG-STM-001 S21; SKG-CAL-001 I |
| Design: lifting and overload limits | Hand capstan with a 4:1 chain, weighted band brake, crank slip clutch and dead-end load indicator (O4, 2026-10-25) | Medium | Brake geometry corrected (K2); the clutch caps the capstan pull at 1,472 N and carries the steady full-grab pull with a 6 % margin on the third layer on a ±5 % setting, to show on CalRig; proof at 1.25 x the rated load, 188 kg | SKG-STM-001 S4 to S11, E2; SKG-CAL-001 C to G |
| Materials | Common S235 and S275 steel section and plate, bought bearings, sheaves, chain and polyester rope | High | Wear-resistant plate for lips and toes may need a stockholder in a city; lead-free paint on wetted parts | BOM; SKG-REG-001 G5, G15 |
| Manufacturing and assembly | Stick welding, drilling, plate rolling for the shells, profile cutting for the ratchet, pawl and end plates | Medium | Plate rolls and a profile cutter are not in every village workshop; 2 mm tube welding needs skill; 21 detail fixes are now in the model and drawings | SKG-BLD-001; SKG-DEC-001 K6 to K21; `cad/fidelity.json` |
| Power and controls | Human power only: two people at the cranks, three during the hoist, two at the T-bar | Medium | Hoist power sets the cycle (PR-004, about 0.2 min over); no engine, so no exhaust in the shaft | SKG-CAL-001 D, J; STEM S8, S9 |
| Supply of parts | Bearings, chain, sheaves, rope, shackles and detectors from general suppliers; HatchSide tripod shared | High | Gas detectors with carbon dioxide may need a city supplier (BOM line 35) | BOM; SKG-MKT-001 |
| Safety case | Nobody in the well; doors over the shaft; overload limits; air test with carbon dioxide; proof load | Medium | Depends on crews keeping the stop rules; the HatchSide tripod is rated for material handling only | SKG-RSK-001; SKG-BLD-001 section 6 |

Ratings: High, Medium, Low.
