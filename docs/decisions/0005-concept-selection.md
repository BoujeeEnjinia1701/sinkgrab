---
doc_id: SKG-DDR-005
title: SinkGrab concept selection, proposed, awaiting Amish
project: SinkGrab
doc_type: Design decision record
version: "0.1"
status: Draft
date: '2026-10-24'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-24'
  author: Amish Chadha
  change: "First issue (kit 1.9.1 upgrade): concept options A and B scored within 10 %, so both are put to Amish without a pick (STANDARDS section 21)"
---

# 0005: Concept selection (proposed, awaiting Amish)

- **Date:** 2026-10-24
- **Status:** proposed, awaiting Amish

## Context

Kit 1.8 asks every design for at least two concept options with different working principles, scored against the same user requirements (STANDARDS section 21). SinkGrab was designed before kit 1.8, so its current design, the rope grab and under-curb scraper, is option A and is not redesigned without Amish's go. Option B, a dart-valve bailer spudded on a jerk line, was developed in this session and modelled to the same detail level (D3) so the two can be compared on the same footing. The comparison is SKG-OPT-001.

## Options considered

| Option | Working principle | Weighted score | Strengths | Weaknesses |
| --- | --- | --- | --- | --- |
| A, rope grab and under-curb scraper | A one-line clamshell grab digs the flooded rings; a pole scraper cuts under the cutting edge so the lining sinks | 167 | Undercuts, steers the lining, digs cohesive soils; drawn, priced and planned | More parts and pins; plate rolls for the shells; sinking still at risk (STEM S21) |
| B, dart-valve bailer on a jerk line | A valved tube is spudded into loose sand by jerking the capstan line sideways; sand runs in from under the edge | 153 | Simple pipe-and-plate build; about USD 330 cheaper and about 40 kg lighter as modelled; no linkage under water | Sand and gravel only; no undercut or tilt control beyond saddles; heavier jerk effort; shock on the line |

The scores are 8.4 % apart, inside the 10 % band, so both go to Amish without a pick.

## Decision

None yet. Amish chooses between:

- **A:** keep the rope grab and under-curb scraper as SinkGrab's concept (no change to the repo), optionally carrying a bailer on the same line as an accessory for clean running sand (the runner-up's best idea).
- **B:** move to the dart-valve bailer, accepting that SinkGrab then serves sand and gravel wells only; the drawings, BOM and build plan would be redone for B.

Until Amish decides, `project.yaml` leaves `concept_chosen` unset and the drawings, BOM and build plan stay on option A, which `cad/src/model.py` names as `CHOSEN` because it is the design of record.

## Consequences

- If A: no change to the design; UR-011 (soils) and UR-003 (tilt) stay covered. The bailer accessory, if wanted, is a new BOM line and a short build plan section.
- If B: PR-001, PR-003, PR-006 and PR-013 would need restating for sand-only wells; the grab, scraper and two sheaves leave the BOM; a new build plan and drawings follow, and the STEM rows OB3, OB5 and OB6 need test-pit evidence.
- Either way the capstan, foot cradle, drawbar, well-head frame, saddles and safety stops are unchanged.
