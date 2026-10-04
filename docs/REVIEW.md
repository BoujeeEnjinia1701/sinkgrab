# Review note: SinkGrab

## Session 2026-10-03: round 2 requirement decisions applied

Amish, 2026-10-03: "i approve all of the 47 recommendations provided by you. Execute them." For SinkGrab that decides the three requirement decisions of the TRL 3 session below as recommended: 1A (R4), 2B (R3) and 3B (R1). They are recorded in `docs/decisions/0003-requirement-decisions-round2.md` (SKG-DDR-003) and moved to Decisions made in `docs/06-design-decisions.md` (SKG-DEC-001 v0.2). Phase cap TRL 3 kept: no test articles, test plans, firmware, build-log entries or purchasing lists. Nothing was committed or pushed.

**What changed.**

- **1A, R4: third person on the hoist.** `cad/src/model.py`: `handle_long` 240 mm on the +X crank (two hands), the -X crank keeps its 120 mm handle. BOM line 4 USD 45 to 55.
- **2B, R3: 3:1 closing tackle.** `cad/src/model.py`: a second bought 150 mm sheave (`upper_sheave`, `upper_axle`) under the head box between two 8 mm cheeks, skewed 20 degrees about the vertical so both of its rope parts hang straight (`head_sheave_skew`, `head_sheave_z`); the dead-end lug and the shear link move from the head to the crosshead's -Y plate, 180 mm above the hinge (`tackle_parts` 3). BOM lines 10 (USD 45 to 50), 13, 14 and 25 (three sheaves to four).
- **3B, R1: toes 40 mm past the ring.** `toe_r` 590 to 615 mm (arms 25 mm longer). BOM line 15 USD 60 to 70.
- **Made to keep 3B constructable.** `fold_lift` 300 to 320 mm: with the longer arms a 300 mm lift folded the toes only to 405.5 mm, outside the 400 mm bore of a 0.8 m ring; 320 mm folds them to 377 mm. The model checks report no overlaps and no floating parts.
- `docs/04-calcs/sizing.py` (crew of three on the hoist, tackle parts from the model, closing time with the third part, R4 and R9 status computed) re-run: `results.csv` and `docs/04-calcs/01-sizing.md` (SKG-CAL-001 v0.2).
- Regenerated with the repo's scripts: STEP and STL (`cad/src/model.py`), SKG-DWG-001 and 002 Rev P3 (`cad/src/sheets.py`), concept media and `media/model.glb` at linear deflection 1.0 and angular 0.35 (`cad/src/concept_media.py`), the build plan overview, making sketches SKG-DWG-101 to 117, joints and steps (`cad/src/build_plan_media.py`, with its notes updated). `cad/src/product_model.py` gained the head sheave and axle for the next render.
- Text: `docs/03-requirements.md` v0.4, `docs/02-concept.md` v0.4, `docs/05-build-plan.md` v0.2, `README.md`; `project.yaml` trl_evidence gains SKG-DDR-003.

**Requirement status, before and after.**

| ID | Before | After |
| --- | --- | --- |
| R4 | Not met on paper, 3.7 min | Not met on paper, 3.16 min with three on the hoist, 5 % over (3.8 min with two) |
| R3 | At risk, lips about 437 N | At risk, lips about 687 N; fill still settled in the test-pit trial |
| R1 | At risk, toes 15 mm past the ring | At risk, toes 40 mm past the ring; friction limit still 1.66 kPa |
| R9 | Met on paper, scraper head 24.9 kg | **Not met on paper, 25.1 kg (0.1 kg over)** |
| R5 | 52 N each with two | 54 N each with two, about 36 N with three |
| R7 | Proof 187 kg, line factor 10.7, link margin 1.19 | Proof 193 kg, line factor 10.4, link margin 1.15 |
| R2 | Folds to 364 mm | Folds to 377 mm with a 320 mm lift |
| R11 | USD 2,506 | USD 2,561 |

The others are unchanged. The text of 01-sizing.md v0.1 quoted 24.6 kg for the scraper head and 2.96 m³ of soil where the script printed 24.9 kg and 3.28 m³; v0.2 quotes the script.

**Cost.** Estimated cost of the constructable design USD 2,506 before, USD 2,561 after (USD 10 handle, USD 35 tackle, USD 10 arms), USD 1,439 under the USD 4,000 value-engineering target. `budget_usd` unchanged (it is the value-engineering target, SKG-DDR-001 item 15). Grab 47.9 to 51.2 kg; kit about 452 to 456 kg.

**New questions for Amish.** Each is **Proposed, awaiting Amish**, listed in SKG-DEC-001 as items 4 to 6.

**4. Scraper fold travel and the 25 kg piece limit (R2, R9).**
- *State:* the stop collar on the scraper spike sits 30 mm below the sleeve's foot, so when the pole is lifted the collar picks up the sleeve after 30 mm, while the arms need 320 mm of lift on the sleeve to fold (300 mm before 3B). This was already the case before round 2 and was found while checking the longer arms. Separately, the longer arms bring the scraper head to 25.1 kg, 0.1 kg over R9.
- *Option A:* remove the stop collar and let the struts carry the sleeve once the arms are folded, the folded geometry to be checked in the model. Fold works; head about 24.8 kg, R9 met; USD 0.
- *Option B:* lengthen the spike by 320 mm and move the collar down with it. Fold works; head about 25.9 kg, R9 not met unless the arms travel unpinned; about USD 5.
- *Option C:* no change. The arms cannot fold, so the scraper passes only bores wider than the open toes; R2 not met.
- **Recommendation: A.** It fixes the fold and the 0.1 kg at no cost.

**5. R4 wording.**
- *State:* R4 reads "3 min or less per grab cycle at 10 m depth with two operators"; with 1A the hoist uses three people, and the cycle is 3.16 min.
- *Option A:* restate R4 as "3 min or less at 10 m with three people at the cranks for the hoist". Status unchanged: not met on paper, within 5 %.
- *Option B:* keep the wording and report R4 against two people: 3.8 min.
- **Recommendation: A.** It states what the crew will do and what the timed trial measures.

**6. Shear link margin.**
- *State:* the 3:1 tackle added 3.3 kg to the grab against the 2.5 kg estimated, so the working pull is 1,042 N and the link's lowest release (1,202 N) is 1.15 times it, down from 1.19. A link that releases too near the working pull would drop full bites.
- *Option A:* keep it and watch for releases in the test-pit bite trial. No change.
- *Option B:* thin the ballast plates from 16 to 10 mm to win back about 2 kg: margin about 1.18; head weight for opening 14.0 to 12.0 kg.
- **Recommendation: A.** The link still releases only above 1.15 times a working pull that already carries the 1.1 dynamic allowance; the bite trial shows whether it releases in use.

**Safety notes.**

- The shear link and the crank shear pin are unchanged and still set the line limits (1.20 to 1.47 kN and 2.1 kN); the dead end, and so the link, now sits on the crosshead. If the link releases, the line runs out through both grab sheaves and the grab opens on the bottom, recovered on the recovery line as before.
- Three people now crank during the hoist; the crank pin caps the line whatever the crew does, and the cranks still come off before lowering on the brake.
- The proof load for R7 rises to 193 kg, still inside the HatchSide proof of 225 kg; safety stop 2 in the build plan says 193 kg.
- The longer toes cut a wider ring under the cutting edge (3.56 m³ for 3 m of sinking): the tilt stops (correct from 1 in 160, stop at 1 in 80) are unchanged and matter more.

**Renders.** The photoreal renders made on Amish's Mac predate this session. The hero view changes only slightly (the long crank handle and the head sheave under the grab head); the exploded grab view changes visibly (a fourth sheave, the shear link on the crosshead) and the detail view shows the longer arms. A re-render of the exploded and detail views is needed; the hero can wait for the next render pass.

**Recommended next step.** Amish decides items 4 to 6. The design is then ready for TRL 4 when the phase allows: build the capstan, cradle and grab, proof-load them on CalRig, break-test the link and crank pins, then the test-pit bite trial and the timed cycle trial with three at the cranks.

## Session 2026-10-03: TRL 3 (kit 1.7.0, /to-trl3 under Amish's pre-approvals, batch 2)

Amish, 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." Then, the same day: "Proceed with the remaining 15 scaffolds", under the same pre-approval; SinkGrab is in that batch. Design choices and recommendations in this session are therefore recorded as decided, dated 2026-10-03, in `docs/06-design-decisions.md`. Requirements that are not met or at risk are not decided here (Amish, 2026-10-03: "A simple statement doesn't add value - ensure you are identifying a state and posing it as a clear recommendation for me to decide on."); they are posed below under "Decisions for Amish". Kit 1.7.0 was installed from the kit source; `.kit/PHASE.yaml` kept as installed. Nothing was committed or pushed.

### TRL 2

**What was done.**

- `docs/01-problem.md` (SKG-PRB-001 v0.2): first co-design candidates, safety section, the scaffold's open questions answered and replaced by questions for the first trials; budget restated as a value-engineering target.
- `docs/03-requirements.md` (SKG-REQ-001 v0.2): concept status for every requirement; R11 restated against the value-engineering target.
- `docs/02-concept.md` (SKG-PRC-001 v0.2): how it works, components, key design choices, safety.
- `docs/decisions/0001-trl2-review-decisions.md` (SKG-DDR-001): fifteen TRL 2 review items decided.

**Results.** On first-order numbers one hand capstan and one rope can dig, lift and dump a grab of about 20 L, the HatchSide tripod's 150 kg rating is the binding limit on the line, and a pole is the only practical way to turn a scraper at depth.

**Requirements not met.** None identified at TRL 2; cycle time was flagged as the tightest.

**Decisions made under the pre-approvals.** SKG-DDR-001, items 1 to 15: two-shell clamshell; one closing line with a head that opens the shells by weight; shear link and crank shear pin (conservative); SinkGrab hand capstan in place of the HatchSide winch; drawbar to a cradle under the leg A foot (conservative); lowering on a weighted band brake with the cranks off (conservative); centred scraper pole with weight-opened arms; no de-watering and a 330 mm sump limit (conservative); tilt read every cycle, correct from 1 in 160, stop at 1 in 80 (conservative); ballast saddles; well-head doors and tubs in place of a chute (conservative); Kerala Ground Water Department as first co-design candidate, Ethiopian highlands NGO second (neither agreed); shared blocks (HatchSide with an 8 mm head sheave, single-drum capstan variant, CalRig); patent search before release; budget kept.

**Safety concerns.** Falls into the shaft; loads dropping into the well; bad air; overload of a tripod rated for material handling only; rings dropping or tilting when undercut.

### TRL 3

**What was done.**

- `docs/04-calcs/01-sizing.md` and `docs/04-calcs/sizing.py` (SKG-CAL-001 v0.1), `docs/04-calcs/results.csv`.
- `cad/src/model.py`: parametric build123d model with constructability checks (no overlaps, no floating parts, folded scraper passes the smallest bore); STEP and STL in `cad/step` and `cad/stl` (capstan, lead, grab, scraper, well-head, saddle; assembly STEP).
- `cad/src/sheets.py`: SKG-DWG-001 (well-head layout) and SKG-DWG-002 (grab and scraper GA), Rev P2.
- `bom/bom.csv`: 34 lines, all priced, suppliers by type.
- `cad/src/concept_media.py`: `media/hero.png`, `exploded.png`, `flow.png`, `concept-blueprint.png` and `.pdf` (SKG-DWG-010), `model.glb` (coarse tessellation) and `viewer.html`. No cutaway; the inside of the well is shown in the detail render and build plan joint 14.
- `docs/decisions/0002-design-for-construction.md` (SKG-DDR-002); `design_state: constructable`.
- `cad/src/build_plan_media.py`: overview, 17 making sketches (SKG-DWG-101 to 117), 14 joint close-ups and 20 step pictures; `docs/05-build-plan.md` (SKG-BLD-001) and `docs/06-design-decisions.md` (SKG-DEC-001).
- `cad/src/product_model.py` (`product_parts()`, `TITLE`, `RENDER_VIEWS` hero, exploded, detail); scenes exported to `/home/claude/renders/sinkgrab`. Photoreal renders, captions and cards are made on Amish's Mac; the README already leads with `media/render-hero.png`.
- `docs/01-problem.md`, `docs/02-concept.md` (v0.3), `docs/03-requirements.md` (v0.3), `README.md`, `project.yaml` (trl 3, trl_target 3).

**Results (SKG-CAL-001).** Bite 21.2 L at 75 % fill (28.3 L closed); grab 47.9 kg, 93 kg full; working line pull 1,006 N; 52 N on each crank with two people; hoist 6.0 m/min; shear link releases 1,202 to 1,469 N, inside the tripod's 1,472 N rating; crank pin caps the line at 2,107 N, inside its 2,207 N proof load; line factor 10.7; brake 314 N m (factor 1.69 at the limit); scraper 136 N each on the T-bar, working limit 25 m; arms fold to 364 mm radius; heaviest piece 24.6 kg; kit about 452 kg. Value-engineering target: USD 4,000. Estimated cost of the constructable design: USD 2,506 (USD 1,494 under the target).

**Requirements not met or at risk.** R4 not met on paper (3.7 min); R3 at risk (fill); R1 at risk (skin friction). R6 can only be verified in a trial. Each of R4, R3 and R1 is posed below.

#### Decisions for Amish

**1. R4, cycle time (not met on paper).**
- *State:* about 3.7 min a cycle at 10 m with two people at the cranks. Cause: two people give about 100 W, so hoisting the full 93 kg grab 11 m takes 111 s, half the cycle; gearing cannot change this.
- *Option A:* a third person at the cranks during the hoist, on one crank with a 240 mm two-hand handle. Cycle about 3.1 min; cost about USD 10; mass about 0.5 kg. The problem statement's crews are three to five people.
- *Option B:* narrower shells, 240 mm wide. Cycle about 3.4 min; bite falls to about 15 L, so R3 is not met; cost about USD 10 less; mass about 4 kg less.
- *Option C:* keep two people and make 4 min the trial target. Cycle 3.7 min; no cost or mass change.
- **Recommendation: A.** It keeps the full bite and brings the cycle within about 5 % of the target with people the crew already has; the timed trial settles the last 0.1 min.

**2. R3, bite per cycle (at risk).**
- *State:* 21.2 L at an assumed 75 % fill; 14.1 L if the fill is 50 % in denser sand. Cause: through the 2:1 tackle the lips close with 0.71 of the line pull, and the line can pull no more than the grab's 618 N submerged weight before it lifts, so the lips close with only about 437 N.
- *Option A:* keep the 2:1 tackle and settle the fill in test-pit trials. No change to cost, mass or cycle.
- *Option B:* a 3:1 tackle, with a second sheave in the head. Lip force about 656 N (+50 %); about 1.5 s more a cycle; cost about USD 35; mass about 2.5 kg.
- *Option C:* 10 kg more ballast on the head. Lip force about 14 % more; working pull rises to about 1,114 N and the shear link's margin falls from 1.19 to 1.08; cost about USD 10; mass 10 kg.
- **Recommendation: B.** It raises the closing force most for the least mass and leaves the link margin unchanged.

**3. R1, depth gained below the water table (at risk).**
- *State:* the 8-ring string (16.4 kN effective) with eight saddles (1.6 kN) keeps sinking to 3 m only while skin friction stays below 1.66 kPa; the estimate for loose saturated sand is 1 to 3 kPa. Cause: the rings' own weight is the only driving force without pumps or jacks, and the saddles add 10 %.
- *Option A:* as designed (toes 15 mm past the ring's outer face) and measure friction in the first trial. No change.
- *Option B:* longer toes that cut 40 mm past the ring's outer face, loosening the soil against the ring so friction stays toward the low end of the range. T-bar force about 4 % more; cost about USD 10; mass about 0.5 kg.
- *Option C:* sixteen saddles instead of eight. The limit rises to 1.81 kPa; cost about USD 340 with lines; kit 165 kg heavier.
- **Recommendation: B.** It acts on the friction itself at almost no cost; C buys little for its weight.

**Decisions made under the pre-approvals.** SKG-DDR-002, the fifteen design-for-construction changes listed below; the scraper's 25 m working limit; the appearance model additions (below). All in `docs/06-design-decisions.md`.

**Build plan findings (design changes made for construction, SKG-DDR-002).**

1. Ground capstan 3.0 m from a lead sheave in a cradle under the leg A foot, joined by a drawbar; the HatchSide tripod sees its own winch load case.
2. A 150 mm head sheave grooved for the 8 mm line replaces HatchSide's wire-rope sheave while SinkGrab works.
3. Capstan frame in 40 x 40 x 2 tube: 22.9 kg (first model 32 kg).
4. Drum flanges and brake web 6 mm with lightening holes: 18.3 kg.
5. Pawl pivot moved behind the nose so its body clears the teeth.
6. Weighted band brake detailed; anchor and link separated.
7. Stake tubes and guard tabs moved to clear the braces and guard.
8. Grab lightened from 72 to 47.9 kg so the shear link keeps a 1.19 margin.
9. Interleaved hinge: shell B's end plates outside shell A's.
10. Shear link at the tackle dead end with a calibrated pin.
11. Scraper arms pinned to the hub and opened by struts from a sliding sleeve; fold to 364 mm.
12. Pole in 2.0 m sections with spigots and M12 bolts; T-bar socket and eye.
13. Well-head frame with two mesh doors, pole hole and datum brackets in place of a chute.
14. Eight U-saddles on their own lines in place of a ballast frame.
15. Pin holes 0.25 to 0.5 mm over the pin so each part rests on what holds it.

**Appearance model.** `product_model.py` uses the `model.py` solids. Additions not in `model.py`: the wound rope on the drum, the context collar, ground disc, spoil tub, cut-away ring pieces and a 1.75 m mannequin (`mannequin()`, standing at the -X crank facing the capstan, beside the kit and not between the camera and it). Decided under the pre-approvals.

**Safety concerns.**

- The HatchSide tripod is rated 150 kg for material handling. The shear link holds the grab to it; the crank pin caps any snag below its proof load. A link or crank pin replaced by a bolt removes both limits; the briefing card and safety stop 6 say so.
- The line jammed in a sheave (above the link) is limited only by the crank pin, up to 2.1 kN, which is inside the tripod's proof load but over its rating; stop 6 (find the snag with the line slack) covers it.
- Lowering depends on the brake weight; the cranks are removed so nothing spins if it slips.
- Undercutting can drop or tilt the rings; the sump limit and tilt stops are conservative and need trial data.
- Bad air: the gas detector is a bought item; its use is a stop, not a design feature.
- Nobody enters the well; any entry is a separate operation with its own equipment.

**Recommended next step.** After Amish decides R4, R3 and R1, the design is ready for TRL 4 when the phase allows: build the capstan, cradle and grab, proof-load them on CalRig with the HatchSide tripod, break-test the link and crank pins, then run the test-pit bite trial and the timed cycle trial before a partner well. Suggestion not added to the repo: an automatic load brake (Weston type) bought in would let the crew lower on the cranks and save about 20 s a cycle.

## Session 2026-09-30: scaffolded

### What was done

- Repository created from kit 1.6.0 at TRL 1, target TRL 2.
- `docs/01-problem.md` (SKG-PRB-001 v0.1): problem with cited evidence, users, environment, constraints, prior work, open questions.
- `docs/02-concept.md` (SKG-PRC-001 v0.1): how it works, components, patent design-arounds, shared blocks, safety.
- `docs/03-requirements.md` (SKG-REQ-001 v0.1): 11 proposed requirements.
- `README.md` with concept rationale, burning platform, where it could be used, and what sparked the idea.

### Next

- Run `/populate` to bring the repo to a strong TRL 2 with concept media.

## 2026-10-03: photoreal renders

Rendered with Blender Cycles on Amish's Mac from `cad/src/product_model.py`; captioned with `.kit/photo_caption.py`; `media/card.png` and `media/social-preview.png` made with `.kit/cards.py`. Views: hero, exploded, detail. image_qc passes and `render.py --check` has no FAIL.
