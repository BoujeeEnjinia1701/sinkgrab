---
doc_id: SKG-DDR-004
title: SinkGrab scraper sleeve travel, decision of 2026-10-04 (R2)
project: SinkGrab
doc_type: Design decision record
version: "0.1"
status: Draft
date: '2026-10-04'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-04'
  author: Amish Chadha
  change: "Amish's round-3 decision 5A of 2026-10-04 recorded and carried out in the model, calculations, bill of materials, drawings and build plan"
---

# 0004: Scraper sleeve travel (R2)

- **Date:** 2026-10-04
- **Status:** accepted

## Context

The scraper's two arms are opened by struts from a sliding sleeve: with the foot on the sump floor, the pole's weight slides the pole down through the sleeve and the struts push the arms out. Lifting the pole must let the sleeve slide 300 mm down the pole for the arms to fold to 389 mm radius, inside the 400 mm bore of a 0.8 m ring. While carrying out decision 29B (SKG-DDR-003) the check found that the first design could not do this: a stop collar sat 40 mm below the sleeve and the pole ended 120 mm below it, so the sleeve could slide only about 40 mm, the toes folded only to about 604 mm radius and the head could not have been lifted out through any ring in the range. The build plan's step 14 and joint 10 showed the same fault.

This was posed to Amish as open decision 4 in the design decisions register (SKG-DEC-001) and `docs/REVIEW.md`, and was item 5 of the portfolio's round-3 list. Amish Chadha (owner), 2026-10-04: "For round 3, I agree with all your proposed recommendations".

## Options considered

| Option | What changes | Cost and mass | Effect |
| --- | --- | --- | --- |
| **A (chosen)** | A 340 mm sleeve, its top just below the hub, with a 300 mm slot each side and a 12 mm cross pin through the pole running in the slots; the stop collar goes; the spike stays 110 mm below the foot | About USD 5, 1.4 kg (estimate when posed) | Nothing is pushed into the sump floor; the 330 mm sump limit keeps its meaning; linkage, struts and fold radius unchanged |
| B | Lengthen the bottom pole and spike 320 mm and move the stop collar down | About USD 3, 0.6 kg | The spike end stands about 430 mm below the foot and has to be pushed that far into the sump floor before the arms open |

## Decision

Option A, as recommended. The sleeve is 340 mm of 54 mm tube, from the foot plate to 15 mm below the hub. A slot 13 mm wide and 312 mm long is cut through each side, starting 14 mm above the bottom end and rounded at the top; the strut lugs stay on the other two sides, 100 mm above the bottom, where they were, so the linkage is unchanged. A 12 mm bright steel cross pin, 70 mm long with an R-clip, passes through one slot, a 12.5 mm cross hole in the pole 140 mm above the tip, and the other slot. Open, the pin bears on the slot bottoms; when the pole is lifted the sleeve slides down until the pin meets the slot tops, a travel of 300 mm. The stop collar is removed.

## Consequences

From SKG-CAL-001 v0.3 and `cad/src/model.py` (no overlaps, no parts adrift, and a new fold check: the sleeve slid 300 mm down is held by the pin at its slot tops without touching the pole, and the folded toes are inside the smallest bore):

| Requirement | Before | After | Target | Status |
| --- | --- | --- | --- | --- |
| R2 fit in rings | Folds to 389 mm only on paper; as drawn about 604 mm, so the head jammed under every ring | Sleeve travel 300 mm; folds to 389 mm radius, 11 mm inside a 0.8 m ring's bore | Rings of 0.8 to 1.3 m | Met by design |
| R9 portability | Scraper head 19.2 kg with the arms unpinned (25.2 kg with them on) | 20.1 kg with the arms unpinned (26.1 kg with them on); heaviest piece still the capstan frame, 22.9 kg | 25 kg or less | Met on paper |
| R11 cost | USD 2,561 | USD 2,566 | Value-engineering target USD 4,000 | Met on paper, within the target |

- **Mass.** The longer sleeve adds 1.1 kg and the pin 0.06 kg, and dropping the stop collar saves 0.3 kg: 0.9 kg net, less than the 1.4 kg estimated when the option was posed. The kit is about 457 kg.
- **Strength.** With the whole 25 m string resting on the foot the pin carries 1,262 N in double shear: 6 MPa, a factor of 43, and 20 MPa bearing on the 2.6 mm pole wall. The 12.5 mm hole sits in the bottom pole well below the hub and centralizer, where the pole carries only the T-bar torque.
- **Use.** The spike still stands 110 mm below the foot, so nothing is pushed into the sump floor and the 330 mm sump limit keeps its meaning. When the scraper is lifted, the sleeve and foot hang about 190 mm below the spike; they pass the bore with the folded arms.
- **Cost.** Value-engineering target: USD 4,000. Estimated cost of the constructable design: USD 2,566 (USD 1,434 under the target). The change adds USD 5 to BOM line 15 (230 mm more tube, two slots, the pin and its R-clip, less the collar).
- **Safety.** No change to the safety case. The scraper no longer risks jamming under the ring, so the earlier warning that nobody enters the well to free a jammed head becomes a general rule rather than a likely event. A missing cross pin lets the sleeve drop off the pole on lifting; the pin and R-clip are checked at each pole change.
- **Changed files.** `cad/src/model.py`, STEP and STL, `docs/04-calcs/sizing.py`, `01-sizing.md` (v0.3) and `results.csv`, `bom/bom.csv` (line 15), `docs/03-requirements.md` (v0.5, status only, no requirement restated), `docs/02-concept.md` (v0.5), `docs/05-build-plan.md` (v0.3), `README.md` (cost), SKG-DWG-002 (Rev P4), SKG-DWG-112 and 113 (Rev P2), joints 10 and 14, steps 14 and 15, the overview, concept media and `cad/src/product_model.py`.
