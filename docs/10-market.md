---
doc_id: SKG-MKT-001
title: SinkGrab market and viability
project: SinkGrab
doc_type: Market and viability
version: "0.2"
status: Draft
date: '2026-10-25'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-24'
  author: Amish Chadha
  change: First market and viability note (kit 1.9.1 upgrade)
- version: "0.2"
  date: '2026-10-25'
  author: Amish Chadha
  change: "Kit cost USD 3,063 after Amish's decision O4 of 2026-10-25 (slip clutch and load indicator)"
---

# SinkGrab market and viability

SinkGrab is for village well-digging crews and the WASH programmes and groundwater departments that employ them, where wells go dry because crews cannot dig far enough below the water table without pumps. What it competes with is not another product but a practice: a petrol pump to keep the well dry and a person digging at the bottom, which is cheaper to start and kills people; no open, village-scale tool for digging a flooded well from the surface was found (SKG-PRB-001, prior work). Prices are cited with the date they were checked; where none was found the entry says "to assess". Method: STANDARDS section 23.

Table 1. Market segments.

| Segment | Target users and region | Competitive benchmark (cited price) | Estimated cost per unit (USD) | Value proposition |
| --- | --- | --- | --- | --- |
| Dry-season deepening of lined wells | Well-digging crews and well committees; Kerala and other Indian states with dug wells; East African highlands | A 2 in petrol dewatering pump of the kind used to keep wells dry: GBP 459 (Honda WB20, Sal Marine, checked 2026-10-25), plus a person digging at the bottom; crew day rates to assess | 2,986 in parts for the kit (BOM), excluding the shared HatchSide tripod | No engine in or at the well, nobody at the bottom, and 2 to 3 m more water depth than the about 1 m crews reach without pumps |
| Rehabilitation and drought response | NGOs and district water departments running programmes across many wells | Bailing with buckets, then digging by hand (Oxfam WASH guidance); equipment cost to assess | 3,063 per kit, reused well after well | One kit on a pickup serves a programme; a documented method with stop rules that can be specified and inspected (UR-013) |
| New caisson wells, the wet part | Contractors and fabricators building new lined wells | Excavation inside smaller caisson rings with electric or compressor pumps (Abbott; WaterAid); price to assess | 3,063 per kit | Finishes the last metres below the water table without de-watering plant |
| Safety kit for any crew | Crews that dig by hand already | A portable carbon dioxide safety monitor: USD 399 (CO2Meter, checked 2026-10-25); a four-gas detector is BOM line 31 | 399 to 949 | Reads the gas most likely to collect in a well, which a four-gas detector does not |

## Open route

SinkGrab is built from steel section, plate, bought bearings, sheaves, chain and rope by a workshop with a stick welder, drill and access to plate rolls and a profile cutter (PR-010). It spreads through the people who already deepen wells: a groundwater department or an NGO commissions a local workshop to build a kit from the published drawings and build plan, proof-loads it on a rig such as CalRig, and lends it to crews with the briefing card. The design stays open under CERN-OHL-S-2.0, so a workshop that improves it shares the improvement; the calculation scripts are MIT licensed. Nothing is sold by Design Molecule. The first step is a co-design partner and a trial well (SKG-PLN-001).

## Sources

- Sal Marine. "Honda WB20 Water Pump, WB20XT4DRX." https://shop.salmarine.com/honda-wb20-water-pump-wb20xt4drx.html, GBP 459.00 special price (checked 2026-10-25).
- CO2Meter. "Portable 5% CO2 Safety Detector." https://co2meter.com/products/personal-co2-monitor, USD 399.00 (checked 2026-10-25).
- Inter Aide and Réseau Pratiques. *Rehabilitation of Hand-Dug Wells: Diagnostic and Technical Solutions*. Sierra Leone, 2012. https://bdd.pseau.org/outils/ouvrages/inter_aide_rehabilitation_of_hand_dug_wells_diagnostic_and_technical_solutions_2012.pdf (checked 2026-10-25): a dewatering pump of about 50 L/min at 15 m depth is what crews use to sink casings.
- Abbott, Akvopedia, Oxfam WASH and WaterAid: see SKG-PRB-001.
