---
doc_id: SKG-DEC-001
title: SinkGrab design decisions register
project: SinkGrab
doc_type: Design decisions register
version: "0.6"
status: Draft
date: '2026-10-25'
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
- version: "0.4"
  date: '2026-10-24'
  author: Amish Chadha
  change: "Kit 1.9.1 upgrade: open decisions O1 to O3 (concept selection, ring-sinking contingency, new requirements) proposed, awaiting Amish; K1 to K5 decided under Amish's standing instruction of 2026-10-23 (STEM check fix rule); K6 to K21 design for construction found by the detailed D3 model; value engineering at USD 2,986"
- version: "0.5"
  date: '2026-10-25'
  author: Amish Chadha
  change: "Independent review of the STEM check: O2 restated (PR-001 not met on paper); O4 (overload window and proof basis) and O5 (scraper turning force) posed, awaiting Amish; K22 (gas readings taken at depth) decided under the standing instruction"
- version: "0.6"
  date: '2026-10-25'
  author: Amish Chadha
  change: "Amish's decisions of 2026-10-25 (\"i approve of your recommendations\"): O2 (bentonite annulus), O3 (PR-012 and PR-013), O4 (crank slip clutch and load indicator, proof at 1.25 x the rated load) and O5 (four people at the T-bar, after the 2.0 m T-bar failed the leg check) moved to Decisions made (SKG-DDR-006); O1 stays open without a pick; cost USD 3,063"
---

# SinkGrab design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/` or in `docs/REVIEW.md`; this register is the index Amish works from. The build plan (`docs/05-build-plan.md`) describes the design as it stands and does not list decisions.

> **Safety:** Several decisions below set SinkGrab's safety case (overload limits, lowering on a brake that is on when let go, the doors over the shaft, no entry). Each took the conservative option; the evidence that would relax it is in SKG-DDR-001, Table 1. None of the requirement decisions of 2026-10-03 and 2026-10-04 changes the safety case. The kit 1.9.1 fixes of 2026-10-24 strengthen it: the brake sets when let go (K2), nobody lifts the grab or a full tub by hand (K3, K4) and the air test reads carbon dioxide (K5). Amish's decision O4 of 2026-10-25 replaces the shear link and crank shear pin with a friction slip clutch that caps the capstan pull at the tripod's 150 kg rating and a load indicator that shows the peak of every lift; a snag now stops the hoist with the pawl holding instead of opening the grab.

## Open decisions

Proposed, awaiting Amish. Each is posed as a state, options and a recommendation (Amish, 2026-10-03: "A simple statement doesn't add value - ensure you are identifying a state and posing it as a clear recommendation for me to decide on").

| # | What is to be decided | Options | Recommendation | What it affects in the build | Source record |
| --- | --- | --- | --- | --- | --- |
| O1 | Concept: kit 1.8 asks for at least two options; option A (rope grab and under-curb scraper, the current design) scores 167 and option B (dart-valve bailer on a jerk line) 153, 8.4 % apart | A: keep the current design, optionally with a bailer accessory for clean running sand. B: move to the bailer, for sand and gravel wells only | None: within 10 %, so both go to Amish without a pick (STANDARDS section 21). A is the only option that undercuts, steers the lining and digs cohesive soils; B is simpler, about USD 330 cheaper and about 40 kg lighter as modelled | A: nothing changes. B: new drawings, BOM and build plan; PR-001, PR-003, PR-006 and PR-013 restated | SKG-OPT-001; SKG-DDR-005 |

O2 to O5 were decided by Amish on 2026-10-25 and are under Decisions made. O1 had no recommendation (the options are within 10 %), so it stays open.

## To confirm when parts are bought

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | Friction of the clutch facings bought on the ground driven discs, dry and after standing damp, and the slip torque on CalRig on each rope layer | The clutch must slip between 1,127 N (third layer) and 1,472 N (first layer) at the capstan; sized on a friction of 0.35 and a ±5 % setting | SKG-CAL-001, C; SKG-DEC-001 O4 |
| 2 | Load and deflection of the disc springs bought: the clutch's 50 x 25.4 x 2.0 pair and the load indicator's 18 x 9.2 x 1.0 stack, and the indicator's rings set on CalRig | Clamp about 1.5 kN; indicator travel about 2.8 mm at 1.47 kN on catalogue values | SKG-CAL-001, C1, C7 |
| 3 | Breaking strength and splice of the 8 mm rope bought | Factors assume 12 kN and 90 % at the splice | SKG-CAL-001, E |
| 4 | Sheave groove, bore and width fit the HatchSide cheeks and 20 mm axle, and the grab head's cheeks 30 mm apart | The head sheave is swapped while SinkGrab works; the upper sheave of the 3:1 tackle uses the same sheave | SKG-DDR-002, item 2; SKG-DDR-003 |
| 5 | HatchSide foot plate size and thickness on the tripod as built | The cradle rim and clamp bars are sized on 140 x 280 mm | SKG-DWG-107 |
| 6 | Brake lining friction on the steel drum | Holding torque assumes 0.35 | SKG-CAL-001, F |
| 7 | Bearing centre heights and bolt pitches | Pads and top plates are drilled to UCP206 and UCP205 catalogue sizes | SKG-DWG-101 |
| 8 | Ring size and wall thickness at the trial well | Toe position, skid holes and saddle slot are set for a 1.0 m ring with a 75 mm wall | SKG-DWG-112, 113, 117 |
| 9 | The sleeve slides the full 300 mm of its slots on the cross pin, and the arms fold to inside an 800 mm circle (387 mm radius on paper) | The head must pass a 0.8 m ring when lifted | SKG-DDR-004; SKG-DEC-001 K6; SKG-DWG-113 |
| 10 | The load indicator's rod slides freely in the housing plate and the O-ring tell-tale holds its place on the rod in muddy water | The indicator must show the peak of each lift | SKG-DEC-001 O4; SKG-DWG-111 |
| 11 | Bore and set screw of the two 30 mm set collars on the hinge pin | They hold the crosshead central | SKG-DEC-001 K8 |
| 12 | The carbon dioxide monitor's range (0 to 5 %), alarm points and calibration certificate | The air test relies on it (PR-012) | SKG-DEC-001 K5; BOM line 35 |
| 13 | Brake lever ratio as built: about 10.3:1 from the pivot to the link line | Holding torque assumes 10.2:1 | SKG-DEC-001 K2; SKG-CAL-001 F |

## Value engineering

Value-engineering target: USD 4,000 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 3,063 (USD 937 under the target). The kit 1.9.1 fixes add USD 420, nearly all of it the carbon dioxide monitor; Amish's decision O4 of 2026-10-25 adds USD 77 (slip clutch, load indicator, crank shaft and guard, all estimates). Main cost drivers and savings worth trying:

- The two gas instruments (four-gas detector USD 550 and carbon dioxide monitor USD 399) are the largest lines; a crew or partner that already owns a pumped detector, or a five-gas detector that reads carbon dioxide, saves one of them.
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
| 2026-10-24 | **K1** Shear link: a hardened 16 mm sleeve carries the rope thimble and fills the 12 mm gap between the link plates, with hardened bushes in both plates, so the calibrated pin works in true double shear; pins break-tested in a spare link. As drawn in kit 1.7 the thimble hung on the bare pin across the gap, where it bends and gives way near 0.15 kN (STEM S5). About USD 3 | Decided under Amish's standing instruction of 2026-10-23 ("when a STEM check row fails, propose and implement the best fix for the design and its constructability"); Amish can reverse it | SKG-STM-001 S5 |
| 2026-10-24 | **K2** Band brake: the lever pivot is lowered to 67 mm on a plate outside the +X rail, and the band's link runs on the tangent to a pin on an upright arm 60 mm above the pivot, so the falling weight tightens the band; the kit 1.7 model had the link pin 25 mm below the pivot on the well side, which slackened it (STEM S11). Ratio about 10.3:1 | As for K1 | SKG-STM-001 S11 |
| 2026-10-24 | **K3** The assembled grab (52.5 kg) is never lifted by hand: it is assembled on the line under the tripod and moved only by the capstan, and travels in pieces of 25 kg or less (STEM B1). No cost | As for K1 | SKG-STM-001 B1; SKG-BLD-001 steps 13, 20 |
| 2026-10-24 | **K4** A full spoil tub (about 50 kg) is never lifted: two people slide it off the closed doors on a board and tip it at the heap (STEM B2). No cost | As for K1 | SKG-STM-001 B2; SKG-BLD-001 section 6 |
| 2026-10-24 | **K5** A portable 0 to 5 % carbon dioxide safety monitor (BOM line 35, USD 399) is used beside the four-gas detector, which does not read carbon dioxide (STEM C2) | As for K1 | SKG-STM-001 C2; PR-012 |
| 2026-10-24 | **K6** Scraper arm pivots 60 mm from the pole axis (45 mm before), so each arm has a closed 18 mm radius eye round its 16 mm pin clear of the 70 mm hub; toe radius and sleeve travel unchanged; fold 387 mm (389 before); lugs 15 mm longer | Design for construction: Amish, 2026-09-30, "fix the design assumptions to match and be physically feasible" (STANDARDS section 18) | SKG-STM-001 S20; SKG-DWG-112, 113 |
| 2026-10-24 | **K7** Grab head box set 19 mm below the head pin axis (15 mm before), so the 25 mm pins pass inside the 6 mm plates; cheeks welded to the box underside | As for K6 | SKG-DWG-110 |
| 2026-10-24 | **K8** Two 30 mm set collars on the hinge pin hold the crosshead central (it could slide 145 mm each way); 0.6 kg, USD 8 | As for K6 | SKG-DWG-111 |
| 2026-10-24 | **K9** Tie rods and struts end in closed eyes 25 and 15 mm beyond their hole centres (the kit 1.7 model ended them at the hole centres) | As for K6 | SKG-DWG-111, 113 |
| 2026-10-24 | **K10** Drum bearing bolts pushed up through the pads and tacked before the pads are welded on; the heads sit inside the pad posts, which leave no room for nuts | As for K6 | SKG-DWG-101; SKG-BLD-001 3.1 |
| 2026-10-24 | **K11** Crank handles turn on 20 mm stub axles welded to the arms, with a washer and split pin, so nothing on a crank's inner face can strike the chain guard as it turns; USD 2 | As for K6 | SKG-DWG-103 |
| 2026-10-24 | **K12** Foot cradle: clamp bars on top of the HatchSide foot plate (the kit 1.7 model had them inside it), held by four welded M12 studs and nuts; rim flats 18 mm high, flush with the foot plate | As for K6 | SKG-DWG-107 |
| 2026-10-24 | **K13** Brake anchor: a 16 mm eye welded across the band end, pinned with a 10 mm pin between two 6 mm posts on the anchor bar, in place of one post | As for K6 | SKG-DWG-105 |
| 2026-10-24 | **K14** Ballast plates bolted with two M10 bolts through spacer tubes at 40 mm either side of the centre (75 mm before), clear of the line rising from the guide tube | As for K6 | SKG-DWG-110 |
| 2026-10-24 | **K15** Toe blades butt-welded to the outer face of the toe plates (a lap through the plate is not possible); cutting radius unchanged at 615 mm | As for K6 | SKG-DWG-113 |
| 2026-10-24 | **K16** Chain guard held by two M6 screws into clip angles on the -X post, with nuts welded inside the guard | As for K6 | SKG-DWG-104 |
| 2026-10-24 | **K17** Pawl pin pressed into a reamed hole in the bracket, with a washer and split pin at its free end | As for K6 | SKG-DWG-105 |
| 2026-10-24 | **K18** Brake lever pivot plate on the outside face of the +X rail, clear of the rear brace | As for K6 | SKG-DWG-101 |
| 2026-10-24 | **K19** Drawbar tubes start 6 mm clear of the clevis plates, so the tongue welds can be made | As for K6 | SKG-DWG-108 |
| 2026-10-24 | **K20** Doors modelled as an angle frame with mesh on the horizontal legs (the kit 1.7 model was a solid 4 mm tray); well-head frame halves joined by corner cleats and four M12 bolts; USD 4 | As for K6 | SKG-DWG-115, 116 |
| 2026-10-24 | **K21** Rope clamp on the drum: a tapped 10 mm boss welded to the -X flange, a 6 mm strap and two M8 bolts, in place of a U-bolt whose nuts would sit in the rope's winding space | As for K6 | SKG-DWG-102 |
| 2026-10-25 | **K22** Gas readings at depth: the four-gas detector and the carbon dioxide monitor are lowered on a cord in a mesh bag and read at 2 m below the collar, at mid depth and 1 m above the water, each held for at least the instrument's stated response time; a reading over range counts as a fail. The independent review found that an instrument held at the collar reads only collar air, while heavy gas pools at depth (STEM C2) | Amish's standing instruction of 2026-10-23 (STEM check fix rule) | SKG-STM-001 C2; SKG-BLD-001 first checks |
| 2026-10-25 | **O2** Ring sinking: a bentonite slurry, mixed in a drum at the well head and pumped down a feed pipe into the 40 mm overcut annulus, is part of the sinking method from the first trial and is tried in the test pit first; about 0.45 m3 over 3 m of sinking; trial kit, not BOM. PR-001 stays not met unaided and is at risk with the annulus | Amish, 2026-10-25 12:43 CT: "i approve of your recommendations" | SKG-DDR-006, item 1; SKG-CAL-001 I6 |
| 2026-10-25 | **O3** PR-012 (air test that reads carbon dioxide) and PR-013 (soils) accepted as written | Amish, as above | SKG-DDR-006, item 2; SKG-PRS-001 |
| 2026-10-25 | **O4** Overload device and proof basis: a friction slip clutch on the crank shaft (two 84 mm driven discs on the sprocket sleeve, woven facings on a welded flange and a keyed pressure plate, two disc springs and a KM5 locknut; set on CalRig to slip at about 34 N m, capstan pull 1,127 to 1,472 N) and a peak-reading load indicator at the tackle's dead end replace the crank shear pin and the shear link; PR-007 restated: proof at 1.25 x the rated load (150 kg), 188 kg; USD 77 (estimates); grab 52.7 kg. Option B of O4 (uprated tripod) stays available if the trials show more bite is worth it | Amish, as above | SKG-DDR-006, item 3; SKG-CAL-001 C, G4; BOM lines 4, 5, 14, 24 |
| 2026-10-25 | **O5** Scraper crew: a 2.0 m T-bar was recommended if the well-head layout allows it, else four people. Its ends clear the HatchSide legs only below 801 mm above ground (doors at 390 mm, 2 m of travel per pole section), so four people turn the 1.4 m T-bar, two on each side: 71 to 84 N each; no hardware change | Amish, as above | SKG-DDR-006, item 4; SKG-CAL-001 H9, H10 |
