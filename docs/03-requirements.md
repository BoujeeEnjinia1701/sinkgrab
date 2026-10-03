---
doc_id: SKG-REQ-001
title: SinkGrab requirements
project: SinkGrab
doc_type: Requirements
version: "0.3"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-30'
  author: Amish Chadha
  change: Initial scaffold
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: TRL 2 requirements with concept status (SKG-DDR-001); R11 restated against the value-engineering target
- version: "0.3"
  date: '2026-10-03'
  author: Amish Chadha
  change: TRL 3 status from SKG-CAL-001 on the constructable design (SKG-DDR-002); R1 and R3 at risk and R4 not met, each posed to Amish as a decision in SKG-DEC-001
---

# SinkGrab requirements

Seven of the eleven requirements are met on paper or by design, one can only be shown in a field trial, two are at risk and one is not met (SKG-CAL-001, section M). The cycle time (R4) is the miss: about 3.7 min a bite at 10 m, because two people at a crank give about 100 W and hoisting the full grab takes half the cycle. The bite (R3) depends on how full the grab comes up, and the depth gained (R1) depends on how much the soil grips the sinking rings; both can only be settled in trials. Each of these three is posed to Amish as a decision, with options and a recommendation, in the design decisions register (SKG-DEC-001) and `docs/REVIEW.md`. "Met on paper" means shown by calculation, not by test.

> **Safety:** SinkGrab is lifting equipment worked over an open well shaft. R7 (proof load) and R8 (nobody in the well) are its safety requirements, and the overload limits behind R7 (a crank shear pin and a shear link, SKG-CAL-001, section C) are checked on paper only. Every lifting part must be proof-loaded before use (SKG-BLD-001, section 6).

Table 1. Requirements and status at TRL 3

| ID | Requirement | Target | Verification (TRL 3 or later) | Status (SKG-CAL-001) |
| --- | --- | --- | --- | --- |
| R1 | Deepen a flooded caisson well below the water table without de-watering | At least 3 m of standing water depth reached (target) | Field trial in a partner well, measured with the dip tape before and after | **At risk:** the 8-ring string sinks only while skin friction stays below about 1.7 kPa; estimated 1 to 3 kPa |
| R2 | Fit common caisson ring sizes | Works inside rings of 0.8 to 1.3 m internal diameter | Fit check in rings of three sizes | Met by design: grab 468 mm across; scraper folds to 364 mm radius; toes, skids and a longer arm pair cover the range |
| R3 | Grab load per cycle | At least 20 L of saturated sand per bite (target) | Test pit trials with a measured tipping bin | **At risk:** 21.2 L at an assumed 75 % fill; 14.1 L at 50 % |
| R4 | Cycle time | 3 min or less per grab cycle at 10 m depth with two operators (target) | Timed trial over 20 cycles | **Not met on paper:** about 3.7 min |
| R5 | Operator effort | Crank force 150 N or less per operator at rated grab load (target) | Spring balance on the crank handle during lifts | Met on paper: 52 N each with two people (104 N for one) |
| R6 | Keep the lining vertical while sinking | Tilt no worse than 1 in 80, the allowance used for sunk well foundations ([Construction Civil](https://www.constructioncivil.com/well-sinking-tilt-shift-in-well-foundation/)) | Four-point dip tape readings every cycle during trials | Not verifiable at TRL 3: readings resolve about 1 in 250; correction by scraping the high side and saddles |
| R7 | Proof load of lifting parts | Tripod, capstan, hooks and rigging proof-loaded to 2 times working load (target) | CalRig proof-load test with record | Met on paper: proof 187 kg, inside the HatchSide proof of 225 kg; line factor 10.7 |
| R8 | No person in the well during digging | 100% of digging and undercutting done from the surface | Trial log and method statement review | Met by design: every task from the surface; doors cover the shaft |
| R9 | Portability | Heaviest single piece 25 kg or less; kit fits in a small pickup (target) | Weigh each piece; load trial | Met on paper: heaviest piece 24.6 kg (scraper head); kit about 452 kg, longest piece 2.0 m |
| R10 | Local build | Built with a stick welder, drill and hand tools from common steel section | Build by a partner workshop from the published drawings | Met by design; the shell skins need plate rolls, which most fabricators have |
| R11 | Prototype cost | At or under the USD 4,000 value-engineering target (a hypothetical control target) | Bill of materials and receipts | Met on paper, within the target: USD 2,506 (USD 1,494 under) |

## Requirements at risk or not met

These are stated here and decided by Amish; the options and recommendations are in SKG-DEC-001.

- **R4 (not met on paper).** Hand power sets the hoist: 111 s of the 3.7 min cycle at 10 m.
- **R3 (at risk).** The lips close with about 0.7 of the line pull, which is capped by the grab's submerged weight, so the fill in denser sand is uncertain.
- **R1 (at risk).** Sinking stops if skin friction on the rings exceeds about 1.7 kPa; the undercut and saddles add little against higher friction.

## Assumptions

- Crews already use precast caisson rings of a smaller diameter below the water table; the design case is a 1.0 m ring with a 75 mm wall inside a 1.3 m lining.
- Soils at the target sites can be taken by a clamshell grab; boulders and hard rock need a separate method.
- The HatchSide tripod keeps its 150 kg rating for material handling; SinkGrab's overload limits keep the line inside it.
- Two or three people are available to work the capstan for a full day; a crew of four or five works the site.
