---
doc_id: SKG-REG-001
title: SinkGrab regulatory and standards register
project: SinkGrab
doc_type: Regulatory and standards register
version: "0.2"
status: Draft
date: '2026-10-25'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-24'
  author: Amish Chadha
  change: First register (kit 1.9.1 upgrade); drinking-water and manual-handling entries reuse the Food and water security focus-area research of WellSense (WLS-REG-001) and BankHaul (BKH-REG-001)
- version: "0.2"
  date: '2026-10-25'
  author: Amish Chadha
  change: "G1 points at PR-007 as restated by Amish's decision O4 of 2026-10-25 (proof at 1.25 x the rated load, slip clutch)"
---

# SinkGrab regulatory and standards register

SinkGrab is hand-powered lifting gear worked over an open well, so the rules that matter most are those for lifting equipment, gas testing at shafts and manual handling, then the rules for working on a drinking-water well. Nothing here is certified: SinkGrab is an open engineering reference at TRL 3, and every entry marked "to assess" needs a qualified reviewer in the trial country before any claim is made. Not legal advice. Drinking-water and manual-handling entries are the focus-area research already done for WellSense and BankHaul, cited again here. Method: STANDARDS section 23.

Table 1. Regulatory and standards register.

| # | Standard or regulation | Jurisdiction | What it covers | Applicability to this design | Owner (role) | Status |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | EN 13157, cranes, safety, hand powered cranes | European Union; reference elsewhere | Design, static and dynamic tests and marking of hand-powered lifting equipment | The hand capstan, lead sheave, line and HatchSide tripod working together as one hand-powered hoist; its test coefficients against PR-007's 1.25 x the rated load (restated 2026-10-25, SKG-DEC-001 O4), and how it treats a slip clutch as the overload limiter | Design lead | To assess |
| G2 | Machinery Directive 2006/42/EC, replaced by Machinery Regulation (EU) 2023/1230 | European Union | Essential safety requirements for machinery, including lifting machinery moved by hand | Only if SinkGrab were supplied in the EU; not at TRL 3 | Design lead | Does not apply now; to assess before any supply |
| G3 | Lifting Operations and Lifting Equipment Regulations 1998 (LOLER) | United Kingdom (practice reference) | Thorough examination, proof testing and records for lifting equipment | Reference practice for the proof load and daily checks (BLD safety stops 2 and 9) | Design lead | Reference only |
| G4 | EN 13889, forged steel shackles for general lifting, grade 6 | European Union; reference elsewhere | Rated shackles and their marking | The swivel and shackles (BOM line 29) | Design lead | To assess (buy rated and marked) |
| G5 | ISO 1141 (polyester fibre ropes), EN ISO 10547 (polyester double braid) and ISO 2307 (test methods) | International | Rope construction, minimum breaking force and its test | The 8 mm closing line, the recovery line and saddle lines (BOM lines 26 to 28); the 12 kN breaking strength assumed in SKG-CAL-001 E3 | Design lead | Applies when buying: specify to EN ISO 10547 or equal and ask for the test certificate |
| G6 | ANSI/ASSP A10.48 (via ASME B30.26 practice) | United States (practice reference) | Minimum sheave-to-rope ratio of 6:1 for double-braid rope | Sheaves and drum: 16.2 and 22.0 rope diameters (STEM S13) | Design lead | Met by design |
| G7 | ISO 11228-1 and ISO 11228-2, manual handling (lifting and carrying; pushing and pulling) | International | Reference masses and force limits for manual work | Pieces of 25 kg or less (PR-009); the grab never lifted by hand (K3); the spoil tub slid, not lifted (K4); the T-bar and jerk-bar forces (STEM B4, OB5) | Design lead | Applies; B4 assessment to do |
| G8 | EN 60079-29-1 (flammable gas detectors) and EN 45544 (toxic gas detectors) | European Union; reference elsewhere | Performance of portable gas detectors | The four-gas detector (BOM line 31) and the carbon dioxide monitor (line 35) are bought, not made | Design lead | To assess: buy detectors with a performance certificate and a calibration record |
| G9 | OSHA 29 CFR 1910.146, permit-required confined spaces | United States (practice reference) | Testing, entry permits, attendants and rescue for confined spaces such as wells | SinkGrab's method forbids entry; any entry for another reason is a separate operation (BLD safety stop 8) | Co-design partner | Reference only |
| G10 | WHO *Guidelines for Drinking-water Quality*, 4th edition incorporating the first and second addenda (2022) | International (guidance) | Microbial and chemical guidance, sanitary protection of groundwater sources | Context: SinkGrab adds nothing to the water; the well is cleaned and disinfected after the work | Co-design partner | Applies as guidance |
| G11 | IS 10500:2012, drinking water specification, Bureau of Indian Standards | India | Limits for drinking water quality | Context for the Kerala trial: the water is tested after the work, as for any well | Co-design partner | Applies as context |
| G12 | AWWA C654-13, disinfection of wells | United States (practice reference) | Disinfecting a well and the equipment put into it | Disinfecting the grab, scraper and well after the work (Oxfam guidance is the field reference) | Co-design partner | Reference only |
| G13 | Kerala Ground Water (Control and Regulation) Act, 2002, and the Central Ground Water Authority guidelines of 24 September 2020 | India (Kerala; pan-India where states do not regulate) | Permission to construct or deepen wells in notified areas | Deepening a well at the Kerala trial site | Co-design partner | To assess with the Kerala Ground Water Department |
| G14 | IS 3955:1967, code of practice for design and construction of well foundations | India | Bridge well foundations: sinking, tilt (1 in 60) and shift limits | Reference only: SinkGrab's 1 in 80 tilt stop is stricter (PR-006) | Design lead | Reference only |
| G15 | EN 10219 and EN 10025-2 (hollow sections; S235 and S275 structural steel), ISO 4017, ISO 4032, ISO 7089, ISO 2341 and ISO 1234 (fasteners and pins) | International | Stock sections, steel grades and fastener dimensions | Every made part and fastener in the detailed model | Design lead | Met by design |
| G16 | Local rules on lifting gear and work at open shafts at the trial site | Trial country | Inspection of lifting gear, barriers, gas tests | Both trial candidates (India, Ethiopia) | Co-design partner | To assess |

Status: to assess, applies, does not apply, met by design, certification needed later.

## Sources

- Bureau of Indian Standards. *IS 10500:2012, Drinking Water, Specification (Second Revision)*. As cited in WellSense (WLS-REG-001).
- American Water Works Association. *AWWA C654-13, Disinfection of Wells*. As cited in WellSense (WLS-REG-001).
- Central Ground Water Authority. *Guidelines to Regulate and Control Ground Water Extraction in India*, notification S.O. 3289(E), 24 September 2020. As cited in WellSense (WLS-REG-001).
- World Health Organization. *Guidelines for Drinking-water Quality*. 4th ed. incorporating the first and second addenda. Geneva: WHO, 2022.
- Messer, Caleb. "Rope and Rigging Compatibility, Part Two of Two." *Inside Towers*, September 6, 2019. https://insidetowers.com/cell-tower-news-rope-and-rigging-compatibility-part-two-of-two/ (checked 2026-10-25).
- BSI. *BS EN ISO 10547:2009, Polyester Fibre Ropes, Double Braid Construction*. https://knowledge.bsigroup.com/products/polyester-fibre-ropes-double-braid-construction (checked 2026-10-25).
- Henderson, Bob. "Measuring Carbon Dioxide Levels." *Safety+Health*, September 1, 2010 (gas detection practice). https://www.safetyandhealthmagazine.com/articles/measuring-carbon-dioxide-levels-2 (checked 2026-10-25).
- Oxfam WASH. "Repairing, Cleaning and Disinfecting Hand Dug Wells." https://www.oxfamwash.org/repairing-cleaning-and-disinfecting-hand-dug-wells/.
- EN 13157, EN 13889, ISO 1141, ISO 2307, ISO 11228-1 and -2, EN 60079-29-1, EN 45544, OSHA 29 CFR 1910.146, LOLER 1998, Directive 2006/42/EC, Regulation (EU) 2023/1230, IS 3955:1967, EN 10219, EN 10025-2 and the ISO fastener standards are cited by number; editions and applicability are to assess where marked.
