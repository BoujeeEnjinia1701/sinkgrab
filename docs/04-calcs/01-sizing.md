---
doc_id: SKG-CAL-001
title: SinkGrab sizing calculations
project: SinkGrab
doc_type: Calculation
version: "0.3"
status: Draft
date: '2026-10-04'
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
  change: "Amish's round-2 decisions of 2026-10-03 (\"i agree with all the 46 recommendations you provided. please proceed.\"): 27A third person on the cranks during the hoist, 28B 3:1 closing tackle, 29B toe blades cutting 40 mm past the ring's outer face (SKG-DDR-003); every section re-run"
- version: "0.3"
  date: '2026-10-04'
  author: Amish Chadha
  change: "Amish's round-3 decision 5A of 2026-10-04 (\"For round 3, I agree with all your proposed recommendations\"): 340 mm slotted sleeve on a 12 mm cross pin so the scraper arms fold to pass the ring (SKG-DDR-004); sections H and K re-run, H7 and H8 added"
---

# SinkGrab sizing calculations

On paper SinkGrab does what it was drawn for, inside the HatchSide tripod's rating, and after Amish's round-2 decisions of 2026-10-03 it comes within about 0.2 min of its 3 min cycle-time target. The grab lifts 21 L of saturated sand a bite at an assumed 75 % fill, now closed by a 3:1 tackle that presses the lips 50 % harder than the first design's 2:1; two people hoist the full 96 kg grab with 54 N each on the cranks, and a third person on a long two-hand handle joins them for the hoist; a shear link and a crank shear pin keep the line below the tripod's 150 kg rating and 225 kg proof load whatever the crew does; the toes now cut 40 mm past the ring's outer face, and since Amish's round-3 decision of 2026-10-04 the scraper's sleeve slides the full 300 mm its arms need to fold through the ring; and the heaviest piece is 22.9 kg once the scraper's arms are unpinned for carrying. The parts cost USD 2,566 against a value-engineering target of USD 4,000. R4 is still not met on paper: a cycle at 10 m takes about 3.2 min (3.17 min) with three people at the hoist, 6 % over the target, and the timed trial decides it. R1 stays at risk, because the rings keep sinking to 3 m only while skin friction stays below about 1.7 kPa; the wider cut acts on that friction but only a trial can measure it. R3 is met on paper at the assumed fill, which the test-pit trial confirms. Every number here is printed by `docs/04-calcs/sizing.py`; the tag in brackets, for example [C2], is the line of that script's output that carries it.

> **Safety:** SinkGrab is lifting equipment over an open well shaft. These are first-principles estimates for a paper proof of concept; they do not show that any part is safe. Every lifting part must be proof-loaded before use (SKG-BLD-001, section 6), nobody stands under the grab or beside a loaded line, and nobody enters the well. A third person at the cranks means three people beside the capstan during the hoist; all three let go together on the stop call, and nobody stands between the capstan and the lead sheave. See SKG-PRC-001, Safety.

## Scope and method

The note checks every requirement in SKG-REQ-001 v0.4 against the design in SKG-PRC-001, as changed by SKG-DDR-003 and SKG-DDR-004, and the parametric model `cad/src/model.py`. The script imports the model's `PARAMS`, `derived()` and `masses()`, so the grab, drum, scraper and frame used here are the ones in the STEP files and drawings SKG-DWG-001 and 002. It also reads `bom/bom.csv` and `budget_usd` in `project.yaml`, and writes `docs/04-calcs/results.csv`.

The design case is a 1.0 m caisson ring with a 75 mm wall inside a 1.3 m lining, the digging face 10 m below ground (R4) and 3 m of water standing over it at the end of the work (R1). The HatchSide tripod stands over the well with SinkGrab's line in place of its winch.

## Assumptions

*Table 1. Main assumptions.*

| Area | Assumption | Basis |
| --- | --- | --- |
| Sand | Saturated fine to medium sand 2.0 kg/L (1.0 kg/L submerged); 3 L of water still in the grab out of the water | Handbook ranges |
| Bite | Shells fill to 75 % in loose saturated sand (range 50 to 90 %) | Estimate; settled only in test-pit trials |
| Hoisting | 1.1 dynamic allowance; 50 W per person sustained at a crank, the third person included; a 400 N short heave | Ergonomic ranges |
| Pins | S235 bar or mild steel wire, ultimate shear strength 240 MPa; crank pin scatter ±20 %; link pins break-tested from one coil, ±10 % | 0.6 times 400 MPa tensile |
| Tripod | HatchSide: 150 kg safe working load for material handling; proof 1.5 times | HTS-CAL-001 |
| Rope | 8 mm polyester double braid, 12 kN minimum breaking strength; eye splice keeps 90 % | Typical catalogue figures |
| Drive | Chain 95 %, each bearing 98 % | Typical figures |
| Brake | Lining on steel, friction 0.35; 270 degree wrap | Typical figures |
| Rings | Precast concrete 2,400 kg/m3; string of 8 rings, 6 under water; skin friction 1 to 3 kPa in loose saturated sand disturbed by the undercut | Estimate; no published figure for small well rings |
| Scraper | 150 N per toe cutting a 25 mm bite of loose saturated sand | Estimate |
| Cycle | Lowering on the brake at 0.5 m/s; cranks off and on 20 s; opening 10 s; closing 16.5 s (15 s plus 1.5 s for the extra line of the 3:1 tackle); doors and dumping 45 s | Estimates |
| Tape | One dip-tape reading at depth ±3 mm | Estimate |

## A. Grab capacity and mass (R3, R9)

The closed shells, 230 mm in radius and 340 mm wide, hold 28.3 L; at a 75 % fill a bite is 21.2 L [A1]. The grab weighs 51.0 kg: the shells 11.6 and 11.8 kg, the head 8.2 kg with 5.3 kg of ballast plates, the tie rods 3.8 kg; the 3:1 tackle (upper sheave, its axle and cheeks, and the dead-end arm on the crosshead) adds 3.1 kg to the first design's 47.9 kg [A2]. Full and out of the water it is 96.4 kg (946 N) [A3]; under water 65.7 kg (645 N) [A4]. With the 1.1 allowance the working line pull is 1,041 N [A5].

## B. Closing force (R3)

The line now runs down through the head's guide tube, under the crosshead sheave, up over the upper sheave in the head and down to the shear link on the crosshead: three parts between head and crosshead (Amish's decision 28B). Closing moves the crosshead 142 mm toward the head, which takes 426 mm of line, while the lips travel 401 mm in all; opened, the lips are 352 mm apart [B1]. The mean force at the lips is therefore 1.06 of the line pull. The line can pull no more than the grab's submerged weight, 645 N, before the grab lifts off the bottom, so the lips close with about 685 N, 1,007 N per metre of lip [B2]. The first design's 2:1 tackle gave 0.71 of the line pull, about 457 N, so the 3:1 tackle closes 50 % harder; the head weighs 13.5 kg with its plates and cheeks, which is what opens the shells [B3]. If the fill falls to 50 % in denser sand, a bite is 14.1 L [B4]. **R3 is met on paper at the assumed 75 % fill**; the harder close makes that fill more likely in denser sand, and the test-pit trial confirms it.

## C. Overload limits (R7)

A 3 mm S235 pin across the 25 mm crank shaft releases at 42.4 N m [C1]. Through the 4:1 chain that is a line pull of 1,756 N on the innermost layer of rope, 1,610 N on the second and 1,486 N on the third; with ±20 % scatter the pin releases between 1,189 and 2,107 N [C2]. The HatchSide tripod's safe working load is 1,472 N and its proof load 2,207 N, so the crank pin never lets the line pass the proof load [C3]. Without the pin, two people heaving 400 N each could put 8,280 N into a snagged line [C6]; a third person on the long handle makes the pin more necessary, not less.

The shear link at the tackle's dead end, now on the crosshead, is the precise limit. Every part of the line carries the same tension, so the link still sees the line pull. A pin of about 1.88 mm in double shear releases at 1,335 N nominal; break-tested pins from one coil, ±10 %, release between 1,202 and 1,469 N, inside the tripod's 1,472 N rating [C4]. Its lowest release is 1.15 times the working pull (1.19 before the 3.1 kg of tackle) [C5]. When it releases, the line runs free through both sheaves and the grab opens on the bottom; it is recovered on the recovery line.

## D. Crank force and speed (R5)

At the rated grab load on the third layer, one person pushes 108 N on a 250 mm crank and two people 54 N each [D1]. **R5 is met on paper.** Two people at 50 W each hoist the full grab at 5.8 m/min, cranking at about 38 rpm [D2].

## E. Drum and rope (R7)

The drum holds 23 turns a layer: 12.7, 13.9 and 15.1 m in three layers, 41.7 m, against the 38.7 m a 30 m well needs [E1]; the 3:1 tackle takes about 0.4 m more line inside the grab, within the 7 m allowed for reeving. The drum stands 3.0 m from the lead sheave for a fleet angle of 1.91 degrees [E2]. The 8 mm line keeps 10.8 kN through its splice: a factor of 10.4 on the working pull and 5.1 on the crank pin's highest release [E3]. The sheaves, the upper sheave included, are 16.2 rope diameters at the pitch line and the drum 22.0 [E4].

## F. Brake and pawl

The band wraps 270 degrees, so the tight side carries 5.20 times the slack side. A 6 kg weight on a 10.2:1 lever gives 598 N on the slack side and 314 N m of holding torque [F1]. The most the line can put on the drum is 186 N m, at the crank pin's limit on the innermost layer: a factor of 1.69, and 2.9 at the working pull [F2]. The ratchet tooth carries 2,211 N at the limit, 17 MPa on its face [F3].

## G. Tripod, cradle, drawbar and capstan stability (R7)

At the limit the lead sheave is pulled 833 N outward and 1,678 N up, and the drawbar pushes the cradle 2,107 N inward. The foot therefore sees the rope along leg A, which is the load case HatchSide was designed for with its own winch [G1]. The 2,470 mm drawbar has an Euler load of 39.4 kN, 19 times the limit [G2]. The capstan weighs 69.7 kg with the long handle; because the rope runs 80 mm above the drawbar, it is pitched forward by 169 N m at the limit, against 253 N m from its weight; the stakes hold it from skating [G3]. The line's rated load is 122 kg, the link's lowest release. Proof at twice the working load is 193 kg, inside HatchSide's 225 kg proof load [G4]. **R7 is met on paper.**

## H. Scraper (R2, R8)

Two toes cutting 150 N each at 615 mm radius need 184 N m, 142 N for each of two people on the T-bar [H1]. The 42.4 x 2.6 mm pole carries that at 30 MPa and winds up 10 degrees over 10 m [H2]. The scraper head weighs 26.1 kg with its arms on, each pole section 7.1 kg and the T-bar 5.6 kg; hung at 10 m it is 67 kg [H3]. At 25 m, with 12 sections, it is 117 kg, 1,262 N with the allowance, under both the crank pin's lowest release on the innermost layer (1,405 N) and the tripod's rating, so 25 m is still the scraper's working limit [H4]. A 10 mm toe blade lapped on each toe plate now reaches 615 mm, 40 mm beyond a 1.0 m ring's outer face (Amish's decision 29B; the first design reached 15 mm); lifted 300 mm on the sleeve the toes fold to 389 mm, inside the 400 mm bore of the smallest ring, with 11 mm to spare [H5]. Against the first design's 590 mm toes the T-bar force rises 4 %; the arms with their blades weigh 5.8 kg [H6]. The fold relies on the sleeve sliding 300 mm down the pole. In the first design a stop collar 40 mm below the sleeve allowed only about 40 mm, so the toes folded only to about 604 mm and the head could not have been lifted out through any ring in the range. Amish's decision 5A (2026-10-04, SKG-DDR-004) replaces the collar with a 340 mm sleeve slotted 13 x 312 mm on each side and a 12 mm cross pin through the pole running in the slots: open, the pin bears on the slot bottoms; lifted, the sleeve slides down until the pin meets the slot tops, a travel of 300 mm, exactly what the fold needs. The sleeve's top stands 15 mm below the hub and the spike stays 110 mm below the foot, so nothing is pushed into the sump floor [H7]. With the whole 25 m string resting on the foot the pin carries 1,262 N in double shear, 6 MPa (a factor of 43), and bears on the pole wall at 20 MPa [H8]. The model checks the folded position: the sleeve slid 300 mm down is held by the pin at its slot tops without touching the pole. **R2 is met by design**, with a longer pair of arms for 1.2 to 1.3 m rings.

## I. Sinking and tilt (R1, R6)

A 1.0 m ring with a 75 mm wall, 0.5 m high, weighs 304 kg. A string of 8 rings with 6 under water weighs 16.4 kN effective, and eight saddles add 1.61 kN, 10 % [I1]. After 3 m of sinking the rings have 10.8 m2 of outer face in the soil, which at 1 to 3 kPa of skin friction holds 10.8 to 32.5 kN [I2]. The string keeps sinking to 3 m only while skin friction stays below 1.66 kPa [I3]. The toe blades cut a 40 mm ring of soil outside the ring's outer face, so the ring slides down through loosened soil rather than soil packed against it; this aims to keep the friction toward the low end of the estimate, but no calculation here can show by how much. **R1 stays at risk:** the outcome depends on a soil property that only the first trial can measure. Removing the soil for 3 m of sinking, out to the toe radius, is about 3.56 m3, 0.28 m3 more than with the first design's toes [I4].

Two dip-tape readings 1,075 mm apart resolve the tilt to ±4.2 mm, 1 in 253; 1 in 80 is 13.4 mm, so the readings can see it clearly [I5]. Whether scraping the high side and moving saddles corrects it is a trial question. **R6 cannot be verified at TRL 3.**

## J. Cycle time and output (R4)

With two people at the cranks a cycle at 10 m takes 22 s to lower, 20 s to take the cranks off and put them back, 10 s to open, 16 s to close, 115 s to hoist and 45 s for the doors and dumping: 3.8 min [J1]. With a third person on the long two-hand handle during the hoist (Amish's decision 27A) the hoist takes 76 s and the cycle 3.17 min, 6 % over the 3 min target [J2]. The output is 402 L an hour of sand in place, so the 3 m of sinking takes about 8.9 h of grabbing [J3]. **R4 is not met on paper, by about 0.2 min:** the hoist is limited by the power the crew can give, not by the gearing, and the 3:1 tackle and its 3.1 kg cost about 4 s a cycle. Amish's decision records that the timed trial settles the remainder.

## K. Masses and cost (R9, R11)

With its arms pinned on, the scraper head weighs 26.1 kg, over the 25 kg limit, so it is carried with its two arms unpinned: 20.1 kg for the head and 6.0 kg for the pair of arms with their pins [K0]. The slotted sleeve and cross pin add 0.9 kg net (the longer sleeve 1.1 kg and the pin 0.06 kg, less the 0.3 kg stop collar), less than the 1.4 kg estimated when the option was posed. The heaviest pieces are then the capstan frame at 22.9 kg, a ballast saddle at 20.6 kg, the scraper head at 20.1 kg, the foot cradle at 19.4 kg and the winding drum at 18.3 kg [K1]. The assembled grab is 51.0 kg, carried by two people; the longest pieces are the pole sections at 2.0 m [K2]. **R9 is met on paper**, with the arms carried separately. Value-engineering target: USD 4,000. Estimated cost of the constructable design: USD 2,566 (USD 1,434 under the target) [K3]. The round-2 changes added USD 55: the upper sheave, cheeks, axle and dead-end arm USD 35, the long handle USD 10 and the toe blades USD 10; the round-3 slotted sleeve and cross pin add USD 5. The kit weighs about 457 kg without ropes, tubs and the tripod [K4].

## M. Results against every requirement

*Table 2. Requirement status from this note [M].*

| ID | Requirement | Value | Target | Status |
| --- | --- | --- | --- | --- |
| R4 | Cycle time at 10 m, three people at the cranks during the hoist | 3.2 min (3.17 min; 3.8 min with two) | 3 min or less | **Not met on paper by about 0.2 min**; the timed trial decides |
| R1 | Water depth reached without de-watering | Sinks while skin friction stays below 1.66 kPa; estimate 1 to 3 kPa; toes cut 40 mm past the ring to keep it low | At least 3 m | **At risk**; friction measured in the first trial |
| R3 | Grab load per bite | 21.2 L at 75 % fill with a 3:1 tackle (50 % more closing force); 14.1 L at 50 % | At least 20 L | Met on paper at the assumed fill; fill confirmed in the test-pit trial |
| R6 | Tilt | Readings resolve 1 in 253; correction by scraping the high side and saddles | 1 in 80 or better | Not verifiable at TRL 3 |
| R5 | Crank force | 54 N each with two people (108 N for one) | 150 N or less | Met on paper |
| R7 | Proof load of lifting parts | Proof 193 kg inside HatchSide's 225 kg; line factor 10.4; link margin 1.15 | 2 times working load | Met on paper |
| R9 | Portability | Heaviest piece 22.9 kg with the scraper arms carried unpinned (scraper head 26.1 kg with them on, 20.1 kg without); kit about 457 kg; longest 2.0 m | 25 kg or less; small pickup | Met on paper |
| R11 | Prototype cost | USD 2,566 | Value-engineering target USD 4,000 | Met on paper, within the target |
| R2 | Fits rings of 0.8 to 1.3 m | Grab 468 mm across; scraper folds to 389 mm radius on a 300 mm sleeve travel (slotted sleeve and cross pin); adjustable toes and skids, longer arms | 0.8 to 1.3 m | Met by design |
| R8 | No person in the well | Every task from the surface; doors cover the shaft | 100 % | Met by design |
| R10 | Local build | Steel section and plate, stick welding, drilling; shell skins rolled | Stick welder and hand tools | Met by design |

Counts: 1 not met (by about 0.2 min), 1 at risk, 1 not verifiable at TRL 3, 5 met on paper, 3 met by design. Amish decided R4, R3 and R1 on 2026-10-03 and the scraper sleeve's travel (R2) on 2026-10-04 (SKG-DEC-001); what is left of R4 and R1 is settled by the timed trial and the first well trial.

## Checks against the TRL 1 concept

| Concept (SKG-PRC-001 v0.1) | This note | Action |
| --- | --- | --- |
| Rope-closed grab with a closing line and a holding line | Two lines need two hoists and two people in step | One line; the head's weight opens the shells (SKG-DDR-001); 3:1 tackle (SKG-DDR-003) |
| Hand capstan on one tripod leg | A 70 kg capstan cannot hang on an aluminium leg | Ground capstan with a drawbar to a cradle under the leg A foot (SKG-DDR-002) |
| HatchSide tripod "can be rated" for the loads | The tripod is rated 150 kg; two people at a crank can reach 8.3 kN | Shear link and crank shear pin (R7) |
| Scraper on a pole or guided frame | A pole is the only way to turn a tool at depth | Centred pole with a centralizer, arms opened by weight |
| Spoil chute and tipping hook | A chute over the mouth must be moved every cycle and cannot cover the shaft | Folding doors and a spoil tub |
