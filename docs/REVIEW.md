# Review note: SinkGrab

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
