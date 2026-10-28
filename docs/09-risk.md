---
doc_id: SKG-RSK-001
title: SinkGrab risk register, hazard analysis and design FMEA
project: SinkGrab
doc_type: Risk register
version: "0.2"
status: Draft
date: '2026-10-25'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-24'
  author: Amish Chadha
  change: First risk register with preliminary hazard analysis and a first-pass design FMEA (kit 1.9.1 upgrade, stage P3)
- version: "0.2"
  date: '2026-10-25'
  author: Amish Chadha
  change: "Amish's decisions of 2026-10-25 (SKG-DEC-001 O2, O4, O5): R1 and R9 restated, R10 added; H5 controls; FMEA F1, F3 and F11 rewritten for the load indicator and the crank slip clutch"
---

# SinkGrab risk register, hazard analysis and design FMEA

The top project risk is that the caisson rings stop sinking before 3 m because skin friction is higher than the 1.66 kPa self-weight can overcome (R1); since Amish's decision O2 of 2026-10-25 a bentonite slurry in the overcut annulus is part of the method, and the test pit shows whether it is enough. The narrow slip window of the crank slip clutch chosen under O4 follows (R9). The top hazards are a person falling into or entering the shaft and a load or ring dropping, all controlled by keeping everyone at the surface behind a barrier with the doors shut. The design FMEA's highest items are the slip clutch tightened past its setting and the load indicator's tell-tale not read (RPN 30 and 27), both kept in check by the CalRig setting, the paint-marked locknut and the reading at every lift; the crosshead and the scraper fold follow, each designed against its failure (SKG-DEC-001 K8, K6). Method: STANDARDS section 23. Likelihood, impact, severity, occurrence and detection are scored 1 (low) to 5 (high; for detection, 5 is hardest to detect).

> **Safety:** SinkGrab is lifting equipment worked over an open well shaft, with a hand-cranked chain drive and loads hanging over the well. This register is a paper assessment for a TRL 3 design; it does not show that any part is safe.

## Project risk register

Table 1. Project risks.

| # | Risk | Cause | Effect | Likelihood | Impact | Owner (role) | Response |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R1 | Rings stop sinking short of 3 m | Skin friction above 1.66 kPa; the central unaided estimate is 2 kPa and soil closes on the ring above the overcut (independent review) | PR-001 not met; well not deepened enough | 4 | 5 | Design lead | Bentonite slurry fed into the overcut annulus as part of the method, decided 2026-10-25 (O2); tried in the test pit before a partner well; jacking against a reaction is the next step if the test pit shows it is not enough |
| R2 | Grab fills poorly in denser sand or laterite | Closing force margin about 30 % in loose sand (STEM S2) | Bite below 20 L (PR-003); slower deepening | 3 | 3 | Design lead | Test-pit bite trial in each soil (PR-013) before a partner well |
| R3 | Cycle over 3 min | Hoist limited by human power (78 s of 3.19 min) | PR-004 not met; more days per well | 4 | 2 | Design lead | Timed trial decides (decision 27A); accept if the daily output suffices |
| R4 | No co-design partner | Neither candidate approached yet | No trial well, no validation of user requirements | 3 | 4 | Amish (owner) | Approach the Kerala Ground Water Department, then the Ethiopian NGO (SKG-DDR-001 item 12) |
| R5 | HatchSide tripod not available or changed | Shared block, rated for material handling only | Interfaces (head sheave, foot cradle) no longer fit | 2 | 4 | Design lead | Keep the interface drawings current; any HatchSide change is checked against SinkGrab |
| R6 | Fabricators lack plate rolls or a profile cutter | Village workshops | Shells and profile-cut parts made in a city | 3 | 2 | Co-design partner | Faceted skin fallback (SKG-DEC-001 value engineering); profile-cut parts ordered as a set |
| R7 | Concept choice changes after the build plan | Options A and B within 10 % (O1) | Redrawing and rebuilding the plan | 2 | 3 | Amish (owner) | Decide O1 before any TRL 4 build |
| R8 | Under-curb scraper claims in Chinese caisson patents | Targeted search not yet run | Release blocked or redesign | 2 | 3 | Amish (owner) | Search before public release (SKG-DDR-001 item 14) |
| R9 | Narrow slip window for the crank slip clutch | Steady full-grab pull 1,068 N against a lowest slip of 1,127 N on the third rope layer (6 %); facing friction moves with moisture and glazing | The clutch slips on a steady hoist and work stops, or it slips high | 3 | 4 | Design lead | Set and checked on CalRig before each campaign on every layer; facings kept dry inside the guard; load indicator read every lift; an uprated tripod (O4 option B) if the trials show more bite is worth it |
| R10 | Four people needed to turn the scraper | Decision O5: the 2.0 m T-bar does not clear the tripod legs | Crew short on the day; scraping slower or pushed past 100 N each | 2 | 2 | Site lead | Crew of five or six planned for scraping days; briefing card says four at the T-bar |

## Preliminary hazard analysis

Table 2. Hazards.

| # | Hazard | Cause | Harm | Severity | Likelihood | Control | Residual |
| --- | --- | --- | --- | --- | --- | --- | --- |
| H1 | Fall into the shaft | Open well mouth while the grab passes | Death or serious injury | 5 | 2 | Doors closed whenever the grab is above them; barrier 2 m outside the tripod feet; nobody on the doors during a lift (BLD stop 3) | 1 |
| H2 | Entry into the well | Freeing a snag, retrieving a tool | Asphyxiation, drowning, struck by load | 5 | 2 | Nobody enters while SinkGrab works; recovery line on the grab; entry only as a separate operation with gas test, harness and rescue (BLD stop 8) | 1 |
| H3 | Bad air at the well mouth | Carbon dioxide, hydrogen sulphide or low oxygen in the shaft | Collapse of a person leaning over the shaft | 5 | 2 | Four-gas detector and carbon dioxide monitor lowered and read at three depths before work, after breaks and before leaning over (PR-012, K5, K22) | 1 |
| H4 | Grab or scraper falls into the well or onto people | Rope, splice, pin or shackle failure | Death or serious injury below or beside the line | 5 | 2 | Line factor 10.2; proof load 196 kg before use; nobody under or beside the line; daily inspection (BLD stops 2, 3, 9) | 2 |
| H5 | Tripod overloaded | Snag while hoisting | Tripod collapse onto the crew | 5 | 2 | Crank slip clutch caps the capstan pull at the 150 kg rating, set on CalRig (O4, 2026-10-25); the load indicator shows the peak of each lift; proof at 1.25 x the rated load, 188 kg, inside the 225 kg proof | 2 |
| H6 | Load runs back while lowering | Brake not set; cranks on while lowering | Spinning cranks strike the crew; grab drops | 4 | 2 | Weighted band brake on when let go, geometry corrected (K2); cranks off before lowering; pawl (BLD stop 4) | 1 |
| H7 | Fingers or clothing in the chain or brake | Guard off; reaching in | Crush and cut injuries | 3 | 2 | Chain guard on M6 screws into clip angles; never turn the cranks with it off | 1 |
| H8 | Rings drop or tilt suddenly | Uneven undercutting | Ring damage; lining out of line | 3 | 3 | Sump at most 330 mm below the edge; tilt read every cycle; stop undercutting at 1 in 80 (BLD stop 7) | 2 |
| H9 | Back injury from heavy pieces | Lifting the grab, a full tub or the capstan by hand | Musculoskeletal injury | 3 | 3 | Pieces of 25 kg or less carried by two; grab only on the line (K3); tub slid, not lifted (K4) | 1 |
| H10 | Contaminated water after the work | Sediment, tools and hands in the well | Illness of the households who use it | 4 | 2 | Clean tools; disinfect the well after the work (Oxfam guidance; SKG-REG-001 G12) | 2 |
| H11 | Three people at the capstan during the hoist | Third person on the long handle | Struck by a handle or the line | 3 | 2 | All three let go together on the stop call; nobody between the capstan and the lead sheave (BLD stop 4) | 1 |
| H12 | Jerk crew beside the loaded line (option B only) | Spudding at the well mouth | Struck by the line or bar if the bailer jams | 3 | 3 | Applies only if Amish chooses option B (O1) | 3 |

## Design FMEA (first pass, P3)

Table 3. Failure modes. RPN = severity x occurrence x detection.

| # | Item | Function | Failure mode | Effect | Cause | S | O | D | RPN | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F1 | Dead-end load indicator | Show the highest pull of each lift | Tell-tale lost or stuck; springs set or corroded | Peak not seen, so a clutch slipping high goes unnoticed | Mud on the rod; O-ring perished; spring stack rusted | 3 | 3 | 3 | 27 | Read and reset at the doors after every lift; stainless rod; spare O-rings on the frame; recalibrated on CalRig with the clutch |
| F2 | Band brake | Hold the drum when the lever is let go | Weight slackens instead of sets; lining wet or worn | Load runs back | Link pin on the wrong side of the pivot (kit 1.7 model); lining glazing | 5 | 2 | 2 | 20 | Lever geometry corrected (K2); brake check before each lift (first checks); inspect lining daily |
| F3 | Crank slip clutch | Cap the capstan pull at the 150 kg rating | Slips high: locknut tightened past its setting or facings rusted to the discs | Line can pass the tripod's rating | Crew tightens it to stop slipping; clutch left wet and standing | 5 | 2 | 3 | 30 | Locknut paint-marked and held by its tab washer; briefing card and stop 6 say "never tighten the clutch"; slip checked against a fixed stop at the start of each day; load indicator read every lift; CalRig check before each campaign |
| F4 | Scraper fold | Fold the arms to pass the ring | Arms stay open | Head jams under the ring; nobody may enter to free it | Sleeve not sliding; cross pin missing; arm eye on the hub | 4 | 2 | 3 | 24 | Pivots at 60 mm so the eyes clear the hub (K6); fold check on the ground through a 0.8 m ring; cross pin checked at every pole change |
| F5 | Closing line | Carry the grab | Abrasion or cut | Grab lost in the well | Rubbing on the door notch or a sheave flange; UV | 4 | 2 | 2 | 16 | Daily inspection; replace at the first damaged strand; fairlead only in option B |
| F6 | Crosshead on the hinge pin | Keep the tackle in line | Crosshead slides along the pin | Line rubs the head; uneven closing | Nothing held it axially (kit 1.7 model) | 3 | 3 | 3 | 27 | Two set collars (K8); check on assembly |
| F7 | Drum bearing bolts | Hold the drum bearings to the pads | Bolts cannot be fitted or work loose | Drum moves; chain jumps | Nuts would sit inside the pad posts (kit 1.7 layout) | 3 | 2 | 2 | 12 | Captive bolts pushed up before the pads are welded (K10); check torque daily |
| F8 | Crank handles | Turn the cranks | Handle hardware strikes the chain guard | Guard damaged; crank jams mid-hoist | Bolt and nut on the inner face of the arm | 3 | 2 | 2 | 12 | Welded stub axles, nothing on the inner face (K11) |
| F9 | Doors | Cover the shaft, carry the tub | Door lifts or a tub tips in | Fall or spoil into the well | Door not seated; tub on the meeting edge | 4 | 2 | 2 | 16 | Doors close flat on the vertical legs; tub stands on the mesh, slid off on a board (K4) |
| F10 | Ballast saddles | Add weight on the high side | Saddle drops into the annulus | Saddle lost; ring knocked | Line not made off | 2 | 2 | 2 | 8 | Each saddle on its own made-off line |
| F11 | Crank slip clutch | Carry the hoisting torque up to its setting | Slips low: facings wet or oily | Hoist stops with the load on the pawl | Rain or grease inside the guard | 2 | 3 | 2 | 12 | Guard closed with a drain hole; no grease near the clutch; facings dried or changed; replaces the crank pin's fatigue mode (STEM S6) |

Highest RPN: F3 (crank slip clutch tightened past its setting, 30), then F1 (load indicator not read, 27) and F6 (crosshead, 27). The responses are partly procedural, so they stay on the briefing card and in the first checks; the crank shear pin's modes (RPN 45 and 36) are gone with the pin.
