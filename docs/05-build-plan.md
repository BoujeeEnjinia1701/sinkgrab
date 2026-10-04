---
doc_id: SKG-BLD-001
title: SinkGrab prototype build plan
project: SinkGrab
doc_type: Build plan
version: "0.3"
status: Draft
date: '2026-10-04'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: First build plan; design made constructable (SKG-DDR-002)
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: "Amish's decisions 27A, 28B and 29B of 2026-10-03 (SKG-DDR-003): long two-hand crank handle, 3:1 closing tackle with an upper sheave in the head and the shear link on the crosshead, toe blades 40 mm past the ring; scraper arms carried unpinned"
- version: "0.3"
  date: '2026-10-04'
  author: Amish Chadha
  change: "Amish's decision 5A of 2026-10-04 (SKG-DDR-004): 340 mm slotted sleeve and 12 mm cross pin in place of the stop collar, so the scraper's arms fold to pass the ring; sketches SKG-DWG-112 and 113, joints 10 and 14, step 14 and the overview redrawn"
---

# SinkGrab prototype build plan

**Plan, not yet built.** How to build the first proof-of-concept prototype, component by component. Building and testing to it is TRL 4 work. Decisions are kept in the design decisions register ([docs/06-design-decisions.md](06-design-decisions.md)), not here.

## 1. What you are building

![Figure 1. Every component, pulled apart and numbered in build order](05-build-plan/overview.png)

*Figure 1. Every component pulled apart and numbered in build order: made parts 1 to 23, bought parts 24 to 26. Ropes, pins and fasteners are not shown.*

The prototype is a kit for deepening a flooded caisson well from the surface. It has five groups: a hand capstan on the ground with a drawbar to a cradle under the HatchSide tripod's leg A foot; a clamshell grab worked on one rope; an under-curb scraper on a pole in 2 m sections; a well-head frame with two folding doors; and eight ballast saddles. You weld the frames, drum, cradle, grab, scraper and saddles from stock steel tube, plate and bar; have the ratchet wheel, pawl and shell end plates profile-cut and the shell skins rolled; and buy the bearings, chain drive, sheaves, ropes, rigging, dip tape, gas detector and tubs. The parts cost about USD 2,566 from the bill of materials. The work needs a stick or MIG welder, a pillar drill, plate rolls (or a fabricator who has them) and hand tools. The HatchSide tripod is built to its own plan.

> **Safety:** SinkGrab is lifting equipment worked over an open well shaft, with a hand-cranked chain drive. A failed pin, rope or shackle can drop the grab; the chain, sprockets, drum, brake and cranks can trap fingers and clothing; the shaft can hold bad air; a person can fall in. The building work involves welding, grinding, rolling plate and lifting parts up to 25 kg. Nobody turns the cranks with the chain guard off, nobody enters the well, and nothing is lifted over the well before the safety stops in section 6 allow it. Load tests are TRL 4 work.

## 2. What changed to make it buildable

The concept showed what SinkGrab does; some of its parts could not be made or fitted as drawn. Each change keeps what SinkGrab does and is recorded in decision record SKG-DDR-002.

*Table 1. Changes from the concept.*

| Component | The concept had | The buildable design has | Why |
| --- | --- | --- | --- |
| Hoist | A capstan clamped on one tripod leg | A ground capstan 3 m from a lead sheave in a cradle under the leg A foot, joined by a drawbar (Figures 15, 13) | The leg cannot carry it; the rope pull stays inside the kit |
| Grab lines | A closing line and a holding line | One line through a 3:1 tackle (over a sheave in the crosshead and one in the head); the head's weight opens the shells (Figures 19, 21) | One hoist, one rope; the 3:1 tackle closes the shells 50 % harder |
| Overload | None | A shear link at the tackle's dead end on the crosshead (Figure 21) and a shear pin in the crank hub (Figure 6) | The tripod is rated 150 kg |
| Lowering | Not defined | Cranks off, lowering on a band brake held on by a weight (Figure 8) | The brake sets if the operator lets go |
| Scraper | A scraper on a pole or a guided frame | Centred pole with a centralizer; two arms opened by struts when the pole's weight rests on the foot (Figures 24, 25) | Turns at depth; folds to pass the bore |
| Spoil chute | A chute and tipping hook | Well-head frame with folding doors; the grab dumps into a tub on the closed doors (Figures 29, 30) | The shaft is covered whenever the grab is up |
| Ballast frame | A frame on the top ring | U-saddles astride the ring wall on their own lines (Figure 32) | Placed and moved from the surface |

## 3. Making the components

Make and check each component before the step that needs it. Sizes are in millimetres. On the capstan, "+X" is the side with the brake and ratchet and "-X" the side with the chain; "front" faces the well. Workshop tolerance is 1 mm unless a step says otherwise. Weld 2 mm tube with MIG or 2.5 mm electrodes; fillets are 3 mm on tube and 5 mm on plate unless stated. Mark every part with its name in paint marker.

### 3.1 Capstan frame

![Figure 2. Making sketch of the capstan frame](../cad/drawings/SKG-DWG-101.png)

*Figure 2. Capstan frame making sketch (SKG-DWG-101).*

**What it is and what it is made from.** The welded frame that carries the drum, the crank shaft, the pawl and the brake. 40 x 40 x 2 mm steel square tube, about 7.4 m; 8 mm plate; 33.7 x 3.2 mm tube for the stake tubes; 12 mm bar for the pawl pin.

**How to make it.**

1. Cut two base rails 660 long, two posts 765 long, four pad posts 89 long, the cross rails, top tie and brake anchor bar 390 long. Cut the braces to fit in step 4.
2. On each base rail, weld a post upright 150 mm behind the drum axis line and two pad posts 60 mm either side of it.
3. Weld a bearing pad (180 x 50 x 8) on the two pad posts, its top 169 mm above the floor, and a top plate (150 x 50 x 8) on the post, its top 805 mm up.
4. Fit the front brace from the front of the rail to the post near 640 mm up and the rear brace from the rear of the rail to the post near 560 mm up; weld.
5. Stand the two side frames 430 mm apart, centre to centre, on a flat floor. Weld in the front and rear cross rails, the top tie between the posts 700 mm up, and the brake anchor bar 125 mm behind the drum axis.
6. Weld the two drawbar clevis plates (8 mm, 70 x 70, 21 mm hole 40 mm up) to the front cross rail, 32 mm apart and centred.
7. Weld the pawl bracket under the +X front brace with its 12 mm pin pointing inward; the brake anchor post (8 mm plate) on the anchor bar; the lever plate on the outside of the +X rail 240 mm behind the axis.
8. Weld a stake tube (33.7 x 80) upright on the outside of each rail, 200 mm either side of the drum axis, and the two guard tabs on the -X post at 560 and 780 mm up.
9. Drill the pads for two M14 bolts and the top plates for two M12 bolts to the bearings bought.

**How it fits the parts next to it.** The drum bearings bolt on the pads (Figure 4), the crank bearings on the top plates, the pawl hangs on its pin (Figure 7), the brake anchors to the post (Figure 8) and the drawbar pins into the clevis (Figure 15).

**Check before moving on.** Diagonals of the base within 3 mm; both pads level and in line within 1 mm; both top plates likewise; about 23 kg.

### 3.2 Winding drum

![Figure 3. Making sketch of the winding drum](../cad/drawings/SKG-DWG-102.png)

*Figure 3. Winding drum making sketch (SKG-DWG-102).*

**What it is and what it is made from.** The drum that winds the line, with its brake drum, ratchet wheel and big sprocket on one shaft. 168.3 x 4.5 mm pipe; 6 mm plate; a 250 x 6 mm ring 50 wide; 8 mm plate for the ratchet; 30 mm bright steel bar (S355 or EN8); the bought 48-tooth sprocket.

**How to make it.**

1. Cut the core 200 mm long with square ends. Cut two flanges 260 mm across from 6 mm plate with a 30 mm centre hole and six 36 mm lightening holes on a 100 mm circle.
2. Push the 549 mm shaft through both flanges; set the flanges on the core ends, the shaft central within 0.5 mm; weld in short stitches, turning as you go.
3. Weld the brake drum web (6 mm, with six 56 mm holes) and ring on the shaft 6 mm outboard of the +X flange, with a spacer ring between.
4. Weld the ratchet wheel (20 teeth, 200 mm outside, 168 mm at the roots) 8 mm outboard of the brake drum, its teeth as in Figure 7.
5. At the -X end, weld the big sprocket on a short hub, outboard of where the bearing will sit.
6. Bolt the rope clamp with its U-bolt to the -X flange.

**How it fits the parts next to it.** The shaft runs in the two drum bearings (Figure 4); the band brake wraps the brake drum (Figure 8); the pawl drops into the ratchet (Figure 7). The line is wound on from below.

**Check before moving on.** Turned in V-blocks, the flanges run true within 1.5 mm and the brake drum within 0.5 mm; about 18 kg.

### 3.3 Drum bearings (bought)

![Figure 4. Joint 1: drum bearing on its pad](05-build-plan/joint-01.png)

*Figure 4. Joint 1. Each UCP206 bearing bolts to its pad with two M14 bolts; its set screws lock the shaft.*

Buy two UCP206 pillow block bearings with 30 mm bores. Nothing to make.

### 3.4 Crank shaft, sprocket hub and cranks

![Figure 5. Making sketch of the crank shaft, hub and cranks](../cad/drawings/SKG-DWG-103.png)

*Figure 5. Crank shaft, hub and cranks making sketch (SKG-DWG-103).*

**What it is and what it is made from.** The shaft the people turn, and the hub that drives the chain through the shear pin. 25 mm bright steel bar; 36 mm tube for the hub; the bought 12-tooth sprocket; 12 mm plate; 32 mm tube; M12 bolts; two ball-lock pins. One crank has a long handle so a third person can join the hoist.

**How to make it.**

1. Cut the shaft 633 mm long; mill or file a 20 mm square, 40 mm long, on each end for the cranks.
2. Cut the hub 26 mm long from 36 mm tube bored to slide on the shaft; weld the 12-tooth sprocket to it.
3. Slide the hub on the -X end, clamp, and drill a 3 mm hole through hub and shaft together, square to the shaft.
4. Make two crank arms 250 mm between centres, each with a square socket to fit the shaft end and a hole for its ball-lock pin. On the -X crank fit a 32 x 120 handle on an M12 bolt; on the +X crank fit a 32 x 240 handle on a longer M12 bolt, long enough for two people's hands side by side.

**How it fits the parts next to it.**

![Figure 6. Joint 2: shear pin through the sprocket hub](05-build-plan/joint-02.png)

*Figure 6. Joint 2. The hub turns freely on the shaft; only the 3 mm pin passes the drive. If the line pull passes about 1.5 to 2.1 kN, the pin shears, the cranks spin free and the pawl holds the drum.*

**Check before moving on.** With the pin out the hub turns freely by hand; with it in, it does not move. Each crank slides on and locks with its pin.

### 3.5 Pawl

The pawl is drawn on the brake's making sketch (Figure 9). Cut it from 8 mm plate: a 12 mm pivot hole and a nose with a 3 mm radius that sits 94 mm from the drum axis. Deburr; keep the nose edge square.

![Figure 7. Joint 3: ratchet wheel and pawl](05-build-plan/joint-03.png)

*Figure 7. Joint 3, seen from the +X side. The pawl drops into the ratchet by its own weight and stops the drum turning to pay out line. To lower, it is flipped up onto the bracket.*

**Check before moving on.** The pawl falls into every tooth gap as the drum is turned slowly by hand.

### 3.6 Band brake and weighted lever

![Figure 8. Joint 4: weighted band brake](05-build-plan/joint-04.png)

*Figure 8. Joint 4. The lined band wraps 270 degrees round the brake drum. Its anchor end is pinned to the post; its live end pulls on the lever 60 mm from the pivot. The 6 kg weight at the lever's end holds the brake on; lifting the lever about 30 mm frees the drum.*

![Figure 9. Making sketch of the pawl and band brake](../cad/drawings/SKG-DWG-105.png)

*Figure 9. Pawl and band brake with weighted lever making sketch (SKG-DWG-105).*

**What it is and what it is made from.** A brake that is on unless someone holds it off. 40 x 3 mm spring steel strip about 1.25 m with bonded lining; 25 x 6 mm flat for the link; 40 x 12 mm flat 650 mm long for the lever; a 6 kg steel block; 12 mm pins.

**How to make it.**

1. Bond or rivet the lining to the band; form the band round a 250 mm former.
2. Weld an eye at each end of the band; pin the anchor end to the anchor post so the band leaves the drum toward the back.
3. Make the link 25 x 6 with 12.5 mm holes; pin it between the band's live end and the lever, 60 mm from the lever pivot.
4. Pin the lever to the lever plate; weld or bolt the 6 kg block to its far end.

**Check before moving on.** With the weight on, two people cannot turn the drum by the flanges; lifting the lever 30 mm frees it.

### 3.7 Chain guard

![Figure 10. Making sketch of the chain guard](../cad/drawings/SKG-DWG-104.png)

*Figure 10. Chain guard making sketch (SKG-DWG-104).*

**What it is and what it is made from.** A closed box round the chain and both sprockets. 1.5 mm steel sheet.

**How to make it.** Cut both side sheets to the outline (22 mm clear of the big sprocket, 30 mm of the small one), cut the shaft holes, bend a 46 mm band round the outline and stitch weld or rivet it to both sheets. Drill for two M6 screws to the frame tabs.

**Check before moving on.** With the guard on, a finger cannot reach the chain or sprockets.

### 3.8 Ground stakes (make 4)

![Figure 11. Making sketch of a ground stake](../cad/drawings/SKG-DWG-106.png)

*Figure 11. Ground stake making sketch (SKG-DWG-106).*

25 mm round bar 500 mm long, ground to a point, with a 34 mm washer welded on top. Each is driven through a stake tube until its head rests on it. The stakes stop the capstan skating; the drawbar carries the pull. Check: straight within 3 mm.

### 3.9 Foot cradle and lead sheave

![Figure 12. Making sketch of the foot cradle](../cad/drawings/SKG-DWG-107.png)

*Figure 12. Foot cradle making sketch (SKG-DWG-107).*

**What it is and what it is made from.** A plate the tripod's leg A foot stands in, carrying the lead sheave and the drawbar clevis. 10 mm plate; 4 mm flat; 10 mm bar for the clamp bars; 8 mm plate; four M12 bolts; the bought sheave on a 20 mm axle.

**How to make it.**

1. Cut the base 320 x 330 with a 120 mm wide tongue running out to the sheave and the clevis.
2. Weld a 30 mm rim of 4 mm flat on three sides of the foot position, open toward the well, 2 mm clear of the foot plate.
3. Drill four 13 mm holes for the clamp bolts, 220 mm apart across and 140 mm apart along.
4. Weld the two sheave cheeks (8 mm, 30 mm apart) on the tongue, their 20.5 mm axle holes 185 mm up and 260 mm beyond the foot centre.
5. Weld the two drawbar clevis plates at the end of the tongue, 21 mm holes 40 mm up, 160 mm beyond the sheave.

**How it fits the parts next to it.**

![Figure 13. Joint 6: HatchSide foot in the cradle](05-build-plan/joint-06.png)

*Figure 13. Joint 6. The HatchSide foot sits inside the rim; two clamp bars across it pull it down with four M12 bolts. The line comes in under the sheave from the capstan and leaves upward beside leg A.*

**Check before moving on.** The foot drops in and sits flat; the sheave turns freely between the cheeks.

### 3.10 Drawbar

![Figure 14. Making sketch of the drawbar](../cad/drawings/SKG-DWG-108.png)

*Figure 14. Drawbar making sketch (SKG-DWG-108).*

**What it is and what it is made from.** The strut that carries the line's pull from the capstan back to the cradle. 48.3 x 3.2 mm tube in two halves; a 41 mm bar spigot 200 long; 12 mm plate tongues; two 20 mm clevis pins with R-clips.

**How to make it.** Cut both halves so the pins are 2,470 mm apart when joined. Weld the spigot 100 mm into one half. Slot a 12 mm tongue with a 21 mm hole into each outer end and weld.

**How it fits the parts next to it.**

![Figure 15. Joint 5: drawbar on the capstan](05-build-plan/joint-05.png)

*Figure 15. Joint 5. The tongue sits between the clevis plates on the capstan's front rail; the 20 mm pin carries the pull. The other end is the same at the cradle.*

**Check before moving on.** Joined, it is straight within 3 mm; both pins slide in by hand.

### 3.11 Grab shells (make 2)

![Figure 16. Making sketch of a grab shell](../cad/drawings/SKG-DWG-109.png)

*Figure 16. Grab shell making sketch (SKG-DWG-109).*

**What it is and what it is made from.** The two scoops that bite the sand. 4 mm plate rolled to a 230 mm inside radius; 6 mm plate end plates (profile cut); 4 mm top cover; a 10 x 50 mm wear-resistant lip.

**How to make it.**

1. Roll the skin to a quarter circle of 230 mm inside radius, 340 mm wide for shell A and 353 mm for shell B.
2. Profile-cut the four end plates: a quarter disc of 234 mm radius with a 70 mm boss round the hinge corner and a lug at the outer top corner; a 30.5 mm hinge hole and a 20.5 mm tie rod hole.
3. Tack the end plates to the skin, shell B's end plates 13 mm further apart than shell A's so they pass outside A's at the hinge.
4. Weld the 4 mm top cover from 50 mm off the hinge out to the skin.
5. Weld the lip inside the bottom edge and grind its face square to the open side.

**How it fits the parts next to it.** Both shells hang on one 30 mm pin through their end plates and the crosshead (Figure 19); each is closed by two tie rods from its lugs (Figure 20).

**Check before moving on.** Pinned together, the lips meet within 2 mm along their length.

### 3.12 Grab head with ballast plates

![Figure 17. Making sketch of the grab head](../cad/drawings/SKG-DWG-110.png)

*Figure 17. Grab head with ballast plates making sketch (SKG-DWG-110).*

**What it is and what it is made from.** The heavy top block that holds the tie rods, guides the line and carries the upper sheave of the tackle. 6 mm plate; 25 mm bright bar; 30 mm tube; 12 mm plate; two 16 mm ballast plates; M10 bolts; the bought upper sheave on a 20 mm axle.

**How to make it.**

1. Weld a box 300 x 120 x 40 from 6 mm plate.
2. Pass the two 25 mm head pins (418 long) through the box ends, 240 mm apart, and weld; drill each end for an R-clip.
3. Weld the rope guide tube (30 mm outside, 14 mm bore) through the box 65 mm from the centre; flare its bottom end.
4. Weld two 6 mm cheek plates under the box, 65 mm the other side of the centre and 30 mm apart, hanging down to a 20.5 mm axle hole 85 mm below the box and 65 mm in from the box's long side. Weld the recovery-line eye on top.
5. Fit the upper sheave between the cheeks on its 20 mm axle with R-clips. It stands across the box, turned 90 degrees to the crosshead sheave, so the line comes up into it on the centre line and goes down again 130 mm to one side.
6. Drill both faces and the ballast plates for M10 bolts.

**Check before moving on.** About 13.5 kg with both plates and the cheeks, and 2.3 kg more with the sheave and axle; the 8 mm line runs freely through the guide and over the upper sheave.

### 3.13 Crosshead, tie rods and shear link

![Figure 18. Making sketch of the crosshead, tie rods and shear link](../cad/drawings/SKG-DWG-111.png)

*Figure 18. Crosshead, tie rods and shear link making sketch (SKG-DWG-111).*

**What it is and what it is made from.** The crosshead carries the hinge pin, the lower sheave of the tackle and the dead end of the line; the four tie rods join the head to the shells; the shear link is the weak point of the tackle. 10 mm plate; 30 mm bar; 30 x 10 mm flat; 6 mm plate; 16 mm pin; calibrated link pins of about 1.9 mm.

**How to make it.**

1. Cut the two crosshead plates with a 30.5 mm hinge hole and a 20.5 mm axle hole 120 mm above it.
2. On one plate weld the dead end: a 10 mm stub plate running out sideways from the plate, a 10 mm arm plate 45 mm deep along the hinge direction to 150 mm from the centre, and a 10 mm lug on its end with a 16.5 mm hole 197 mm above the hinge and 130 mm from the centre. Keep the arm above 140 mm so the open shells clear it.
3. Cut the hinge pin 404 mm long from 30 mm bar; drill both ends for R-clips.
4. Cut four tie rods 30 x 10 with 20.5 and 25.5 mm holes 420 mm apart.
5. Cut the two link plates 87 x 30 from 6 mm plate with a 16.5 mm hole at the bottom and a 6.5 mm hole 62 mm above it; the link pin goes through a bush in the small hole so the pin can be swapped.

**How it fits the parts next to it.**

![Figure 19. Joint 7: grab hinge and crosshead](05-build-plan/joint-07.png)

*Figure 19. Joint 7. One 30 mm pin carries shell A's end plates, shell B's end plates outside them, and the two crosshead plates between. The sheave (not shown) turns on its own axle 120 mm above the pin.*

![Figure 20. Joint 8: tie rod on the shell lug](05-build-plan/joint-08.png)

*Figure 20. Joint 8. Each tie rod is pinned to its shell's lug with a 20 mm pin and R-clip; shell A's rods run outside A's end plates, shell B's outside B's.*

![Figure 21. Joint 9: upper sheave and shear link](05-build-plan/joint-09.png)

*Figure 21. Joint 9. The line comes up from the crosshead sheave, over the upper sheave in the head and down to the shear link on the crosshead's dead-end lug; its thimble hangs on the small calibrated pin. Three parts of line between head and crosshead close the shells 50 % harder than two. If the grab snags and the line pulls more than about 1.2 to 1.5 kN, the pin shears, the line runs out over both sheaves and the grab opens.*

**Check before moving on.** The crosshead turns on the pin; the rods swing freely; a test link pin from the same coil has been broken at the right load (see the register).

### 3.14 Scraper head

![Figure 22. Making sketch of the scraper head](../cad/drawings/SKG-DWG-112.png)

*Figure 22. Scraper head (pole, hub and centralizer) making sketch (SKG-DWG-112).*

**What it is and what it is made from.** The bottom pole section that carries the arms and centres itself in the ring. 42.4 x 2.6 mm tube; 50 mm bar for the spike; 70 mm tube for the hub; 8 mm plate lugs; 40 x 8 flat; 10 mm skid plates.

**How to make it.**

1. Cut the pole 1,420 mm and weld a 50 mm solid spike in the bottom end. Drill a 12.5 mm cross hole through the pole 140 mm above the tip, square to the arm lugs, for the sleeve's cross pin. There is no stop collar: the pin stops the sleeve.
2. Weld the hub 80 mm above the toe line, with two pairs of 8 mm lugs either side, 16.5 mm holes 45 mm off the pole axis.
3. Weld the centralizer collar 700 mm up with three arms 120 degrees apart; drill each arm for the skids at 340, 440 and 590 mm radius; bolt the skids at 440 for a 1.0 m ring.
4. Drill a 13 mm cross hole 75 mm below the top end for the next section's bolt.

**Check before moving on.** Straight within 3 mm; the skids lie on an 880 mm circle.

### 3.15 Scraper arms, struts and sleeve

![Figure 23. Making sketch of the scraper arms, struts and sleeve](../cad/drawings/SKG-DWG-113.png)

*Figure 23. Scraper arms, struts and sleeve making sketch (SKG-DWG-113).*

**What it is and what it is made from.** Two arms whose toes cut under the ring and 40 mm beyond its outer face, opened by the pole's weight, and the slotted sleeve that lets them fold to pass the ring. 50 x 10 mm flat; 10 mm wear-resistant plate for the toes and toe blades; 30 x 6 mm flat for the struts; 54 mm tube and a 250 mm, 10 mm disc for the sleeve and foot; 12 mm bright bar for the cross pin; 12 and 16 mm pins.

**How to make it.**

1. Cut two arms 540 mm from pivot hole to toe; weld a toe plate 100 x 80 x 10 square across each end.
2. Cut two toe blades 100 x 35 from 10 mm wear-resistant plate. Weld one under the end of each arm at the cutting level, lapped 10 mm on the arm and toe plate and standing 25 mm out beyond the toe plate, so the blade's edge is 615 mm from the pole axis.
3. Drill each arm for its 16 mm pivot pin and, 339 mm out, a 12.5 mm strut pin.
4. Cut four struts 30 x 6 with 12.5 mm holes 398 mm apart.
5. Cut the sleeve 340 mm long from 54 mm tube. Cut a slot 13 mm wide and 312 mm long through each side, starting 14 mm above the bottom end, with the top of each slot rounded; the two slots face each other. Weld the foot disc under the sleeve, and a 10 mm strut lug on each of the other two sides, 100 mm above the bottom, with a 12.5 mm hole.
6. Cut the cross pin 70 mm long from 12 mm bright bar and drill a small hole near one end for an R-clip.
7. For 1.2 to 1.3 m rings, make a second pair of arms 660 mm long, with the same blades.

**How it fits the parts next to it.**

![Figure 24. Joint 10: arm, strut and sliding sleeve](05-build-plan/joint-10.png)

*Figure 24. Joint 10. The sleeve slides on the pole, held by a cross pin through the pole that runs in a slot on each side of the sleeve. When the foot rests on the sump floor and the line is slacked, the pole slides down through the sleeve until the pin reaches the bottom of the slots, and the struts push the arms out.*

![Figure 25. Joint 14: toe under the cutting edge](05-build-plan/joint-14.png)

*Figure 25. Joint 14, the ring cut away. Open, the toe blade reaches 40 mm past the ring's outer face, just below its cutting edge, so the ring slides down through loosened soil; the skid bears on the bore above. Lifting the pole lets the sleeve slide 300 mm down it until the pin reaches the top of the slots; that folds the blades to 389 mm radius so the head passes the ring.*

**Check before moving on.** The arms open and fold freely by hand by sliding the sleeve the full length of its slots; folded, the blades sit inside an 800 mm circle. The head weighs about 26.1 kg with the arms on, so unpin the two arms for carrying: about 20.1 kg for the head and 6.0 kg for the arms.

### 3.16 Pole sections and T-bar

![Figure 26. Making sketch of the pole section and T-bar](../cad/drawings/SKG-DWG-114.png)

*Figure 26. Pole section and T-bar making sketch (SKG-DWG-114).*

**What it is and what it is made from.** 2 m extensions and the handle. 42.4 x 2.6 mm tube; 36 mm bar; 48.3 x 2.7 mm tube; 33.7 x 3.2 mm tube; 12 mm plate; M12 bolts.

**How to make it.** Cut each section 2,000 mm; weld a 36 mm spigot 250 mm long into the bottom end, 150 mm out; drill 13 mm cross holes 75 mm from each end. For the T-bar, weld the 1,400 mm handle across a 200 mm socket of 48.3 tube and the eye plate on top.

![Figure 27. Joint 11: pole section joint](05-build-plan/joint-11.png)

*Figure 27. Joint 11, cut open. The spigot slides into the tube below; one M12 bolt through both carries the weight and the turning.*

**Check before moving on.** Two sections bolted together are straight within 5 mm over 4 m.

### 3.17 Well-head frame

![Figure 28. Making sketch of the well-head frame](../cad/drawings/SKG-DWG-115.png)

*Figure 28. Well-head frame making sketch (SKG-DWG-115).*

**What it is and what it is made from.** A square frame that sits on the well collar and carries the doors and the tilt datum. 50 x 50 x 5 mm angle; 6 mm plate; 24 mm tube for the hinge knuckles; M12 bolts.

**How to make it.**

1. Cut and weld the angle into two L-shaped halves that bolt at two corners into a frame with a 1,360 mm square opening, horizontal legs out and down onto the collar, vertical legs up at the inner edge.
2. Weld four datum brackets (6 mm plate) under the frame at the middle of each side, each with a 10 mm hole 537 mm from the centre, over the caisson ring wall.
3. Weld two hinge knuckles on each of the two hinged sides, 1,000 mm apart.

**Check before moving on.** It sits on the collar without rocking; the four datum holes lie on a square within 3 mm.

### 3.18 Folding doors (make 2)

![Figure 29. Making sketch of a folding door](../cad/drawings/SKG-DWG-116.png)

*Figure 29. Folding door making sketch (SKG-DWG-116).*

**What it is and what it is made from.** Two mesh doors that close over the shaft. 40 x 40 x 4 mm angle; expanded steel mesh; 6 mm plate doubler; 16 mm bar.

**How to make it.** Weld a frame 1,364 x 680 from angle with the mesh inside. Cut a 32 mm radius notch at the middle of the meeting edge and weld a 6 mm doubler round it. Weld two hinge pins on the outer edge to match the knuckles.

![Figure 30. Joint 12: door hinge and pole notch](05-build-plan/joint-12.png)

*Figure 30. Joint 12. Each door hinges on two pins in the frame knuckles at its outer edge and rests on the frame's vertical legs. Closed, the two notches make a 64 mm hole for the pole.*

**Check before moving on.** Both doors close flat and meet within 5 mm; each is about 18 kg.

### 3.19 Ballast saddles (make 8)

![Figure 31. Making sketch of a ballast saddle](../cad/drawings/SKG-DWG-117.png)

*Figure 31. Ballast saddle making sketch (SKG-DWG-117).*

25 and 20 mm plate offcuts welded into a U: inner leg 200 x 300 x 25, outer leg 200 x 150 x 20, bridge 25 mm, a 95 mm slot, and a lifting eye with a 20 mm hole for its own 6 mm line. About 20.6 kg each.

![Figure 32. Joint 13: saddle astride the top ring](05-build-plan/joint-13.png)

*Figure 32. Joint 13. The saddle drops over the ring wall: the inner leg inside the ring, the outer leg in the gap to the lining.*

**Check before moving on.** It drops over a 75 mm board without binding.

### 3.20 Bought components

Buy to specification, not brand. Line numbers are those of the bill of materials.

- **Bearings (lines 21 and 22).** Two UCP206 (30 mm) and two UCP205 (25 mm) pillow block ball bearings.
- **Sprockets and chain (line 23).** ISO 08B-1: a 12-tooth sprocket bored to suit the hub and a 48-tooth plate wheel bored 30 mm; 1.6 m of chain, breaking load at least 17.8 kN, with one connecting link.
- **Crank shear pins (line 24).** 3 mm S235 mild steel bar cut 40 mm long, with split pins; never hardened steel.
- **Sheaves (line 25).** Four sheaves 150 mm outside, 130 mm at the rope, grooved for 8 mm fibre rope, 28 mm wide, 20 mm bore with a ball bearing, rated at least 500 kg: one for the cradle, one for the crosshead, one for the grab head (the 3:1 tackle), one to fit in the HatchSide head in place of its wire-rope sheave.
- **Ropes (lines 26 to 28).** 45 m of 8 mm polyester double braid (at least 12 kN) with a thimble eye splice for the closing line; 40 m of 8 mm for the recovery line; eight 32 m lengths of 6 mm braid (at least 5 kN) for the saddles.
- **Rigging (line 29).** A ball-bearing swivel and bow shackles, WLL 500 kg, and one WLL 1,000 kg shackle for the T-bar eye.
- **Dip tape and plumb line (line 30), gas detector (line 31), spoil tubs (line 32), barrier kit and briefing card (line 33), fasteners and consumables (line 34).**

## 4. Putting it together

In each picture the parts already fitted are grey and the part being fitted is in colour, with an arrow showing the way it goes in. Steps 1 to 15 are done in the workshop; steps 16 to 20 at the well. Two people throughout.

### Step 1: drum bearings onto the drum shaft

![Step 1](05-build-plan/step-01.png)

Slide a UCP206 onto each end of the drum shaft, grease nipples up, set screws loose.

### Step 2: lower the drum onto the pads

![Step 2](05-build-plan/step-02.png)

Two people lower the drum and bearings onto the pads, sprocket to the -X side. Bolt each bearing with two M14 bolts, centre the drum and tighten the set screws.

### Step 3: crank shaft, hub and bearings onto the top plates

![Step 3](05-build-plan/step-03.png)

Slide the crank bearings onto the crank shaft with the sprocket hub on the -X end. Bolt the bearings to the top plates with M12 bolts, the small sprocket in line with the big one within 1 mm.

### Step 4: fit the chain

![Step 4](05-build-plan/step-04.png)

Lay the chain over both sprockets and join it with the connecting link, the clip's closed end leading when hoisting. It should lift about 10 mm at mid-span.

### Step 5: fit the shear pin

![Step 5](05-build-plan/step-05.png)

Push a 3 mm shear pin through the hub and shaft and fit its split pin. Hang spares on the frame.

### Step 6: chain guard on

![Step 6](05-build-plan/step-06.png)

Fit the guard and fix it with two M6 screws. From now on the cranks are never turned with it off.

### Step 7: pawl on its pin

![Step 7](05-build-plan/step-07.png)

Hang the pawl on its pin with a washer and R-clip; check it drops into the ratchet.

### Step 8: band brake and weighted lever

![Step 8](05-build-plan/step-08.png)

Wrap the band round the brake drum, pin the anchor end, then the link and lever; fit the weight. Check the drum is held.

### Step 9: cranks on

![Step 9](05-build-plan/step-09.png)

Slide each crank onto its square, 180 degrees apart, and push in the ball-lock pin. The crank with the long two-hand handle goes on the +X end, away from the chain guard; during the hoist two people work it and one the other crank.

### Step 10: crosshead and hinge pin into the shells

![Step 10](05-build-plan/step-10.png)

Lay the shells lip to lip. Fit the sheave between the crosshead plates on its axle, set the crosshead between the shells and push the hinge pin through all end plates and both crosshead plates; R-clips.

### Step 11: tie rods onto the shell lugs

![Step 11](05-build-plan/step-11.png)

Pin two tie rods to each shell's lugs, outside that shell's end plates.

### Step 12: head onto the tie rods

![Step 12](05-build-plan/step-12.png)

Lift the head over the rods and pass the head pins through their upper holes; R-clips. The grab now opens when the head is pushed down and closes when the crosshead is lifted toward it.

### Step 13: ballast plates, upper sheave and shear link

![Step 13](05-build-plan/step-13.png)

Bolt both ballast plates on with M10 bolts. Fit the upper sheave between the head's cheeks on its axle; R-clips. Pin the shear link to the crosshead's dead-end lug and fit a calibrated link pin. The assembled grab weighs about 51 kg; two people lift it.

### Step 14: arms, struts and sleeve onto the pole

![Step 14](05-build-plan/step-14.png)

Slide the sleeve onto the pole from the spike end, slots facing the cross hole. Push the cross pin through one slot, the pole and the other slot, and fit its R-clip. Pin the arms to the hub lugs and the struts between the arms and the sleeve lugs.

### Step 15: pole section and T-bar

![Step 15](05-build-plan/step-15.png)

Push a section's spigot into the scraper head and bolt it; fit the T-bar socket over the top spigot. At the well, sections are added one at a time at the doors.

### Step 16: well-head frame on the collar

![Step 16](05-build-plan/step-16.png)

Clear and level the collar top. Set the two frame halves on it, bolt the corners and turn the frame so its datum holes lie over the caisson ring wall.

### Step 17: hang the doors

![Step 17](05-build-plan/step-17.png)

Drop each door's hinge pins into the knuckles and close both. The doors stay closed whenever nothing is passing through.

### Step 18: cradle under the leg A foot

![Step 18](05-build-plan/step-18.png)

With the HatchSide tripod standing over the well and its winch removed, lift the leg A foot a few centimetres, slide the cradle under it with the sheave pointing away from the well, lower the foot inside the rim and bolt the two clamp bars down.

### Step 19: capstan and drawbar

![Step 19](05-build-plan/step-19.png)

Carry the capstan frame and the drum separately and reassemble them (steps 2, 4 to 9). Set the capstan in line with leg A, 3 m beyond the sheave. Join the drawbar halves and pin it to both clevises; drive the four stakes.

### Step 20: reeve the line and hang the grab

![Step 20](05-build-plan/step-20.png)

Fit the 8 mm head sheave in the HatchSide head. Clamp the line on the drum, wind on three dead turns, lead it under the lead sheave, up beside leg A, over the head sheave and down the well axis. Thread it down through the grab head's guide, under the crosshead sheave, up over the upper sheave in the head and down to the shear link on the crosshead; shackle the thimble on the link pin. Tie the recovery line to the head's eye and make it off at the frame.

## 5. First checks

These are listed here and recorded in a TRL 4 test report, not in this plan.

*Table 2. First checks.*

| Check | Requirement | How | Pass when |
| --- | --- | --- | --- |
| Fit in rings | R2 | Pass the closed grab and the folded scraper through rings of 0.8, 1.0 and 1.3 m on the ground | Nothing binds; the arms open below the ring edge |
| Proof load | R7 | CalRig or a load cell, held 1 min: line, tripod, cradle and capstan to 193 kg (1.89 kN) | No movement over 2 mm, no damage |
| Shear link release | R7 | Pull the dead end through a load cell | Releases between 1.20 and 1.47 kN; the grab opens |
| Crank pin release | R7 | Hold the grab against a fixed stop, crank slowly | Pin shears below 2.2 kN on the innermost layer; the pawl holds |
| Brake | R7 | Lower the full grab on the brake, let go of the lever | The drum stops within one turn |
| Crank force | R5 | Spring balance on a handle, full grab | 150 N or less per person |
| Bite | R3 | Test pit of saturated sand, 20 bites into a measured tub | Record the mean bite |
| Cycle time | R4 | 20 cycles at 10 m, three people at the cranks during the hoist (two otherwise); then 20 with two | 3 min or less a cycle with three at the hoist; record both |
| Sinking and tilt | R1, R6 | Partner well; dip tape every cycle | Record depth gained and tilt |
| Mass and packing | R9 | Weigh each piece, the scraper head with its arms unpinned; load the kit | Each 25 kg or less; record the vehicle used |

## 6. Safety stops

Work stops at each of these points until what is listed is true.

1. **Before anything is lifted over the well.** The barrier stands 2 m outside the tripod feet. The shaft air has been tested with the gas detector. The chain guard is on and the brake weight is fitted. Everyone has been briefed with the card: one signaller, whistle and hand signals; one blast stops all work.
2. **Before the first lift on a site.** The line, cradle, drawbar, capstan and tripod have been proof-loaded for 1 min at 193 kg with nobody near the well. The rope, splice, shackles and pins have been inspected that day. The link pin is a calibrated pin from the tested coil; the crank pin is a 3 mm mild steel pin.
3. **Before each lift.** Nobody is under the grab, beside the line or on the doors. The doors are open only while the grab passes.
4. **Before lowering.** The cranks are off and the pawl is up; the person on the brake has both hands on the lever. During the hoist three people work the cranks; on the stop call all three let go together, the pawl holds the drum, and nobody stands between the capstan and the lead sheave.
5. **Before dumping.** The doors are closed under the grab and the tub is in place; nobody reaches under the grab.
6. **After a shear link or crank pin breaks.** Stop, slack the line, find the snag, and recover the grab on the recovery line if it is on the bottom. Fit a new pin of the specified kind only.
7. **When tilt passes 1 in 160.** Scrape only the high side and move saddles to it. At 1 in 80, stop all undercutting until it is back under 1 in 160.
8. **If anyone must look into or enter the shaft.** SinkGrab work stops. Entry is a separate operation: gas test, harness on a separate line with rescue equipment, a person at the top throughout. SinkGrab's line is never used for a person.
9. **At the end of each day.** Close the doors, inspect the rope, pins, pawl, brake lining and shackles, and replace anything damaged.

## 7. Tools, skills and workspace

- Stick welder with 2.5 mm electrodes or MIG, and a person who can weld 2 mm tube without burning through; welding screen, gloves and mask.
- Angle grinder with cutting and grinding discs; metal saw; pillar drill with bits to 30 mm.
- Plate rolls for the shell skins, or a fabricator who has them; a profile cutter for the ratchet, pawl and end plates.
- Spanners to M14, R-clip pliers, a splicing fid if the eye splices are made in house.
- A flat floor or welding table about 1.5 x 1.5 m; two people for the drum, frames and grab.
- At the well: the HatchSide tripod and its crew of two; a crew of four or five in all.

## 8. Where the numbers come from

- `cad/src/model.py`: the parametric model, its constructability checks and the STEP and STL files in `cad/step` and `cad/stl`.
- `cad/drawings/SKG-DWG-001` and `SKG-DWG-002`: the well-head layout and the grab and scraper general arrangement; `SKG-DWG-101` to `SKG-DWG-117`: making sketches.
- `docs/04-calcs/01-sizing.md` and `docs/04-calcs/sizing.py` (SKG-CAL-001): loads, limits, forces, masses and cost.
- `bom/bom.csv`: parts, specifications and prices.
- `docs/decisions/0002-design-for-construction.md` (SKG-DDR-002): the changes in section 2; `docs/decisions/0003-round-2-requirement-decisions.md` (SKG-DDR-003): the third person at the cranks, the 3:1 tackle and the toe blades.
- `cad/src/build_plan_media.py`: every picture in this plan.
