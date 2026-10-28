---
doc_id: SKG-PRS-001
title: SinkGrab product requirements and specifications
project: SinkGrab
doc_type: Product requirements and specifications
version: "0.8"
status: Draft
date: '2026-10-25'
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
- version: "0.6"
  date: '2026-10-24'
  author: Amish Chadha
  change: "Kit 1.9.1 upgrade: SKG-REQ-001 becomes SKG-PRS-001 (STANDARDS section 22); R1 to R11 are PR-001 to PR-011 with the same text, traced to SKG-URS-001; tolerance and units added; status from SKG-CAL-001 v0.4 on the detailed model; PR-012 (air test with carbon dioxide) and PR-013 (soils) added, proposed, awaiting Amish"
- version: "0.7"
  date: '2026-10-25'
  author: Amish Chadha
  change: "Independent review of the STEM check: PR-001 not met on paper (O2); PR-003 and PR-007 at risk (O4)"
- version: "0.8"
  date: '2026-10-25'
  author: Amish Chadha
  change: "Amish's decisions of 2026-10-25 (\"i approve of your recommendations\", SKG-DEC-001): PR-007 restated for the crank slip clutch, proof at 1.25 x the rated load (O4); PR-001 at risk with the bentonite annulus (O2); PR-012 and PR-013 accepted as written (O3); cost USD 3,063"
supersedes: SKG-REQ-001
---

# SinkGrab product requirements and specifications

What SinkGrab must do, each requirement traced to a user need in SKG-URS-001 (links in SKG-RTM-001). Until kit 1.8 this document was SKG-REQ-001, and R1 to R11 are now PR-001 to PR-011 with the same text; the "Was" column gives the old number, which the calculation note, build plan and earlier records still cite. Status comes from SKG-CAL-001 v0.6, which since 2026-10-24 reads its masses from the detailed kit 1.9 model (every pin, clip, collar and bolt counted), and from the STEM check SKG-STM-001. Of the eleven requirements Amish set, three are met on paper, three are met by design, one can only be shown in a field trial, three are at risk and one is not met on paper (PR-001 is not met unaided and at risk with the bentonite annulus Amish chose on 2026-10-25). The detailed model changed no status; the independent review of the STEM check on 2026-10-25 changed three: PR-001 is not met on paper, and PR-003 and PR-007 are at risk. The cycle time (PR-004) is 3.19 min at 10 m, about 0.2 min over its 3 min target, and the timed trial decides it; the depth gained (PR-001) depends on how much the soil grips the sinking rings, and on paper the central friction estimate already stops the rings, so Amish chose on 2026-10-25 to make a bentonite-lubricated annulus part of the method (SKG-DEC-001 O2), and PR-001 is at risk until the test pit shows the friction; the shear devices behind PR-007 had no release window, so the same day Amish chose a friction slip clutch on the crank shaft with a load indicator at the dead end and a proof at 1.25 times the rated load (O4), and PR-007 is restated and at risk until CalRig shows the clutch window. PR-012 (UR-012, safe air, a test that reads carbon dioxide) and PR-013 (UR-011, soils) were accepted as written on 2026-10-25 (O3). Targets remain proposals for review with a co-design partner. "Met on paper" means shown by calculation, not by test.

> **Safety:** SinkGrab is lifting equipment worked over an open well shaft. PR-007 (proof load), PR-008 (nobody in the well) and PR-012 (air test) are its safety requirements, and the overload limit behind PR-007 (a friction slip clutch on the crank shaft, with a load indicator at the dead end, SKG-CAL-001, section C) is checked on paper only. Every lifting part must be proof-loaded before use (SKG-BLD-001, section 6).

*Table 1. Product requirements and specifications.*

| ID | Traces to | Category | Title | Requirement | Target | Tolerance | Units | Verification | Status | Was |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PR-001 | UR-001 | Performance | Depth below the water table | The kit shall deepen a flooded caisson well below the water table without de-watering | At least 3 m of standing water depth reached | min | m | Field trial in a partner well, dip tape before and after (TRL 5) | The 8-ring string sinks only while skin friction stays below 1.66 kPa; the central estimate for disturbed sand (2 kPa) exceeds it and soil in full contact gives about 25 kPa (STEM S21). Unaided this is **not met on paper**; with the bentonite slurry in the overcut annulus that Amish chose on 2026-10-25 (SKG-DEC-001 O2) it is **at risk** until the test pit shows the lubricated friction below the limit | R1 |
| PR-002 | UR-004 | Physical architecture | Ring sizes | The grab and scraper shall work inside caisson rings of 0.8 to 1.3 m inside diameter | 0.8 to 1.3 | range | m | Fit check in rings of three sizes (TRL 4) | Met by design: grab 468 mm across; scraper folds to 387 mm radius on 300 mm of sleeve travel (arm pivots at 60 mm, SKG-DEC-001 K6); toes, skids and a longer arm pair cover the range | R2 |
| PR-003 | UR-005 | Performance | Bite | The grab shall lift at least 20 L of saturated sand per bite | 20 | min | L | Test-pit trial with a measured tub (TRL 4) | **At risk:** 21.2 L at 75 % fill, 3:1 tackle; 14.1 L at 50 %; closing margin over passive drag between about 0.9 and 1.8 once the empty grab and sheave friction are counted (STEM S2) | R3 |
| PR-004 | UR-005, UR-006 | Performance | Cycle time | One grab cycle at 10 m depth shall take 3 min or less with three people at the cranks during the hoist and two otherwise (restated 2026-10-03, decision 27A) | 3 | max | min | Timed trial over 20 cycles (TRL 4) | **Not met on paper by about 0.2 min:** 3.19 min with three at the hoist (3.8 min with two); the timed trial decides | R4 |
| PR-005 | UR-006 | Usability | Crank force | Crank force per operator at the rated grab load shall be 150 N or less | 150 | max | N | Spring balance on the crank handle (TRL 4) | Met on paper: 55 N each with two people (110 N for one) | R5 |
| PR-006 | UR-003 | Performance | Tilt | The lining shall be kept within a tilt of 1 in 80 while sinking | 1 in 80 | max | slope | Four-point dip tape readings every cycle in trials (TRL 5) | To verify at TRL 4 and 5: readings resolve about 1 in 250; correction by scraping the high side and saddles | R6 |
| PR-007 | UR-007 | Safety | Proof load | Tripod, capstan, hooks and rigging shall be proof-loaded to 1.25 times the rated load of the line, the highest pull the crank slip clutch passes (150 kg), and the clutch shall be set and checked to slip at or below that pull before each campaign (restated 2026-10-25, decision O4) | 1.25 | min | x rated load | CalRig proof-load test with record, clutch slip test on each rope layer, load indicator calibration (TRL 4) | **At risk:** proof 188 kg, inside the HatchSide proof of 225 kg; the clutch slips at 1,127 to 1,472 N against a steady full-grab pull of 1,068 N (margin 1.06 on the third layer) on a ±5 % setting that only CalRig can show (STEM S4, S6, S7, E2; SKG-CAL-001 C, G4) | R7 |
| PR-008 | UR-002, UR-013 | Safety | Nobody in the well | All digging and undercutting shall be done from the surface | 100 | min | % of tasks | Trial log and method statement review (TRL 4) | Met by design: every task from the surface; doors cover the shaft | R8 |
| PR-009 | UR-008 | Packaging and transport | Portability | The heaviest single piece shall be 25 kg or less and the kit shall fit a small pickup | 25 | max | kg | Weigh each piece; load trial (TRL 4) | Met on paper: heaviest piece 22.4 kg (capstan frame) with the scraper arms carried unpinned (scraper head 27.3 kg with them on, 21.9 kg without); kit about 467 kg, longest piece 2.0 m; the assembled grab (52.7 kg) is moved only on the line (SKG-DEC-001 K3) | R9 |
| PR-010 | UR-009 | Materials | Local build | The kit shall be built with a stick welder, drill and hand tools from common steel section | Stick welder and hand tools | pass or fail | n/a | Build by a partner workshop from the published drawings (TRL 4) | Met by design; the shell skins need plate rolls, which most fabricators have | R10 |
| PR-011 | UR-010 | Cost | Prototype cost | Parts cost at or under the USD 4,000 value-engineering target (a hypothetical control target) | 4,000 | max | USD | Bill of materials (analysis, TRL 3); receipts (TRL 4) | Met on paper, within the target: USD 3,063 (USD 937 under) | R11 |
| PR-012 | UR-012 | Safety | Air test | The kit shall include a four-gas detector and a carbon dioxide monitor, and the method shall test the shaft air before work, after every break and whenever anyone leans over the shaft | Oxygen, carbon monoxide, hydrogen sulphide, flammable gas and carbon dioxide read | pass or fail | n/a | BOM and method review (inspection, TRL 3); bump test before use (TRL 4) | Met by design: BOM lines 31 and 35, build plan safety stop 1 (accepted by Amish on 2026-10-25, SKG-DEC-001 O3) | |
| PR-013 | UR-011 | Performance | Soils | The grab and scraper shall dig loose to medium silt, fine sand, laterite and clayey sand under water; boulders and rock are out of scope | Bite and undercut in each soil | pass or fail | n/a | Test-pit trials in each soil (TRL 4) | To verify at TRL 4: closing force on paper in loose sand only (STEM S2); accepted by Amish on 2026-10-25 (SKG-DEC-001 O3) | |

Categories: physical architecture, performance, materials, usability, packaging and transport, safety, electrical, software. Status: met on paper, met by design, at risk, not met, over target, withdrawn, to verify at TRL 4.

## Requirements at risk or not met

Amish decided PR-004, PR-003 and PR-001 on 2026-10-03 ("i agree with all the 46 recommendations you provided. please proceed.") and PR-001 and PR-007 again on 2026-10-25 ("i approve of your recommendations"); the records are SKG-DDR-003, SKG-DDR-006 and SKG-DEC-001. The kit 1.9.1 upgrade changed no status.

- **PR-004 (R4, not met on paper by about 0.2 min).** Restated by decision 27A: the target is 3 min a cycle at 10 m with three people at the cranks during the hoist. Hand power still sets the hoist: 78 s of the 3.19 min cycle. The timed trial over 20 cycles decides.
- **PR-003 (R3, at risk).** Decision 28B: a 3:1 tackle closes the lips 50 % harder (about 700 N). The fill is confirmed in the test-pit trial; the STEM check keeps the closing force open until then (S2).
- **PR-001 (R1, not met on paper).** Decision 29B: toe blades cut 40 mm past the ring's outer face to loosen the soil against it. Sinking still stops if skin friction exceeds about 1.7 kPa; the first trial measures it. The STEM check (S21) shows why this is the largest uncertainty. Decision O2 (2026-10-25): bentonite slurry is fed down a pipe into the overcut annulus from the first trial and tested in the test pit first.
- **PR-007 (R7, at risk).** Decision O4 (2026-10-25): a friction slip clutch on the crank shaft caps the capstan pull at the tripod's 150 kg rating and a load indicator at the dead end shows the peak of each lift, in place of the crank shear pin and shear link; proof at 1.25 times the rated load, 188 kg. The window between the steady pull and the lowest slip is 6 % on the third rope layer, so the setting is shown on CalRig.

## Assumptions

- Crews already use precast caisson rings of a smaller diameter below the water table; the design case is a 1.0 m ring with a 75 mm wall inside a 1.3 m lining.
- Soils at the target sites can be taken by a clamshell grab; boulders and hard rock need a separate method.
- The HatchSide tripod keeps its 150 kg rating for material handling; SinkGrab's overload limits keep the line inside it.
- Three people are available to work the capstan for a full day (two between hoists, three during the hoist); a crew of four or five works the site.
