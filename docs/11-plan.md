---
doc_id: SKG-PLN-001
title: SinkGrab project plan
project: SinkGrab
doc_type: Project plan
version: "0.2"
status: Draft
date: '2026-10-25'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-24'
  author: Amish Chadha
  change: First project plan with the reference list (kit 1.9.1 upgrade, stage P3)
- version: "0.2"
  date: '2026-10-25'
  author: Amish Chadha
  change: "Amish's decisions of 2026-10-25 (O2 to O5) recorded; O1 still open; CalRig tasks for the slip clutch and load indicator; cost USD 3,063"
---

# SinkGrab project plan

SinkGrab is at TRL 3 and stage P3 (design outputs): the detailed model, drawings, priced BOM, build plan and decisions register exist for option A, and option B is modelled to the same detail. The next gate is P4 (verification, TRL 4), on hold under the portfolio cap; before it Amish is asked to decide the concept (SKG-DEC-001 O1), how the rings are helped to sink (O2), the two new requirements (O3), the overload device and proof basis (O4) and the scraper turning force (O5). Method: STANDARDS sections 19 and 23.

## Workstreams

Table 1. Workstreams.

| Workstream | Owner (role) | Deliverable | Status |
| --- | --- | --- | --- |
| Concept and requirements | Amish (owner) | Concept choice (O1); PR-012 and PR-013 accepted 2026-10-25 (O3) | Concept choice awaiting Amish |
| Design and model | Design lead | Detailed D3 model of both options; drawings, STEP and STL of option A | Done on paper (2026-10-24) |
| Calculations and STEM check | Design lead | SKG-CAL-001 v0.6; SKG-STM-001 v0.3 with two rows failing (option B, with O1) and thirteen open until trials, after Amish's decisions of 2026-10-25 | Done on paper; open rows need TRL 4 |
| Build plan | Design lead | SKG-BLD-001 for option A with the kit 1.9.1 fixes | Done on paper |
| Co-design partner | Amish (owner) | Agreement with the Kerala Ground Water Department or the Ethiopian NGO | Not started |
| Proof loading | Test lead (CalRig) | Proof-load record for the line, cradle, capstan and tripod | On hold (TRL 4) |
| Trials | Co-design partner with the design lead | Bite trial, timed cycle trial, fold check, first well | On hold (TRL 4 and 5) |
| Patent screen | Amish (owner) | Targeted search for under-curb scraper claims | Before public release |

## Resources needed

Table 2. Resources (P4 and later on hold).

| Resource | Deliverable | Effort | Estimated cost (USD) |
| --- | --- | --- | --- |
| Partner workshop | Build of the option A kit from the drawings | About 2 to 3 weeks for two people (estimate) | 3,063 in parts (BOM); labour to assess |
| CalRig and a load cell | Proof load of 188 kg (1.25 x the rated load); slip clutch setting on each rope layer; load indicator calibration | 2 days (estimate) | To assess |
| Test pit of saturated sand, laterite and clayey sand | Bite and fill per soil (PR-003, PR-013); option B fill if chosen | 1 week (estimate) | To assess |
| Partner well and crew | Timed cycle (PR-004), sinking and skin friction (PR-001), tilt (PR-006) | 2 weeks (estimate) | To assess |
| Ergonomics reviewer | ISO 11228-2 assessment of the T-bar (STEM B4) | 2 days (estimate) | To assess |
| Regulatory reviewer in the trial country | Lifting gear, gas testing and well permission rules (SKG-REG-001) | 2 days (estimate) | To assess |

## Stage gates

Table 3. Stages (P4 to P6 on hold while the stage cap is P3).

| Stage | Gate criteria | Status |
| --- | --- | --- |
| P0 Proposal | PRB, STM, OPT, REG, FEA, PLN | Met (2026-10-24 for the pipeline documents) |
| P1 Definition | URS, PRS, RSK, MKT | Met |
| P2 Design inputs | PRS with targets and verification, CAL, RTM, concept selection DDR | Met; the concept selection is awaiting Amish (SKG-DDR-005) |
| P3 Design outputs | Model at D3, STEP, drawings, priced BOM, BLD, DEC, design FMEA, traceability | Met on paper (2026-10-24) |
| P4 Verification | Proof-load and lab test reports, verification report | On hold |
| P5 Validation | Partner well trials, human factors | On hold |
| P6 Commercialization | Open route with a named deployment partner | On hold |

## Next steps and decision requested

1. Amish decides O1 (concept: A, the current design, or B). O2 to O5 were decided on 2026-10-25 (bentonite annulus, PR-012 and PR-013, slip clutch and load indicator with proof at 1.25 x the rated load, four people at the T-bar).
2. The coordinator renders `media/options.png` and the product renders (hero, studio) in Cycles from `cad/src/model.py` and `cad/src/product_model.py`.
3. When the portfolio phase allows TRL 4: build, set the slip clutch and calibrate the load indicator on CalRig, proof-load, fold the scraper through a 0.8 m ring, then the bite and timed cycle trials and the bentonite annulus in the test pit before a partner well.

## References

- Abbott. *Hand Dug Wells: Choice of Technology and Construction Manual*. https://sswm.info/sites/default/files/reference_attachments/ABBOT%204000%20Hand%20Dug%20Well%20Manual.pdf.
- Akvopedia. "Traditional Hand-Dug Wells." https://akvopedia.org/wiki/Traditional_hand-dug_wells.
- American Water Works Association. *AWWA C654-13, Disinfection of Wells*.
- British Geological Survey. "Study Shows Boreholes Are Key to Drought Resilience in Ethiopia." https://www.bgs.ac.uk/news/study-shows-boreholes-are-key-to-drought-resilience-in-ethiopia/.
- Bureau of Indian Standards. *IS 10500:2012, Drinking Water, Specification*; *IS 3955:1967, Code of Practice for Design and Construction of Well Foundations*.
- Central Ground Water Authority. *Guidelines to Regulate and Control Ground Water Extraction in India*, S.O. 3289(E), September 24, 2020.
- Construction Civil. "Well Sinking: Tilt and Shift in Well Foundation." https://www.constructioncivil.com/well-sinking-tilt-shift-in-well-foundation/.
- CO2Meter. "Portable 5% CO2 Safety Detector." https://co2meter.com/products/personal-co2-monitor (checked 2026-10-25).
- Deccan Chronicle. "Thiruvananthapuram: Well Diggers Strike Gold in Summer." 2017. https://www.deccanchronicle.com/nation/in-other-news/040517/thiruvananthapuram-well-diggers-strike-gold-in-summer.html.
- Henderson, Bob. "Measuring Carbon Dioxide Levels." *Safety+Health*, September 1, 2010. https://www.safetyandhealthmagazine.com/articles/measuring-carbon-dioxide-levels-2.
- Inter Aide and Réseau Pratiques. *Rehabilitation of Hand-Dug Wells: Diagnostic and Technical Solutions*. 2012.
- Messer, Caleb. "Rope and Rigging Compatibility, Part Two of Two." *Inside Towers*, September 6, 2019.
- Network Rail. "Lifting and Handling in Teams." https://safety.networkrail.co.uk/safety/manual-handling/principles-of-manual-handling/lifting-and-handling-in-teams/.
- Our World in Data. "What Does It Mean to Not Have Access to Safe Water?" https://ourworldindata.org/what-no-safe-water-means.
- Oxfam WASH. "Repairing, Cleaning and Disinfecting Hand Dug Wells." https://www.oxfamwash.org/repairing-cleaning-and-disinfecting-hand-dug-wells/.
- Sal Marine. "Honda WB20 Water Pump, WB20XT4DRX." https://shop.salmarine.com/honda-wb20-water-pump-wb20xt4drx.html (checked 2026-10-25).
- SOPPECOM. *Groundwater Resource and Governance in Kerala*. https://www.soppecom.org/pdf/Groundwater-Resource-and-Governance-in-Kerala.pdf.
- Terzaghi, Karl, Ralph B. Peck and Gholamreza Mesri. *Soil Mechanics in Engineering Practice*. 3rd ed. New York: Wiley, 1996.
- The Tribune. "4 Die of Asphyxiation after Inhaling Toxic Gas inside Well in Bihar's Gaya Ji." 2026. https://www.tribuneindia.com/news/india/4-die-of-asphyxiation-after-inhaling-toxic-gas-inside-well-in-bihars-gaya-ji/.
- WaterAid. *Technology Brief: Hand-Dug Wells*. 2013. https://sswm.info/sites/default/files/reference_attachments/WATERAID%202013.%20Hand-dug%20wells.pdf.
- World Health Organization. *Guidelines for Drinking-water Quality*. 4th ed. incorporating the first and second addenda. Geneva: WHO, 2022.
- ZimLive. "3 Killed in Carbon Monoxide Poisoning after Turning on Generator in a Well." 2023. https://www.zimlive.com/3-killed-in-carbon-monoxide-poisoning-after-turning-on-generator-in-a-well/.
- Patents: CN101787703B and US1750728A, see SKG-PRB-001.
- Standards cited by number in SKG-REG-001: EN 13157, EN 13889, EN ISO 10547, ISO 1141, ISO 2307, ISO 11228-1 and -2, EN 60079-29-1, EN 45544, OSHA 29 CFR 1910.146, LOLER 1998, Directive 2006/42/EC, Regulation (EU) 2023/1230, EN 10219, EN 10025-2, ISO 4017, ISO 4032, ISO 7089, ISO 2341, ISO 1234.
