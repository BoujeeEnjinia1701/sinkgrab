"""SinkGrab parametric model (build123d), TRL 3, constructable design (SKG-DDR-002).

Run from the repo root:  python cad/src/model.py          (checks, masses and exports)
                         python cad/src/model.py --check  (constructability checks only)
Exports STEP and STL into cad/step and cad/stl:
    sinkgrab-capstan     hand capstan: frame, winding drum with brake drum and ratchet wheel, bearings,
                         chain drive with shear pin hub, chain guard, pawl, weighted band brake, cranks
    sinkgrab-lead        foot cradle with lead sheave (stands under the HatchSide leg A foot) and drawbar
    sinkgrab-grab        two-shell clamshell grab, closed: head with ballast plates, tie rods, shells,
                         crosshead with hinge pin and sheave, shear link
    sinkgrab-scraper     under-curb scraper head (deployed), one pole section and the turning T-bar
    sinkgrab-wellhead    well-head frame with two folding doors and four datum brackets
    sinkgrab-saddle      one ballast saddle
    sinkgrab-assembly    the kit at the well head (grab over the closed doors), tripod not included

Axes (site): the well axis is Z with the ground at z = 0; leg A of the HatchSide tripod stands on -Y,
the capstan stands on the same line 3 m beyond the lead sheave, the closing line runs along x = 0.
The HatchSide tripod, the well collar, the lining and the caisson rings are context, not SinkGrab parts.

Constructable design, 2026-10-03 (SKG-DDR-002, decided under Amish's pre-approvals of 2026-10-03):
    one closing line does everything: the grab is lowered closed, opens under its head's weight when
    the line is slacked on the bottom, and is closed and lifted by the same line through a 2:1 tackle;
    a calibrated shear link at the tackle's dead end limits the line to the tripod's 150 kg rating;
    the hand capstan is a single winding drum with a 4:1 chain drive, a shear pin hub, a ratchet and
    pawl, and a weighted band brake that is on unless its lever is lifted; a drawbar to a cradle
    under the leg A foot closes the rope load inside the kit, so the tripod sees its own winch case;
    the under-curb scraper is a centred pole head with two arms that the pole's weight opens under
    the cutting edge, turned from the surface with a T-bar; the well-head frame carries folding doors
    (cover, barrow deck and pole guide) and the tilt datum; ballast saddles straddle the top ring.
"""
import math
import sys
from dataclasses import dataclass
from pathlib import Path

from build123d import (Box, Cylinder, Pos, Rot, Vector, Solid, Plane, Polygon, Compound, extrude,
                       export_step, export_stl)

# ----------------------------------------------------------------------------- parameters (mm)
PARAMS = {
    # well (design case) and the HatchSide interface (from HTS-DWG-001, Rev P2)
    "ring": (1000.0, 75.0, 500.0),        # caisson ring: inside diameter, wall, height
    "lining": (1300.0, 100.0),            # upper lining inside diameter, wall
    "collar_h": 300.0,                    # collar (top of lining) above ground
    "hs_r_foot": 1500.0, "hs_pin_z": 2250.0, "hs_r_hub": 110.0, "hs_foot_pin_z": 70.0,
    "hs_leg_az": (270.0, 30.0, 150.0),
    "hs_sheave": (0.0, -62.5, 2420.0),    # head sheave centre (x, y, z)
    "hs_foot": (140.0, 280.0, 18.0),      # foot plate and pad: across, along the leg line, height
    # rope
    "rope_d": 8.0,                        # 8 mm polyester double braid closing line
    "sheave": (75.0, 65.0, 28.0, 20.0),   # bought sheave: outside radius, pitch radius, width, bore
    # lead cradle and drawbar
    "lead_y": -1760.0, "lead_z": 185.0,   # lead sheave centre
    "draw_tube": (48.3, 3.2), "draw_z": 40.0,
    "cap_gap": 3000.0,                    # lead sheave centre to drum axis (fleet angle)
    # capstan (drum axis along X)
    "hd": 220.0,                          # drum axis height
    "core": (168.3, 4.5), "drum_w": 200.0, "flange": (260.0, 6.0),
    "brake_drum": (250.0, 50.0, 6.0),     # OD, width, wall
    "ratchet": (200.0, 168.0, 20, 8.0),   # OD, root diameter, teeth, thickness
    "drum_shaft": 30.0, "crank_shaft": 25.0,
    "x_brg": (-200.0, 230.0),             # bearing centre planes (frame side planes)
    "hc": 850.0, "yc_off": -150.0,        # crank shaft height and offset from the drum axis (away from the well)
    "chain_p": 12.7, "z_small": 12, "z_big": 48, "sprocket_t": 8.0,
    "crank_r": 250.0, "handle": (32.0, 120.0),
    "shs": (40.0, 2.0),                   # frame tube
    "rail_half": 330.0,                   # base rails run y_d +/- this
    "ucp206": (42.9, 165.0, 48.0, 17.0, 80.0, 38.0),   # centre height, base length, base width, base t, housing dia, housing width
    "ucp205": (36.5, 140.0, 38.0, 15.0, 70.0, 34.0),
    "brake_lever": 650.0, "brake_weight": (120.0, 80.0, 80.0),
    # grab (local: hinge axis along Y at the origin, closed)
    "shell_R": 230.0, "shell_B": 340.0, "shell_t": 4.0, "end_t": 6.0, "top_t": 4.0,
    "hinge_pin": 30.0, "rod_len": 420.0, "rod_bar": (30.0, 10.0), "shell_pin": (190.0, 25.0),
    "head_pin_x": 120.0, "head_block": (300.0, 120.0, 40.0), "ballast_plate": (190.0, 110.0, 16.0),
    "open_deg": 50.0,
    # scraper (local: pole axis = Z, z = 0 at the toe cutting level, deployed)
    "pole": (42.4, 2.6), "pole_sec": 2000.0, "spigot": (36.0, 150.0),
    "hub": (70.0, 90.0), "pivot": (45.0, 80.0), "toe_r": 590.0, "arm_bar": (50.0, 10.0),
    "toe": (100.0, 80.0, 10.0), "sleeve": (54.0, 110.0), "foot_d": 250.0, "sump": 330.0,
    "cent_z": 700.0, "fold_lift": 300.0, "cent_r": 440.0, "skid": (40.0, 150.0, 10.0), "head_len": 1300.0,
    "tbar": (33.7, 1400.0), "socket": (48.3, 200.0),
    # well-head frame and doors
    "wh_frame": (1360.0, 50.0, 5.0),      # inner opening (square), angle leg, angle thickness
    "door_angle": (40.0, 4.0), "mesh_t": 3.0, "pole_hole": 32.0,
    # ballast saddle
    "saddle": (200.0, 25.0, 300.0, 20.0, 150.0, 25.0, 95.0),  # width, inner leg t, inner leg h, outer t, outer h, bridge t, slot
    # densities (kg/m3)
    "rho_steel": 7850.0,
}

ROOT = Path(__file__).resolve().parents[2]
GUARD_TABS = (560.0, 780.0)      # chain guard screw tabs on the -X post (heights, mm)


# ----------------------------------------------------------------------------- helpers
def bx(x0, x1, y0, y1, z0, z1):
    return Pos((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2) * Box(abs(x1 - x0), abs(y1 - y0), abs(z1 - z0))


def rod(a, b, r):
    a, b = Vector(*a), Vector(*b)
    d = b - a
    return Solid.make_cylinder(r, d.length, Plane(origin=a, z_dir=d.normalized()))


def tube(a, b, ro, ri):
    return rod(a, b, ro) - rod(a, b, ri)


def xcyl(y, z, r, x0, x1):
    return rod((x0, y, z), (x1, y, z), r)


def ycyl(x, z, r, y0, y1):
    return rod((x, y0, z), (x, y1, z), r)


def zcyl(x, y, r, z0, z1):
    return rod((x, y, z0), (x, y, z1), r)


def bar(a, b, w, t, up=(0, 0, 1)):
    """Flat bar w x t from a to b; the w side lies in the plane of (b - a) and `up`."""
    a, b = Vector(*a), Vector(*b)
    d = b - a
    L = d.length
    z = d.normalized()
    u = Vector(*up)
    xd = (u - z * u.dot(z)).normalized()
    pl = Plane(origin=a, x_dir=xd, z_dir=z)
    return pl * Pos(0, 0, L / 2) * Box(w, t, L)


def sq(a, b, s, w=None):
    """Square tube s x s (wall w) from a to b."""
    a, b = Vector(*a), Vector(*b)
    d = b - a
    z = d.normalized()
    xd = Vector(1, 0, 0) if abs(z.X) < 0.9 else Vector(0, 1, 0)
    xd = (xd - z * xd.dot(z)).normalized()
    pl = Plane(origin=a, x_dir=xd, z_dir=z)
    out = pl * Pos(0, 0, d.length / 2) * Box(s, s, d.length)
    if w:
        out = out - pl * Pos(0, 0, d.length / 2) * Box(s - 2 * w, s - 2 * w, d.length + 2)
    return out


def _ccw(points):
    a = sum(x0 * y1 - x1 * y0 for (x0, y0), (x1, y1) in zip(points, points[1:] + points[:1]))
    return list(points) if a > 0 else list(points)[::-1]


def prism_xz(points, y0, y1):
    f = Plane.XZ.offset(-y0) * Polygon(*_ccw(points), align=None)
    return extrude(f, amount=-(y1 - y0))


def prism_yz(points, x0, x1):
    f = Plane.YZ.offset(x0) * Polygon(*_ccw(points), align=None)
    return extrude(f, amount=x1 - x0)


def prism_xy(points, z0, z1):
    f = Plane.XY.offset(z0) * Polygon(*_ccw(points), align=None)
    return extrude(f, amount=z1 - z0)


def ring_sector_xz(r0, r1, a0, a1, y0, y1, n=40):
    """Annular sector in the XZ plane (angles in degrees from +X toward +Z), extruded y0 to y1."""
    outer = [(r1 * math.cos(math.radians(a0 + (a1 - a0) * k / n)), r1 * math.sin(math.radians(a0 + (a1 - a0) * k / n))) for k in range(n + 1)]
    inner = [(r0 * math.cos(math.radians(a1 - (a1 - a0) * k / n)), r0 * math.sin(math.radians(a1 - (a1 - a0) * k / n))) for k in range(n + 1)]
    return prism_xz(outer + inner, y0, y1)


def fuse(shapes):
    out = None
    for s in shapes:
        out = s if out is None else out.fuse(s)
    return out.clean()


def annulus_z(r0, r1, z0, z1):
    return zcyl(0, 0, r1, z0, z1) - zcyl(0, 0, r0, z0 - 1, z1 + 1)


# ----------------------------------------------------------------------------- derived numbers
def derived(P=PARAMS):
    D = {}
    D["y_d"] = P["lead_y"] - P["cap_gap"]                    # drum axis y
    D["y_c"] = D["y_d"] + P["yc_off"]                        # crank shaft y
    core = P["core"][0]
    d = P["rope_d"]
    D["turns_layer"] = int(P["drum_w"] / (d * 1.06))
    D["layer_pd"] = [core + d + 2 * d * k for k in range(4)]
    D["layer_len"] = [D["turns_layer"] * math.pi * pd / 1000.0 for pd in D["layer_pd"]]
    D["fleet_deg"] = math.degrees(math.atan((P["drum_w"] / 2) / P["cap_gap"]))
    p = P["chain_p"]
    D["pd_small"] = p / math.sin(math.pi / P["z_small"])
    D["pd_big"] = p / math.sin(math.pi / P["z_big"])
    D["ratio"] = P["z_big"] / P["z_small"]
    D["centres"] = math.hypot(P["yc_off"], P["hc"] - P["hd"])
    # x positions along the drum shaft
    half = P["drum_w"] / 2
    ft = P["flange"][1]
    D["x_flange"] = ((-half - ft, -half), (half, half + ft))
    bd_w = P["brake_drum"][1]
    D["x_brake"] = (half + ft + 6.0, half + ft + 6.0 + bd_w)
    D["x_ratchet"] = (D["x_brake"][1] + 8.0, D["x_brake"][1] + 8.0 + P["ratchet"][3])
    D["x_spr"] = P["x_brg"][0] - 62.0                        # sprocket plane, outboard of the -X bearing
    D["x_guard"] = (D["x_spr"] - 26.0, D["x_spr"] + 20.0)
    D["drum_shaft_x"] = (D["x_spr"] - 12.0, P["x_brg"][1] + 45.0)
    D["crank_shaft_x"] = (D["x_guard"][0] - 40.0, P["x_brg"][1] + 75.0)
    D["x_crank"] = ((D["x_guard"][0] - 22.0, D["x_guard"][0] - 12.0), (P["x_brg"][1] + 55.0, P["x_brg"][1] + 65.0))
    # rope geometry
    sx, sy, sz = P["hs_sheave"]
    rp = P["sheave"][1]
    ly, lz = P["lead_y"], P["lead_z"]
    D["rope_z_low"] = lz - rp                                # horizontal run from the drum to the lead sheave
    # common tangent of the lead sheave (rope under it) and the head sheave (rope over it), both radius rp
    dy, dz = sy - ly, sz - lz
    L = math.hypot(dy, dz)
    ang = math.atan2(dz, dy)
    D["up_angle"] = math.degrees(ang)
    nrm = (-math.sin(ang), math.cos(ang))                    # left normal of the centre line
    # rope passes below-right of the lead sheave and outside (-Y side) of the head sheave: offset -nrm
    D["up_a"] = (ly - nrm[0] * rp, lz - nrm[1] * rp)
    D["up_b"] = (sy - nrm[0] * rp, sz - nrm[1] * rp)
    D["drop_y"] = sy + rp
    # grab: closed hinge height in the site layout (over the doors) and tie rod head pin height
    sxp, szp = P["shell_pin"]
    D["head_pin_z"] = szp + math.sqrt(P["rod_len"] ** 2 - (sxp - P["head_pin_x"]) ** 2)
    th = math.radians(P["open_deg"])
    ox, oz = sxp * math.cos(th) - szp * math.sin(th), sxp * math.sin(th) + szp * math.cos(th)
    D["head_pin_z_open"] = oz + math.sqrt(P["rod_len"] ** 2 - (ox - P["head_pin_x"]) ** 2)
    D["stroke"] = D["head_pin_z_open"] - D["head_pin_z"]
    D["lip_span_open"] = 2 * P["shell_R"] * math.sin(th)
    D["grab_hinge_site"] = 1330.0
    # scraper linkage (deployed)
    px, pz = P["pivot"]
    D["arm_len"] = math.hypot(P["toe_r"] - P["toe"][2] - px, pz - 10.0)
    D["arm_end"] = (P["toe_r"] - P["toe"][2], 10.0)
    t = 0.55
    D["strut_top"] = (px + t * (D["arm_end"][0] - px), pz + t * (D["arm_end"][1] - pz))
    D["sleeve_z"] = (-P["sump"] + 10.0, -P["sump"] + 10.0 + P["sleeve"][1])
    D["strut_bot"] = (P["sleeve"][0] / 2 + 12.0, D["sleeve_z"][1] - 10.0)
    D["strut_len"] = math.hypot(D["strut_top"][0] - D["strut_bot"][0], D["strut_top"][1] - D["strut_bot"][1])
    # folded: lift the pole 220 mm relative to the sleeve; solve the arm angle (4-bar: pivot fixed on pole)
    lift = P["fold_lift"]
    sbx, sbz = D["strut_bot"][0], D["strut_bot"][1] - lift      # sleeve hangs 220 lower relative to the pole
    a_len = t * D["arm_len"]
    best = None
    for k in range(0, 1800):
        phi = math.radians(-90 + k * 0.1)                       # arm angle from +X
        mx, mz = px + a_len * math.cos(phi), pz + a_len * math.sin(phi)
        err = abs(math.hypot(mx - sbx, mz - sbz) - D["strut_len"])
        if best is None or err < best[0]:
            best = (err, phi)
    phi = best[1]
    D["fold_deg"] = math.degrees(phi)
    D["fold_toe_r"] = px + D["arm_len"] * math.cos(phi) + P["toe"][2]
    D["bore_r_min"] = 400.0
    return D


# ----------------------------------------------------------------------------- capstan
def _pillow(P, kind, x, y, zc, shaft):
    h, L, W, t, hd, hw = P[kind]
    base = bx(x - W / 2, x + W / 2, y - L / 2, y + L / 2, zc - h, zc - h + t)
    web = bx(x - hw / 2, x + hw / 2, y - hd * 0.42, y + hd * 0.42, zc - h + t - 0.1, zc)
    housing = xcyl(y, zc, hd / 2, x - hw / 2, x + hw / 2)
    return (base + web + housing) - xcyl(y, zc, shaft / 2, x - hw, x + hw)


def _ratchet(P, y0, z0, x0):
    od, rd, n, t = P["ratchet"]
    R, r = od / 2, rd / 2
    pts = []
    for k in range(n):
        a = math.radians(90.0 + 360.0 * k / n)
        b = math.radians(90.0 + 360.0 * (k + 1) / n)
        pts += [(y0 + r * math.cos(a), z0 + r * math.sin(a)), (y0 + R * math.cos(b - 0.002), z0 + R * math.sin(b - 0.002))]
    w = prism_yz(pts, x0, x0 + t)
    return w - xcyl(y0, z0, P["drum_shaft"] / 2, x0 - 1, x0 + t + 1)


def STAKE_Y(yd):
    """Stake tubes 200 mm either side of the drum axis, clear of the braces."""
    return (yd - 200.0, yd + 200.0)


def PAWL_PIVOT(P, yd, hd):
    """Pawl pivot: 150 mm from the drum axis at 75 deg (on the side away from the well, above)."""
    a = math.radians(75.0)
    return (yd + 150.0 * math.cos(a), hd + 150.0 * math.sin(a))


def capstan_parts(P=PARAMS):
    D = derived(P)
    yd, yc, hd, hc = D["y_d"], D["y_c"], P["hd"], P["hc"]
    s, w = P["shs"]
    xa, xb = P["x_brg"]
    rh = P["rail_half"]
    ucp6, ucp5 = P["ucp206"], P["ucp205"]
    pad_top = hd - ucp6[0]
    top_top = hc - ucp5[0]
    out = {}
    # ---- frame
    fr = []
    for xs in (xa, xb):
        fr.append(sq((xs, yd - rh, s / 2), (xs, yd + rh, s / 2), s, w))                     # base rail
        fr.append(sq((xs, yc, s), (xs, yc, top_top - 8.0), s, w))                           # post
        for dy in (-60.0, 60.0):
            fr.append(sq((xs, yd + dy, s), (xs, yd + dy, pad_top - 8.0), s, w))            # pad posts
        fr.append(bx(xs - 25, xs + 25, yd - 90, yd + 90, pad_top - 8.0, pad_top))          # bearing pad 8 mm
        fr.append(bx(xs - 25, xs + 25, yc - 75, yc + 75, top_top - 8.0, top_top))        # top plate 8 mm
        fr.append(sq((xs, yd + rh - 40, s), (xs, yc + 22, 640.0), s, w))                   # front brace
        fr.append(sq((xs, yd - rh + 40, s), (xs, yc - 22, 560.0), s, w))                   # rear brace
    xl, xr = xa + s / 2, xb - s / 2
    fr.append(sq((xl, yd + rh - s / 2, s / 2), (xr, yd + rh - s / 2, s / 2), s, w))      # front cross rail
    fr.append(sq((xl, yd - rh + s / 2, s / 2), (xr, yd - rh + s / 2, s / 2), s, w))      # rear cross rail
    fr.append(sq((xl, yc, 700.0), (xr, yc, 700.0), s, w))                                 # top tie
    # drawbar clevis on the front cross rail: two 10 mm plates, 22 mm pin hole at draw_z
    dz = P["draw_z"]
    for x0 in (-20.0, 12.0):
        lug = bx(x0, x0 + 8, yd + rh, yd + rh + 70, 0.0, 70.0) - xcyl(yd + rh + 40, dz, 10.5, x0 - 1, x0 + 9)
        fr.append(lug)
    # pawl bracket (+X side, inner face of the post region) with its pin
    pv = PAWL_PIVOT(P, yd, hd)
    fr.append(bx(D["x_ratchet"][1] + 1.0, xb - s / 2, pv[0] - 25, pv[0] + 25, pv[1] - 25, pv[1] + 75))
    fr.append(xcyl(pv[0], pv[1], 6.0, D["x_ratchet"][0] - 6.0, D["x_ratchet"][1] + 1.0))
    # brake anchor lug and lever pivot (on the +X rail, rear)
    xbr = (D["x_brake"][0] + D["x_brake"][1]) / 2
    fr.append(bx(xbr - 14, xbr - 6, yd - 150, yd - 100, s, 120.0))                        # band anchor post
    fr.append(sq((xl, yd - 125, s / 2), (xr, yd - 125, s / 2), s, w))                    # anchor cross bar
    fr.append(bx(xb + s / 2 - 8.0, xb + s / 2, yd - 260, yd - 220, s, 150.0))             # lever pivot plate
    # stake tubes on the outsides of the rails, front and rear
    for xs, sgn in ((xa, -1), (xb, 1)):
        for yy in STAKE_Y(yd):
            xo = xs + sgn * (s / 2 + 16.85)
            fr.append(zcyl(xo, yy, 16.85, 0.0, 80.0) - zcyl(xo, yy, 13.65, -1, 81))
    # chain guard tabs on the -X post
    for zt in GUARD_TABS:
        fr.append(bx(D["x_guard"][1], xa - s / 2, yc - 20, yc + 20, zt, zt + 3))
    out["frame"] = fuse(fr)
    # ---- drum with flanges, brake drum, ratchet wheel and big sprocket on its shaft
    core_o, core_t = P["core"]
    half = P["drum_w"] / 2
    fo, ft = P["flange"]
    dr = [xcyl(yd, hd, core_o / 2, -half, half) - xcyl(yd, hd, core_o / 2 - core_t, -half - 1, half + 1)]
    for (x0, x1) in D["x_flange"]:
        fl = xcyl(yd, hd, fo / 2, x0, x1) - xcyl(yd, hd, P["drum_shaft"] / 2, x0 - 1, x1 + 1)
        for k in range(6):
            a = math.radians(30 + 60 * k)
            fl -= xcyl(yd + 50 * math.cos(a), hd + 50 * math.sin(a), 18.0, x0 - 1, x1 + 1)
        dr.append(fl)
    bo, bw, bt = P["brake_drum"]
    x0, x1 = D["x_brake"]
    dr.append(xcyl(yd, hd, bo / 2, x0, x1) - xcyl(yd, hd, bo / 2 - bt, x0 - 1, x1 + 1))
    web = xcyl(yd, hd, bo / 2, x0, x0 + 6.0) - xcyl(yd, hd, P["drum_shaft"] / 2, x0 - 1, x0 + 7)
    for k in range(6):
        a = math.radians(60 * k)
        web -= xcyl(yd + 75 * math.cos(a), hd + 75 * math.sin(a), 28.0, x0 - 1, x0 + 7)
    dr.append(web)                                                                        # brake drum web
    dr.append(xcyl(yd, hd, bo / 2 - bt + 0.5, D["x_flange"][1][1] - 0.5, x0 + 0.5) - xcyl(yd, hd, bo / 2 - bt - 6, D["x_flange"][1][1] - 1, x0 + 1))  # spacer ring
    dr.append(_ratchet(P, yd, hd, D["x_ratchet"][0]))
    dr.append(xcyl(yd, hd, 22.0, x1 - 0.5, D["x_ratchet"][0] + 0.5))                     # collar between
    xs0, xs1 = D["drum_shaft_x"]
    dr.append(xcyl(yd, hd, P["drum_shaft"] / 2, xs0, xs1))
    xsp = D["x_spr"]
    big = xcyl(yd, hd, D["pd_big"] / 2 + 4.0, xsp - 4, xsp + 4) - xcyl(yd, hd, P["drum_shaft"] / 2, xsp - 5, xsp + 5)
    dr.append(big)
    dr.append(xcyl(yd, hd, 25.0, xsp + 4, xsp + 30))                                      # sprocket hub
    out["drum"] = fuse(dr)
    # ---- bearings
    out["drum_bearings"] = _pillow(P, "ucp206", xa, yd, hd, P["drum_shaft"]) + _pillow(P, "ucp206", xb, yd, hd, P["drum_shaft"])
    out["crank_bearings"] = _pillow(P, "ucp205", xa, yc, hc, P["crank_shaft"]) + _pillow(P, "ucp205", xb, yc, hc, P["crank_shaft"])
    # ---- crank shaft, small sprocket hub, shear pin
    c0, c1 = D["crank_shaft_x"]
    out["crank_shaft"] = xcyl(yc, hc, P["crank_shaft"] / 2, c0, c1)
    hub = xcyl(yc, hc, 18.0, xsp - 4.0, xsp + 22.0) - xcyl(yc, hc, P["crank_shaft"] / 2, xsp - 5, xsp + 23)
    small = xcyl(yc, hc, D["pd_small"] / 2 + 3.0, xsp - 4, xsp + 4) - xcyl(yc, hc, 18.0, xsp - 5, xsp + 5)
    out["small_sprocket"] = fuse([hub, small])
    out["shear_pin"] = rod((xsp + 12.0, yc, hc - 22.0), (xsp + 12.0, yc, hc + 22.0), 2.0)
    out["crank_shaft"] = out["crank_shaft"] - rod((xsp + 12.0, yc, hc - 22.0), (xsp + 12.0, yc, hc + 22.0), 2.0)
    out["small_sprocket"] = out["small_sprocket"] - rod((xsp + 12.0, yc, hc - 22.0), (xsp + 12.0, yc, hc + 22.0), 2.0)
    # ---- chain (simplified as a flat loop band round both pitch circles)
    rb, rs = D["pd_big"] / 2, D["pd_small"] / 2
    pts = []
    for k in range(48):
        a = 2 * math.pi * k / 48
        pts.append((yd + (rb + 4) * math.cos(a), hd + (rb + 4) * math.sin(a)))
        pts.append((yc + (rs + 4) * math.cos(a), hc + (rs + 4) * math.sin(a)))
    from_hull = _hull(pts)
    inner = []
    for k in range(48):
        a = 2 * math.pi * k / 48
        inner.append((yd + (rb - 4) * math.cos(a), hd + (rb - 4) * math.sin(a)))
        inner.append((yc + (rs - 4) * math.cos(a), hc + (rs - 4) * math.sin(a)))
    out["chain"] = prism_yz(from_hull, xsp - 4.0, xsp + 4.0) - prism_yz(_hull(inner), xsp - 5.0, xsp + 5.0)
    # ---- chain guard: closed box round both sprockets, open holes for the shafts
    g0, g1 = D["x_guard"]
    gpts = []
    for k in range(48):
        a = 2 * math.pi * k / 48
        gpts.append((yd + (rb + 24) * math.cos(a), hd + (rb + 24) * math.sin(a)))
        gpts.append((yc + (rs + 30) * math.cos(a), hc + (rs + 30) * math.sin(a)))
    gh = _hull(gpts)
    gin = []
    for k in range(48):
        a = 2 * math.pi * k / 48
        gin.append((yd + (rb + 22.5) * math.cos(a), hd + (rb + 22.5) * math.sin(a)))
        gin.append((yc + (rs + 28.5) * math.cos(a), hc + (rs + 28.5) * math.sin(a)))
    guard = prism_yz(gh, g0, g1) - prism_yz(_hull(gin), g0 + 1.5, g1 - 1.5)
    guard -= xcyl(yd, hd, 30.0, g0 - 1, g1 + 1)
    guard -= xcyl(yc, hc, 22.0, g0 - 1, g1 + 1)
    out["guard"] = guard
    # ---- cranks: arm 250 between centres, handle on an M12 bolt; removable (pinned square on the shaft)
    cr = []
    for (x0, x1), sgn, ang in ((D["x_crank"][0], -1, 90.0), (D["x_crank"][1], 1, -90.0)):
        a = math.radians(ang)
        ey, ez = yc + P["crank_r"] * math.cos(a), hc + P["crank_r"] * math.sin(a)
        arm = prism_yz(_hull([(yc + 22 * math.cos(t), hc + 22 * math.sin(t)) for t in [2 * math.pi * k / 24 for k in range(24)]] +
                             [(ey + 18 * math.cos(t), ez + 18 * math.sin(t)) for t in [2 * math.pi * k / 24 for k in range(24)]]), x0, x1)
        arm -= xcyl(yc, hc, P["crank_shaft"] / 2, x0 - 1, x1 + 1)
        hx0, hx1 = (x0 - P["handle"][1], x0) if sgn < 0 else (x1, x1 + P["handle"][1])
        hnd = xcyl(ey, ez, P["handle"][0] / 2, hx0, hx1)
        cr += [arm, hnd]
    out["cranks"] = fuse(cr)
    # ---- pawl (8 mm plate, in the ratchet plane) on its pin
    r0, r1 = D["x_ratchet"]
    tip_a = math.radians(56.0)
    R = P["ratchet"][0] / 2
    tip = (yd + (R - 6.0) * math.cos(tip_a), hd + (R - 6.0) * math.sin(tip_a))
    ppts = _hull([(pv[0] + 16 * math.cos(t), pv[1] + 16 * math.sin(t)) for t in [2 * math.pi * k / 24 for k in range(24)]] +
                 [(tip[0] + 3 * math.cos(t), tip[1] + 3 * math.sin(t)) for t in [2 * math.pi * k / 12 for k in range(12)]] +
                 [(pv[0] - 35, pv[1] + 20)])
    out["pawl"] = prism_yz(ppts, r0, r1) - xcyl(pv[0], pv[1], 6.5, r0 - 1, r1 + 1)
    # ---- band brake: lined band round the brake drum (270 deg), lever with weight
    bxm = (D["x_brake"][0] + 3.0, D["x_brake"][1] - 3.0)
    band = None
    rr = P["brake_drum"][0] / 2
    pts_o = [(yd + (rr + 6) * math.cos(math.radians(a)), hd + (rr + 6) * math.sin(math.radians(a))) for a in range(-100, 171, 5)]
    pts_i = [(yd + (rr + 0.5) * math.cos(math.radians(a)), hd + (rr + 0.5) * math.sin(math.radians(a))) for a in range(170, -101, -5)]
    band = prism_yz(pts_o + pts_i, bxm[0], bxm[1])
    # band ends: anchor end (rear, at 170 deg) to the anchor post, live end (bottom, -100 deg) to the lever
    a_end = (yd + (rr + 3) * math.cos(math.radians(170)), hd + (rr + 3) * math.sin(math.radians(170)))
    band += bar((xbr - 10, a_end[0] - 6.0, a_end[1]), (xbr - 10, yd - 134.0, 120.0), 30, 6, up=(1, 0, 0))
    l_end = (yd + (rr + 3) * math.cos(math.radians(-100)), hd + (rr + 3) * math.sin(math.radians(-100)))
    lever_pv = (yd - 240.0, 130.0)
    lev = bar((xb + s / 2 + 1.0 + 6.0, lever_pv[0], lever_pv[1]), (xb + s / 2 + 7.0, lever_pv[0] - P["brake_lever"], lever_pv[1] + 170.0), 40, 12, up=(0, 0, 1))
    link = bar((xbr + 12, l_end[0], l_end[1]), (xbr + 12, lever_pv[0] + 60.0, lever_pv[1] - 25.0), 25, 6, up=(1, 0, 0))
    cross = xcyl(lever_pv[0] + 60.0, lever_pv[1] - 25.0, 6.0, xbr, xb + s / 2 + 13.0)
    pivot = xcyl(lever_pv[0], lever_pv[1], 6.0, xb + s / 2, xb + s / 2 + 14.0)
    wx, wy, wz = P["brake_weight"]
    wpos = (lever_pv[0] - P["brake_lever"] + 40.0, lever_pv[1] + 170.0 * (P["brake_lever"] - 40.0) / P["brake_lever"])
    weight = bx(xb + s / 2 + 13.0, xb + s / 2 + 13.0 + wx, wpos[0] - wy / 2, wpos[0] + wy / 2, wpos[1] - wz / 2, wpos[1] + wz / 2)
    out["brake"] = fuse([band, lev, link, cross, pivot, weight])
    # ---- ground stakes (4): 25 mm bar 500 long through the stake tubes, 32 mm washer head on top
    st = []
    for xs, sgn in ((xa, -1), (xb, 1)):
        for yy in STAKE_Y(yd):
            xo = xs + sgn * (s / 2 + 16.85)
            st.append(zcyl(xo, yy, 12.5, -420.0, 80.0) + zcyl(xo, yy, 17.0, 80.0, 86.0))
    out["stakes"] = Compound(st)
    return out


def _hull(pts):
    pts = sorted(set((round(x, 4), round(y, 4)) for x, y in pts))

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lower, upper = [], []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


# ----------------------------------------------------------------------------- lead cradle and drawbar
def lead_parts(P=PARAMS):
    D = derived(P)
    ly, lz = P["lead_y"], P["lead_z"]
    fa, fl, fh = P["hs_foot"]
    yf = -P["hs_r_foot"]
    so, sp, sw, sb = P["sheave"]
    out = {}
    cr = [bx(-160, 160, yf - fl / 2 - 30, yf + fl / 2 + 20, 0.0, 10.0),                    # base under the foot
          bx(-60, 60, ly - 120, yf - fl / 2 - 30, 0.0, 10.0)]                                # tongue to the sheave
    # rim angles round the foot (the foot sits inside them): 30 x 30 x 4 on three sides
    cr.append(bx(-fa / 2 - 6, fa / 2 + 6, yf - fl / 2 - 6, yf - fl / 2 - 2, 10.0, 40.0))
    cr.append(bx(-fa / 2 - 6, -fa / 2 - 2, yf - fl / 2 - 6, yf + fl / 2, 10.0, 40.0))
    cr.append(bx(fa / 2 + 2, fa / 2 + 6, yf - fl / 2 - 6, yf + fl / 2, 10.0, 40.0))
    # two clamp bars over the foot plate (M12 through the base), holding the cradle to the foot
    for yy in (yf - 70.0, yf + 70.0):
        cr.append(bx(-130, 130, yy - 20, yy + 20, fh, fh + 10.0))
        for xx in (-110.0, 110.0):
            cr.append(zcyl(xx, yy, 6.0, 10.0, fh))
    # sheave cheeks: 8 mm plates either side of the sheave, 21 mm axle hole
    for x0 in (-sw / 2 - 1 - 8, sw / 2 + 1):
        ch = prism_yz([(ly - 110, 10.0), (ly + 110, 10.0), (ly + 60, lz + 85), (ly - 60, lz + 85)], x0, x0 + 8)
        cr.append(ch - xcyl(ly, lz, sb / 2 + 0.25, x0 - 1, x0 + 9))
    # drawbar clevis at the outer end, pin at draw_z
    dz = P["draw_z"]
    for x0 in (-20.0, 12.0):
        cr.append(bx(x0, x0 + 8, ly - 190, ly - 110, 10.0, 70.0) - xcyl(ly - 160, dz, 10.5, x0 - 1, x0 + 9))
    cr.append(bx(-60, 60, ly - 200, ly - 120, 0.0, 10.0))
    out["cradle"] = fuse(cr)
    sh = xcyl(ly, lz, so, -sw / 2, sw / 2) - xcyl(ly, lz, sb / 2, -sw / 2 - 1, sw / 2 + 1)
    groove = None
    out["lead_sheave"] = sh - _groove(ly, lz, sp, P["rope_d"] / 2 + 0.5)
    out["lead_axle"] = xcyl(ly, lz, sb / 2 - 0.25, -sw / 2 - 18, sw / 2 + 18)
    # drawbar in two halves with a spigot joint; tongues at both ends with 22 mm pin holes
    do, dt = P["draw_tube"]
    y_front = D["y_d"] + P["rail_half"] + 40.0                 # capstan clevis pin
    y_back = ly - 160.0                                        # cradle clevis pin
    ym = (y_front + y_back) / 2
    h1 = tube((0, y_front + 30, dz), (0, ym, dz), do / 2, do / 2 - dt)
    h2 = tube((0, ym, dz), (0, y_back - 30, dz), do / 2, do / 2 - dt)
    spig = ycyl(0, dz, do / 2 - dt - 0.5, ym - 100, ym + 100)
    tg1 = bx(-6, 6, y_front - 25, y_front + 31, dz - 20, dz + 20) - xcyl(y_front, dz, 10.5, -7, 7)
    tg2 = bx(-6, 6, y_back - 31, y_back + 25, dz - 20, dz + 20) - xcyl(y_back, dz, 10.5, -7, 7)
    out["drawbar"] = fuse([h1, h2, spig, tg1, tg2])
    out["draw_pins"] = xcyl(y_front, dz, 10.0, -28, 28) + xcyl(y_back, dz, 10.0, -28, 28)
    return out


def _groove(y, z, rp, rg):
    """Torus-like groove cutter approximated by a thin disc ring at the pitch radius."""
    return xcyl(y, z, rp + rg, -rg, rg) - xcyl(y, z, rp - rg, -rg - 1, rg + 1)


# ----------------------------------------------------------------------------- grab (local coordinates)
def grab_parts(P=PARAMS, open_deg=0.0):
    """Closed grab in local coordinates: hinge axis along Y at the origin, shells below, head above."""
    D = derived(P)
    R, B, t, et, tt = P["shell_R"], P["shell_B"], P["shell_t"], P["end_t"], P["top_t"]
    hp = P["hinge_pin"]
    sx, sz = P["shell_pin"]
    out = {}

    def shell(side):
        yi = B / 2 if side > 0 else B / 2 + et + 1.0          # inner face of the end plates
        parts = [ring_sector_xz(R, R + t, -90, 0, -yi, yi)]                                  # skin
        parts.append(bx(50, R, -yi, yi, -tt, 0.0))                                           # top cover
        for sgn in (-1, 1):
            y0, y1 = (yi, yi + et) if sgn > 0 else (-yi - et, -yi)
            q = [(0.0, 0.0)] + [((R + t) * math.cos(math.radians(a)), (R + t) * math.sin(math.radians(a))) for a in range(-90, 1, 5)]
            ep = prism_xz(q, y0, y1)
            ep += ycyl(0, 0, 35.0, y0, y1)                                                    # hinge boss
            ep += prism_xz([(150, -5), (sx + 30, -5), (sx + 30, sz + 25), (150, sz + 25)], y0, y1)   # tie rod lug
            ep -= ycyl(0, 0, hp / 2 + 0.25, y0 - 1, y1 + 1)
            ep -= ycyl(sx, sz, 10.25, y0 - 1, y1 + 1)
            parts.append(ep)
        parts.append(bx(1.0, 11.0, -yi, yi, -R - t, -R + 45))                               # cutting lip 10 x 50
        s = fuse(parts)
        if side < 0:
            s = Rot(0, 0, 180) * s
        return s

    sp, sm = shell(1), shell(-1)
    if open_deg:
        sp = Rot(0, -open_deg, 0) * sp
        sm = Rot(0, open_deg, 0) * sm
    out["shell_a"] = sp
    out["shell_b"] = sm
    yA = B / 2 + et                     # outer face of shell A's end plates
    yB = B / 2 + 2 * et + 1.0           # outer face of shell B's end plates
    rb_w, rb_t = P["rod_bar"]
    out["hinge_pin"] = ycyl(0, 0, hp / 2, -yB - 12, yB + 12)
    # crosshead: two 10 mm plates either side of the sheave; sheave axle 120 above the hinge
    so, rp, sw, sb = P["sheave"]
    zs = 120.0
    ch = []
    for y0 in (-sw / 2 - 1 - 10, sw / 2 + 1):
        pl = prism_xz(_hull([(40 * math.cos(a), 40 * math.sin(a)) for a in [2 * math.pi * k / 24 for k in range(24)]] +
                            [(45 * math.cos(a), zs + 45 * math.sin(a)) for a in [2 * math.pi * k / 24 for k in range(24)]]), y0, y0 + 10)
        pl -= ycyl(0, 0, hp / 2 + 0.25, y0 - 1, y0 + 11)
        pl -= ycyl(0, zs, sb / 2 + 0.25, y0 - 1, y0 + 11)
        ch.append(pl)
    out["crosshead"] = fuse(ch)
    out["cross_sheave"] = (ycyl(0, zs, so, -sw / 2, sw / 2) - ycyl(0, zs, sb / 2, -sw / 2 - 1, sw / 2 + 1)) - \
        (ycyl(0, zs, rp + 4.5, -4.5, 4.5) - ycyl(0, zs, rp - 4.5, -5, 5))
    out["cross_axle"] = ycyl(0, zs, sb / 2 - 0.25, -sw / 2 - 11 - 6, sw / 2 + 11 + 6)
    # tie rods: 30 x 10 flat, 21 mm holes; shell A's rods outside its end plates, shell B's outside B's
    zh = D["head_pin_z"]
    xh = P["head_pin_x"]
    rods, pins = [], []
    for side, yo in ((1, yA), (-1, yB)):
        for sgn in (-1, 1):
            y0 = yo if sgn > 0 else -yo - rb_t
            r = bar((side * sx, 0, sz), (side * xh, 0, zh), rb_w, rb_t, up=(1, 0, 0))
            r = Pos(0, y0 + rb_t / 2, 0) * r
            r -= ycyl(side * sx, sz, 10.25, y0 - 1, y0 + rb_t + 1)
            r -= ycyl(side * xh, zh, 12.75, y0 - 1, y0 + rb_t + 1)
            rods.append(r)
            # short 20 mm pin through the rod and the lug, with a head outside the rod
            yi0 = (yo - et) if sgn > 0 else (-yo - rb_t - 6)
            yi1 = (yo + rb_t + 6) if sgn > 0 else (-yo + et)
            pins.append(ycyl(side * sx, sz, 10.0, yi0, yi1))
    out["tie_rods"] = Compound(rods)
    out["shell_pins"] = Compound(pins)
    # head: welded box 300 x 120 x 40 (6 mm plate), two 25 mm head pins along Y, rope guide tube,
    # dead-end lug underneath, recovery-line eye on top
    hx, hy, hz = P["head_block"]
    z0, z1 = zh - 15, zh - 15 + hz
    shell_box = bx(-hx / 2, hx / 2, -hy / 2, hy / 2, z0, z1) - bx(-hx / 2 + 6, hx / 2 - 6, -hy / 2 + 6, hy / 2 - 6, z0 + 6, z1 - 6)
    yp = yB + rb_t + 2
    hb = [shell_box]
    for s in (-1, 1):
        hb.append(ycyl(s * xh, zh, 12.5, -yp, yp))
    hb.append(zcyl(-rp, 0, 15.0, z0 - 25, z1 + 20))                                       # rope guide tube
    hb.append(bx(rp - 6, rp + 6, -20, 20, zh - 75, z0))                                   # dead-end lug
    hb.append(bx(-30, 30, -6, 6, z1, z1 + 50))                                            # recovery-line eye
    head = fuse(hb)
    head -= zcyl(-rp, 0, 7.0, z0 - 26, z1 + 21)
    head -= xcyl(0, zh - 55, 8.25, rp - 7, rp + 7)
    head -= ycyl(0, z1 + 28, 10.0, -7, 7)
    out["head"] = head
    bpx, bpy, bpt = P["ballast_plate"]
    out["ballast"] = Compound([bx(-bpx / 2, bpx / 2, s * (hy / 2) if s > 0 else -(hy / 2 + bpt), s * (hy / 2 + bpt) if s > 0 else -(hy / 2), z0, z0 + bpy)
                               for s in (-1, 1)])
    # shear link: two 6 mm side plates on a 16 mm pin through the dead-end lug, calibrated 6 mm pin below
    zl = zh - 55
    lk = [bx(rp - 13, rp - 7, -15, 15, zl - 75, zl + 12), bx(rp + 7, rp + 13, -15, 15, zl - 75, zl + 12)]
    lk.append(xcyl(0, zl, 8.0, rp - 14, rp + 14))
    link = fuse(lk) - xcyl(0, zl - 62, 3.25, rp - 14, rp + 14)
    out["shear_link"] = link
    out["link_pin"] = xcyl(0, zl - 62, 3.0, rp - 15, rp + 15)
    return out


# ----------------------------------------------------------------------------- scraper (local: pole axis Z)
def scraper_parts(P=PARAMS):
    D = derived(P)
    po, pt = P["pole"]
    out = {}
    px, pz = P["pivot"]
    hub_d, hub_h = P["hub"]
    aw, at = P["arm_bar"]
    z_top = P["head_len"]
    z_bot = D["sleeve_z"][0] - 120.0
    pole = tube((0, 0, z_bot + 50), (0, 0, z_top), po / 2, po / 2 - pt)
    pole += zcyl(0, 0, po / 2, z_bot, z_bot + 50.5)                                        # solid spike end
    hub = zcyl(0, 0, hub_d / 2, pz - hub_h / 2, pz + hub_h / 2) - zcyl(0, 0, po / 2, pz - hub_h, pz + hub_h)
    stop = zcyl(0, 0, 32.0, z_bot + 60, z_bot + 80) - zcyl(0, 0, po / 2, z_bot + 50, z_bot + 90)
    # arm lugs on the hub: a pair of 8 mm plates either side of each arm, 16.5 mm pin holes
    lugs = []
    for s in (-1, 1):
        x0, x1 = (hub_d / 2 - 2, px + 18) if s > 0 else (-(px + 18), -(hub_d / 2 - 2))
        for y0 in (-at / 2 - 8, at / 2):
            lugs.append(bx(x0, x1, y0, y0 + 8, pz - 22, pz + 22) - ycyl(s * px, pz, 8.25, y0 - 1, y0 + 9))
    # centralizer collar and three radial arms with skids
    cz = P["cent_z"]
    cent = [zcyl(0, 0, 32.0, cz - 30, cz + 30) - zcyl(0, 0, po / 2, cz - 31, cz + 31)]
    sk_w, sk_h, sk_t = P["skid"]
    r_end = P["cent_r"] - sk_t
    for k in range(3):
        a = 90 + 120 * k
        cent.append(Rot(0, 0, a) * bx(30, r_end, -4, 4, cz - 20, cz + 20))
        cent.append(Rot(0, 0, a) * bx(r_end, P["cent_r"], -sk_w / 2, sk_w / 2, cz - sk_h / 2, cz + sk_h / 2))
    out["scraper_pole"] = fuse([pole, hub, stop] + lugs + cent)
    # arms (50 x 10 flat on edge) and toes (deployed)
    ex, ez = D["arm_end"]
    tw, th, tt = P["toe"]
    arms = []
    for s in (-1, 1):
        arms.append(bar((s * px, 0, pz), (s * ex, 0, ez), at, aw, up=(0, 1, 0)))
        xa0, xa1 = (ex, ex + tt) if s > 0 else (-(ex + tt), -ex)
        arms.append(bx(xa0, xa1, -tw / 2, tw / 2, ez - th + 15, ez + 15))
    out["arms"] = fuse(arms) - Compound([ycyl(s * px, pz, 8.25, -30, 30) for s in (-1, 1)])
    stx, stz = D["strut_top"]
    out["arms"] = out["arms"] - Compound([ycyl(s * stx, stz, 6.25, -30, 30) for s in (-1, 1)])
    out["arm_pins"] = Compound([ycyl(s * px, pz, 8.0, -at / 2 - 12, at / 2 + 12) for s in (-1, 1)] +
                               [ycyl(s * stx, stz, 6.0, -at / 2 - 10, at / 2 + 10) for s in (-1, 1)])
    # sliding sleeve with foot plate and a 10 mm strut lug each side; struts are pairs of 6 x 30 flats
    s0, s1 = D["sleeve_z"]
    sl = [zcyl(0, 0, P["sleeve"][0] / 2, s0, s1) - zcyl(0, 0, po / 2 + 0.5, s0 - 1, s1 + 1)]
    sl.append(zcyl(0, 0, P["foot_d"] / 2, s0 - 10, s0) - zcyl(0, 0, po / 2 + 0.5, s0 - 11, s0 + 1))
    sbx, sbz = D["strut_bot"]
    for s in (-1, 1):
        x0, x1 = (P["sleeve"][0] / 2 - 2, sbx + 14) if s > 0 else (-(sbx + 14), -(P["sleeve"][0] / 2 - 2))
        sl.append(bx(x0, x1, -at / 2, at / 2, sbz - 16, sbz + 16) - ycyl(s * sbx, sbz, 6.25, -at, at))
    out["sleeve"] = fuse(sl)
    out["sleeve_pins"] = Compound([ycyl(s * sbx, sbz, 6.0, -at / 2 - 10, at / 2 + 10) for s in (-1, 1)])
    struts = []
    for s in (-1, 1):
        for y0 in (-at / 2 - 6, at / 2):
            st = bar((s * sbx, 0, sbz), (s * stx, 0, stz), 6.0, 30.0, up=(0, 1, 0))
            st = Pos(0, y0 + 3.0, 0) * st
            st -= ycyl(s * sbx, sbz, 6.25, y0 - 1, y0 + 7) + ycyl(s * stx, stz, 6.25, y0 - 1, y0 + 7)
            struts.append(st)
    out["struts"] = Compound(struts)
    # one 2 m pole section: tube with a 36 mm spigot (250 long, 150 out) at the bottom
    L = P["pole_sec"]
    z0 = z_top
    sec = tube((0, 0, z0), (0, 0, z0 + L), po / 2, po / 2 - pt)
    sec += zcyl(0, 0, P["spigot"][0] / 2, z0 - P["spigot"][1], z0 + 100)
    out["pole_section"] = sec
    # T-bar: 48.3 socket over the next spigot, 33.7 x 3.2 handle 1.4 m across, eye on top
    zt = z0 + L
    so_d, so_l = P["socket"]
    tb = [tube((0, 0, zt - 20), (0, 0, zt + so_l - 20), so_d / 2, po / 2 + 0.5)]
    tb.append(zcyl(0, 0, so_d / 2, zt + so_l - 20, zt + so_l - 10))
    tb.append(zcyl(0, 0, P["spigot"][0] / 2, zt + 0.5, zt + so_l - 19))                      # spigot inside the socket
    hz = zt + so_l - 40
    tb.append(tube((-P["tbar"][1] / 2, 0, hz), (P["tbar"][1] / 2, 0, hz), P["tbar"][0] / 2, P["tbar"][0] / 2 - 3.2))
    tb.append(bx(-6, 6, -25, 25, zt + so_l - 10, zt + so_l + 40) - xcyl(0, zt + so_l + 20, 9.0, -7, 7))
    out["tbar"] = fuse(tb)
    return out


# ----------------------------------------------------------------------------- well-head frame and doors
def wellhead_parts(P=PARAMS):
    D = derived(P)
    a_in, a_leg, a_t = P["wh_frame"]
    zc = P["collar_h"]
    h = a_in / 2
    out = {}
    fr = []
    # square frame of 50 x 50 x 5 angle: horizontal leg on the collar, vertical leg up at the inner edge
    for s in (-1, 1):
        fr.append(bx(-h - a_leg, h + a_leg, s * h if s > 0 else -h - a_leg, s * (h + a_leg) if s > 0 else -h, zc, zc + a_t))
        fr.append(bx(s * h if s > 0 else -h - a_leg, s * (h + a_leg) if s > 0 else -h, -h, h, zc, zc + a_t))
    for s in (-1, 1):
        fr.append(bx(-h, h, s * h if s > 0 else -h - a_t, s * (h + a_t) if s > 0 else -h, zc, zc + a_leg))
        fr.append(bx(s * h if s > 0 else -h - a_t, s * (h + a_t) if s > 0 else -h, -h, h, zc, zc + a_leg))
    # datum brackets: 6 mm plate from the frame side inward, 10 mm datum hole at the caisson wall centre
    rd = P["ring"][0] / 2 + P["ring"][1] / 2
    for k in range(4):
        a = 90.0 * k
        br = bx(rd - 25, h + 1.0, -25, 25, zc + a_t, zc + a_t + 6) - zcyl(rd, 0, 5.0, zc, zc + 20)
        fr.append(Rot(0, 0, a) * br)
    # hinge knuckles for the doors on the +Y and -Y sides
    for s in (-1, 1):
        for xk in (-500.0, 500.0):
            fr.append(xcyl(s * (h + 15), zc + a_leg + 12, 12.0, xk - 40, xk + 40) - xcyl(s * (h + 15), zc + a_leg + 12, 8.5, xk - 41, xk + 41))
            fr.append(bx(xk - 40, xk + 40, s * (h + a_t) if s > 0 else -h - 15, s * (h + 15) if s > 0 else -h - a_t, zc + a_leg - 5, zc + a_leg + 0.5))
    out["wh_frame"] = fuse(fr)
    # two doors: 40 x 40 x 4 angle frame with 3 mm expanded mesh; pole notch at the meeting edge
    da, dt = P["door_angle"]
    zd = zc + a_leg                     # doors rest on the vertical angle legs
    doors = []
    for s in (-1, 1):
        y_out, y_in = s * (h + 2.0), s * 4.0
        y0, y1 = min(y_out, y_in), max(y_out, y_in)
        x0, x1 = -h - 2.0, h + 2.0
        frame = bx(x0, x1, y0, y1, zd, zd + da) - bx(x0 + dt, x1 - dt, y0 + dt, y1 - dt, zd + dt, zd + da + 1)
        mesh = bx(x0 + dt, x1 - dt, y0 + dt, y1 - dt, zd + 4.0, zd + 4.0 + P["mesh_t"])
        door = frame + mesh
        door -= zcyl(0, 0, P["pole_hole"], zd - 1, zd + da + 1)
        notch = zcyl(0, 0, P["pole_hole"] + 30, zd, zd + 6) - zcyl(0, 0, P["pole_hole"], zd - 1, zd + 7)
        door += notch & bx(-70, 70, y0, y1, zd - 1, zd + 7)                                  # 6 mm doubler round the notch
        # hinge pins at the outer edge
        for xk in (-500.0, 500.0):
            door += xcyl(s * (h + 15), zc + a_leg + 12, 8.0, xk - 60, xk + 60)
            door += bx(xk - 55, xk - 41, s * (h - 10) if s > 0 else -h - 15, s * (h + 15) if s > 0 else -h + 10, zd, zd + 20)
            door += bx(xk + 41, xk + 55, s * (h - 10) if s > 0 else -h - 15, s * (h + 15) if s > 0 else -h + 10, zd, zd + 20)
        doors.append(door)
    out["doors"] = Compound(doors)
    return out


def door_mass(P=PARAMS):
    """One door: 40 x 40 x 4 angle frame (2.42 kg/m) plus expanded steel mesh at 8 kg/m2."""
    a_in = P["wh_frame"][0]
    L, W = a_in + 4.0, a_in / 2 - 2.0
    return 2 * (L + W) / 1000.0 * 2.42 + (L * W) * 1e-6 * 8.0 + 1.0     # + hinge tabs, pins, doubler


# ----------------------------------------------------------------------------- ballast saddle (local)
def saddle_part(P=PARAMS):
    """One ballast saddle, local: radial direction +X, the ring wall centre at x = 0, ring top at z = 0."""
    w, ti, hi, to, ho, tb, slot = P["saddle"]
    wall = P["ring"][1]
    xi = -slot / 2                      # inner face of the slot
    xo = slot / 2
    s = [bx(xi - ti, xi, -w / 2, w / 2, -hi + tb, tb),                                      # inner leg (inside the ring)
         bx(xo, xo + to, -w / 2, w / 2, -ho + tb, tb),                                      # outer leg (in the annulus)
         bx(xi - ti, xo + to, -w / 2, w / 2, 0.0, tb),                                      # bridge resting on the wall
         bx(-30, 30, -8, 8, tb, tb + 50) - ycyl(0, tb + 28, 10.0, -9, 9)]                  # lifting eye
    return fuse(s)


# ----------------------------------------------------------------------------- context
def tripod_context(P=PARAMS):
    """Simplified HatchSide tripod (shared block, not in this BOM): feet, legs, head plate and cheeks."""
    R, zp, rh, zf = P["hs_r_foot"], P["hs_pin_z"], P["hs_r_hub"], P["hs_foot_pin_z"]
    fa, fl, fh = P["hs_foot"]
    parts = []
    for az in P["hs_leg_az"]:
        a = math.radians(az)
        c, s = math.cos(a), math.sin(a)
        foot = Rot(0, 0, az + 90) * Pos(0, -R, 0) * bx(-fa / 2, fa / 2, -fl / 2, fl / 2, 10.0, 10.0 + fh)
        parts.append(foot)
        a0 = (R * c, R * s, zf + fh)
        a1 = (rh * c, rh * s, zp)
        parts.append(sq(a0, a1, 50.0))
    parts.append(zcyl(0, 0, 160.0, zp + 60, zp + 70))
    for x0 in (-23.0, 17.0):
        parts.append(bx(x0, x0 + 6, -150, 30, zp + 70, 2515.0))
    return Compound(parts)


def head_sheave(P=PARAMS):
    sx, sy, sz = P["hs_sheave"]
    so, rp, sw, sb = P["sheave"]
    return xcyl(sy, sz, so, -sw / 2, sw / 2) - xcyl(sy, sz, sb / 2, -sw / 2 - 1, sw / 2 + 1) - _groove(sy, sz, rp, P["rope_d"] / 2 + 0.5)


def well_context(P=PARAMS, depth=600.0):
    li, lw = P["lining"]
    collar = annulus_z(li / 2, li / 2 + lw, -depth, P["collar_h"])
    ground = annulus_z(li / 2 + lw, 2600.0, -60.0, 0.0)
    return collar, ground


def barrow_context(P=PARAMS):
    """Bought builder's tub (90 L) standing on the closed doors, for the dump position."""
    z0 = P["collar_h"] + P["wh_frame"][1] + P["door_angle"][0]
    tub = prism_xy([(-330, -270), (330, -270), (330, 270), (-330, 270)], z0 + 60, z0 + 360)
    inner = prism_xy([(-310, -250), (310, -250), (310, 250), (-310, 250)], z0 + 66, z0 + 361)
    legs = [bx(sx * 280 - 10, sx * 280 + 10, sy * 220 - 10, sy * 220 + 10, z0, z0 + 61) for sx in (-1, 1) for sy in (-1, 1)]
    return fuse([tub - inner] + legs)


# ----------------------------------------------------------------------------- components
@dataclass
class Comp:
    name: str
    shape: object
    bom: int
    group: str
    material: str = "steel"


BOM = {  # key: (BOM line, plain name)
    "frame": (1, "Capstan frame"),
    "drum": (2, "Winding drum with brake drum, ratchet wheel and big sprocket"),
    "pawl": (3, "Pawl"),
    "crank_shaft": (4, "Crank shaft"),
    "small_sprocket": (4, "Small sprocket on its shear pin hub"),
    "cranks": (4, "Removable cranks (2)"),
    "guard": (5, "Chain guard"),
    "brake": (6, "Band brake with weighted lever"),
    "stakes": (7, "Ground stakes (4)"),
    "cradle": (8, "Foot cradle with sheave cheeks"),
    "drawbar": (9, "Drawbar (two halves)"),
    "draw_pins": (9, "Drawbar pins (2)"),
    "head": (10, "Grab head"),
    "ballast": (10, "Grab head ballast plates (2)"),
    "tie_rods": (11, "Tie rods (4)"),
    "shell_pins": (11, "Tie rod pins (4)"),
    "shell_a": (12, "Grab shell A"),
    "shell_b": (12, "Grab shell B"),
    "crosshead": (13, "Crosshead plates"),
    "hinge_pin": (13, "Hinge pin"),
    "cross_axle": (13, "Crosshead sheave axle"),
    "shear_link": (14, "Shear link"),
    "link_pin": (14, "Calibrated link pin"),
    "scraper_pole": (15, "Scraper head: bottom pole with hub, centralizer and spike"),
    "arms": (15, "Scraper arms with toes (2)"),
    "arm_pins": (15, "Arm pins (2)"),
    "sleeve": (15, "Sliding sleeve with foot plate"),
    "struts": (15, "Struts (4)"),
    "sleeve_pins": (15, "Strut pins (2)"),
    "pole_section": (16, "Pole section, 2 m"),
    "tbar": (17, "T-bar with swivel eye"),
    "wh_frame": (18, "Well-head frame with datum brackets"),
    "doors": (19, "Folding doors (2)"),
    "saddles": (20, "Ballast saddles"),
    "drum_bearings": (21, "Drum bearings (2)"),
    "crank_bearings": (22, "Crank bearings (2)"),
    "chain": (23, "Roller chain"),
    "shear_pin": (24, "Crank shear pin"),
    "lead_sheave": (25, "Lead sheave"),
    "lead_axle": (25, "Lead sheave axle"),
    "cross_sheave": (25, "Crosshead sheave"),
    "hs_sheave": (25, "Head sheave for the 8 mm line (fits the HatchSide head)"),
    "rope": (26, "Closing line, 8 mm"),
}

GROUP = {"capstan": ["frame", "drum", "drum_bearings", "crank_bearings", "crank_shaft", "small_sprocket", "shear_pin",
                     "chain", "guard", "cranks", "pawl", "brake", "stakes"],
         "lead": ["cradle", "lead_sheave", "lead_axle", "drawbar", "draw_pins"],
         "grab": ["head", "ballast", "tie_rods", "shell_pins", "shell_a", "shell_b", "crosshead", "hinge_pin",
                  "cross_sheave", "cross_axle", "shear_link", "link_pin"],
         "scraper": ["scraper_pole", "arms", "arm_pins", "sleeve", "sleeve_pins", "struts", "pole_section", "tbar"],
         "wellhead": ["wh_frame", "doors"],
         "saddle": ["saddles"]}

BOUGHT = {"drum_bearings", "crank_bearings", "chain", "shear_pin", "lead_sheave", "cross_sheave", "hs_sheave", "rope", "link_pin"}


def grab_site(P=PARAMS, z_hinge=None):
    D = derived(P)
    z = D["grab_hinge_site"] if z_hinge is None else z_hinge
    return {k: Pos(0, 0, z) * Rot(0, 0, 90) * v for k, v in grab_parts(P).items()}


def scraper_site(P=PARAMS):
    """Scraper laid on the ground on the +X side, pole along Y, arms deployed (as stored for transport
    the arms fold; drawn deployed so the parts show)."""
    out = {}
    for k, v in scraper_parts(P).items():
        out[k] = Pos(1900.0, -300.0, 260.0) * Rot(90, 0, 0) * v
    return out


def saddles_site(P=PARAMS, n=4):
    s = saddle_part(P)
    return Compound([Pos(-1900.0, -600.0 + 320.0 * k, P["saddle"][2] - P["saddle"][5]) * Rot(0, 0, 90) * s for k in range(n)])


def rope_shape(P=PARAMS):
    D = derived(P)
    r = P["rope_d"] / 2
    yd, hd = D["y_d"], P["hd"]
    z_low = D["rope_z_low"]
    core = P["core"][0]
    parts = [rod((0, yd, z_low), (0, P["lead_y"], z_low), r)]
    a, b = D["up_a"], D["up_b"]
    parts.append(rod((0, a[0], a[1]), (0, b[0], b[1]), r))
    zg = D["grab_hinge_site"] + D["head_pin_z"] + P["head_block"][2] - 15 + 40
    parts.append(rod((0, D["drop_y"], P["hs_sheave"][2]), (0, D["drop_y"], zg), r))
    # wound rope on the drum (two layers)
    half = P["drum_w"] / 2
    wound = xcyl(yd, hd, core / 2 + 2 * P["rope_d"], -half, half) - xcyl(yd, hd, core / 2, -half - 1, half + 1)
    parts.append(wound)
    return Compound(parts)


def build_components(P=PARAMS):
    """Every component placed at the well head, in build order."""
    C = {}
    cap = capstan_parts(P)
    for k, v in cap.items():
        C[k] = Comp(BOM[k][1], v, BOM[k][0], "capstan", "cast iron" if k.endswith("bearings") else "steel")
    for k, v in lead_parts(P).items():
        C[k] = Comp(BOM[k][1], v, BOM[k][0], "lead")
    for k, v in grab_site(P).items():
        C[k] = Comp(BOM[k][1], v, BOM[k][0], "grab")
    for k, v in scraper_site(P).items():
        C[k] = Comp(BOM[k][1], v, BOM[k][0], "scraper")
    for k, v in wellhead_parts(P).items():
        C[k] = Comp(BOM[k][1], v, BOM[k][0], "wellhead")
    C["saddles"] = Comp("Ballast saddles (4 of 8 shown)", saddles_site(P), BOM["saddles"][0], "saddle")
    C["hs_sheave"] = Comp(BOM["hs_sheave"][1], head_sheave(P), BOM["hs_sheave"][0], "rope")
    C["rope"] = Comp(BOM["rope"][1], rope_shape(P), BOM["rope"][0], "rope", "polyester")
    return C


# ----------------------------------------------------------------------------- checks, masses, export
def _dist(a, b):
    try:
        return a.distance_to(b)
    except Exception:
        return float("nan")


def _vol(s):
    if s is None:
        return 0.0
    try:
        return s.volume
    except Exception:
        return float("nan")


def checks(P=PARAMS, verbose=True):
    """No two separate parts overlap; every part touches what holds it; folded scraper passes the bore."""
    C = build_components(P)
    D = derived(P)
    res = {"overlaps": [], "floating": [], "clearances": {}}
    holds = [("drum_bearings", "frame"), ("crank_bearings", "frame"), ("drum", "drum_bearings"),
             ("crank_shaft", "crank_bearings"), ("small_sprocket", "crank_shaft"), ("shear_pin", "small_sprocket"),
             ("cranks", "crank_shaft"), ("guard", "frame"), ("pawl", "frame"), ("brake", "frame"), ("stakes", "frame"),
             ("lead_sheave", "lead_axle"), ("lead_axle", "cradle"), ("drawbar", "draw_pins"), ("draw_pins", "cradle"),
             ("draw_pins", "frame"),
             ("hinge_pin", "crosshead"), ("hinge_pin", "shell_a"), ("hinge_pin", "shell_b"), ("cross_axle", "crosshead"),
             ("cross_sheave", "cross_axle"), ("tie_rods", "head"), ("tie_rods", "shell_pins"), ("shell_pins", "shell_a"),
             ("ballast", "head"), ("shear_link", "head"), ("link_pin", "shear_link"),
             ("arms", "arm_pins"), ("arm_pins", "scraper_pole"), ("struts", "arm_pins"), ("struts", "sleeve_pins"), ("sleeve_pins", "sleeve"),
             ("sleeve", "scraper_pole"), ("pole_section", "scraper_pole"), ("tbar", "pole_section"),
             ("doors", "wh_frame")]
    for a, b in holds:
        d = _dist(C[a].shape, C[b].shape)
        if not d <= 0.6:
            res["floating"].append((a, b, round(d, 2)))
    keys = list(C)
    skip = {frozenset(p) for p in [("drum", "chain"), ("small_sprocket", "chain"), ("rope", "drum"), ("rope", "lead_sheave"),
                                   ("rope", "hs_sheave"), ("rope", "head"), ("rope", "cradle"), ("rope", "drawbar"),
                                   ("rope", "frame"), ("rope", "guard"), ("rope", "brake"), ("rope", "ballast")]}
    for i, a in enumerate(keys):
        for b in keys[i + 1:]:
            if frozenset((a, b)) in skip:
                continue
            ba, bb_ = C[a].shape.bounding_box(), C[b].shape.bounding_box()
            if (ba.min.X > bb_.max.X or bb_.min.X > ba.max.X or ba.min.Y > bb_.max.Y or bb_.min.Y > ba.max.Y
                    or ba.min.Z > bb_.max.Z or bb_.min.Z > ba.max.Z):
                continue
            try:
                v = _vol(C[a].shape & C[b].shape)
            except Exception:
                v = float("nan")
            if not v < 1.0:
                res["overlaps"].append((a, b, round(v, 1)))
    res["clearances"]["folded toe radius (mm)"] = round(D["fold_toe_r"], 1)
    res["clearances"]["smallest ring bore radius (mm)"] = D["bore_r_min"]
    res["clearances"]["closed grab half-span (mm)"] = P["shell_R"] + P["shell_t"]
    if verbose:
        print("overlaps (should be none):", res["overlaps"] or "none")
        print("parts not touching what holds them (should be none):", res["floating"] or "none")
        print("clearances:", res["clearances"])
    return res


def masses(P=PARAMS):
    """kg per component from model volumes (steel 7850, cast iron 7200)."""
    m = {}
    cap = capstan_parts(P)
    lead = lead_parts(P)
    grab = grab_parts(P)
    scr = scraper_parts(P)
    wh = wellhead_parts(P)
    rho = {"steel": P["rho_steel"], "cast iron": 7200.0}
    for src in (cap, lead, grab, scr, wh):
        for k, v in src.items():
            mat = "cast iron" if k.endswith("bearings") else "steel"
            m[k] = _vol(v) * 1e-9 * rho[mat]
    m["saddle"] = _vol(saddle_part(P)) * 1e-9 * P["rho_steel"]
    m["doors"] = door_mass(P) * 2
    for k in ("lead_sheave", "cross_sheave"):
        m[k] = 2.2                                                # bought sheave with bearing, catalogue estimate
    m["hs_sheave"] = 2.2
    return m


def export(P=PARAMS):
    (ROOT / "cad" / "step").mkdir(parents=True, exist_ok=True)
    (ROOT / "cad" / "stl").mkdir(parents=True, exist_ok=True)
    cap, lead, grab, scr, wh = capstan_parts(P), lead_parts(P), grab_parts(P), scraper_parts(P), wellhead_parts(P)
    groups = {"capstan": list(cap.values()), "lead": list(lead.values()), "grab": list(grab.values()),
              "scraper": list(scr.values()), "wellhead": list(wh.values()), "saddle": [saddle_part(P)]}
    for g, shapes in groups.items():
        cmp = Compound(shapes)
        export_step(cmp, str(ROOT / "cad" / "step" / f"sinkgrab-{g}.step"))
        export_stl(cmp, str(ROOT / "cad" / "stl" / f"sinkgrab-{g}.stl"), tolerance=0.5, angular_tolerance=0.3)
    C = build_components(P)
    export_step(Compound([c.shape for c in C.values()]), str(ROOT / "cad" / "step" / "sinkgrab-assembly.step"))
    print("exported STEP and STL to cad/step and cad/stl")


if __name__ == "__main__":
    D = derived()
    print({k: (round(v, 2) if isinstance(v, float) else v) for k, v in D.items()})
    checks()
    for k, v in sorted(masses().items()):
        print(f"{k:16s} {v:6.2f} kg")
    if "--check" not in sys.argv:
        export()
