---
doc_id: SKG-CAL-001
title: SinkGrab sizing calculations
project: SinkGrab
doc_type: Calculation
version: "0.6"
status: Draft
date: '2026-10-25'
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
- version: "0.4"
  date: '2026-10-24'
  author: Amish Chadha
  change: "Kit 1.9.1 upgrade: masses from the detailed D3 model (pins, clips, collars, bolts and welds counted); design fixes of SKG-DEC-001 K1 to K21 (arm pivot at 60 mm, set collars on the hinge pin, CO2 monitor, brake lever geometry and others); every section re-run; new section N; no requirement changes status"
- version: "0.5"
  date: '2026-10-25'
  author: Amish Chadha
  change: "Independent review of the STEM check (section O): R1 not met on paper; R3 and R7 at risk; missing checks listed for the next revision"
- version: "0.6"
  date: '2026-10-25'
  author: Amish Chadha
  change: "Amish's decisions of 2026-10-25 (\"i approve of your recommendations\", SKG-DEC-001 O2 to O5): crank slip clutch and dead-end load indicator in place of both shear devices, proof at 1.25 x the rated load (sections C, E, F, G); four people at the T-bar after the 2.0 m T-bar failed the tripod leg check (H9, H10); bentonite slurry in the overcut annulus (I6); grab 52.7 kg; cost USD 3,063"
---

# SinkGrab sizing calculations

On paper SinkGrab does what it was drawn for, inside the HatchSide tripod's rating, and after Amish's round-2 decisions of 2026-10-03 it comes within about 0.2 min of its 3 min cycle-time target. The grab lifts 21 L of saturated sand a bite at an assumed 75 % fill, now closed by a 3:1 tackle that presses the lips 50 % harder than the first design's 2:1; two people hoist the full 98 kg grab with 55 N each on the cranks, and a third person on a long two-hand handle joins them for the hoist; a friction slip clutch on the crank shaft keeps the capstan pull at or below the tripod's 150 kg rating whatever the crew does, and a load indicator at the tackle's dead end shows the peak of every lift (Amish's decision O4 of 2026-10-25); the toes now cut 40 mm past the ring's outer face, and since Amish's round-3 decision of 2026-10-04 the scraper's sleeve slides the full 300 mm its arms need to fold through the ring; and the heaviest piece is the 22.4 kg capstan frame once the scraper's arms are unpinned for carrying. The parts cost USD 3,063 against a value-engineering target of USD 4,000. Since the kit 1.9.1 upgrade of 2026-10-24 every mass comes from the detailed model, with every pin, clip, collar, bolt and weld counted, and the design carries the fixes of SKG-DEC-001 K1 to K21; the grab is 1.5 kg heavier than the kit 1.7 model gave and no requirement changes status (section N). R4 is still not met on paper: a cycle at 10 m takes about 3.2 min (3.19 min) with three people at the hoist, 6 % over the target, and the timed trial decides it. R1 stays at risk, because the rings keep sinking to 3 m only while skin friction stays below about 1.7 kPa; the wider cut acts on that friction but only a trial can measure it. R3 is met on paper at the assumed fill, which the test-pit trial confirms. The independent review of the STEM check on 2026-10-25 changed three statuses (section O): R1 is not met on paper, and R3 and R7 are at risk. Amish's decisions of 2026-10-25 (SKG-DEC-001 O2, O4 and O5) put a bentonite-lubricated annulus into the sinking method, replace both shear devices with the slip clutch and load indicator and proof at 1.25 times the rated load, and put four people on the T-bar; R1 and R7 stay at risk until the test pit and CalRig show the friction and the clutch window. Every number here is printed by `docs/04-calcs/sizing.py`; the tag in brackets, for example [C2], is the line of that script's output that carries it.

> **Safety:** SinkGrab is lifting equipment over an open well shaft. These are first-principles estimates for a paper proof of concept; they do not show that any part is safe. Every lifting part must be proof-loaded before use (SKG-BLD-001, section 6), nobody stands under the grab or beside a loaded line, and nobody enters the well. A third person at the cranks means three people beside the capstan during the hoist; all three let go together on the stop call, and nobody stands between the capstan and the lead sheave. See SKG-PRC-001, Safety.

## Scope and method

The note checks every product requirement in SKG-PRS-001 (R1 to R11 there are PR-001 to PR-011) against the design in SKG-PRC-001, as changed by SKG-DDR-003, SKG-DDR-004 and the kit 1.9.1 fixes in SKG-DEC-001, and the parametric model `cad/src/model.py`. The script imports the model's `PARAMS`, `derived()` and `masses()`; since kit 1.9 `masses()` sums the detailed parts of option A (STANDARDS section 24), so the grab, drum, scraper and frame used here are the ones in the STEP files and drawings SKG-DWG-001 and 002. It also reads `bom/bom.csv` and `budget_usd` in `project.yaml`, and writes `docs/04-calcs/results.csv`.

The design case is a 1.0 m caisson ring with a 75 mm wall inside a 1.3 m lining, the digging face 10 m below ground (R4) and 3 m of water standing over it at the end of the work (R1). The HatchSide tripod stands over the well with SinkGrab's line in place of its winch.

## Assumptions

*Table 1. Main assumptions.*

| Area | Assumption | Basis |
| --- | --- | --- |
| Sand | Saturated fine to medium sand 2.0 kg/L (1.0 kg/L submerged); 3 L of water still in the grab out of the water | Handbook ranges |
| Bite | Shells fill to 75 % in loose saturated sand (range 50 to 90 %) | Estimate; settled only in test-pit trials |
| Hoisting | 1.1 dynamic allowance; 50 W per person sustained at a crank, the third person included; a 400 N short heave | Ergonomic ranges |
| Overload | Crank slip clutch: woven facings on ground steel, friction 0.35 dry; slip setting ±5 % after setting on CalRig; sheave and guide tube friction about 11 % when hoisting; breakout suction about 160 N; proof at 1.25 times the rated load | Brake lining figure; review of 2026-10-25; static test coefficients 1.25 to 1.5 (standard to assess, SKG-REG-001) |
| Load indicator | Disc springs 18 x 9.2 x 1.0, about 0.30 mm each at 2.17 kN | Catalogue value to confirm when bought |
| Tripod | HatchSide: 150 kg safe working load for material handling; proof 1.5 times | HTS-CAL-001 |
| Rope | 8 mm polyester double braid, 12 kN minimum breaking strength; eye splice keeps 90 % | Typical catalogue figures |
| Drive | Chain 95 %, each bearing 98 % | Typical figures |
| Brake | Lining on steel, friction 0.35; 270 degree wrap | Typical figures |
| Rings | Precast concrete 2,400 kg/m3; string of 8 rings, 6 under water; skin friction 1 to 3 kPa in loose saturated sand disturbed by the undercut | Estimate; no published figure for small well rings |
| Scraper | 150 N per toe cutting a 25 mm bite of loose saturated sand | Estimate |
| Cycle | Lowering on the brake at 0.5 m/s; cranks off and on 20 s; opening 10 s; closing 16.5 s (15 s plus 1.5 s for the extra line of the 3:1 tackle); doors and dumping 45 s | Estimates |
| Tape | One dip-tape reading at depth ±3 mm | Estimate |

## A. Grab capacity and mass (R3, R9)

The closed shells, 230 mm in radius and 340 mm wide, hold 28.3 L; at a 75 % fill a bite is 21.2 L [A1]. The grab weighs 52.7 kg in the detailed model, which counts every pin, split pin, collar and bolt: the shells 11.6 and 11.9 kg, the head 8.6 kg with 5.6 kg of ballast plates, spacers and bolts, the tie rods 3.9 kg, the load indicator 0.5 kg; the kit 1.7 simplified model gave 51.0 kg and the first design 47.9 kg [A2]. Full and out of the water it is 98.1 kg (962 N) [A3]; under water 67.2 kg (659 N) [A4]. With the 1.1 allowance the working line pull is 1,058 N [A5].

## B. Closing force (R3)

The line now runs down through the head's guide tube, under the crosshead sheave, up over the upper sheave in the head and down to the load indicator on the crosshead: three parts between head and crosshead (Amish's decision 28B). Closing moves the crosshead 142 mm toward the head, which takes 426 mm of line, while the lips travel 401 mm in all; opened, the lips are 352 mm apart [B1]. The mean force at the lips is therefore 1.06 of the line pull. The line can pull no more than the grab's submerged weight, 657 N, before the grab lifts off the bottom, so the lips close with about 700 N, 1,029 N per metre of lip [B2]. The first design's 2:1 tackle gave 0.71 of the line pull, about 467 N, so the 3:1 tackle closes 50 % harder; the head weighs 14.3 kg with its plates, cheeks, pins and spacers, which is what opens the shells [B3]. The STEM check compares this force with the passive drag on each lip at full bite depth in loose sand, about 270 N against 350 N per shell, and keeps it open until a bite trial (SKG-STM-001, S2). If the fill falls to 50 % in denser sand, a bite is 14.1 L [B4]. **R3 is at risk** (section O): at the assumed 75 % fill it is met on paper, but the closing margin rests on assumptions the independent review questioned, and the test-pit trial confirms it.

## C. Overload limits (R7)

Amish's decision O4 of 2026-10-25 (SKG-DEC-001) replaces both shear devices: the independent review found no release window for a shear pin between the working pull and the tripod's rating, and the crank pin ran above shear yield in ordinary hoisting. A friction slip clutch on the crank shaft now caps the capstan pull. The sprocket and two driven discs run on a sleeve on the shaft; woven facings 84 x 44 mm on an inner flange welded to the shaft and on a keyed pressure plate grip the discs, clamped by two disc springs and a KM5 locknut. At a friction of 0.35 and a mean facing radius of 33.0 mm a clamp of 1,464 N gives a nominal slip of 33.8 N m on the crank shaft, set on CalRig [C1]. Through the 4:1 chain that is a capstan pull of 1,401 N on the innermost layer of rope, 1,285 N on the second and 1,186 N on the third; with a ±5 % setting tolerance the clutch slips between 1,127 N (third layer, low end) and 1,472 N (first layer, high end) [C2]. The HatchSide tripod's safe working load is 1,472 N and its proof load 2,207 N, so the capstan pull never passes the rating, and the grab side carries less again by the sheave friction [C3].

The steady pull of the full grab at the capstan, with about 11 % lost in the lead and head sheaves and the guide tube, is 1,068 N, against the lowest slip of 1,127 N: a margin of 1.06 on the third layer and 1.14 on the second [C4]. A jerked start (1,175 N) or breakout suction on the closed grab (1,245 N) can pass the lowest slip, so the clutch slips for a moment; the pawl holds the drum, nothing releases, and the crew lets the suction ease and hoists again [C5]. The window is narrow: at a ±10 % tolerance the third-layer low end would be 1,019 N, under the steady pull, so the setting is checked on CalRig before each campaign and the lining kept dry inside the guard [C6]. In ordinary hoisting the clutch carries 27.5 N m, 81 % of its nominal slip; a friction face takes that without the fatigue that would have broken the shear pin [C9]. Without an overload device two people heaving 400 N each could put 8,280 N into a snagged line [C8].

The load indicator at the tackle's dead end replaces the shear link. Every part of the line carries the same tension, so it sees the line pull. Its fork draws an M8 rod up through a housing plate and squeezes 14 disc springs 18 x 9.2 x 1.0 in series; at about 0.30 mm a disc at 2.17 kN (catalogue value to confirm) the rod travels about 2.8 mm at the rated 1.47 kN, read against rings set on CalRig in 0.25 kN steps, and an O-ring tell-tale on the rod keeps the peak of each lift [C7]. It does not release: a snag now stops the hoist at the clutch instead of opening the grab.

## D. Crank force and speed (R5)

At the rated grab load on the third layer, one person pushes 110 N on a 250 mm crank and two people 55 N each [D1]. **R5 is met on paper.** Two people at 50 W each hoist the full grab at 5.7 m/min, cranking at about 38 rpm [D2].

## E. Drum and rope (R7)

The drum holds 23 turns a layer: 12.7, 13.9 and 15.1 m in three layers, 41.7 m, against the 38.7 m a 30 m well needs [E1]; the 3:1 tackle takes about 0.4 m more line inside the grab, within the 7 m allowed for reeving. The drum stands 3.0 m from the lead sheave for a fleet angle of 1.91 degrees [E2]. The 8 mm line keeps 10.8 kN through its splice: a factor of 10.2 on the working pull and 7.3 on the clutch's highest slip [E3]. The sheaves, the upper sheave included, are 16.2 rope diameters at the pitch line and the drum 22.0 [E4].

## F. Brake and pawl

The band wraps 270 degrees, so the tight side carries 5.20 times the slack side. A 6 kg weight on a 10.2:1 lever gives 598 N on the slack side and 314 N m of holding torque [F1]. The kit 1.7 model hung the band's link on a pin below the lever pivot on the well side, so the falling weight would have slackened the band; the link now runs on the band's tangent to a pin on an upright arm 60 mm above the pivot, and the model's ratio is about 10.3:1 (SKG-DEC-001 K2). The most the line can put on the drum is 130 N m, at the clutch's limit on the innermost layer (186 N m with the crank pin): a factor of 2.42, and 2.9 at the working pull [F2]. The ratchet tooth carries 1,544 N at the limit, 12 MPa on its face [F3].

## G. Tripod, cradle, drawbar and capstan stability (R7)

At the clutch's limit the lead sheave is pulled 581 N outward and 1,172 N up, and the drawbar pushes the cradle 1,472 N inward. The foot therefore sees the rope along leg A, which is the load case HatchSide was designed for with its own winch [G1]. The 2,470 mm drawbar has an Euler load of 39.4 kN, 27 times the limit [G2]. The capstan weighs 71.1 kg with the long handle and the clutch; because the rope runs 80 mm above the drawbar, it is pitched forward by 118 N m at the limit, against 258 N m from its weight; the stakes hold it from skating [G3]. The line's rated load is now 150 kg, the clutch's highest slip. Under decision O4 PR-007 proofs at 1.25 times the rated load, 188 kg, inside HatchSide's 225 kg proof load, with the clutch locked out for the test; the full grab, 98 kg, is 65 % of the rated load [G4]. 1.25 sits at the low end of the static test coefficients in lifting standards, and which standard applies is still to assess (SKG-REG-001). **R7 is at risk**: the proof basis is now consistent, but the clutch window rests on a ±5 % setting that only CalRig can show (TRL 4).

## H. Scraper (R2, R8)

Two toes cutting 150 N each at 615 mm radius need 184 N m, 142 N for each of two people on the T-bar [H1], over sustained limits of about 100 N for repeated work; Amish's decision O5 of 2026-10-25 sets the crew (see the end of this section). The 42.4 x 2.6 mm pole carries that at 30 MPa and winds up 10 degrees over 10 m [H2]. The scraper head weighs 27.3 kg with its arms on, each pole section 7.2 kg and the T-bar 6.1 kg; hung at 10 m it is 70 kg [H3]. At 25 m, with 12 sections, it is 120 kg, 1,295 N with the allowance, under both the clutch's lowest slip on the innermost layer (1,331 N) and the tripod's rating; sections come off at the doors as it rises, so it is lighter by the time the line reaches the second layer, and 25 m is still the scraper's working limit [H4]. A 10 mm toe blade lapped on each toe plate now reaches 615 mm, 40 mm beyond a 1.0 m ring's outer face (Amish's decision 29B; the first design reached 15 mm); lifted 300 mm on the sleeve the toes fold to 387 mm, inside the 400 mm bore of the smallest ring, with 13 mm to spare [H5]. The arm pivots now stand 60 mm from the pole axis (45 mm in kit 1.7, where the 50 mm arm could not have a closed eye round its 16 mm pin without cutting into the 70 mm hub; SKG-DEC-001 K6); the toe radius and the sleeve travel are unchanged. Against the first design's 590 mm toes the T-bar force rises 4 %; the arms with their blades weigh 5.2 kg [H6]. The fold relies on the sleeve sliding 300 mm down the pole. In the first design a stop collar 40 mm below the sleeve allowed only about 40 mm, so the toes folded only to about 604 mm and the head could not have been lifted out through any ring in the range. Amish's decision 5A (2026-10-04, SKG-DDR-004) replaces the collar with a 340 mm sleeve slotted 13 x 312 mm on each side and a 12 mm cross pin through the pole running in the slots: open, the pin bears on the slot bottoms; lifted, the sleeve slides down until the pin meets the slot tops, a travel of 300 mm, exactly what the fold needs. The sleeve's top stands 15 mm below the hub and the spike stays 110 mm below the foot, so nothing is pushed into the sump floor [H7]. With the whole 25 m string resting on the foot the pin carries 1,295 N in double shear, 6 MPa (a factor of 42), and bears on the pole wall at 21 MPa [H8]. The model checks the folded position: the sleeve slid 300 mm down is held by the pin at its slot tops without touching the pole. **R2 is met by design**, with a longer pair of arms for 1.2 to 1.3 m rings.

Decision O5 asked for a 2.0 m T-bar if the well-head layout allows it, else four people. The 2.0 m bar's ends sweep 1,017 mm and clear the HatchSide legs only below 801 mm above ground, while the doors stand at 390 mm and the T-bar travels 2 m with each pole section, so the layout does not allow it [H10]. Four people turn the scraper, two on each side of the 1.4 m bar: 71 N each if all push at 0.65 m, 84 N each with the inner pair at 0.45 m, both under the about 100 N limit [H9]. The leg check also shows that the 1.4 m bar clears the legs only below 1,267 mm, which the crew works within by fitting pole sections so the T-bar stays low; that is a finding for the build plan, not a change here.

## I. Sinking and tilt (R1, R6)

A 1.0 m ring with a 75 mm wall, 0.5 m high, weighs 304 kg. A string of 8 rings with 6 under water weighs 16.4 kN effective, and eight saddles add 1.61 kN, 10 % [I1]. After 3 m of sinking the rings have 10.8 m2 of outer face in the soil, which at 1 to 3 kPa of skin friction holds 10.8 to 32.5 kN [I2]. The string keeps sinking to 3 m only while skin friction stays below 1.66 kPa [I3]. The toe blades cut a 40 mm ring of soil outside the ring's outer face, so the ring slides down through loosened soil rather than soil packed against it; this aims to keep the friction toward the low end of the estimate, but no calculation here can show by how much. Amish's decision O2 of 2026-10-25 makes a bentonite slurry, pumped down a feed pipe into the 40 mm overcut annulus as the rings sink, part of the method from the first trial; about 0.45 m3 fills the annulus over 3 m of sinking, and the slurry keeps the soil off the rings, as in caisson practice. The limit itself does not change: the string still sinks only while the lubricated friction stays below 1.66 kPa, and no figure for it is claimed here [I6]. **R1 is not met on paper unaided and at risk with the annulus**: the outcome depends on a soil property that only the test pit and the first trial can measure. Removing the soil for 3 m of sinking, out to the toe radius, is about 3.56 m3, 0.28 m3 more than with the first design's toes [I4].

Two dip-tape readings 1,075 mm apart resolve the tilt to ±4.2 mm, 1 in 253; 1 in 80 is 13.4 mm, so the readings can see it clearly [I5]. Whether scraping the high side and moving saddles corrects it is a trial question. **R6 cannot be verified at TRL 3.**

## J. Cycle time and output (R4)

With two people at the cranks a cycle at 10 m takes 22 s to lower, 20 s to take the cranks off and put them back, 10 s to open, 16 s to close, 117 s to hoist and 45 s for the doors and dumping: 3.8 min [J1]. With a third person on the long two-hand handle during the hoist (Amish's decision 27A) the hoist takes 78 s and the cycle 3.19 min, 6 % over the 3 min target [J2]. The output is 399 L an hour of sand in place, so the 3 m of sinking takes about 8.9 h of grabbing [J3]. **R4 is not met on paper, by about 0.2 min:** the hoist is limited by the power the crew can give, not by the gearing, and the 3:1 tackle and its 3.1 kg cost about 4 s a cycle. Amish's decision records that the timed trial settles the remainder.

## K. Masses and cost (R9, R11)

With its arms pinned on, the scraper head weighs 27.3 kg, over the 25 kg limit, so it is carried with its two arms unpinned: 21.9 kg for the head and 5.5 kg for the pair of arms with their pins [K0]. The slotted sleeve and cross pin add 0.9 kg net (the longer sleeve 1.1 kg and the pin 0.06 kg, less the 0.3 kg stop collar), less than the 1.4 kg estimated when the option was posed. The heaviest pieces are then the capstan frame at 22.4 kg, the scraper head at 21.9 kg, a ballast saddle at 20.6 kg, a door at 20.3 kg and the foot cradle at 19.4 kg [K1]. The assembled grab is 52.7 kg, more than two people can lift together (two thirds of their combined 50 kg), so it is assembled on the line under the tripod and moved only by the capstan; it travels in pieces of 25 kg or less (SKG-DEC-001 K3). The longest pieces are the pole sections at 2.0 m [K2]. **R9 is met on paper**, with the arms carried separately. Value-engineering target: USD 4,000. Estimated cost of the constructable design: USD 3,063 (USD 937 under the target) [K3]. The round-2 changes added USD 55: the upper sheave, cheeks, axle and dead-end arm USD 35, the long handle USD 10 and the toe blades USD 10; the round-3 slotted sleeve and cross pin add USD 5. The kit 1.9.1 fixes add USD 420: the CO2 safety monitor USD 399 (SKG-DEC-001 K5) and USD 21 of hardware (set collars USD 8, shear link sleeve and bushes USD 3, corner cleats USD 4, stub axles USD 2, brake eye and posts USD 3, ballast spacers USD 1). Decision O4 adds USD 77, all estimates: the slip clutch USD 60 in place of USD 8 of shear pins, the load indicator USD 35 in place of the USD 18 shear link, the longer keyed and threaded crank shaft USD 5 and the wider chain guard USD 3; decisions O2 and O5 add nothing to the BOM (the bentonite, pipe and drum belong to the trial kit). The kit weighs about 467 kg without ropes, tubs and the tripod [K4].

## M. Results against every requirement

*Table 2. Requirement status from this note [M].*

| ID | Requirement | Value | Target | Status |
| --- | --- | --- | --- | --- |
| R4 | Cycle time at 10 m, three people at the cranks during the hoist | 3.2 min (3.19 min; 3.8 min with two) | 3 min or less | **Not met on paper by about 0.2 min**; the timed trial decides |
| R1 | Water depth reached without de-watering | Sinks while skin friction stays below 1.66 kPa; estimate 1 to 3 kPa unaided; toes cut 40 mm past the ring; bentonite slurry in the annulus (decision O2) | At least 3 m | **Not met on paper unaided; at risk** with the annulus until the test pit shows the friction |
| R3 | Grab load per bite | 21.2 L at 75 % fill with a 3:1 tackle (50 % more closing force); 14.1 L at 50 % | At least 20 L | **At risk**; closing force and fill confirmed in the test-pit trial (STEM S2) |
| R6 | Tilt | Readings resolve 1 in 253; correction by scraping the high side and saddles | 1 in 80 or better | Not verifiable at TRL 3 |
| R5 | Crank force | 55 N each with two people (110 N for one) | 150 N or less | Met on paper |
| R7 | Proof load of lifting parts | Proof 188 kg (1.25 x the 150 kg rated load) inside HatchSide's 225 kg; clutch margin 1.06 on the third layer; line factor 10.2 | 1.25 times the rated load; clutch slips at or below the 150 kg rating | **At risk**; the clutch window rests on a ±5 % setting, shown on CalRig (TRL 4) |
| R9 | Portability | Heaviest piece 22.4 kg with the scraper arms carried unpinned (scraper head 27.3 kg with them on, 21.9 kg without); kit about 467 kg; longest 2.0 m | 25 kg or less; small pickup | Met on paper |
| R11 | Prototype cost | USD 3,063 | Value-engineering target USD 4,000 | Met on paper, within the target |
| R2 | Fits rings of 0.8 to 1.3 m | Grab 468 mm across; scraper folds to 387 mm radius on a 300 mm sleeve travel (slotted sleeve and cross pin); adjustable toes and skids, longer arms | 0.8 to 1.3 m | Met by design |
| R8 | No person in the well | Every task from the surface; doors cover the shaft | 100 % | Met by design |
| R10 | Local build | Steel section and plate, stick welding, drilling; shell skins rolled | Stick welder and hand tools | Met by design |

Counts since the independent review of 2026-10-25: 2 not met on paper (R4 by about 0.2 min, R1), 2 at risk (R3, R7), 1 not verifiable at TRL 3, 3 met on paper, 3 met by design. Amish decided R4, R3 and R1 on 2026-10-03 and the scraper sleeve's travel (R2) on 2026-10-04 (SKG-DEC-001); what is left of R4 and R1 is settled by the timed trial and the first well trial. Amish's decisions of 2026-10-25 (O2, O4, O5) change no count: R1 and R7 stay at risk and not met unaided until the test pit and CalRig.

## N. Detailed model check (kit 1.9.1, 2026-10-24)

The kit 1.9 model (STANDARDS section 24) builds every part of the design from real stock, with every bolt, nut, washer, pin, split pin, collar and weld bead, and checks that no two parts overlap (`cad/fidelity.json`, detail level D3). This note now reads its masses from that model. Building it found details the kit 1.7 model could not show, and each is fixed in the design (SKG-DEC-001): five under Amish's standing instruction of 2026-10-23 because a STEM claim failed (K1 the shear link's pin bent across an open gap, K2 the brake weight slackened the band, K3 the assembled grab was lifted by two people, K4 the full spoil tub had no safe way off the doors, K5 the gas detector did not read carbon dioxide), and sixteen as design for construction (K6 to K21, among them the arm pivots at 60 mm, set collars that hold the crosshead central on its pin, captive bearing bolts, closed eyes on the tie rods and struts, and the clamp bars of the foot cradle on top of the foot plate).

*Table 3. What the detailed model changes in this note.*

| Quantity | Kit 1.7 model | Detailed model | Effect |
| --- | --- | --- | --- |
| Grab | 51.0 kg | 52.5 kg | Working pull 1,056 N; link margin 1.14; R7 still met on paper (2026-10-24; 52.7 kg and 1,058 N with the load indicator of decision O4) |
| Full grab in air | 96.4 kg | 97.9 kg | Crank force 55 N each (R5); hoist 78 s; cycle 3.19 min (R4 still about 0.2 min over) |
| Scraper head, arms on | 26.1 kg | 27.3 kg | Carried with the arms unpinned, 21.9 kg (R9) |
| Heaviest piece | 22.9 kg (capstan frame) | 22.4 kg (capstan frame) | R9 still met |
| Folded toe radius | 389 mm | 387 mm | Pivot at 60 mm (K6); R2 still met by design |
| Kit mass | 457 kg | 466 kg | |
| Parts cost | USD 2,566 | USD 2,986 | CO2 monitor and hardware; within the target (R11) |

No requirement changes status. The detailed model of option A has 519 parts (170 fasteners, 103 weld beads) and weighs 361 kg as modelled at the well head, with four of the eight saddles, the scraper with one pole section, the ropes and the spoil tub; this note's kit mass of 466 kg counts all eight saddles and six pole sections but not the ropes and tubs.

## O. Independent review (2026-10-25)

An independent reviewer, who saw only the STEM check, this note, SKG-PRS-001 and `sizing.py`, tried to refute every verdict (SKG-STM-001, Independent review). The arithmetic reproduced; the assumptions behind it did not all hold, and three statuses change.

- **R1, not met on paper.** The string sinks only below 1.66 kPa of skin friction [I3], and the central estimate of the 1 to 3 kPa range already exceeds that; saturated sand closes onto the ring above the 40 mm overcut, and soil in full contact (about 25 kPa) would need about 270 kN against 18 kN. A lubricated annulus or jacking is a change of method, awaiting Amish (SKG-DEC-001 O2).
- **R3, at risk.** Closing starts with the grab empty (about 449 N submerged, not 657 N), the three sheaves lose 10 to 15 %, and whether 1.06 times the line pull acts on each lip or on both is not settled; the margin over passive drag lies between about 0.9 and 1.8 [B2].
- **R7, at risk (as found before decision O4; see section C for the slip clutch).** The link's highest release, 1,469 N, leaves 3 N to the tripod's 1,472 N rating on a pin diameter no stock wire meets; sheave friction puts the line pull at release near 1,630 N, and breakout suction of about 160 N exceeds the 146 N margin over the working pull. The crank pin carries about 70 % of its release torque in ordinary hoisting, above shear yield, so it fatigues. Twice the rated load (244 kg) exceeds the tripod's proof. The fix changes the rated load, the tripod or the overload device, awaiting Amish (SKG-DEC-001 O4).
- **Other findings, no status change.** The 75 W sustained figure behind D2 has no source, and arm cranking is nearer 30 to 40 W: at 35 W each the cycle is about 3.7 min, so R4 is further from its target than section J shows. The brake [F1] is computed with the weight on the band's slack end; wet, at a friction coefficient of 0.25, it holds about 168 N m, below the 186 N m limit [F2] but above the 103 N m the scraper string needs. The rope's 12 kN breaking strength [E3] should be read from the supplier's datasheet. The scraper T-bar force of 142 N each [H1] exceeds sustained limits of about 100 N (SKG-DEC-001 O5).
- **Decided 2026-10-25.** Amish chose the recommended fixes: a bentonite-lubricated annulus (O2, section I), the slip clutch with a load indicator and proof at 1.25 times the rated load (O4, sections C and G) and four people at the T-bar (O5, section H).
- **Missing checks to add in the next revision:** the clutch's slip torque wet and after standing (TRL 4); breakout suction; friction through the whole tackle; the pole couplings under 184 to 520 N m and the string's buckling when it rests on the foot; tripod overturning and ground bearing under a snag; ring joints during sinking; rope abrasion; and the time for the whole job, not only grabbing.

## Checks against the TRL 1 concept

| Concept (SKG-PRC-001 v0.1) | This note | Action |
| --- | --- | --- |
| Rope-closed grab with a closing line and a holding line | Two lines need two hoists and two people in step | One line; the head's weight opens the shells (SKG-DDR-001); 3:1 tackle (SKG-DDR-003) |
| Hand capstan on one tripod leg | A 70 kg capstan cannot hang on an aluminium leg | Ground capstan with a drawbar to a cradle under the leg A foot (SKG-DDR-002) |
| HatchSide tripod "can be rated" for the loads | The tripod is rated 150 kg; two people at a crank can reach 8.3 kN | Crank slip clutch and dead-end load indicator (R7; SKG-DEC-001 O4, in place of the shear link and crank shear pin) |
| Scraper on a pole or guided frame | A pole is the only way to turn a tool at depth | Centred pole with a centralizer, arms opened by weight |
| Spoil chute and tipping hook | A chute over the mouth must be moved every cycle and cannot cover the shaft | Folding doors and a spoil tub |
