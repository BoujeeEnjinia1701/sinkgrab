---
doc_id: SKG-CAL-001
title: SinkGrab sizing calculations
project: SinkGrab
doc_type: Calculation
version: "0.2"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: First issue for TRL 3 on the constructable design (SKG-DDR-002); grab capacity and closing force, overload limits, crank force and speed, drum and rope, brake, tripod and drawbar, scraper, sinking and tilt, cycle time, masses and cost
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: 'Re-run with Amish''s round 2 decisions (SKG-DDR-003): three people hoist on a 240 mm two-hand handle, 3:1 closing tackle, toes 40 mm past the ring, fold lift 320 mm'
---

# SinkGrab sizing calculations

On paper SinkGrab does what it was drawn for, inside the HatchSide tripod's rating, but not quite in the 3 min its cycle-time requirement asks for. This issue carries Amish's round 2 decisions (SKG-DDR-003): three people at the cranks for the hoist, a 3:1 closing tackle and toes that cut 40 mm past the ring. The grab lifts 21 L of saturated sand a bite at an assumed 75 % fill and now closes its lips with about 687 N; three people hoist the full 97 kg grab at 8.7 m/min; a shear link and a crank shear pin keep the line below the tripod's 150 kg rating and 225 kg proof load whatever the crew does. The parts cost USD 2,561 against a value-engineering target of USD 4,000. R4 is still missed: a cycle at 10 m takes about 3.16 min, 5 % over. R9 is now missed by 0.1 kg, because the longer arms bring the scraper head to 25.1 kg. Two requirements are at risk: R3, because the fill in denser sand is uncertain, and R1, because the rings keep sinking to 3 m only while skin friction stays below about 1.7 kPa. Six are met on paper or by design and R6 can only be shown in a trial. Every number here is printed by `docs/04-calcs/sizing.py`; the tag in brackets, for example [C2], is the line of that script's output that carries it.

> **Safety:** SinkGrab is lifting equipment over an open well shaft. These are first-principles estimates for a paper proof of concept; they do not show that any part is safe. Every lifting part must be proof-loaded before use (SKG-BLD-001, section 6), nobody stands under the grab or beside a loaded line, and nobody enters the well. See SKG-PRC-001, Safety.

## Scope and method

The note checks every requirement in SKG-REQ-001 v0.3 against the design in SKG-PRC-001 v0.3 and the parametric model `cad/src/model.py`. The script imports the model's `PARAMS`, `derived()` and `masses()`, so the grab, drum, scraper and frame used here are the ones in the STEP files and drawings SKG-DWG-001 and 002. It also reads `bom/bom.csv` and `budget_usd` in `project.yaml`, and writes `docs/04-calcs/results.csv`.

The design case is a 1.0 m caisson ring with a 75 mm wall inside a 1.3 m lining, the digging face 10 m below ground (R4) and 3 m of water standing over it at the end of the work (R1). The HatchSide tripod stands over the well with SinkGrab's line in place of its winch.

## Assumptions

*Table 1. Main assumptions.*

| Area | Assumption | Basis |
| --- | --- | --- |
| Sand | Saturated fine to medium sand 2.0 kg/L (1.0 kg/L submerged); 3 L of water still in the grab out of the water | Handbook ranges |
| Bite | Shells fill to 75 % in loose saturated sand (range 50 to 90 %) | Estimate; settled only in test-pit trials |
| Hoisting | 1.1 dynamic allowance; 50 W per person sustained at a crank; three people at the cranks for the hoist, two on the 240 mm two-hand handle (SKG-DDR-003); a 400 N short heave | Ergonomic ranges |
| Pins | S235 bar or mild steel wire, ultimate shear strength 240 MPa; crank pin scatter ±20 %; link pins break-tested from one coil, ±10 % | 0.6 times 400 MPa tensile |
| Tripod | HatchSide: 150 kg safe working load for material handling; proof 1.5 times | HTS-CAL-001 |
| Rope | 8 mm polyester double braid, 12 kN minimum breaking strength; eye splice keeps 90 % | Typical catalogue figures |
| Drive | Chain 95 %, each bearing 98 % | Typical figures |
| Brake | Lining on steel, friction 0.35; 270 degree wrap | Typical figures |
| Rings | Precast concrete 2,400 kg/m3; string of 8 rings, 6 under water; skin friction 1 to 3 kPa in loose saturated sand disturbed by the undercut | Estimate; no published figure for small well rings |
| Scraper | 150 N per toe cutting a 25 mm bite of loose saturated sand | Estimate |
| Cycle | Lowering on the brake at 0.5 m/s; cranks off and on 20 s; opening 10 s; closing 15 s through a 2:1 tackle plus the extra line of the third part at hoist speed; doors and dumping 45 s | Estimates |
| Tape | One dip-tape reading at depth ±3 mm | Estimate |

## A. Grab capacity and mass (R3, R9)

The closed shells, 230 mm in radius and 340 mm wide, hold 28.3 L; at a 75 % fill a bite is 21.2 L [A1]. The grab weighs 51.2 kg: the shells 11.6 and 11.8 kg, the head 8.7 kg with 5.3 kg of ballast plates, the head sheave and its axle 2.3 kg, the tie rods 3.8 kg [A2]. Full and out of the water it is 96.6 kg (948 N) [A3]; under water 65.9 kg (646 N) [A4]. With the 1.1 allowance the working line pull is 1,042 N [A5]. The 3:1 tackle added 3.3 kg to the grab, against the 2.5 kg estimated when it was proposed.

## B. Closing force (R3)

The closing line runs down the head's guide tube, under the crosshead sheave, up over the head sheave and down to the shear link on the crosshead: a 3:1 tackle (SKG-DDR-003). Closing moves the crosshead 142 mm toward the head, which takes 426 mm of line, while the lips travel 401 mm in all; opened, the lips are 352 mm apart [B1]. The mean force at the lips is therefore 1.06 of the line pull. The line can pull no more than the grab's submerged weight, 646 N, before the grab lifts off the bottom, so the lips close with about 687 N, 1,010 N per metre of lip [B2]. With the former 2:1 tackle the factor was 0.71 and the lip force about 458 N on today's grab, so the 3:1 tackle gives 50 % more; the head weighs 14.0 kg with its plates, which is what opens the shells [B3]. If the fill falls to 50 % in denser sand, a bite is 14.1 L [B4]. **R3 is at risk:** it is met at the assumed fill and missed at 50 %; the fill is settled in the TRL 4 test-pit bite trial.

## C. Overload limits (R7)

A 3 mm S235 pin across the 25 mm crank shaft releases at 42.4 N m [C1]. Through the 4:1 chain that is a line pull of 1,756 N on the innermost layer of rope, 1,610 N on the second and 1,486 N on the third; with ±20 % scatter the pin releases between 1,189 and 2,107 N [C2]. The HatchSide tripod's safe working load is 1,472 N and its proof load 2,207 N, so the crank pin never lets the line pass the proof load [C3]. Without the pin, two people heaving 400 N each could put 8,280 N into a snagged line [C6].

The shear link at the tackle's dead end is the precise limit. A pin of about 1.88 mm in double shear releases at 1,335 N nominal; break-tested pins from one coil, ±10 %, release between 1,202 and 1,469 N, inside the tripod's 1,472 N rating [C4]. Its lowest release is 1.15 times the working pull, down from 1.19 because the grab is 3.3 kg heavier [C5]. When it releases, the dead end runs free through the head and crosshead sheaves and the grab opens on the bottom; it is recovered on the recovery line.

## D. Crank force and speed (R5)

At the rated grab load on the third layer, one person pushes 108 N on a 250 mm crank and two people 54 N each [D1]. **R5 is met on paper.** Two people at 50 W each hoist the full grab at 5.8 m/min, cranking at about 38 rpm [D2]. With a third person on the hoist (two on the 240 mm two-hand handle of the +X crank) the grab rises at 8.7 m/min, with about 36 N each on average [D3].

## E. Drum and rope (R7)

The drum holds 23 turns a layer: 12.7, 13.9 and 15.1 m in three layers, 41.7 m, against the 38.7 m a 30 m well needs [E1]. The drum stands 3.0 m from the lead sheave for a fleet angle of 1.91 degrees [E2]. The 8 mm line keeps 10.8 kN through its splice: a factor of 10.4 on the working pull and 5.1 on the crank pin's highest release [E3]. The sheaves are 16.2 rope diameters at the pitch line and the drum 22.0 [E4].

## F. Brake and pawl

The band wraps 270 degrees, so the tight side carries 5.20 times the slack side. A 6 kg weight on a 10.2:1 lever gives 598 N on the slack side and 314 N m of holding torque [F1]. The most the line can put on the drum is 186 N m, at the crank pin's limit on the innermost layer: a factor of 1.69, and 2.9 at the working pull [F2]. The ratchet tooth carries 2,211 N at the limit, 17 MPa on its face [F3].

## G. Tripod, cradle, drawbar and capstan stability (R7)

At the limit the lead sheave is pulled 833 N outward and 1,678 N up, and the drawbar pushes the cradle 2,107 N inward. The foot therefore sees the rope along leg A, which is the load case HatchSide was designed for with its own winch [G1]. The 2,470 mm drawbar has an Euler load of 39.4 kN, 19 times the limit [G2]. The capstan weighs 69.7 kg with the longer handle; because the rope runs 80 mm above the drawbar, it is pitched forward by 169 N m at the limit, against 253 N m from its weight; the stakes hold it from skating [G3]. The line's rated load is 122 kg, the link's lowest release. Proof at twice the working load is 193 kg, inside HatchSide's 225 kg proof load [G4]. **R7 is met on paper.**

## H. Scraper (R2, R8)

Two toes cutting 150 N each at 615 mm radius need 184 N m, 142 N for each of two people on the T-bar, 4 % more than with the former 590 mm toes [H1]. The 42.4 x 2.6 mm pole carries that at 30 MPa and winds up 10 degrees over 10 m [H2]. The scraper head weighs 25.1 kg, each pole section 7.1 kg and the T-bar 5.6 kg; hung at 10 m it is 66 kg [H3]. At 25 m, with 12 sections, it is 116 kg, 1,251 N with the allowance, under both the crank pin's lowest release on the innermost layer (1,405 N) and the tripod's rating, so 25 m is the scraper's working limit [H4]. The toes reach 615 mm, 40 mm beyond a 1.0 m ring's outer face (SKG-DDR-003); lifted 320 mm on the sleeve they fold to 377 mm, inside the 400 mm bore of the smallest ring [H5]. With the former 300 mm lift the longer arms would fold only to 405.5 mm, so the lift was raised. **R2 is met by design**, with a longer pair of arms for 1.2 to 1.3 m rings. As modelled, though, the stop collar on the spike sits 30 mm below the sleeve's foot, so the pole can lift only 30 mm on the sleeve before it picks the sleeve up; this was already the case with the 300 mm lift and is posed to Amish as a new question.

## I. Sinking and tilt (R1, R6)

A 1.0 m ring with a 75 mm wall, 0.5 m high, weighs 304 kg. A string of 8 rings with 6 under water weighs 16.4 kN effective, and eight saddles add 1.61 kN, 10 % [I1]. After 3 m of sinking the rings have 10.8 m2 of outer face in the soil, which at 1 to 3 kPa of skin friction holds 10.8 to 32.5 kN [I2]. The string keeps sinking to 3 m only while skin friction stays below 1.66 kPa [I3]. **R1 is at risk:** the outcome depends on a soil property that only a trial can measure. Removing the soil for 3 m of sinking, out to the toe radius, is about 3.56 m3 [I4]. The wider cut is meant to loosen the soil against the ring so the friction stays toward the low end of the estimate; only the trial can show whether it does.

Two dip-tape readings 1,075 mm apart resolve the tilt to ±4.2 mm, 1 in 253; 1 in 80 is 13.4 mm, so the readings can see it clearly [I5]. Whether scraping the high side and moving saddles corrects it is a trial question. **R6 cannot be verified at TRL 3.**

## J. Cycle time and output (R4)

With three people at the cranks for the hoist (SKG-DDR-003), a cycle at 10 m takes 22 s to lower, 20 s to take the cranks off and put them back, 10 s to open, 16 s to close through the 3:1 tackle, 77 s to hoist and 45 s for the doors and dumping: 190 s, 3.16 min, 5 % over the target [J1]. With two people the hoist takes 115 s and the cycle 3.8 min [J2]. The output is 402 L an hour of sand in place, so the 3 m of sinking takes about 8.9 h of grabbing [J3]. **R4 is not met on paper**, by 5 %: the hoist is limited by the power the crew can give, not by the gearing, and the timed trial settles the rest.

## K. Masses and cost (R9, R11)

The heaviest pieces are the scraper head at 25.1 kg, the capstan frame at 22.9 kg, a ballast saddle at 20.6 kg, the foot cradle at 19.4 kg and the winding drum at 18.3 kg [K1]. The assembled grab is 51.2 kg, carried by two people; the longest pieces are the pole sections at 2.0 m [K2]. **R9 is not met on paper, by 0.1 kg**: the longer arms brought the scraper head from 24.9 to 25.1 kg (removing the stop collar, a new question, would bring it to 24.8 kg). Value-engineering target: USD 4,000. Estimated cost of the constructable design: USD 2,561.00 (USD 1,439.00 under the target), USD 55 more for the two-hand handle, the 3:1 tackle and the longer arms [K3]. The kit weighs about 456 kg without ropes, tubs and the tripod [K4].

## M. Results against every requirement

*Table 2. Requirement status from this note [M].*

| ID | Requirement | Value | Target | Status |
| --- | --- | --- | --- | --- |
| R4 | Cycle time at 10 m, two operators | 3.16 min with a third person at the cranks for the hoist (3.8 min with two) | 3 min or less | **Not met on paper** (5 % over) |
| R9 | Portability | Heaviest piece 25.1 kg (scraper head); kit about 456 kg; longest 2.0 m | 25 kg or less; small pickup | **Not met on paper** (0.1 kg over) |
| R1 | Water depth reached without de-watering | Sinks while skin friction stays below 1.66 kPa; estimate 1 to 3 kPa; toes cut 40 mm past the ring | At least 3 m | **At risk** |
| R3 | Grab load per bite | 21.2 L at 75 % fill; 14.1 L at 50 %; lips close with about 687 N (3:1) | At least 20 L | **At risk** |
| R6 | Tilt | Readings resolve 1 in 253; correction by scraping the high side and saddles | 1 in 80 or better | Not verifiable at TRL 3 |
| R5 | Crank force | 54 N each with two people (108 N for one) | 150 N or less | Met on paper |
| R7 | Proof load of lifting parts | Proof 193 kg inside HatchSide's 225 kg; line factor 10.4 | 2 times working load | Met on paper |
| R11 | Prototype cost | USD 2,561 | Value-engineering target USD 4,000 | Met on paper, within the target |
| R2 | Fits rings of 0.8 to 1.3 m | Grab 468 mm across; scraper folds to 377 mm radius with a 320 mm lift; adjustable toes and skids, longer arms | 0.8 to 1.3 m | Met by design |
| R8 | No person in the well | Every task from the surface; doors cover the shaft | 100 % | Met by design |
| R10 | Local build | Steel section and plate, stick welding, drilling; shell skins rolled | Stick welder and hand tools | Met by design |

Counts: 2 not met, 2 at risk, 1 not verifiable at TRL 3, 3 met on paper, 3 met by design. R4, R3 and R1 were decided by Amish on 2026-10-03 (SKG-DDR-003) and stay not met or at risk until the trials; R9 and the questions found while carrying out the decisions are posed in SKG-DEC-001.

## Checks against the TRL 1 concept

| Concept (SKG-PRC-001 v0.1) | This note | Action |
| --- | --- | --- |
| Rope-closed grab with a closing line and a holding line | Two lines need two hoists and two people in step | One line; the head's weight opens the shells (SKG-DDR-001) |
| Hand capstan on one tripod leg | A 69 kg capstan cannot hang on an aluminium leg | Ground capstan with a drawbar to a cradle under the leg A foot (SKG-DDR-002) |
| HatchSide tripod "can be rated" for the loads | The tripod is rated 150 kg; two people at a crank can reach 8.3 kN | Shear link and crank shear pin (R7) |
| Scraper on a pole or guided frame | A pole is the only way to turn a tool at depth | Centred pole with a centralizer, arms opened by weight |
| Spoil chute and tipping hook | A chute over the mouth must be moved every cycle and cannot cover the shaft | Folding doors and a spoil tub |
