# SinkGrab

![SinkGrab: rope grab and under-curb scraper that deepen village wells under water](media/render-hero.png)

![TRL 3](https://img.shields.io/badge/TRL-3%20of%209-0F766E) ![Stage P3](https://img.shields.io/badge/stage-P3%20design%20outputs-0F766E) ![Hardware: CERN-OHL-S-2.0](https://img.shields.io/badge/hardware-CERN--OHL--S--2.0-111827) ![Software: MIT](https://img.shields.io/badge/software-MIT-111827) [![REUSE compliant](https://github.com/BoujeeEnjinia1701/sinkgrab/actions/workflows/reuse.yml/badge.svg)](https://github.com/BoujeeEnjinia1701/sinkgrab/actions/workflows/reuse.yml) [![Archived in Software Heritage](https://archive.softwareheritage.org/badge/origin/https://github.com/BoujeeEnjinia1701/sinkgrab/)](https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/BoujeeEnjinia1701/sinkgrab) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23132246.svg)](https://doi.org/10.5281/zenodo.23132246)

**Area:** Food and water security · **TRL:** 3 of 9 (proof of concept on paper; constructable design) · **Stage:** P3, design outputs · **Value-engineering target:** USD 4,000; estimated parts cost USD 3,063 · **Difficulty:** 3 of 5

Deepens village wells under water with a rope grab and under-curb scraper, without divers or pumps.

![SinkGrab: rope grab and under-curb scraper that deepen village wells under water](media/render-hero.png)

[Interactive 3D model](media/viewer.html) · [Concept blueprint (PDF)](media/concept-blueprint.pdf) · [Well-head layout SKG-DWG-001 (PDF)](cad/drawings/SKG-DWG-001.pdf) · [STEM check](docs/01b-stem-check.md) · [Concept options](docs/02a-concept-options.md) · [Requirements](docs/03-requirements.md) · [Traceability](docs/03b-traceability.md) · [Sizing note SKG-CAL-001](docs/04-calcs/01-sizing.md) · [Prototype build plan](docs/05-build-plan.md) · [Decisions](docs/06-design-decisions.md) · [Review note](docs/REVIEW.md)

> CONCEPT, NOT FOR FABRICATION. SinkGrab is a TRL 3 design on paper: it has not been built or tested.

## Concept rationale

A hand-dug well only gives water all year if its intake sits well below the lowest seasonal water level. Guidance for caisson wells is to keep excavating and sinking rings typically 2 to 3 m below the water table ([Abbott, Hand Dug Wells manual](https://sswm.info/sites/default/files/reference_attachments/ABBOT%204000%20Hand%20Dug%20Well%20Manual.pdf)). Without de-watering the practical limit is about 1 m ([Akvopedia](https://akvopedia.org/wiki/Traditional_hand-dug_wells)). The usual answers are a motor pump to bail the well, or a person working under water. SinkGrab removes both: the digging and the undercutting are done by tools on ropes, worked from the surface.

SinkGrab is two tools and a routine. A rope-closed grab bites soil from the bottom of the flooded well inside the caisson rings and lifts it out. An under-curb scraper reaches under the cutting edge of the bottom ring so the lining sinks evenly as the soil is removed. Both hang from the HatchSide tripod and are worked with a hand capstan, so the crew stays at the top. Everything is built from steel section, rope and hand tools, and is published under open licences so village fabricators can copy and repair it.

## Burning platform

About 296 million people still drink from unprotected wells or springs ([Our World in Data, from WHO/UNICEF JMP 2024](https://ourworldindata.org/what-no-safe-water-means)). Many more rely on protected hand-dug wells that fail in the dry season: 'Hand-dug wells have a tendency to have very little water or even dry up in the dry season', largely because the intake is not deep enough below the seasonal water table, which can move several metres between seasons ([Akvopedia](https://akvopedia.org/wiki/Traditional_hand-dug_wells)). In Ethiopia's 2015/16 drought, hand-dug wells dried up while monitored boreholes kept the same flow all year, and people without boreholes queued for up to 10 hours for water ([BGS](https://www.bgs.ac.uk/news/study-shows-boreholes-are-key-to-drought-resilience-in-ethiopia/)).

Going deeper under water is dangerous. Oxfam's guidance says a diesel or petrol pump or its engine must never be lowered into a well, because carbon monoxide collects there ([Oxfam WASH](https://www.oxfamwash.org/repairing-cleaning-and-disinfecting-hand-dug-wells/)). In August 2023 three men died in Mutare, Zimbabwe, while draining a well about 19 m deep with a petrol pump ([ZimLive, 2023](https://www.zimlive.com/3-killed-in-carbon-monoxide-poisoning-after-turning-on-generator-in-a-well/)). In August 2026 four men died of suspected toxic gas while repairing a motor inside a well in Gaya Ji, Bihar ([The Tribune, 2026](https://www.tribuneindia.com/news/india/4-die-of-asphyxiation-after-inhaling-toxic-gas-inside-well-in-bihars-gaya-ji/)). Every hour a person spends at the bottom of a well is exposure; tools that dig from the surface cut that exposure.

## Where it could be used

### By industry

| Industry | Use |
| --- | --- |
| Rural water supply and WASH programmes | Deepening existing hand-dug wells so they last through the dry season |
| Well-digging contractors and village fabricators | A safer, pump-free way to finish the wet part of a new caisson well |
| Smallholder irrigation | Deepening dug wells used for garden and livestock water |
| Drought and humanitarian response | Rehabilitating dry community wells quickly with a kit that travels on a pickup |
| Small civil works | Sinking small precast caissons for pump sumps and soakaways |
| Engineering education | A documented case study in caisson sinking, rope mechanics and field safety |

### By country or region

| Country or region | Why it matters there |
| --- | --- |
| India (Kerala) | About 65% of rural and 59% of urban households depend on wells, and 48% of 45 lakh wells surveyed in 2003 dried up in summer ([SOPPECOM, citing Census 2011 and the Kerala Water Authority](https://www.soppecom.org/pdf/Groundwater-Resource-and-Governance-in-Kerala.pdf)). |
| India (Thiruvananthapuram) | Well diggers report that in summer they must dig an extra 10 to 15 feet (3 to 4.5 m) down, and one crew dug more than 70 wells in three months ([Deccan Chronicle, 2017](https://www.deccanchronicle.com/nation/in-other-news/040517/thiruvananthapuram-well-diggers-strike-gold-in-summer.html)). |
| Ethiopia | In the 2015/16 drought hand-dug wells dried up and many became grossly contaminated, while boreholes held their flow ([BGS](https://www.bgs.ac.uk/news/study-shows-boreholes-are-key-to-drought-resilience-in-ethiopia/)). |
| Zimbabwe | Three men died of carbon monoxide in 2023 while draining a 19 m well with a petrol pump, the risk SinkGrab is designed to remove ([ZimLive, 2023](https://www.zimlive.com/3-killed-in-carbon-monoxide-poisoning-after-turning-on-generator-in-a-well/)). |
| Global | About 296 million people use unprotected wells or springs ([Our World in Data, 2024 JMP data](https://ourworldindata.org/what-no-safe-water-means)); upgrading and deepening dug wells is one of the cheapest paths to year-round water for them. |

## What sparked the idea

In August 2023 three men in Mutare, Zimbabwe, were draining a well about 19 m deep so they could work at the bottom. The petrol pump they used filled the shaft with exhaust and all three died ([ZimLive, 2023](https://www.zimlive.com/3-killed-in-carbon-monoxide-poisoning-after-turning-on-generator-in-a-well/)). Oxfam's field guidance forbids exactly this ([Oxfam WASH](https://www.oxfamwash.org/repairing-cleaning-and-disinfecting-hand-dug-wells/)), yet the job still has to be done, because a well that is not deep enough goes dry. SinkGrab starts from that gap: if the water cannot safely be taken out, the soil has to be.

## Problem

Hand-dug wells go dry in the dry season because crews cannot dig far enough below the water table without pumps, and pumps and divers in wells kill people. Well diggers need a way to keep digging under water and sink the lining from the surface.

Full problem statement: [docs/01-problem.md](docs/01-problem.md)

## Concept

A rope grab and under-curb scraper worked from the HatchSide tripod and a hand capstan; well diggers lower them into a flooded hand-dug well to dig soil out under water and undercut the curb ring so the lining sinks, without divers or pumps. One 8 mm line does everything: the grab goes down closed, its head's weight opens it on the bottom, and two people at the cranks, three during the hoist, close it through a 3:1 tackle on a bite of about 21 L and lift it. A friction slip clutch on the crank shaft keeps the line inside the tripod's 150 kg rating, and a load indicator at the tackle's dead end shows the peak of every lift. The scraper's arms open under the cutting edge when the pole's weight rests on its foot, and four people turn it with a T-bar through the closed well-head doors. On paper it lifts 21 L a bite with 55 N on each crank, a cycle at 10 m takes about 3.2 min (0.2 min over the target, for the timed trial to settle), and the rings keep sinking to 3 m only while skin friction stays below about 1.7 kPa, which the first well trial must measure; a bentonite slurry fed into the overcut annulus is part of the sinking method to keep it low (SKG-CAL-001).

![SinkGrab concept at the well head, with a 1.75 m person for scale](media/hero.png)

Full design precis: [docs/02-concept.md](docs/02-concept.md) · Problem statement: [docs/01-problem.md](docs/01-problem.md)

## STEM check

Forty-eight claims are checked for both concept options (SKG-STM-001): 33 are within known science, 13 need a trial at TRL 4 and two fail with a fix proposed for option B only, so the check stays open. An independent reviewer found that two things the design relied on did not hold on paper: the caisson rings sinking 3 m without de-watering (the central friction estimate already stops them) and a release window for the shear link and crank pin between the working pull and the tripod's rating; the scraper's turning force was also over sustained push limits. On 2026-10-25 Amish chose the recommended fixes: a bentonite-lubricated annulus, a calibrated slip clutch with a load indicator in place of both shear devices (proof at 1.25 times the rated load), and four people at the T-bar; the test pit and CalRig confirm them at TRL 4. Five details failed when first checked on the detailed model and are now fixed in the design under Amish's standing instruction: the shear link's pin bent across an open gap (the link has since been replaced), the brake's weight slackened the band, the assembled grab was lifted by two people, the full spoil tub had no safe way off the doors, and the gas detector did not read carbon dioxide; after the review, the gas is also read at depth, not only at the collar.

## Concept options

![Two ways to dig a flooded well from the surface, side by side at one scale](media/options.png)

Option A, the rope grab and under-curb scraper (score 167), is the current design; option B, a dart-valve bailer spudded on a jerk line (153), is modelled to the same detail. They are within 10 % of each other, so both are with Amish to decide (SKG-OPT-001, SKG-DDR-005). Option A is the only one that cuts under the ring, steers the lining and digs laterite and clay; option B is simpler, lighter and cheaper but works only in running sand. The picture is a shaded preview until the Cycles render is made.

## Key components

- Hand capstan: winding drum, 4:1 chain with a friction slip clutch, pawl, weighted band brake, removable cranks
- Foot cradle with lead sheave under the HatchSide leg A foot, and a drawbar back to the capstan
- Two-shell clamshell grab on one closing line, with a load indicator at its tackle's dead end
- Under-curb scraper head on 2 m pole sections, turned with a T-bar
- Well-head frame with folding doors, pole hole and tilt datum; spoil tubs
- Ballast saddles (8) and a dip tape and plumb line for tilt
- Four-gas detector, carbon dioxide monitor and barrier kit

## Building the prototype

The capstan, cradle, drawbar, grab, scraper, well-head frame and saddles are welded from stock steel tube, plate and bar, with the shell skins rolled and a few plates profile-cut; the bearings, chain drive, sheaves, ropes and rigging are bought. The build plan takes a capable maker through every component in build order with a making sketch, joint close-ups and a picture for each of its 20 assembly steps, all drawn from the detailed model with every bolt, pin and weld, and lists the safety stops before anything is lifted over a well. The parts cost about USD 3,063. It is a plan, not yet built.

![SinkGrab prototype: every component in build order](docs/05-build-plan/overview.png)

## Safety

> Published as an open engineering reference, not certified lifting or well-construction equipment.
>
> This is lifting equipment over an open shaft: the tripod, capstan, hooks and ropes must be proof-loaded (CalRig) and inspected before use, and nobody stands under a suspended load.
>
> No one enters the well while the grab or scraper is in use. Any entry needs a gas test, a harness on a separate line and a person at the top at all times.
>
> Test the shaft air with the four-gas detector and the carbon dioxide monitor before work, after breaks and before anyone leans over the shaft; a four-gas detector alone does not read carbon dioxide, which collects in wells.
>
> The assembled grab (52.7 kg) and a full spoil tub are never lifted by hand: the grab moves only on the line, the tub is slid off the doors on a board.
>
> Never lower or run a petrol or diesel engine in or beside the well mouth; exhaust collects in the shaft.
>
> Undercutting can make rings drop suddenly or tilt; scrape evenly, keep a controlled sump and stop if tilt exceeds the limit.
>
> Keep a barrier and cover around the well head to prevent falls.
>
> The line is limited by a friction slip clutch on the crank shaft, set on CalRig, so the HatchSide tripod is never loaded past its rating; never tighten the clutch on site, and read the load indicator after every lift. The well-head doors are closed whenever the grab is up, and the cranks come off before lowering on the brake. Stop and correct when tilt passes 1 in 160; stop undercutting at 1 in 80. See the safety stops in the [build plan](docs/05-build-plan.md).
>
> This design is published as an open engineering reference. It is not certified equipment.

## Repository layout

```
docs/                 controlled documents (PRB, STM, OPT, PRC, URS, PRS, RTM, CAL, BLD, DEC, REG, FEA, RSK, MKT, PLN, DDR) and REVIEW.md
docs/04-calcs/        sizing.py (SKG-CAL-001) and stem_check.py (SKG-STM-001)
cad/src/model.py      parametric model of options A and B (kit 1.9, detail level D3)
cad/src/              skg_detail.py, skg_option_b.py, skg_parts.py, sheets.py, build_plan_media.py, concept_media.py,
                      product_model.py, options_preview.py
cad/step/, cad/stl/   STEP per part of option A, an assembly STEP per option, group STEP and STL of option A
cad/drawings/         SKG-DWG-001 and 002 general arrangements, SKG-DWG-101 to 117 making sketches
bom/bom.csv           priced bill of materials
media/                concept media and renders
.kit/                 shared documentation kit 1.9.1 (do not edit here)
```

## Documentation

Controlled documents follow the portfolio [documentation standard](.kit/STANDARDS.md). Each carries a document ID (SKG-PRC-001 for the precis), a version and a revision history. Run `python .kit/render.py --check` to validate them, `python .kit/cad_check.py --export` for the CAD fidelity check, `python docs/04-calcs/sizing.py` for the calculations and `python docs/04-calcs/stem_check.py` for the STEM check. Branded PDFs are built with `python .kit/render.py` and attached to GitHub Releases when a document is tagged, for example `SKG-PRC-001/v1.0`.

## Credits

Designed by Amish Chadha at Design Molecule Labs. See [CONTRIBUTORS.md](CONTRIBUTORS.md) for roles. To cite this design, use [CITATION.cff](CITATION.cff) (GitHub shows it as "Cite this repository").

AI assistance (Claude) was used to accelerate research, calculations, CAD and documentation. Design direction and all decisions are Amish Chadha's, recorded in [docs/06-design-decisions.md](docs/06-design-decisions.md) and the decision records (`docs/decisions/`).

## Licenses

- **Hardware** (CAD, drawings, BOM, electronics): [CERN-OHL-S v2](LICENSE)
- **Software** (firmware, scripts, notebooks): [MIT](LICENSE-SOFTWARE)

A project of the [Design Molecule](https://designmolecule.com) lab.
