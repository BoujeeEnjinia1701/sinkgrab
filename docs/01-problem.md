---
doc_id: SKG-PRB-001
title: SinkGrab problem statement
project: SinkGrab
doc_type: Problem statement
version: "0.2"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-30'
  author: Amish Chadha
  change: Initial scaffold
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: TRL 2 update; first co-design candidate, safety section, open questions answered by the TRL 2 review (SKG-DDR-001) and replaced by questions for the first trials
---

# SinkGrab problem statement

A hand-dug well is only as reliable as its depth below the dry-season water table. Crews stop near the water table because digging further means pumping the well dry or working under water, and both are costly and dangerous.

## The problem

Standard practice for lined wells is to dig below the water table inside smaller precast caisson rings that sink as soil is removed from under them ([WaterAid technical brief](https://sswm.info/sites/default/files/reference_attachments/WATERAID%202013.%20Hand-dug%20wells.pdf)). The target is a minimum of 2 to 3 m of water depth ([Abbott, Hand Dug Wells manual](https://sswm.info/sites/default/files/reference_attachments/ABBOT%204000%20Hand%20Dug%20Well%20Manual.pdf)). Without de-watering pumps the limit of penetration is only about 1 m ([Akvopedia](https://akvopedia.org/wiki/Traditional_hand-dug_wells)), so the dry season finds the intake too shallow. The manual also warns that one of the greatest challenges in caisson sinking is keeping the bottom ring from falling out of line, with one side going ahead of the other ([Abbott](https://sswm.info/sites/default/files/reference_attachments/ABBOT%204000%20Hand%20Dug%20Well%20Manual.pdf)).

Existing methods all put a person at the bottom. The manual method is a short hoe and buckets inside the ring, with electric or compressor-driven pumps to keep the water down ([Abbott](https://sswm.info/sites/default/files/reference_attachments/ABBOT%204000%20Hand%20Dug%20Well%20Manual.pdf)); Oxfam's rehabilitation method is to bail the well with buckets and then excavate by hand ([Oxfam WASH](https://www.oxfamwash.org/repairing-cleaning-and-disinfecting-hand-dug-wells/)). Large bridge-foundation wells are sunk without anyone inside by dredging with a plate grab from a crane, and tilt is corrected by eccentric grabbing and loading ([Construction Civil](https://www.constructioncivil.com/well-sinking-tilt-shift-in-well-foundation/)). That principle works, but the equipment is crane-scale. Nothing open exists at the scale of a 1 m village well, worked by two or three people from a tripod.

## Users and context

| User | Need | Context |
| --- | --- | --- |
| Village well-digging crews | Dig 2 to 3 m below the water table without pumps or anyone under water | Dry-season deepening and new caisson wells, crews of 3 to 5 |
| WASH programme engineers (NGOs, district water departments) | A documented, repeatable method they can specify, train and inspect | Well rehabilitation programmes and drought response |
| Well committees and households | A well that gives water all year at a cost they can meet | Community and household wells, often shared |
| Local fabricators | Drawings they can build and repair with a welder, drill and hand tools | Small workshops near the well sites |

## Operating environment

- Hand-dug wells about 0.8 to 1.5 m internal diameter (estimate of the common range), lined with precast concrete or brick rings, with smaller caisson rings below the water table.
- Well depth about 5 to 30 m (estimate); water standing 0 to 3 m over the digging face.
- Soils from silt and fine sand to laterite, clay and gravel; boulders possible. Fine sand can boil up into the ring.
- Hot, dusty or wet surroundings; no mains power; work often in the dry season when water tables are lowest.
- Possible foul air in the shaft (carbon monoxide, carbon dioxide or hydrogen sulphide).

## Constraints

- Value-engineering target of USD 4,000 for the full kit, excluding the HatchSide tripod (a hypothetical control target, not a spending limit).
- No motor pump in or at the well during digging; human-powered only (hand capstan).
- No one in the well while the grab or scraper is working.
- Every piece carried by one or two people; total kit fits in a small pickup (target).
- Built from common steel section, rope and fasteners with hand tools and a stick welder.
- Hardware under CERN-OHL-S-2.0; any software or calculation scripts under MIT.

## Out of scope

- Drilled boreholes and machine-dug wells.
- Suction or jet dredging (sand dredger methods).
- Well lining design and ring casting (uses existing precast rings).
- Water quality treatment and handpump selection.
- Rescue from wells; HatchSide covers entry-free retrieval separately.

## Prior work

| Prior work | What it does | Gap for these users | Source |
| --- | --- | --- | --- |
| Abbott, Hand Dug Wells: Choice of Technology and Construction Manual | Field manual for caisson wells: dig with a short hoe inside the ring, sink rings 2 to 3 m below the water table, de-water with electric or compressor pumps | Needs a person at the bottom and a pump; does not cover digging from the surface | [link](https://sswm.info/sites/default/files/reference_attachments/ABBOT%204000%20Hand%20Dug%20Well%20Manual.pdf) |
| WaterAid technology brief, hand-dug wells | Excavation below the water table inside smaller precast caisson rings, with de-watering | Assumes de-watering to keep excavating | [link](https://sswm.info/sites/default/files/reference_attachments/WATERAID%202013.%20Hand-dug%20wells.pdf) |
| Oxfam, repairing, cleaning and disinfecting hand-dug wells | Bail with buckets, then excavate debris by hand; never lower a petrol or diesel pump into a well | Manual excavation at the bottom; slow bailing limits depth gained | [link](https://www.oxfamwash.org/repairing-cleaning-and-disinfecting-hand-dug-wells/) |
| Well foundation sinking with plate grab | Bridge-foundation wells sunk by grabbing soil under water, with eccentric grabbing and kentledge to correct tilt | Crane-scale plant for multi-metre wells; not usable at a 1 m village well | [link](https://www.constructioncivil.com/well-sinking-tilt-shift-in-well-foundation/) |
| CN101787703B, sinking well construction in saturated gravel (China 22MCC Group) | Open-caisson sinking in saturated gravel and pebble beds using a sand dredger moved around the well; active, anticipated expiry 2030 | Machine dredger method; SinkGrab uses a rope grab and scraper, not a dredger | [link](https://patents.google.com/patent/CN101787703B/en) |
| US1750728A, well-tool grab (expired) | Four-arm grab worked from the well mouth to retrieve lost tools | Fishing tool for lost equipment, not a soil grab | [link](https://patents.google.com/patent/US1750728) |

## Co-design

The design is meant to be tested in real wells with the crews who will use it. The first candidate to approach is the Kerala Ground Water Department through one of its district offices, with a village well-digging crew it already works with; a rural water NGO in the Ethiopian highlands is the second (SKG-DDR-001, item 12). Neither has been approached or has agreed.

## Safety

> **Safety:** Deepening a well is lifting work over an open shaft. People can fall into the well, be struck by a falling tool or a dropped load, be overcome by bad air in the shaft, or be caught when a lining ring drops suddenly. SinkGrab exists so that nobody works at the bottom; every part of the method keeps people at the surface, behind a barrier, with the shaft covered whenever the grab is up. It is an open engineering reference, not certified lifting or well-construction equipment.

## Questions for the first trials

The TRL 2 review answered the scaffold's open questions on paper (SKG-DDR-001): a two-shell clamshell rather than an orange peel; a centred pole and centralizer to guide the scraper; no de-watering, so the water inside the rings stays level with the water outside and the sand has no upward gradient to boil; tilt checked every cycle with a stop at 1 in 80; and the patent search for under-curb scraper claims before release. What only a trial can settle:

- How full the grab comes up in saturated fine sand, laterite and clayey sand (SKG-CAL-001 assumes 75 %).
- Whether the rings keep sinking to 3 m below the water table, and the skin friction that sets it (SKG-CAL-001 shows the limit is about 1.7 kPa).
- How evenly the scraper undercuts, and whether scraping the high side alone corrects tilt.
- The real cycle time at 10 m with two and with three people at the cranks.
