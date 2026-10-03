---
doc_id: SKG-DDR-001
title: SinkGrab TRL 2 review decisions
project: SinkGrab
doc_type: Design decision record
version: "0.1"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: TRL 2 review items decided under Amish's pre-approvals of 2026-10-03
---

# 0001: TRL 2 review decisions

- **Date:** 2026-10-03
- **Status:** accepted

## Context

The TRL 2 review (`docs/REVIEW.md`, TRL 2 section) raised the items below, including the five open questions of SKG-PRB-001 v0.1. On 2026-10-03 Amish wrote: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." He then wrote, the same day: "Proceed with the remaining 15 scaffolds", under the same pre-approval; SinkGrab is one of those fifteen. Every design recommendation below is therefore decided as recommended. Choices that touch safety take the conservative option, with the evidence that would relax them stated. Partners and regions are the first candidates to approach, not agreements. Requirements that are not met or at risk are not decided here; they are posed to Amish in SKG-DEC-001.

## Options considered

Table 1 lists the options for each item and the one chosen.

## Decision

*Table 1. Items decided on 2026-10-03 under Amish's pre-approvals.*

| # | Item | Options | Decision | What would relax a safety choice |
| --- | --- | --- | --- | --- |
| 1 | Grab type | (a) two-shell clamshell; (b) multi-tine orange peel | (a): two shells from rolled plate on one pin; an orange peel needs four to six tines, each on its own pin and link | Not a safety choice |
| 2 | Grab operation | (a) closing line plus holding line on two hoists; (b) one closing line, grab lowered closed and opened by its head's weight when the line is slacked | (b): one capstan, one rope, two people | Not a safety choice |
| 3 | Overload | (a) size everything on what two people can heave (8.3 kN); (b) a calibrated shear link at the grab's tackle (1.20 to 1.47 kN) plus a 3 mm shear pin in the crank hub that caps the line below the tripod's proof load | (b), conservative: the HatchSide tripod is never loaded past its 150 kg rating by the grab, nor past its proof load by anything | Break tests on a batch of link pins showing a tighter scatter could raise the rated load toward 150 kg, never past it |
| 4 | Hoist | (a) HatchSide's own hand winch; (b) a SinkGrab hand capstan derived from the SiltHaul block, with a single drum, 4:1 chain, pawl and band brake | (b): two people at 50 W each; the HatchSide winch is removed while SinkGrab works | Not a safety choice |
| 5 | Capstan anchor | (a) ground anchors or a sling to a tree; (b) a drawbar to a cradle under the tripod's leg A foot | (b), conservative: the rope pull closes inside the kit, and the tripod sees only its own winch load case | None proposed |
| 6 | Lowering | (a) crank backward with the pawl lifted; (b) cranks removed, lowering on a band brake that a weighted lever holds on | (b), conservative: no spinning cranks, and the brake sets if the operator lets go | A load brake of the automatic (Weston) type, if one is bought and proof-tested, would allow lowering on the cranks |
| 7 | Scraper guide | (a) rope-hung frame bearing on the wall; (b) centred pole in 2 m sections with a centralizer, arms opened by the pole's weight, turned with a T-bar | (b): a rope cannot turn a tool at depth; the arms fold to pass the bore | Not a safety choice |
| 8 | Sand boiling | (a) bail or pump to lower the water inside; (b) no de-watering; water inside stays level with outside; sump at most 330 mm below the cutting edge | (b), conservative: no upward gradient, no pump in or near the well | Trials showing stable sand with a deeper sump could relax the 330 mm |
| 9 | Tilt limits | Check every 5 cycles or every cycle; act at 1 in 80 or earlier | Read every cycle; correct from 1 in 160; stop undercutting at 1 in 80 until corrected (conservative) | Trial records showing tilt changes slowly could reduce the reading interval |
| 10 | Ballast | (a) a ballast frame on the top ring loaded with plates; (b) U-saddles that straddle the top ring wall, each on its own line, placed by where its line is paid out at the rim | (b): no person needed to place them, and each can be moved to the high side | Not a safety choice |
| 11 | Spoil handling and cover | (a) a chute swung over the mouth with a tipping hook; (b) a well-head frame with two folding doors, the grab dumping into a tub on the closed doors | (b), conservative: the shaft is covered whenever the grab is up; the doors also guide the pole and carry the tilt datum | None proposed |
| 12 | Co-design partner | Kerala, Ethiopian highlands, NGO or water department | First candidate to approach: the Kerala Ground Water Department through a district office, with a well-digging crew it already works with; second, a rural water NGO in the Ethiopian highlands (neither agreed) | |
| 13 | Shared blocks | HatchSide tripod; SiltHaul and SaltDrag hand capstan; CalRig proof loads | HatchSide tripod used unchanged except for a 150 mm sheave grooved for 8 mm rope fitted in its head while SinkGrab works; SinkGrab's capstan is recorded as the single-drum variant of the common capstan block; CalRig is the first candidate rig for proof loads | |
| 14 | Patent screen | Release with or without the targeted search | The targeted search of Chinese open-caisson excavator patents for under-curb scraper claims is run before public release | |
| 15 | Budget | Keep `budget_usd` at 4,000 | Kept; it is a value-engineering target, not a limit | |

## Consequences

- SKG-PRC-001 and SKG-REQ-001 move to v0.2 with these choices; the design for construction (SKG-DDR-002) works from them.
- The open questions of SKG-PRB-001 v0.1 are answered on paper; the questions only trials can answer are listed in SKG-PRB-001 v0.2.
- R1, R3 and R4 are not decided here; they are posed to Amish in SKG-DEC-001 with options and a recommendation.
