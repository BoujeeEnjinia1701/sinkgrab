"""SinkGrab STEM check (SKG-STM-001, STANDARDS section 20), kit 1.9.1 upgrade.

Run from the repo root:  python docs/04-calcs/stem_check.py
Writes docs/04-calcs/stem_results.csv (one row per claim), read by docs/01b-stem-check.md.
Geometry and masses come from the detailed kit 1.9 model (cad/src/model.py PARAMS, derived(), masses() and the
option B parts); the assumptions are those of SKG-CAL-001 Table 1. First-order screens, not the calculation note.
Rows that failed when first checked on 2026-10-24 and were fixed under Amish's standing instruction of 2026-10-23
are closed here by the decision that fixed them (SKG-DEC-001); the failure is described in SKG-STM-001.
Rows revised after the independent review of 2026-10-25 say so in their detail (SKG-STM-001, Independent review).
Rows S4 to S7, S10, S10a, S15, S16, S18, S21, E2, B4 and OB2 were restated on 2026-10-25 for Amish's decisions O2, O4 and O5
of that day (SKG-DEC-001): bentonite in the overcut annulus, a crank slip clutch and dead-end load indicator in place of
both shear devices with proof at 1.25 x the rated load, and four people at the T-bar.
"""
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
from stem_check import Check, limits, WITHIN, PLAUSIBLE, FIX, FAILS  # noqa: E402,F401
from model import PARAMS as P, derived, masses  # noqa: E402
import cad_parts as cp  # noqa: E402
import skg_option_b as OB  # noqa: E402

D = derived(P)
M = masses(P)
g = 9.81
c = Check(ROOT / "docs/04-calcs/stem_results.csv")

# same assumptions as SKG-CAL-001 Table 1
A = dict(rho_sand=2.00, rho_sub=1.00, fill=0.75, water_L=3.0, dyn=1.10, tau=240e6, phi=30.0, gamma_sub=10.0e3,
         hs_swl=150.0, person_W=50.0, f_lo=1.0, f_hi=3.0, rho_conc=2400.0, k_fric=1.11, mu_lining=0.35, tol=0.05)

grab_keys = ["head", "ballast", "tie_rods", "shell_pins", "shell_a", "shell_b", "crosshead", "hinge_pin",
             "cross_sheave", "cross_axle", "upper_sheave", "upper_axle", "load_link"]
m_grab = sum(M[k] for k in grab_keys)
R, B = P["shell_R"] / 1000, P["shell_B"] / 1000
V_geo = math.pi * R * R / 2 * B * 1000
V_bite = V_geo * A["fill"]
m_air = m_grab + V_bite * A["rho_sand"] + A["water_L"]
m_sub = m_grab * (1 - 1000 / 7850) + V_bite * A["rho_sub"]
T_work = m_air * g * A["dyn"]
swl = A["hs_swl"] * g
# crank slip clutch (decision O4): highest slip (layer 1, +5 %) set to the HatchSide rating, as SKG-CAL-001 C
eta = 0.95 * 0.98 ** 2
rp_l = [pd / 2000 for pd in D["layer_pd"][:3]]
slip = [swl / (1 + A["tol"]) * rp_l[0] / r for r in rp_l]
slip_lo, slip_hi = slip[2] * (1 - A["tol"]), slip[0] * (1 + A["tol"])
T_slip = slip[0] * rp_l[0] / (D["ratio"] * eta)
Ro, Ri = P["clutch"][0] / 2000, (P["clutch"][1] / 2 + 2.0) / 1000
r_m = 2 / 3 * (Ro ** 3 - Ri ** 3) / (Ro ** 2 - Ri ** 2)
steady = m_air * g * A["k_fric"]

# ------------------------------------------------------------------------------------------------ physics
c.order_of_magnitude("M1", "Closed shells hold 28.3 L; a bite is 21.2 L at the assumed 75 % fill", "Mathematics", "Units and dimensional analysis",
                     claimed=28.3, estimate=V_geo, unit="L", law="Two quarter cylinders, V = pi R^2 B / 2", closed_by="SKG-CAL-001 A1")
stroke = D["stroke"]
lip = 2 * P["shell_R"] * math.radians(P["open_deg"])
k_close = P["tackle"] * stroke / lip
c.order_of_magnitude("S1", "3:1 tackle closes the lips with about 1.06 times the line pull", "Physics", "Mechanics and statics",
                     claimed=1.06, estimate=k_close, unit="x line pull", law="Virtual work: line travel / lip travel (frictionless)", closed_by="SKG-CAL-001 B2")
# closing resistance: passive drag on each lip at the bite depth (Rankine Kp) against the force the tackle gives
kp = math.tan(math.radians(45 + A["phi"] / 2)) ** 2
d_bite = P["shell_R"] / 1000
F_res = 0.5 * A["gamma_sub"] * d_bite ** 2 * kp * B
F_lip = k_close * m_sub * g / 2
m_empty_sub = m_grab * (1 - 1000 / 7850)
c.cited("S2", "The lips close a full bite in loose saturated sand (force per shell against passive drag at full bite depth)", "Physics", "Mechanics and statics",
        law="Rankine passive resistance 0.5 gamma' d^2 Kp B, phi' 30 deg, gamma' 10 kN/m3, d = shell radius; virtual work through the 3:1 tackle",
        detail=(f"Drag about {F_res:.0f} N per shell against {F_lip:.0f} N per shell with the full grab's submerged weight on the line. Revised after the independent review: "
                f"closing starts with the grab empty ({m_empty_sub * g:.0f} N submerged), sheave friction (three sheaves, 10 to 15 %) is left out, whether 1.06 T acts on each lip "
                "or on both is not settled, and denser sand (phi' 40 deg) roughly doubles the drag; the margin lies between about 0.9 and 1.8, so the bite stays open until the test-pit trial"),
        verdict=PLAUSIBLE)
c.cited("S3", "The head's weight opens the shells when the line is slacked on the bottom", "Physics", "Mechanics and statics",
        law="Single-rope grabs open under their own head weight on slack line; resistance is the shells' pins and the sand lying on the lips",
        detail=f"head and ballast {M['head'] + M['ballast']:.1f} kg; the lips ride up and outward over the surface as they open; confirmed only by a bite trial",
        verdict=PLAUSIBLE)
c.claim("S4", "The steady pull of the full grab at the capstan stays below the slip clutch's lowest slip", "Physics", "Mechanics and statics",
        law="Weight of the full grab in air x 1.11 sheave and guide tube friction against the clutch's slip on the third layer at the low end of a +/-5 % setting",
        value=round(steady), limit=round(slip_lo), unit="N", rule="below", closed_by="SKG-CAL-001 C4; SKG-DEC-001 O4")
c.cited("S5", "The dead-end load indicator shows the highest pull of each lift", "Physics", "Mechanics and statics",
        law="Hooke's law for a stack of disc springs in series (deflection adds, load is shared); a friction tell-tale on the rod keeps the largest travel",
        detail=("Restated for Amish's decision O4 of 2026-10-25: the shear link and its calibrated pin are gone (they were fixed under K1 for true double shear). Fourteen "
                "disc springs 18 x 9.2 x 1.0 give about 2.8 mm of rod travel at 1.47 kN on catalogue values to confirm; disc springs have some hysteresis and the tell-tale "
                "reads to about one 0.25 kN ring; calibrated on CalRig and checked in the mud at TRL 4"), verdict=PLAUSIBLE)
work_frac = (m_air * g * rp_l[2] / (D["ratio"] * eta)) / T_slip
c.cited("S6", "The crank slip clutch caps the capstan pull at the HatchSide tripod's 150 kg rating", "Physics", "Mechanics and statics",
        law="Friction clutch, T = 2 mu F r_m (two faces, uniform pressure), mu 0.35 for a dry woven facing on ground steel; 4:1 chain; innermost rope layer",
        detail=(f"Restated for Amish's decision O4 of 2026-10-25 (it replaces the 3 mm shear pin, which ran above shear yield in normal hoisting): a {T_slip:.1f} N m slip from a "
                f"{T_slip / (2 * A['mu_lining'] * r_m):.0f} N clamp gives {slip_hi:.0f} N at the high end of a +/-5 % setting on the first layer. The facing friction moves "
                f"with moisture and glazing, so the setting rests on CalRig before each campaign and a dry lining inside the guard; in ordinary hoisting it carries about "
                f"{work_frac:.0%} of its slip torque, which a friction face takes without fatigue"), verdict=PLAUSIBLE)
c.cited("S7", "The slip window carries the full grab on every rope layer and stays inside the rating", "Physics", "Mechanics and statics",
        law="One slip torque gives a line pull that falls as the rope builds up on the drum (layer radii 88 to 104 mm); sheave and guide tube friction about 11 %",
        detail=(f"Lowest slip {slip_lo:.0f} N (layer 3, low end) against a steady pull of {steady:.0f} N, a margin of {slip_lo / steady:.2f}; highest {slip_hi:.0f} N against the "
                f"{swl:.0f} N rating. A jerked start or breakout suction (about 160 N) makes it slip for a moment and the pawl holds; nothing releases. At +/-10 % the "
                f"layer 3 low end falls to about {slip[2] * 0.9 * 1.05 / 1.10:.0f} N, under the steady pull, so the narrow window is confirmed on CalRig (TRL 4)"), verdict=PLAUSIBLE)
c.cited("S8", "Hoisting power per person is sustainable for a working day", "Biology", "Human physiology and biomechanics",
        law="Sustained arm cranking by an adult; CAL assumes 50 W each against about 75 W sustained, a figure with no source",
        detail=("Revised after the independent review: 75 W is typical of leg pedalling, and sustained arm cranking is nearer 30 to 40 W. At 35 W each the three-person "
                "hoist takes about 111 s and the cycle about 3.7 min; with the lead and head sheaves (about 8 %) about 3.3 min at 50 W. A cited arm-crank figure and the "
                "timed trial decide; PR-004 is already not met on paper"), verdict=PLAUSIBLE)
r_top = (D["layer_pd"][2]) / 2000
F_crank = m_air * g * r_top / (D["ratio"] * 0.95 * 0.98 ** 2) / (P["crank_r"] / 1000) / 2
c.claim("S9", "Crank force for each of two people at the rated grab load", "Biology", "Ergonomics",
        law="Torque balance through the 4:1 chain (95 %) and two bearings (98 %), 250 mm crank, third rope layer; R5 limit 150 N",
        value=round(F_crank), limit=150, unit="N", rule="below", closed_by="SKG-CAL-001 D1")
mu, th = 0.35, math.radians(270)
ratio_b = math.exp(mu * th)
c.claim("S10", "The band brake holds the drum at the slip clutch's limit", "Physics", "Mechanics and statics",
        law="Band brake (capstan equation) T1/T2 = e^(mu theta), mu 0.35, 270 deg wrap; 6 kg on a 10.2:1 lever on the band's slack end, the anchored end tight",
        value=round(slip_hi * rp_l[0]), limit=314, unit="N m", rule="below", closed_by="SKG-CAL-001 F2")
c.cited("S10a", "The band brake holds when the lining is wet or muddy", "Physics", "Mechanics and statics",
        law="Capstan equation with mu 0.20 to 0.25 for a wet lining",
        detail=("Added after the independent review: at mu 0.25 the brake gives about 168 N m and at 0.20 about 117 N m; with the slip clutch of decision O4 the line can "
                f"apply at most {slip_hi * rp_l[0]:.0f} N m (186 N m with the shear pin), so a wet lining at mu 0.20 falls just below it but stays above the "
                "103 N m the 25 m scraper string needs; keep the lining dry and covered, and measure the holding torque wet before use (TRL 4)"), verdict=PLAUSIBLE)
c.cited("S11", "The weighted lever applies the brake when it is let go", "Physics", "Mechanics and statics",
        law="Lever kinematics: the link pin must move away from the band's live end as the weight falls",
        detail=("Kit 1.7 model: link pin 25 mm below the pivot on the well side, so the falling weight moved it toward the live end and slackened the band; "
                "fixed: pivot lowered to 67 mm, link pin on an upright arm 60 mm above it, link on the band's tangent; ratio about 10.3:1 (CAL uses 10.2)"),
        verdict=WITHIN, closed_by="SKG-DEC-001 K2 (fix rule)")
c.claim("S12", "8 mm polyester line has an adequate factor on the working pull", "Engineering and technology", "Standards practice",
        law="12 kN minimum breaking strength, 90 % at the splice; fibre rope slings use 5:1 to 7:1 (EN 1492-4); the reviewer finds catalogue values of 8 to 10 kN, which still give about 7.7",
        value=round(10.8e3 / T_work, 1), limit=5.0, unit="x", rule="above", closed_by="SKG-CAL-001 E3")
c.claim("S13", "Sheave pitch diameter suits the double-braid line", "Engineering and technology", "Standards practice",
        law="ANSI/ASSP A10.48: at least 6:1 for double-braid rope (Messer 2019)", value=round(2 * P["sheave"][1] / P["rope_d"], 1), limit=6.0, unit="D/d", rule="above",
        closed_by="SKG-CAL-001 E4")
c.claim("S14", "Fleet angle at the drum keeps the line winding evenly", "Engineering and technology", "Standards practice",
        law="Drum practice: fleet angle about 1.5 to 2 deg or less for a plain drum", value=round(D["fleet_deg"], 2), limit=2.0, unit="deg", rule="below", closed_by="SKG-CAL-001 E2")
c.cited("S14a", "The line spools evenly over three layers on the plain drum", "Engineering and technology", "Standards practice",
        law="Wire-rope guidance for a smooth drum is about 1.5 deg; multi-layer plain drums usually need grooving or a level wind",
        detail=f"Added after the independent review: {D['fleet_deg']:.2f} deg is over 1.5 deg; the operator guides the line by hand on the third layer; to confirm in the timed trial",
        verdict=PLAUSIBLE)
c.claim("S15", "The drawbar does not buckle at the slip clutch's limit", "Physics", "Strength of materials",
        law="Euler buckling of a pinned 48.3 x 3.2 tube, E 200 GPa", value=round(slip_hi), limit=39400, unit="N", rule="below", closed_by="SKG-CAL-001 G2")
cap_keys = ["frame", "drum", "drum_bearings", "crank_bearings", "crank_shaft", "small_sprocket", "chain", "guard", "cranks", "pawl", "brake"]
m_cap = sum(M[k] for k in cap_keys)
couple = slip_hi * (D["rope_z_low"] - P["draw_z"]) / 1000
c.claim("S16", "The capstan does not pitch forward at the slip clutch's limit", "Physics", "Mechanics and statics",
        law="Overturning couple of rope and drawbar against the capstan's weight about the front rail", value=round(couple), limit=round(m_cap * g * (P["rail_half"] + 40) / 1000),
        unit="N m", rule="below", closed_by="SKG-CAL-001 G3")
po, pt = P["pole"]
J = math.pi / 32 * ((po / 1000) ** 4 - ((po - 2 * pt) / 1000) ** 4)
Tq = 2 * 150 * P["toe_r"] / 1000
tau_pole = Tq * (po / 2000) / J
c.claim("S17", "The 42.4 x 2.6 pole carries the scraper torque", "Physics", "Strength of materials",
        law="Torsion of a thin tube against shear yield 0.58 x 235 MPa", value=round(tau_pole / 1e6), limit=136, unit="MPa", rule="below", closed_by="SKG-CAL-001 H2")
m_head = sum(M[k] for k in ["scraper_pole", "arms", "arm_pins", "sleeve", "sleeve_pins", "cross_pin", "struts"])
m25 = m_head + 12 * M["pole_section"] + M["tbar"]
c.claim("S18", "The 25 m scraper string hangs inside the slip clutch's lowest slip on the first layer and the tripod rating", "Physics", "Mechanics and statics",
        law=f"String weight x 1.1 against {slip[0] * (1 - A['tol']):,.0f} N (clutch, innermost layer, low end of the setting) and 1,472 N; sections come off as it rises",
        value=round(m25 * g * A["dyn"]), limit=round(slip[0] * (1 - A["tol"])), unit="N", rule="below", closed_by="SKG-CAL-001 H4")
c.claim("S19", "Folded, the scraper toes pass the smallest ring bore", "Mathematics", "Numerical method",
        law="Four-bar linkage solved in the model; sleeve slides 300 mm on the cross pin", value=round(D["fold_toe_r"]), limit=400, unit="mm radius", rule="below",
        closed_by="SKG-CAL-001 H5")
c.cited("S20", "The scraper arm's pivot eye closes round its 16 mm pin and clears the 70 mm hub", "Engineering and technology", "Manufacturing tolerances",
        law="An eye needs material round the hole; the hub's radius is the limit",
        detail=("Kit 1.7 model: pivot 45 mm from the pole axis, 10 mm outside the hub, so the 50 mm arm ended in an open half hole; fixed: pivot at 60 mm, an 18 mm "
                f"radius eye clears the hub by 7 mm; toe radius unchanged at {P['toe_r']:.0f} mm, fold {D['fold_toe_r']:.0f} mm"), verdict=WITHIN,
        closed_by="SKG-DEC-001 K6 (design for construction)")
# sinking
ri, wall, hr = P["ring"][0] / 2000, P["ring"][1] / 1000, P["ring"][2] / 1000
V_ring = math.pi * ((ri + wall) ** 2 - ri ** 2) * hr
W_eff = (8 * V_ring * A["rho_conc"] - 6 * V_ring * 1000) * g + 8 * M["saddle"] * g
area = 2 * math.pi * (ri + wall) * 3.0
f_crit = W_eff / area / 1000
sv_mid = (18.0 * 7.0 + 8.0 * 1.5)                   # kPa at 8.5 m: 7 m above the water table at 18 kN/m3, 1.5 m below at 8
tau_contact = 0.5 * sv_mid * math.tan(math.radians(2 / 3 * A["phi"]))
c.cited("S21", "The 8-ring string sinks 3 m below the water table under its own weight and eight saddles, without de-watering", "Physics", "Mechanics and statics",
        law="Self-weight against skin friction; skin friction = K sigma'v tan delta for soil in contact (K 0.5, delta 2/3 phi')",
        detail=(f"Sinks only while friction stays below {f_crit:.2f} kPa (CAL estimate 1 to 3 kPa for disturbed sand); soil in full contact at mid depth gives about "
                f"{tau_contact:.0f} kPa, so sinking depends on the 40 mm overcut keeping the soil loose and off the ring. Field practice sinks rings this way with de-watering "
                "(Abbott; WaterAid); without it there is no published figure. Revised after the independent review: the central estimate (2 kPa) already exceeds the limit, "
                "the overcut is only at the toe and saturated sand closes onto the ring above it, and full contact would need about 270 kN against 18 kN; the claim fails on "
                "first order. Decided by Amish on 2026-10-25 (SKG-DEC-001 O2): bentonite slurry fed down a pipe into the overcut annulus is part of the method from the "
                "first trial, as in caisson practice and as water-well drillers use bentonite muds. No figure for the lubricated friction is claimed; the test pit must show it "
                "below the limit, so the row stays open at TRL 4 and PR-001 is at risk"),
        verdict=PLAUSIBLE)
c.cited("S22", "Sand does not boil into the rings during digging", "Physics", "Fluid mechanics",
        law="Quick condition needs an upward hydraulic gradient near 1 (Terzaghi); with no de-watering the water inside the rings stands level with the water outside",
        detail=("Gradient about zero while the crew does not bail; the grab removes about 21 L a bite, too little to draw the level down. Revised after the independent "
                "review: a fast hoist of a sealed grab can draw a transient gradient, and sand can run in under the edge (loss of ground) without boiling; hoist slowly off "
                "the bottom and keep the inside level with the outside; to confirm in the trial"), verdict=PLAUSIBLE)
tilt_res = math.sqrt(2) * 3 / 1075
c.claim("S23", "Four dip-tape readings resolve tilt finer than the 1 in 80 limit", "Mathematics", "Statistics and uncertainty",
        law="Two readings of +/-3 mm across 1,075 mm (root sum of squares, as CAL I5); resolves the top ring only, so ring flatness and joints add to it", value=round(tilt_res, 4), limit=round(1 / 80, 4), unit="rad", rule="below", closed_by="SKG-CAL-001 I5")
c.cited("S24", "The grab hangs from its line about 8 to 9 degrees out of level", "Physics", "Mechanics and statics",
        law="A body hung from one point rests with its centre of gravity under that point",
        detail="The line enters the guide tube 65 mm off the grab's axis, about 410 mm above the empty grab's centre of gravity; the grab settles level on the bottom once the line is slack, so the bite is unaffected; no change",
        verdict=WITHIN, closed_by="This file (observation from the detailed model)")
cycle = (22 + 20 + 10 + 16.5 + 76 * m_air / 96.4 + 45) / 60
c.order_of_magnitude("M2", "Cycle at 10 m with three people at the hoist is about 3.2 min", "Mathematics", "Orders of magnitude",
                     claimed=3.2, estimate=cycle, unit="min", law="Sum of lowering, crank change, open, close, hoist (50 W each) and dumping", closed_by="SKG-CAL-001 J2")
c.order_of_magnitude("M3", "About 3.6 m3 of soil is removed for 3 m of sinking", "Mathematics", "Orders of magnitude",
                     claimed=3.56, estimate=math.pi * (P["toe_r"] / 1000) ** 2 * 3.0, unit="m3", law="Cylinder to the toe radius", closed_by="SKG-CAL-001 I4")
c.claim("E1", "The drum holds the line for a 30 m well", "Engineering and technology", "Power and link budgets",
        law="Turns per layer x pitch circumference over three layers against depth plus reeving and dead turns", value=38.7, limit=round(sum(D["layer_len"][:3]), 1), unit="m",
        rule="below", closed_by="SKG-CAL-001 E1")
c.cited("E2", "Proof load at 1.25 x the rated load is a conservative test for hand-powered lifting gear", "Engineering and technology", "Standards practice",
        law="Static test coefficients in lifting standards are typically 1.25 to 1.5; the applicable standard is to assess (SKG-REG-001)",
        detail=("Restated for Amish's decision O4 of 2026-10-25. The independent review found the old basis inconsistent (2 x the link's 122 kg release, 244 kg, exceeded "
                f"the tripod's 225 kg proof). PR-007 now proofs at 1.25 x the rated load, the clutch's highest slip ({swl / g:.0f} kg): {1.25 * swl / g:.0f} kg, inside the "
                "HatchSide proof, with the clutch locked out for the test. 1.25 sits at the low end of static test coefficients in lifting standards; which standard applies "
                "is still to assess (SKG-REG-001)"), verdict=PLAUSIBLE)
c.cited("E3", "Every part fits: no two detailed parts overlap and every made part is drawable", "Engineering and technology", "Manufacturing tolerances",
        law="Kit 1.9 D3 fidelity check (cad_check.py): interference over 5 mm3, bare primitives, fasteners, BOM lines",
        detail="Passed for options A and B after the fixes of SKG-DEC-001 K6 to K20", verdict=WITHIN, closed_by="cad/fidelity.json")
# ------------------------------------------------------------------------------------------------ chemistry
c.cited("C1", "No exhaust gas in the shaft: the method has no engine in or at the well", "Chemistry", "Environmental and atmospheric chemistry",
        law="Carbon monoxide comes from incomplete combustion; it collects in a shaft (Oxfam WASH guidance)",
        detail="Hand capstan only; the gas check stays because the shaft can hold gas from the ground", verdict=WITHIN, closed_by="SKG-PRC-001 Safety")
c.cited("C2", "The daily gas test shows the shaft air is safe", "Chemistry", "Analytical",
        law="CO2 is 1.5 times as dense as air and collects in wells; 40,000 ppm is immediately dangerous, yet it can take about 7 % CO2 to pull oxygen down to a 19.5 % alarm (Henderson 2010)",
        detail=("Kit 1.7 BOM: a four-gas detector (O2, CO, H2S, flammable), which does not read CO2; fixed: a portable 0 to 5 % CO2 safety monitor with alarms at 0.5 % and 3 % "
                "(BOM line 35, USD 399) used with it before work, after breaks and whenever anyone leans over the shaft. The independent review found that a monitor held at the "
                "collar reads only collar air; fixed: both instruments are lowered on a cord in a mesh bag and read at 2 m, at mid depth and 1 m above the water, held for "
                "at least the stated response time at each level, and a reading over range counts as a fail"), verdict=WITHIN, closed_by="SKG-DEC-001 K5, K22 (fix rule)")
c.cited("C3", "Steel tools and polyester rope do not contaminate the well water", "Chemistry", "Inorganic",
        law="Painted mild steel, zinc and polyester are common in wells; lead-based paint is the risk",
        detail="Lead-free primer and paint on every part that enters the well (BOM line 34); the well is disinfected after the work as the Oxfam guidance describes", verdict=WITHIN,
        closed_by="SKG-BLD-001 section 7")
# ------------------------------------------------------------------------------------------------ biology
team2 = 2.0 / 3.0 * (25 + 25)
c.cited("B1", "The assembled grab is never lifted by hand", "Biology", "Ergonomics",
        law="Team lifting: two people handle two thirds of the sum of their individual capacities, three people half (Network Rail, after HSE); 25 kg each",
        detail=(f"Kit 1.7 build plan: two people lift the assembled grab ({m_grab:.1f} kg) against a two-person capacity of {team2:.0f} kg; "
                "fixed: the grab is assembled on the line under the tripod and moved only by the capstan; it travels in pieces of 25 kg or less"),
        verdict=WITHIN, closed_by="SKG-DEC-001 K3 (fix rule)")
m_tub_full = V_bite * A["rho_sand"] + A["water_L"] + 5.0
c.cited("B2", "A full spoil tub is never lifted by hand", "Biology", "Ergonomics",
        law="Team lifting as B1; push and pull limits of about 200 N to start a load (ISO 11228-2, order of magnitude)",
        detail=(f"A tub with one bite holds about {m_tub_full:.0f} kg, over the {team2:.0f} kg two-person capacity, and the kit 1.7 design did not say how it is emptied; "
                f"fixed: two people slide it off the closed doors on a board and tip it at the heap, about {0.5 * m_tub_full * g:.0f} N to start it"),
        verdict=WITHIN, closed_by="SKG-DEC-001 K4 (fix rule)")
heavy = max(M["frame"], M["drum"], M["cradle"], m_head - M["arms"] - M["arm_pins"], M["saddle"])
c.claim("B3", "No single piece needs more than two people to carry", "Biology", "Ergonomics",
        law="Heaviest piece against R9's 25 kg and the 33 kg two-person team capacity", value=round(heavy, 1), limit=25.0, unit="kg", rule="below", closed_by="SKG-CAL-001 K1")
c.cited("B4", "Four people can turn the scraper for an hour at a time", "Biology", "Ergonomics",
        law="Push and pull force limits for repeated work (ISO 11228-2; EN 1005-3 for machinery) depend on frequency and duration",
        detail=("About 142 N for each of two people on the 1.4 m T-bar (SKG-CAL-001 H1), turning continuously, failed against sustained limits of about 100 N or less after "
                "the independent review. Decided by Amish on 2026-10-25 (SKG-DEC-001 O5): a 2.0 m T-bar if the layout allows, else four people. The 2.0 m bar clears the "
                "HatchSide legs only below about 0.8 m above ground (SKG-CAL-001 H10), so four people turn it, two on each side: 71 to 84 N each (H9). The 150 N toe force "
                "is an estimate, so the timed scraping trial confirms it (TRL 4)"), verdict=PLAUSIBLE)
c.cited("B5", "Nobody is in the well while SinkGrab works", "Biology", "Human physiology and biomechanics",
        law="Bad air and falling loads are the causes of death in well work; removing the person removes the exposure",
        detail="Every task is worked from the surface; the doors cover the shaft whenever the grab is up", verdict=WITHIN, closed_by="SKG-PRC-001; PR-008")
c.cited("B6", "Deepening does not leave the well contaminated", "Biology", "Microbiology",
        law="Digging stirs sediment and brings tools and hands to the water; disinfection after work is standard practice (Oxfam WASH)",
        detail="SinkGrab makes no water-quality claim; the method ends with cleaning and disinfecting the well (out of scope, SKG-PRB-001)", verdict=WITHIN, closed_by="SKG-PRB-001 Out of scope")
# ------------------------------------------------------------------------------------------------ option B
gb = OB.geometry(P)
bl = OB.bailer(P)
m_bl = sum(cp.mass_kg(p) for p in bl)
fill_b = OB.B["fill"]
V_b = gb["volume_L"]
m_b_air = m_bl + V_b * fill_b * A["rho_sand"] + V_b * (1 - fill_b) * 1.0
m_b_sub = m_bl * (1 - 1000 / 7850) + V_b * fill_b * A["rho_sub"]
c.order_of_magnitude("OB1", "Option B: the bailer holds about 36 L above its valve seat", "Mathematics", "Units and dimensional analysis",
                     claimed=36.0, estimate=V_b, unit="L", law="Cylinder, 210 mm bore, seat to rim", closed_by="SKG-OPT-001")
c.claim("OB2", "Option B: the steady pull of the full bailer stays below the slip clutch's lowest slip", "Physics", "Mechanics and statics",
        law="Bailer, sand at 50 % fill and water in air x 1.11 sheave friction against the clutch's lowest slip (decision O4; the shear link it was sized on is gone); barrel 1.0 m",
        value=round(m_b_air * g * A["k_fric"]), limit=round(slip_lo), unit="N", rule="below", closed_by="SKG-OPT-001 (barrel 1.0 m)")
c.cited("OB3", "Option B: spudding fills a dart-valve bailer in loose saturated sand", "Physics", "Fluid mechanics",
        law="Cable-tool and manual percussion drillers clear loose sand with dart-valve bailers worked up and down on the bottom",
        detail=f"Fill assumed {fill_b:.0%} (range 30 to 70 %), {V_b * fill_b:.0f} L a run; no figure for a 220 mm bailer in a 1 m ring; to confirm in a test pit", verdict=PLAUSIBLE)
c.order_of_magnitude("OB4", "Option B: pulling the line 0.5 m sideways over 2 m lifts the bailer about 0.24 m", "Mathematics", "Orders of magnitude",
                     claimed=0.24, estimate=gb["stroke"] / 1000, unit="m", law="Geometry of a line deflected at mid span between two fixed points", closed_by="SKG-OPT-001")
F_jerk = gb["pull_factor"] * m_b_sub * g
c.cited("OB5", "Option B: two people can spud the bailer about 30 times a run", "Biology", "Ergonomics",
        law="Force to hold the line deflected: 2 T sin(theta); push and pull limits for repeated work (ISO 11228-2)",
        detail=(f"{gb['pull_factor'] * m_bl * (1 - 1000 / 7850) * g:.0f} to {F_jerk:.0f} N in all as the bailer fills, {F_jerk / 2:.0f} N each at the end, plus the jerk. "
                "Revised after the independent review: that exceeds the 150 N limit of PR-005 and the 200 N start limit of B2, so it fails by the document's own criteria; "
                "a jerk lever or a third person is the fix if Amish chooses option B (SKG-DEC-001 O1)"), verdict=FIX)
c.cited("OB6", "Option B: the rings sink as loose sand runs from under the cutting edge into the bailer's crater", "Physics", "Mechanics and statics",
        law="Cohesionless soil slumps to its angle of repose under water; cohesive soil (clay, laterite) stands and does not run in",
        detail=("Works in sand and gravel only; no way to cut under the edge or to correct tilt except saddles. Revised after the independent review: the rings still have "
                "to overcome skin friction, as in S21, with no undercut, so it fails on first order like S21. The bentonite annulus Amish chose on 2026-10-25 (SKG-DEC-001 O2) "
                "needs the overcut that only option A cuts, so it does not close this row; it stays with the concept choice (O1)"), verdict=FIX)
c.claim("OB7", "Option B: setting the bailer down on its dart stem opens the valve", "Physics", "Mechanics and statics",
        law="Bailer weight on the stem against the sand column on the 140 mm dart", value=round(A["rho_sand"] * 1000 * g * 1.0 * math.pi * 0.07 ** 2), limit=round(m_bl * g),
        unit="N", rule="below", closed_by="SKG-OPT-001")

state = c.write()
print(f"grab {m_grab:.1f} kg, working pull {T_work:.0f} N, crank {F_crank:.0f} N, cycle {cycle:.2f} min, string at 25 m {m25 * g * A['dyn']:.0f} N, "
      f"f_crit {f_crit:.2f} kPa, contact estimate {tau_contact:.0f} kPa, closing resistance {F_res:.0f} N against {F_lip:.0f} N per shell; "
      f"bailer {m_bl:.1f} kg, full {m_b_air:.1f} kg, pull {F_jerk:.0f} N, heaviest piece {heavy:.1f} kg")
