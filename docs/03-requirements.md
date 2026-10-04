---
doc_id: SKG-REQ-001
title: SinkGrab requirements
project: SinkGrab
doc_type: Requirements
version: "0.5"
status: Draft
date: '2026-10-04'
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
- version: "0.4"
  date: '2026-10-03'
  author: Amish Chadha
  change: "Amish's decisions 27A, 28B and 29B of 2026-10-03 (\"i agree with all the 46 recommendations you provided. please proceed.\"), SKG-DDR-003: R4 restated for three people at the cranks during the hoist; status of R1, R3, R4, R5, R7, R9 and R11 from SKG-CAL-001 v0.2"
- version: "0.5"
  date: '2026-10-04'
  author: Amish Chadha
  change: "Amish's round-3 decision 5A of 2026-10-04 (\"For round 3, I agree with all your proposed recommendations\"), SKG-DDR-004: slotted sleeve and cross pin give the scraper's arms the 300 mm of sleeve travel they need to fold; status of R2, R9 and R11 from SKG-CAL-001 v0.3; no requirement restated"
---

# SinkGrab requirements

Eight of the eleven requirements are met on paper or by design, one can only be shown in a field trial, one is at risk and one is not met on paper by a small margin (SKG-CAL-001 v0.2, section M). Amish decided the three open requirements on 2026-10-03 ("i agree with all the 46 recommendations you provided. please proceed."; SKG-DDR-003): a third person at the cranks during the hoist (R4, restated below), a 3:1 closing tackle (R3) and toe blades that cut 40 mm past the ring's outer face (R1). The cycle time (R4) is now about 3.2 min at 10 m, 6 % over the target; the timed trial decides it. The depth gained (R1) still depends on how much the soil grips the sinking rings, which only the first trial can measure. On 2026-10-04 Amish decided the scraper sleeve's travel ("For round 3, I agree with all your proposed recommendations"; SKG-DDR-004): a 340 mm slotted sleeve on a 12 mm cross pin, so the arms fold to pass the ring and R2 is met by design as stated. "Met on paper" means shown by calculation, not by test.

> **Safety:** SinkGrab is lifting equipment worked over an open well shaft. R7 (proof load) and R8 (nobody in the well) are its safety requirements, and the overload limits behind R7 (a crank shear pin and a shear link, SKG-CAL-001, section C) are checked on paper only. Every lifting part must be proof-loaded before use (SKG-BLD-001, section 6).

Table 1. Requirements and status at TRL 3

| ID | Requirement | Target | Verification (TRL 3 or later) | Status (SKG-CAL-001) |
| --- | --- | --- | --- | --- |
| R1 | Deepen a flooded caisson well below the water table without de-watering | At least 3 m of standing water depth reached (target) | Field trial in a partner well, measured with the dip tape before and after | **At risk:** the 8-ring string sinks only while skin friction stays below about 1.7 kPa; estimated 1 to 3 kPa; the toes now cut 40 mm past the ring's outer face to keep it low (decision 29B); friction measured in the first trial |
| R2 | Fit common caisson ring sizes | Works inside rings of 0.8 to 1.3 m internal diameter | Fit check in rings of three sizes | Met by design: grab 468 mm across; scraper folds to 389 mm radius on 300 mm of sleeve travel (slotted sleeve and cross pin, SKG-DDR-004); toes, skids and a longer arm pair cover the range |
| R3 | Grab load per cycle | At least 20 L of saturated sand per bite (target) | Test pit trials with a measured tipping bin | Met on paper at the assumed fill: 21.2 L at 75 % fill, closed by a 3:1 tackle with 50 % more lip force (decision 28B); 14.1 L at 50 %; fill confirmed in the test-pit trial |
| R4 | Cycle time | 3 min or less per grab cycle at 10 m depth with three people at the cranks during the hoist and two otherwise (target; restated 2026-10-03, decision 27A) | Timed trial over 20 cycles | **Not met on paper by about 0.2 min:** 3.17 min with three at the hoist (3.8 min with two); the timed trial decides |
| R5 | Operator effort | Crank force 150 N or less per operator at rated grab load (target) | Spring balance on the crank handle during lifts | Met on paper: 54 N each with two people (108 N for one) |
| R6 | Keep the lining vertical while sinking | Tilt no worse than 1 in 80, the allowance used for sunk well foundations ([Construction Civil](https://www.constructioncivil.com/well-sinking-tilt-shift-in-well-foundation/)) | Four-point dip tape readings every cycle during trials | Not verifiable at TRL 3: readings resolve about 1 in 250; correction by scraping the high side and saddles |
| R7 | Proof load of lifting parts | Tripod, capstan, hooks and rigging proof-loaded to 2 times working load (target) | CalRig proof-load test with record | Met on paper: proof 193 kg, inside the HatchSide proof of 225 kg; line factor 10.4; shear link margin 1.15 |
| R8 | No person in the well during digging | 100% of digging and undercutting done from the surface | Trial log and method statement review | Met by design: every task from the surface; doors cover the shaft |
| R9 | Portability | Heaviest single piece 25 kg or less; kit fits in a small pickup (target) | Weigh each piece; load trial | Met on paper: heaviest piece 22.9 kg (capstan frame) with the scraper arms carried unpinned (scraper head 26.1 kg with them on, 20.1 kg without); kit about 457 kg, longest piece 2.0 m |
| R10 | Local build | Built with a stick welder, drill and hand tools from common steel section | Build by a partner workshop from the published drawings | Met by design; the shell skins need plate rolls, which most fabricators have |
| R11 | Prototype cost | At or under the USD 4,000 value-engineering target (a hypothetical control target) | Bill of materials and receipts | Met on paper, within the target: USD 2,566 (USD 1,434 under) |

## Requirements at risk or not met

Amish decided each of these on 2026-10-03 ("i agree with all the 46 recommendations you provided. please proceed."); the records are SKG-DDR-003 and SKG-DEC-001.

- **R4 (not met on paper by about 0.2 min).** Restated by decision 27A: the target is 3 min a cycle at 10 m with three people at the cranks during the hoist. Hand power still sets the hoist: 76 s of the 3.17 min cycle. The timed trial over 20 cycles decides.
- **R3 (met on paper at the assumed fill).** Decision 28B: a 3:1 tackle closes the lips 50 % harder (about 685 N). The fill is confirmed in the test-pit trial.
- **R1 (at risk).** Decision 29B: toe blades cut 40 mm past the ring's outer face to loosen the soil against it. Sinking still stops if skin friction exceeds about 1.7 kPa; the first trial measures it.

## Assumptions

- Crews already use precast caisson rings of a smaller diameter below the water table; the design case is a 1.0 m ring with a 75 mm wall inside a 1.3 m lining.
- Soils at the target sites can be taken by a clamshell grab; boulders and hard rock need a separate method.
- The HatchSide tripod keeps its 150 kg rating for material handling; SinkGrab's overload limits keep the line inside it.
- Three people are available to work the capstan for a full day (two between hoists, three during the hoist); a crew of four or five works the site.
