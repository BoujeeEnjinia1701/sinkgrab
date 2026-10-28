"""SinkGrab sizing calculations (SKG-CAL-001), TRL 3.

Run from the repo root:  python docs/04-calcs/sizing.py
Prints every figure quoted in docs/04-calcs/01-sizing.md, tagged [A1], [B2] and so on, and writes
docs/04-calcs/results.csv (one row per requirement). Geometry and masses come from cad/src/model.py
(PARAMS, derived(), masses()); costs from bom/bom.csv; the value-engineering target from project.yaml.
First-principles estimates for a paper proof of concept, not test results.
v0.2 (2026-10-03): Amish's decisions 27A (third person on the cranks during the hoist), 28B (3:1
closing tackle) and 29B (toe blades cutting 40 mm past the ring's outer face), SKG-DDR-003.
v0.3 (2026-10-04): Amish's decision 5A (340 mm slotted sleeve on a 12 mm cross pin so the scraper
arms fold to pass the ring), SKG-DDR-004.
v0.4 (2026-10-24): kit 1.9.1 upgrade. masses() now comes from the detailed D3 model (every pin, clip, collar,
bolt and weld counted); the design fixes of SKG-DEC-001 K1 to K21 (arm pivot at 60 mm, set collars, CO2
monitor and others) are in the model and the BOM.
v0.6 (2026-10-25): Amish's decisions of 2026-10-25 (SKG-DEC-001): O4, a friction slip clutch on the crank shaft and
a peak-reading load indicator at the dead end replace both shear devices, proof at 1.25 x the rated load (section C,
F, G); O5, four people at the T-bar after the 2.0 m T-bar failed the tripod leg check (H9, H10); O2, a bentonite
slurry fed into the overcut annulus is part of the sinking method (I6).
"""
import csv
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / "cad" / "src")]
from model import PARAMS as P, derived, masses  # noqa: E402

D = derived(P)
M = masses(P)
g = 9.81
OUT = []


def say(tag, text):
    line = f"[{tag}] {text}"
    print(line)
    OUT.append(line)


# ------------------------------------------------------------------ assumptions
A = dict(
    rho_sand=2.00,            # kg/L saturated fine to medium sand in the grab (range 1.9 to 2.1)
    rho_sand_sub=1.00,        # kg/L submerged
    fill=0.75,                # bite fill of the closed shells in loose saturated sand (range 0.5 to 0.9)
    water_L=3.0,              # L of water still in the grab when it clears the water
    dyn=1.10,                 # hand hoisting, slow starts
    tau=240e6,                # Pa, ultimate shear strength of S235 bar or mild steel wire (0.6 x 400 MPa)
    k_fric=1.11,              # capstan pull over grab-side tension when hoisting: lead and head sheaves and the guide tube (independent review)
    mu_lining=0.35,           # woven clutch facing on ground steel, dry (as the brake lining)
    clutch_tol=0.05,          # slip setting tolerance after setting on CalRig (to confirm at TRL 4)
    disc_ind=(2170.0, 0.30),  # N and mm per disc at 75 % of h0, disc spring 18 x 9.2 x 1.0 series A (catalogue value to confirm)
    proof_k=1.25,             # proof load over the rated load (decision O4; the standard is to confirm in SKG-REG-001)
    breakout=160.0,           # N, suction on the closed grab at breakout (independent review)
    hs_swl=150.0,             # kg, HatchSide tripod safe working load (material handling)
    hs_proof=1.5,             # HatchSide proof load factor
    eta_chain=0.95, eta_brg=0.98,
    crank_power=50.0,         # W per person sustained at a crank
    heave=400.0,              # N short heave by one person on a crank
    mu_brake=0.35, wrap_deg=270.0,
    lower_speed=0.5,          # m/s lowering on the brake
    depth=10.0,               # m, design case: digging face 10 m below ground (R4)
    water=3.0,                # m of water standing over the face at the end of the work (R1)
    rope_mbs=12.0e3, splice=0.90,
    ring_rho=2400.0,          # kg/m3 precast concrete
    f_skin=(1.0, 3.0),        # kPa, skin friction on the sinking rings in loose saturated sand, disturbed
    overlap=1.0,              # m of caisson string above the water table (inside the lining)
    cut_force=150.0,          # N per toe cutting a 25 mm bite of loose saturated sand (estimate)
    tbar_r=0.65,              # m, hand position on the T-bar
    tape_sigma=3.0,           # mm, one dip-tape reading at depth
)

# ------------------------------------------------------------------ A. grab capacity and mass (R3, R9)
R, B = P["shell_R"] / 1000, P["shell_B"] / 1000
V_geo = math.pi * R * R / 2 * B * 1000
V_bite = V_geo * A["fill"]
grab_keys = ["head", "ballast", "tie_rods", "shell_pins", "shell_a", "shell_b", "crosshead", "hinge_pin",
             "cross_sheave", "cross_axle", "upper_sheave", "upper_axle", "load_link"]
m_grab = sum(M[k] for k in grab_keys)
say("A1", f"Closed shells hold {V_geo:.1f} L; at a {A['fill']:.0%} fill a bite is {V_bite:.1f} L (R3)")
say("A2", f"Grab mass {m_grab:.1f} kg in the detailed model (pins, clips, collars and bolts counted): shells {M['shell_a']:.1f} and {M['shell_b']:.1f}, head {M['head']:.1f} with ballast {M['ballast']:.1f}, tie rods {M['tie_rods']:.1f}; the kit 1.7 simplified model gave 51.0 kg and the first design 47.9 kg")
m_soil = V_bite * A["rho_sand"]
m_air = m_grab + m_soil + A["water_L"]
W_air = m_air * g
say("A3", f"Full grab in air {m_air:.1f} kg ({W_air:.0f} N): sand {m_soil:.1f} kg, water {A['water_L']:.0f} kg")
m_sub = m_grab * (1 - 1000 / 7850) + V_bite * A["rho_sand_sub"]
say("A4", f"Full grab under water {m_sub:.1f} kg ({m_sub * g:.0f} N)")
T_work = W_air * A["dyn"]
say("A5", f"Working line pull {T_work:.0f} N with a {A['dyn']:.2f} dynamic allowance")

# ------------------------------------------------------------------ B. closing force (R3)
stroke = D["stroke"]
lip_travel = 2 * P["shell_R"] * math.radians(P["open_deg"])
n_t = P["tackle"]
k_close = n_t * stroke / lip_travel
T_close_max = m_sub * g
say("B1", f"Head to crosshead stroke {stroke:.0f} mm; the {n_t}:1 tackle takes {n_t * stroke:.0f} mm of line; lips travel {lip_travel:.0f} mm in all; open span {D['lip_span_open']:.0f} mm")
say("B2", f"Mean lip force is {k_close:.2f} of the line pull; the line can pull at most the submerged weight, {T_close_max:.0f} N, before the grab lifts, so the lips close with about {k_close * T_close_max:.0f} N ({k_close * T_close_max / (2 * P['shell_B'] / 1000):.0f} N per metre of lip)")
k2 = 2 * stroke / lip_travel
say("B3", f"The 2:1 tackle of the first design gave {k2:.2f} of the line pull, about {k2 * T_close_max:.0f} N: the 3:1 tackle closes {k_close / k2 - 1:.0%} harder; head weight for opening {M['head'] + M['ballast']:.1f} kg")
fill_low = 0.5
say("B4", f"At a {fill_low:.0%} fill in denser sand a bite is {V_geo * fill_low:.1f} L")

# ------------------------------------------------------------------ C. overload limits: crank slip clutch and load indicator (O4)
rp_layers = [pd / 2000 for pd in D["layer_pd"][:3]]
eta = A["eta_chain"] * A["eta_brg"] ** 2
ratio = D["ratio"]
cd, cf, ct, cpt, cft = P["clutch"]
Ro, Ri = cd / 2000, (cf / 2 + 2.0) / 1000                 # facing 84 x 44 mm
r_m = 2 / 3 * (Ro ** 3 - Ri ** 3) / (Ro ** 2 - Ri ** 2)
tol = A["clutch_tol"]
swl = A["hs_swl"] * g
proof_hs = A["hs_swl"] * A["hs_proof"] * g
P_max = swl                                                # highest slip (layer 1, upper tolerance) set to the rating
T_slip = P_max / (1 + tol) * rp_layers[0] / (ratio * eta)
F_clamp = T_slip / (2 * A["mu_lining"] * r_m)
slip = [T_slip * ratio * eta / r for r in rp_layers]
say("C1", f"Crank slip clutch: two woven facings 84 x 44 mm (mean radius {r_m * 1000:.1f} mm), mu {A['mu_lining']:.2f}; nominal slip {T_slip:.1f} N m on the crank shaft from a {F_clamp:.0f} N clamp (two disc springs 50 x 25.4 x 2.0 and a KM5 locknut), set on CalRig")
say("C2", "Line pull at the capstan when the clutch slips, layers 1 to 3: " + ", ".join(f"{x:.0f} N" for x in slip) +
    f"; with the ±{tol:.0%} setting tolerance, {slip[2] * (1 - tol):.0f} N (layer 3, low) to {slip[0] * (1 + tol):.0f} N (layer 1, high)")
say("C3", f"HatchSide tripod: safe working load {swl:.0f} N, proof load {proof_hs:.0f} N; the clutch never lets the capstan pull pass {slip[0] * (1 + tol):.0f} N, and the grab side carries less by the sheave friction")
steady = m_air * g * A["k_fric"]
say("C4", f"Steady pull of the full grab at the capstan with about {A['k_fric'] - 1:.0%} sheave and guide tube friction {steady:.0f} N against the lowest slip {slip[2] * (1 - tol):.0f} N: margin {slip[2] * (1 - tol) / steady:.2f} on layer 3 and {slip[1] * (1 - tol) / steady:.2f} on layer 2")
jerk = steady * A["dyn"]
brk = (m_air * g + A["breakout"]) * A["k_fric"]
say("C5", f"A jerked start ({jerk:.0f} N) or breakout suction on the closed grab ({brk:.0f} N) can pass the lowest slip, so the clutch slips for a moment; the pawl holds the drum, nothing releases, and the crew lets the suction ease and hoists again")
say("C6", f"At a ±10 % tolerance the lowest slip on layer 3 would be {slip[2] / (1 + 0.10) * (1 + tol) * (1 - 0.10):.0f} N, under the steady pull: the setting is checked on CalRig before each campaign and the lining kept dry inside the guard")
Fd, sd = A["disc_ind"]
trav = 14 * sd * P_max / Fd
say("C7", f"Load indicator at the dead end: 14 disc springs 18 x 9.2 x 1.0 in series, about {sd:.2f} mm a disc at {Fd / 1000:.2f} kN, so the rod travels about {trav:.1f} mm at the rated {P_max / 1000:.2f} kN; rings on the rod are set on CalRig in 0.25 kN steps and the tell-tale keeps the peak of each lift")
heave_T = 2 * A["heave"] * P["crank_r"] / 1000 * ratio * eta / rp_layers[0]
say("C8", f"Without an overload device two people heaving {A['heave']:.0f} N each could put {heave_T:.0f} N into a snagged line")
T_hoist = m_air * g * rp_layers[2] / (ratio * eta)
say("C9", f"In ordinary hoisting the clutch carries {T_hoist:.1f} N m (full grab, layer 3), {T_hoist / T_slip:.0%} of its nominal slip; friction facings do not fatigue as the shear pin did (it ran at about 70 % of its release torque, above shear yield)")

# ------------------------------------------------------------------ D. crank force and speed (R5)
r_top = rp_layers[2]
F_crank_one = T_work / A["dyn"] * r_top / (ratio * eta) / (P["crank_r"] / 1000)
say("D1", f"At the rated grab load on layer 3 one person pushes {F_crank_one:.0f} N on a 250 mm crank; two people {F_crank_one / 2:.0f} N each (R5)")
v = 2 * A["crank_power"] * eta / (W_air)
rpm = v * 60 / (math.pi * D["layer_pd"][1] / 1000) * ratio
say("D2", f"Two people at {A['crank_power']:.0f} W each hoist the full grab at {v * 60:.1f} m/min (crank {rpm:.0f} rpm on layer 2)")

# ------------------------------------------------------------------ E. drum and rope (R7)
cap = sum(D["layer_len"][:3])
need = 30.0 + 7.0 + 3 * math.pi * D["layer_pd"][0] / 1000
say("E1", f"Drum holds {D['turns_layer']} turns a layer: {D['layer_len'][0]:.1f}, {D['layer_len'][1]:.1f} and {D['layer_len'][2]:.1f} m in three layers, {cap:.1f} m; a 30 m well needs {need:.1f} m")
say("E2", f"Fleet angle {D['fleet_deg']:.2f} deg with the drum {P['cap_gap'] / 1000:.1f} m from the lead sheave")
mbs = A["rope_mbs"] * A["splice"]
say("E3", f"8 mm line: {mbs / 1000:.1f} kN through the splice; factor {mbs / T_work:.1f} on the working pull and {mbs / P_max:.1f} on the clutch's highest slip")
say("E4", f"Sheave pitch diameter {2 * P['sheave'][1]:.0f} mm is {2 * P['sheave'][1] / P['rope_d']:.1f} rope diameters; drum {D['layer_pd'][0] / P['rope_d']:.1f}")

# ------------------------------------------------------------------ F. brake and pawl
rb = P["brake_drum"][0] / 2000
k = math.exp(A["mu_brake"] * math.radians(A["wrap_deg"]))
lever_ratio = (P["brake_lever"] - 40.0) / 60.0
W_b = 6.0 * g
T2 = W_b * lever_ratio
T_brake = T2 * (k - 1) * rb
T_need = P_max * rp_layers[0]
say("F1", f"Band brake: e^(mu theta) = {k:.2f}; a 6 kg weight on a {lever_ratio:.1f}:1 lever gives {T2:.0f} N slack-side tension and {T_brake:.0f} N m")
say("F2", f"Highest drum torque the line can apply {T_need:.0f} N m (clutch limit, layer 1): brake factor {T_brake / T_need:.2f}; at the working pull {T_brake / (T_work * r_top):.1f}")
tooth = T_need / (P["ratchet"][1] / 2000)
say("F3", f"Ratchet tooth load at the limit {tooth:.0f} N on an 8 x 16 mm face: {tooth / (8 * 16):.0f} MPa")

# ------------------------------------------------------------------ G. tripod, cradle, drawbar, capstan stability (R7)
ang = math.radians(D["up_angle"])
Tm = P_max
Fy, Fz = Tm * (math.cos(ang) - 1), Tm * math.sin(ang)
say("G1", f"Lead sheave force at the limit: {abs(Fy):.0f} N outward and {Fz:.0f} N up; the drawbar pushes the cradle {Tm:.0f} N inward, so the foot sees the rope along leg A, the HatchSide winch case")
do, dt = P["draw_tube"]
I = math.pi / 64 * (do ** 4 - (do - 2 * dt) ** 4)
L = abs((D["y_d"] + P["rail_half"] + 40) - (P["lead_y"] - 160))
Pcr = math.pi ** 2 * 210e3 * I / L ** 2
say("G2", f"Drawbar {L:.0f} mm long between pins: Euler load {Pcr / 1000:.1f} kN, factor {Pcr / Tm:.0f} on the limit")
cap_keys = ["frame", "drum", "drum_bearings", "crank_bearings", "crank_shaft", "small_sprocket", "chain", "guard", "cranks", "pawl", "brake"]
m_cap = sum(M[k] for k in cap_keys)
arm = (P["rail_half"] + 40) / 1000
couple = Tm * (D["rope_z_low"] - P["draw_z"]) / 1000
say("G3", f"Capstan {m_cap:.1f} kg; rope at {D['rope_z_low']:.0f} mm and drawbar at {P['draw_z']:.0f} mm make a {couple:.0f} N m pitching couple at the limit against {m_cap * g * arm:.0f} N m from its weight")
rated = P_max
proof = A["proof_k"] * rated / g
say("G4", f"Rated load of the SinkGrab line {rated / g:.0f} kg, the clutch's highest slip; R7 proof at {A['proof_k']:.2f} x the rated load is {proof:.0f} kg, inside the HatchSide proof of {A['hs_swl'] * A['hs_proof']:.0f} kg; the full grab ({m_air:.0f} kg) is {m_air / (rated / g):.0%} of the rated load")

# ------------------------------------------------------------------ H. scraper (R6, R8)
po, pt = P["pole"]
Jp = math.pi / 32 * (po ** 4 - (po - 2 * pt) ** 4)
Tq = 2 * A["cut_force"] * P["toe_r"] / 1000
F_hand = Tq / (2 * A["tbar_r"])
twist = Tq * 1000 * A["depth"] * 1000 / (80e3 * Jp)
tau_p = Tq * 1000 * (po / 2) / Jp
say("H1", f"Two toes cutting {A['cut_force']:.0f} N each at {P['toe_r']:.0f} mm need {Tq:.0f} N m: {F_hand:.0f} N for each of two people on the T-bar")
say("H2", f"Pole 42.4 x 2.6: {tau_p:.0f} MPa shear and {math.degrees(twist):.0f} deg of wind-up over {A['depth']:.0f} m")
m_head = sum(M[k] for k in ["scraper_pole", "arms", "arm_pins", "sleeve", "sleeve_pins", "cross_pin", "struts"])
m_sec = M["pole_section"]
say("H3", f"Scraper head {m_head:.1f} kg, pole section {m_sec:.1f} kg, T-bar {M['tbar']:.1f} kg; hung at 10 m: {m_head + 5 * m_sec + M['tbar']:.0f} kg")
n25 = 12
m25 = m_head + n25 * m_sec + M["tbar"]
say("H4", f"At 25 m (12 sections) {m25:.0f} kg, {m25 * g * A['dyn']:.0f} N with the allowance, under the clutch's lowest slip on layer 1 ({slip[0] * (1 - tol):.0f} N) and the {A['hs_swl']:.0f} kg rating; sections come off at the doors as it rises, so it is lighter by the time the line reaches layer 2")
say("H5", f"Toe blade reaches {P['toe_r']:.0f} mm, {P['toe_r'] - (P['ring'][0] / 2 + P['ring'][1]):.0f} mm beyond the ring's outer face (first design 15 mm); folded it is {D['fold_toe_r']:.0f} mm, inside the 400 mm bore of the smallest ring")
say("H6", f"Against the first design's 590 mm toe the T-bar force rises {P['toe_r'] / 590.0 - 1:.0%}; the arms with blades weigh {M['arms']:.1f} kg")
say("H7", f"Sleeve {P['sleeve_len']:.0f} mm long with a {P['slot'][0]:.0f} x {P['slot'][1]:.0f} mm slot each side; the {P['cross_pin'][0]:.0f} mm cross pin lets it slide {D['sleeve_travel']:.0f} mm, the {P['fold_lift']:.0f} mm the fold needs (first design about 40 mm before the stop collar, toes about 604 mm); sleeve top {P['pivot'][1] - P['hub'][1] / 2 - D['sleeve_top']:.0f} mm below the hub; spike {120 - 10:.0f} mm below the foot")
pin_A = math.pi / 4 * (P['cross_pin'][0] / 1000) ** 2
say("H8", f"Cross pin in double shear with the whole string resting on the foot at 25 m ({m25:.0f} kg, {m25 * g * A['dyn']:.0f} N): {m25 * g * A['dyn'] / (2 * pin_A) / 1e6:.0f} MPa, a factor of {A['tau'] / (m25 * g * A['dyn'] / (2 * pin_A)):.0f} on {A['tau'] / 1e6:.0f} MPa; bearing on the 2.6 mm pole wall {m25 * g * A['dyn'] / (2 * P['cross_pin'][0] * P['pole'][1]):.0f} MPa")
F4 = Tq / (4 * A["tbar_r"])
F4b = Tq / (2 * (A["tbar_r"] + 0.45))
say("H9", f"Four people, two on each side of the T-bar (decision O5): {F4:.0f} N each if all push at {A['tbar_r']:.2f} m, {F4b:.0f} N each with the inner pair at 0.45 m; both under the about 100 N sustained limit for repeated work")
Rf, zt_, rh_, z0_ = P["hs_r_foot"], P["hs_pin_z"], P["hs_r_hub"], P["hs_foot_pin_z"] + P["hs_foot"][2]
z_clear = lambda r_end: z0_ + (Rf - 25.0 - r_end) * (zt_ - z0_) / (Rf - rh_)
z_doors = P["collar_h"] + P["wh_frame"][1] + P["door_angle"][0]
say("H10", f"Tripod leg check for a 2.0 m T-bar (option A of O5): its ends sweep {1000 + P['tbar'][0] / 2:.0f} mm and clear the HatchSide legs only below {z_clear(1000 + P['tbar'][0] / 2):.0f} mm above ground, against doors at {z_doors:.0f} mm and 2 m of T-bar travel per pole section, so the layout does not allow it; the 1.4 m T-bar clears them below {z_clear(700 + P['tbar'][0] / 2):.0f} mm")

# ------------------------------------------------------------------ I. sinking and tilt (R1, R6)
ri, wall, hr = P["ring"][0] / 2000, P["ring"][1] / 1000, P["ring"][2] / 1000
ro = ri + wall
v_ring = math.pi * (ro ** 2 - ri ** 2) * hr
m_ring = v_ring * A["ring_rho"]
n = int((A["water"] + A["overlap"]) / hr)
n_sub = int(A["water"] / hr)
W_str = (n * m_ring - n_sub * v_ring * 1000) * g
m_sad = M["saddle"]
W_bal = 8 * m_sad * g
area = math.pi * 2 * ro * A["water"]
f_lo, f_hi = A["f_skin"]
say("I1", f"Ring 1.0 m x 75 mm x 0.5 m: {m_ring:.0f} kg; a string of {n} rings with {n_sub} under water weighs {W_str / 1000:.1f} kN effective; eight saddles add {W_bal / 1000:.2f} kN ({W_bal / W_str:.0%})")
say("I2", f"Outer area in the soil after {A['water']:.0f} m of sinking {area:.1f} m2: skin friction {area * f_lo:.1f} to {area * f_hi:.1f} kN at {f_lo:.0f} to {f_hi:.0f} kPa")
f_crit = (W_str + W_bal) / 1000 / area
say("I3", f"The string keeps sinking to {A['water']:.0f} m only while skin friction stays below {f_crit:.2f} kPa")
vol = math.pi * (P["toe_r"] / 1000) ** 2 * A["water"]
say("I4", f"Soil to remove for {A['water']:.0f} m of sinking (to the toe radius): {vol:.2f} m3")
d_ring = 2 * (ri + wall / 2) * 1000
sig = math.sqrt(2) * A["tape_sigma"]
say("I5", f"Tilt from two readings {d_ring:.0f} mm apart: ±{sig:.1f} mm, a resolution of 1 in {d_ring / sig:.0f}; 1 in 80 is {d_ring / 80:.1f} mm")
v_ann = math.pi * ((P["toe_r"] / 1000) ** 2 - ro ** 2) * A["water"]
say("I6", f"Decision O2: bentonite slurry pumped down a feed pipe into the {P['toe_r'] - ro * 1000:.0f} mm overcut annulus keeps the soil off the rings; about {v_ann:.2f} m3 of slurry fills it over {A['water']:.0f} m of sinking. The string still sinks only while the lubricated skin friction stays below {f_crit:.2f} kPa; no figure is claimed here, the test pit must show it")

# ------------------------------------------------------------------ J. cycle time and output (R4)
h = A["depth"] + 1.05
t_lower = h / A["lower_speed"]
t_cranks = 20.0
t_open, t_close = 10.0, 15.0 + 1.5        # 3:1 tackle: about 1.5 s more line to close
t_hoist = h / v
t_dump = 10 + 15 + 10 + 10
cyc = t_lower + t_cranks + t_open + t_close + t_hoist + t_dump
say("J1", f"Cycle at {A['depth']:.0f} m with two people at the cranks: lower {t_lower:.0f} s, cranks off and on {t_cranks:.0f} s, open {t_open:.0f} s, close {t_close:.0f} s, hoist {t_hoist:.0f} s, doors and dump {t_dump:.0f} s: {cyc / 60:.1f} min")
v3 = 3 * A["crank_power"] * eta / W_air
cyc3 = cyc - t_hoist + h / v3
say("J2", f"With a third person on the long +X handle during the hoist (decision 27A) the hoist takes {h / v3:.0f} s and the cycle {cyc3 / 60:.2f} min, {cyc3 / 180 - 1:.0%} over the 3 min target")
rate = V_bite / (cyc3 / 60) * 60
say("J3", f"Output {rate:.0f} L an hour of in-place sand; {vol * 1000 / rate:.1f} h of grabbing for {A['water']:.0f} m of sinking")

# ------------------------------------------------------------------ K. masses and cost (R9, R11)
m_arms = M["arms"] + M["arm_pins"]
heavy = {"Capstan frame": M["frame"], "Winding drum": M["drum"], "Foot cradle": M["cradle"],
         "Scraper head, arms unpinned": m_head - m_arms, "Scraper arms with blades (pair)": m_arms, "Ballast saddle": m_sad, "Door": M["doors"] / 2,
         "Well-head frame half": M["wh_frame"] / 2, "Grab shell": max(M["shell_a"], M["shell_b"]),
         "Drawbar half": M["drawbar"] / 2}
hk = max(heavy, key=heavy.get)
say("K0", f"Scraper head with its arms pinned on {m_head:.1f} kg: it is carried with the two arms unpinned ({m_head - m_arms:.1f} and {m_arms:.1f} kg)")
say("K1", "Heaviest pieces: " + ", ".join(f"{k} {v:.1f} kg" for k, v in sorted(heavy.items(), key=lambda kv: -kv[1])[:5]))
say("K2", f"Assembled grab {m_grab:.1f} kg, moved only on the line (SKG-DEC-001 K3); longest pieces 1.46 m (well-head frame), 1.40 m (T-bar), 2.0 m (pole sections)")
rows = list(csv.DictReader(open(ROOT / "bom" / "bom.csv")))
cost = sum(float(r["qty"]) * float(r["unit_cost_usd"]) for r in rows)
target = float(re.search(r"budget_usd:\s*([\d.]+)", (ROOT / "project.yaml").read_text()).group(1))
say("K3", f"Value-engineering target: USD {target:,.0f}. Estimated cost of the constructable design: USD {cost:,.2f} (USD {target - cost:,.2f} under the target)")
kit = m_cap + M["stakes"] + M["cradle"] + M["drawbar"] + m_grab + m_head + 6 * m_sec + M["tbar"] + M["wh_frame"] + M["doors"] + 8 * m_sad
say("K4", f"Kit about {kit:.0f} kg without ropes, tubs and the HatchSide tripod")

# ------------------------------------------------------------------ results table
res = [
    ("R1", "Water depth reached without de-watering", f"Sinks while skin friction < {f_crit:.2f} kPa; estimate {f_lo:.0f} to {f_hi:.0f} kPa; toes cut {P['toe_r'] - (P['ring'][0] / 2 + P['ring'][1]):.0f} mm past the ring; bentonite slurry in the annulus", "At least 3 m", "Not met on paper unaided; at risk with the bentonite annulus of decision O2 until the test pit shows the friction (TRL 4)"),
    ("R2", "Fits rings of 0.8 to 1.3 m", f"Grab 468 mm across; scraper folds to {D['fold_toe_r']:.0f} mm radius on a {D['sleeve_travel']:.0f} mm sleeve travel; toes and skids adjustable", "0.8 to 1.3 m", "Met by design"),
    ("R3", "Grab load per bite", f"{V_bite:.1f} L at 75 % fill with a {n_t}:1 tackle ({k_close / k2 - 1:.0%} more closing force); {V_geo * fill_low:.1f} L at 50 %", "At least 20 L", "At risk; closing force and fill confirmed in the test-pit trial (STEM S2)"),
    ("R4", "Cycle time at 10 m, three people at the cranks during the hoist", f"{cyc3 / 60:.1f} min ({cyc / 60:.1f} min with two)", "3 min or less", "Not met on paper by about 0.2 min; the timed trial decides"),
    ("R5", "Crank force", f"{F_crank_one / 2:.0f} N each with two ({F_crank_one:.0f} N for one)", "150 N or less", "Met on paper"),
    ("R6", "Tilt", f"Resolution 1 in {d_ring / sig:.0f}; corrected by scraping the high side and saddles", "1 in 80 or better", "Not verifiable at TRL 3"),
    ("R7", "Proof load of lifting parts", f"Proof {proof:.0f} kg (1.25 x the {rated / g:.0f} kg rated load) within HatchSide proof {A['hs_swl'] * A['hs_proof']:.0f} kg; clutch margin {slip[2] * (1 - tol) / steady:.2f} on layer 3; line factor {mbs / T_work:.1f}", "1.25 x rated load; clutch slips at or below the 150 kg rating", "At risk; the clutch window rests on a ±5 % setting, shown on CalRig (TRL 4)"),
    ("R8", "No person in the well", "Every task from the surface; doors close the shaft", "100 %", "Met by design"),
    ("R9", "Portability", f"Heaviest piece {heavy[hk]:.1f} kg ({hk.lower()})", "25 kg or less; small pickup", "Met on paper"),
    ("R10", "Local build", "Steel section, plate, stick welding, drilling; rolled shell skins", "Stick welder and hand tools", "Met by design"),
    ("R11", "Prototype cost", f"USD {cost:,.2f}", f"Value-engineering target USD {target:,.0f}", "Met on paper, within the target"),
]
with open(ROOT / "docs" / "04-calcs" / "results.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["id", "requirement", "value", "target", "status"])
    w.writerows(res)
say("M", "; ".join(f"{r[0]} {r[4]}" for r in res))
