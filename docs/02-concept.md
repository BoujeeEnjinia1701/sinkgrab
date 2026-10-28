---
doc_id: SKG-PRC-001
title: SinkGrab design precis
project: SinkGrab
doc_type: Precis
version: "0.7"
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
  change: TRL 2 precis; single closing line with a gravity-opening grab, overload limits, centred scraper pole, doors and saddles (SKG-DDR-001)
- version: "0.3"
  date: '2026-10-03'
  author: Amish Chadha
  change: TRL 3 numbers from SKG-CAL-001 on the constructable design (SKG-DDR-002); concept media from the model
- version: "0.4"
  date: '2026-10-03'
  author: Amish Chadha
  change: "Amish's decisions 27A, 28B and 29B of 2026-10-03 (SKG-DDR-003): third person at the cranks during the hoist, 3:1 closing tackle, toe blades 40 mm past the ring; numbers from SKG-CAL-001 v0.2"
- version: "0.5"
  date: '2026-10-04'
  author: Amish Chadha
  change: "Amish's round-3 decision 5A of 2026-10-04 (SKG-DDR-004): 340 mm slotted sleeve on a 12 mm cross pin in place of the stop collar, so the scraper's arms fold to pass the ring; cost from SKG-CAL-001 v0.3"
- version: "0.6"
  date: '2026-10-24'
  author: Amish Chadha
  change: "Kit 1.9.1 upgrade: concept options (SKG-OPT-001, the current design is option A, choice awaiting Amish) and STEM check (SKG-STM-001); numbers from SKG-CAL-001 v0.4 on the detailed model; fixes K1 to K21 (SKG-DEC-001): shear link sleeve, brake geometry, grab moved only on the line, spoil tub slid, carbon dioxide monitor, arm pivots at 60 mm and others"
- version: "0.7"
  date: '2026-10-25'
  author: Amish Chadha
  change: "Amish's decisions of 2026-10-25 (SKG-DEC-001 O2 to O5): crank slip clutch and dead-end load indicator in place of the shear pin and shear link; bentonite annulus for sinking; four people at the T-bar; grab 52.7 kg; cost USD 3,063"
---

# SinkGrab design precis

Deepens village wells under water with a rope grab and under-curb scraper, without divers or pumps.

![Figure 1. SinkGrab at the well head](../media/hero.png)

*Figure 1. SinkGrab at the well head: hand capstan, drawbar and lead cradle on the left, well-head frame with its doors closed, the grab at the dump position over a spoil tub, the scraper and ballast saddles on the ground. The HatchSide tripod is shown in grey. Concept, not for fabrication.*

## Summary

SinkGrab lets a village crew dig the last 3 m of a caisson well under water from the surface. A clamshell grab on one rope digs sand out of the flooded rings, an under-curb scraper on a pole cuts the soil from under the bottom ring so the lining sinks, and a hand capstan worked by two people, three during the hoist, does the lifting through the HatchSide tripod. On paper it lifts 21 L a bite with 55 N on each crank handle; the cycle at 10 m is about 3.2 min, 6 % over the 3 min target, which the timed trial decides. The parts cost about USD 2,986 against a value-engineering target of USD 4,000. This design is option A of two concept options; option B, a dart-valve bailer on a jerk line, scores within 10 % of it, so the choice is with Amish (SKG-OPT-001, SKG-DDR-005). Its STEM check is open: an independent review found that, on paper, the rings do not keep sinking without de-watering and that the shear link and crank pin have no release window between the working pull and the tripod's 150 kg rating; on 2026-10-25 Amish chose the fixes for both, a bentonite-lubricated annulus and a crank slip clutch with a load indicator, which the test pit and CalRig confirm at TRL 4 (SKG-STM-001; SKG-DEC-001 O2, O4).

## How it works

The crew stands the HatchSide tripod over the well and replaces its winch with SinkGrab's line: an 8 mm rope runs from the hand capstan on the ground, through a lead sheave in a cradle under the tripod's leg A foot, up beside the leg, over the head sheave and straight down the well. A drawbar joins the capstan to the cradle, so the rope pull is carried inside the kit and the tripod sees the same loads as with its own winch.

The grab is lowered closed on the capstan's band brake. On the bottom the crew slacks the line by about 0.3 m: the grab's head settles under its own weight and pushes the two shells open into the sand. Cranking then pulls the crosshead up toward the head through a 3:1 tackle inside the grab (under the crosshead sheave, over an upper sheave in the head, down to the load indicator on the crosshead, which shows the highest pull of each lift), which closes the shells on a bite and lifts it. A third person joins the cranks for the hoist on a long two-hand handle. At the top the crew closes the well-head doors under the grab, lowers it into a spoil tub standing on them and slacks the line again: the shells open and the sand falls into the tub. The full tub is slid off the doors on a board and tipped at the heap, never lifted. Cranking closes the empty grab and lifts it off; the doors open and the cycle repeats.

When the centre has been dug about 330 mm below the cutting edge, the scraper goes down on 2 m pole sections. Its foot lands in the sump, the pole's weight slides it down through the foot sleeve, and two struts push two arms out until the blades on their toes reach 40 mm beyond the ring's outer face, under the cutting edge, so the ring slides down through loosened soil. Two people turn the pole with a T-bar through the hole in the closed doors, and the toes cut a ring of soil from under the wall, which the grab then removes. Lifting the pole lets the sleeve slide 300 mm down it on a cross pin running in two slots, which folds the arms to 387 mm radius to pass the ring.

Every cycle the crew reads the dip tape at four datum holes on the well-head frame. If one side is ahead, they scrape only on the high side and hang ballast saddles on the high side of the top ring.

## Main components

*Table 1. Components (numbers are bill of materials lines).*

| # | Component | Role |
| --- | --- | --- |
| 1 to 7 | Hand capstan: frame, winding drum with brake drum and ratchet wheel, pawl, crank shaft with a friction slip clutch, removable cranks, chain guard, weighted band brake, stakes | Two-person hoist; holds the load at any depth, limits the line pull |
| 8, 9 | Foot cradle with lead sheave, and drawbar | Turns the line up leg A; carries the pull back to the capstan |
| 10 to 14 | Clamshell grab: head with ballast plates and upper sheave, tie rods, two shells, crosshead with hinge pin, sheave and dead-end arm, load indicator | Digs and lifts 21 L a bite under water on one line |
| 15 to 17 | Under-curb scraper head, 2 m pole sections, T-bar | Cuts the soil from under the ring's cutting edge |
| 18, 19 | Well-head frame with datum brackets, folding doors | Covers the shaft, carries the spoil tub, guides the pole, holds the tilt datum |
| 20 | Ballast saddles (8) | Add weight on the high side of the top ring |
| 21 to 35 | Bought: bearings, chain drive, clutch facings and springs, sheaves, ropes, swivel and shackles, dip tape and plumb line, four-gas detector and carbon dioxide monitor, spoil tubs, barrier kit, fasteners | |

## Numbers from the TRL 3 calculations

*Table 2. First-order numbers (SKG-CAL-001).*

| Quantity | Value | Assumption or basis |
| --- | --- | --- |
| Bite | 21.2 L (28.3 L closed) | 75 % fill in loose saturated sand |
| Closing force | About 700 N at the lips, 1.06 of the line pull | 3:1 tackle; margin over passive drag in loose sand about 0.9 to 1.8 (STEM S2) |
| Grab mass | 52.7 kg; 98 kg full in air | Detailed model; sand 2.0 kg/L, 3 L of water |
| Working line pull | 1,058 N | 1.1 for hand hoisting |
| Crank force at rated load | 55 N each, two people | 4:1 chain, 250 mm cranks, outer layer |
| Hoist speed | 5.7 m/min with two people | 50 W per person |
| Cycle at 10 m | 3.19 min with three at the cranks during the hoist (3.8 min with two) | Lowering 0.5 m/s on the brake |
| Crank slip clutch | Capstan pull limited to 1,127 to 1,472 N (third to first rope layer) | Set on CalRig at about 34 N m, ±5 % (decision O4) |
| Proof load | 188 kg, 1.25 x the 150 kg rated load | Inside the HatchSide proof of 225 kg |
| Tripod | Inside its 150 kg rating and 225 kg proof | HatchSide HTS-CAL-001 |
| Scraper | 142 N each on the T-bar; toe blades 40 mm past the ring; fold to 387 mm radius | 150 N per toe in loose sand |
| Sinking | Continues while skin friction is below 1.66 kPa | 8-ring string, 8 saddles |
| Heaviest piece | 22.4 kg (capstan frame), the scraper arms carried unpinned; the assembled grab moved only on the line | Detailed model masses |
| Parts cost | USD 3,063 | Value-engineering target USD 4,000 |

## Key design choices

All decided under Amish's pre-approvals of 2026-10-03 (SKG-DDR-001 and SKG-DDR-002); the third person at the cranks, the 3:1 tackle and the toe blades by Amish's decisions of 2026-10-03 (SKG-DDR-003); the details of the kit 1.9.1 upgrade under Amish's standing instruction of 2026-10-23 and his design-for-construction instruction of 2026-09-30 (SKG-DEC-001 K1 to K21).

- **One line does everything.** A two-line grab needs a second winch and two people keeping two ropes in step. SinkGrab's grab is lowered closed and opened by its own head weight, so one capstan and one rope dig, lift and dump.
- **The tripod never sees more than its rating.** A friction slip clutch on the crank shaft, set on CalRig, caps the capstan pull at the tripod's 150 kg rating whatever the crew does at the cranks; if the grab snags it slips and the pawl holds the drum, and nothing has to be replaced. A load indicator at the tackle's dead end shows the peak of every lift (Amish's decision O4, 2026-10-25).
- **The rope pull stays inside the kit.** The drawbar between the capstan and the cradle under the leg A foot means nothing is anchored to the ground but the tripod's own feet.
- **The brake is on unless someone holds it off.** A weighted lever applies the band brake when it is let go: its link pulls on an arm above the lever pivot, so the falling weight tightens the band; the cranks come off before any lowering.
- **The scraper is centred and opened by weight.** A pole with a centralizer reaches any depth to 25 m, and its own weight opens the arms only when the foot is on the sump floor.
- **Doors over the shaft.** The well is covered whenever the grab is up; the doors also carry the spoil tub, guide the pole and hold the tilt datum.

## Patent design-arounds

From the preliminary patent, trademark and prior-art screen (not legal advice):

- Rope grab and scraper only; no sand dredger or suction dredging, to stay clear of CN101787703B (China 22MCC Group, active to about 2030).
- A targeted search of Chinese open-caisson excavator patents for under-curb scraper claims is run before public release (decided, SKG-DDR-001, item 14).
- US1750728A (well-tool grab) is expired and a different tool; no constraint.

## Relationship to other lab projects

- **HatchSide** provides the tripod. SinkGrab removes the HatchSide winch, fits a 150 mm sheave grooved for its 8 mm line in the HatchSide head, and clamps its cradle under the leg A foot. Nothing in HatchSide is changed.
- **SiltHaul and SaltDrag** share the hand capstan block: the same frame layout, 4:1 chain and pawl, here with a single drum, a band brake and, since 2026-10-25, a slip clutch in place of the shared block's shear pin hub.
- **CalRig** is the first candidate rig for the proof loads.

## Safety

> **Safety:** SinkGrab is lifting equipment worked over an open well shaft, with a hand-cranked chain drive and loads hanging over the well. The hazards are falls into the shaft, loads or tools falling into the well or onto people, rope or pin failure, fingers and clothing caught in the chain, drum or brake, bad air in the shaft, and rings dropping or tilting suddenly as they are undercut.
>
> - Nobody enters the well while SinkGrab is in use. Any entry for another reason needs a gas test, a harness on a separate line from separate rescue equipment, and a person at the top throughout. SinkGrab's line is never used to lift or lower a person.
> - Test the shaft air with the four-gas detector and the carbon dioxide monitor before work starts each day, after any break and before anyone leans over the shaft; a four-gas detector alone does not read carbon dioxide. Never run a petrol or diesel engine in or near the well mouth.
> - The assembled grab (52.5 kg) and a full spoil tub are never lifted by hand: the grab moves only on the line, the tub is slid off the doors on a board.
> - The doors are closed whenever the grab is above them and at every stop. A barrier stands 2 m outside the tripod feet.
> - Every lifting part is proof-loaded before first use (SKG-BLD-001, section 6). Nobody stands under the grab or beside the line while it is loaded.
> - The slip clutch is set on CalRig and never tightened on site; its locknut carries a paint mark.
> - Four people turn the scraper's T-bar, two on each side.
> - The cranks come off before lowering on the brake; the chain guard stays on.
> - Stop and correct when tilt passes 1 in 160; stop all undercutting at 1 in 80 until it is corrected.
>
> This design is published as an open engineering reference. It is not certified lifting or well-construction equipment.

## Open questions

The open questions of SKG-PRB-001 v0.1 were answered on paper at TRL 2 (SKG-DDR-001). What only trials can answer is listed in SKG-PRB-001, "Questions for the first trials", and in the open rows of SKG-STM-001. One decision awaits Amish in the design decisions register (SKG-DEC-001): the concept choice between options A and B (O1), sent without a pick because they score within 10 %. On 2026-10-25 Amish decided O2 to O5: a bentonite slurry in the overcut annulus is part of the sinking method, PR-012 and PR-013 are accepted, the slip clutch and load indicator replace the shear devices with proof at 1.25 times the rated load, and four people turn the scraper.
