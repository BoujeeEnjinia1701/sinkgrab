"""SinkGrab option A at detail level D3 (kit 1.9, STANDARDS section 24): every made part as its own solid from
real stock, every bolt, nut, washer, pin, clip and stud with its hole, weld beads, bought parts at catalogue size.

Built from the same PARAMS and derived() as cad/src/model.py, in the same coordinate frames:
    capstan(), lead(), wellhead()   site frame: well axis Z, ground z = 0, leg A of the tripod on -Y
    grab()                          grab frame: hinge axis along Y at the origin, shells closed below
    scraper()                       scraper frame: pole axis Z, z = 0 at the toe cutting level, arms open
    saddle()                        saddle frame: radial +X, ring wall centre x = 0, ring top z = 0
Each function returns a list of cad_parts.part() dicts with an extra "key", the component key of
model.BOM (frame, drum, head ...), so the build plan pictures and drawings can group them.
CONCEPT, NOT FOR FABRICATION.
"""
from __future__ import annotations

import math

from build123d import Box, Cylinder, Pos, Rot, Compound, Plane, Vector

import cad_parts as cp
from cad_parts import part, break_edges
import skg_parts as sp

PAINT, GALV, MILD, ZINC, YELLOW, RED = "painted_steel", "galvanised", "mild_steel", "zinc_plated", "safety_yellow", "safety_red"
FAST_BOM = 34


def _M():
    import model
    return model


def mk(name, shape, mat, kind, bom, key, group, explode=(0, 0, 0)):
    d = part(name, shape, mat, kind=kind, bom=bom, group=group, explode=explode)
    d["key"] = key
    return d


def fasteners(items, key, group, bom=FAST_BOM, mat=ZINC):
    return [mk(n, s, mat, "fastener", bom, key, group) for n, s in items]


def weld(name, shape, key, group):
    return mk(f"Weld, {name}", shape, MILD, "weld", None, key, group)


# ================================================================================================ capstan
def capstan(P=None):
    M = _M()
    P = P or M.PARAMS
    D = M.derived(P)
    bx, xcyl, prism_yz, _hull = M.bx, M.xcyl, M.prism_yz, M._hull
    yd, yc, hd, hc = D["y_d"], D["y_c"], P["hd"], P["hc"]
    s, w = P["shs"]
    xa, xb = P["x_brg"]
    rh = P["rail_half"]
    u6, u5 = sp.UCP["UCP206"], sp.UCP["UCP205"]
    pad_top = hd - u6["h"]
    top_top = hc - u5["h"]
    G = "capstan"
    out = []
    FR = lambda n, sh: out.append(mk(f"Capstan frame: {n}", sh, PAINT, "made", 1, "frame", G))  # noqa: E731
    WF = lambda n, sh: out.append(weld(f"capstan frame: {n}", sh, "frame", G))  # noqa: E731

    # ---------------------------------------------------------------- frame members (40 x 40 x 2 SHS, 8 mm plate)
    env = []
    for xs, side in ((xa, "-X"), (xb, "+X")):
        rail = sp.shs_between((xs, yd - rh, s / 2), (xs, yd + rh, s / 2), s, w)
        FR(f"base rail {side}", rail)
        env.append(bx(xs - s / 2, xs + s / 2, yd - rh, yd + rh, 0, s))
        post = sp.shs_between((xs, yc, s), (xs, yc, top_top - 8.0), s, w, up=(0, 1, 0))
        FR(f"post {side}", post)
        post_env = bx(xs - s / 2, xs + s / 2, yc - s / 2, yc + s / 2, s, top_top - 8.0)
        for dy in (-60.0, 60.0):
            FR(f"pad post {side} {'rear' if dy < 0 else 'front'}",
               sp.shs_between((xs, yd + dy, s), (xs, yd + dy, pad_top - 8.0), s, w, up=(0, 1, 0)))
        FR(f"bearing pad {side}", sp.plate(xs - 25, xs + 25, yd - 90, yd + 90, pad_top - 8.0, pad_top,
                                            holes=[("z", xs, yd - u6["J"] / 2, 15.0), ("z", xs, yd + u6["J"] / 2, 15.0)], edge=1.0))
        FR(f"top plate {side}", sp.plate(xs - 25, xs + 25, yc - 75, yc + 75, top_top - 8.0, top_top,
                                          holes=[("z", xs, yc - u5["J"] / 2, 13.5), ("z", xs, yc + u5["J"] / 2, 13.5)], edge=1.0))
        rail_env = bx(xs - s / 2 - 1, xs + s / 2 + 1, yd - rh - 1, yd + rh + 1, -1, s)
        pe = bx(xs - s / 2 - 1, xs + s / 2 + 1, yc - s / 2, yc + s / 2, s - 1, top_top)
        fb = sp.shs_between((xs, yd + rh - 40, s), (xs, yc + 22, 640.0), s, w, up=(1, 0, 0)) - rail_env - pe
        rb = sp.shs_between((xs, yd - rh + 40, s), (xs, yc - 22, 560.0), s, w, up=(1, 0, 0)) - rail_env - pe
        FR(f"front brace {side}", fb)
        FR(f"rear brace {side}", rb)
        # welds: post and pad posts to the rail (front and back faces), plates on posts
        for yy, nm in ((yc, "post"), (yd - 60, "rear pad post"), (yd + 60, "front pad post")):
            for sg in (-1, 1):
                WF(f"{nm} to rail {side} {'front' if sg > 0 else 'back'}",
                   sp.weld_bead((xs - s / 2, yy + sg * s / 2, s), (xs + s / 2, yy + sg * s / 2, s), 4.0, (0, 0, 1), (0, sg, 0)))
        WF(f"pad to posts {side}", sp.weld_bead((xs - s / 2, yd - 90, pad_top - 8), (xs + s / 2, yd - 90, pad_top - 8), 4.0, (0, 0, -1), (0, 1, 0)))
        WF(f"top plate to post {side}", sp.weld_bead((xs - s / 2, yc - 75 + 55, top_top - 8), (xs + s / 2, yc - 75 + 55, top_top - 8), 4.0, (0, 0, -1), (0, -1, 0)))
    xl, xr = xa + s / 2, xb - s / 2
    FR("front cross rail", sp.shs_between((xl, yd + rh - s / 2, s / 2), (xr, yd + rh - s / 2, s / 2), s, w))
    FR("rear cross rail", sp.shs_between((xl, yd - rh + s / 2, s / 2), (xr, yd - rh + s / 2, s / 2), s, w))
    FR("top tie", sp.shs_between((xl, yc, 700.0), (xr, yc, 700.0), s, w))
    FR("brake anchor bar", sp.shs_between((xl, yd - 125, s / 2), (xr, yd - 125, s / 2), s, w))
    for xx, nm in ((xl, "-X"), (xr, "+X")):
        sg = 1 if nm == "-X" else -1
        for yy, n2 in ((yd + rh - s / 2, "front cross rail"), (yd - rh + s / 2, "rear cross rail"), (yd - 125, "anchor bar")):
            WF(f"{n2} {nm} top", sp.weld_bead((xx, yy - s / 2, s), (xx, yy + s / 2, s), 3.0, (sg, 0, 0), (0, 0, 1)))
        WF(f"top tie {nm}", sp.weld_bead((xx, yc - s / 2, 700 + s / 2), (xx, yc + s / 2, 700 + s / 2), 3.0, (sg, 0, 0), (0, 0, 1)))
    dz = P["draw_z"]
    for x0 in (-20.0, 12.0):
        FR(f"drawbar clevis plate at x {x0 + 4:+.0f}",
           sp.plate(x0, x0 + 8, yd + rh, yd + rh + 70, 0.0, 70.0, holes=[("x", yd + rh + 40, dz, 21.0)], edge=1.0))
        for xe, sg in ((x0, -1), (x0 + 8, 1)):
            WF(f"clevis plate {x0 + 4:+.0f} to cross rail {'-X' if sg < 0 else '+X'}", sp.weld_bead((xe, yd + rh, 0.0), (xe, yd + rh, s), 4.0, (sg, 0, 0), (0, 1, 0)))
    pv = M.PAWL_PIVOT(P, yd, hd)
    r0, r1 = D["x_ratchet"]
    FR("pawl bracket", sp.plate(r1 + 1.0, xb - s / 2, pv[0] - 25, pv[0] + 25, pv[1] - 25, pv[1] + 75, holes=[("x", pv[0], pv[1], 12.0)], edge=1.5)
       - M.xcyl(pv[0], pv[1], 6.0, r1, xb - s / 2 + 1))
    pin, clips = sp.pin_with_clips(12.0, (r1 + 21.0, pv[0], pv[1]), (r0 - 14.0, pv[0], pv[1]), clip_axis=(0, 0, 1), inset=6.0)
    out.append(mk("Capstan frame: pawl pin 12 mm", pin, MILD, "made", 1, "frame", G))
    out += fasteners([("Pawl pin split pin (ISO 1234)", clips[1])], "pawl", G)
    out += fasteners([("M12 washer (ISO 7089) on the pawl pin", sp.between(sp.washer(12), (r0, pv[0], pv[1]), (r0 - 5, pv[0], pv[1])))], "pawl", G)
    # brake anchor post (pin hole for the anchor strap) and the lever pivot plate (pivot lowered, SKG-DEC-001)
    xbr = (D["x_brake"][0] + D["x_brake"][1]) / 2
    bk = brake_geometry(P)
    ey = bk["eye"]
    bxm = (D["x_brake"][0] + 3.0, D["x_brake"][1] - 3.0)
    for x0_, nm in ((bxm[0] - 8.0, "-X"), (bxm[1] + 2.0, "+X")):
        FR(f"brake anchor post {nm}", sp.plate(x0_, x0_ + 6.0, yd - 150, yd - 128, s, ey[1] + 16.0, holes=[("x", ey[0], ey[1], 10.5)], edge=1.0))
        WF(f"brake anchor post {nm} to bar", sp.weld_bead((x0_, yd - 145, s), (x0_, yd - 128, s), 3.0, (-1, 0, 0), (0, 0, 1)))
    FR("brake lever pivot plate", sp.plate(xb + s / 2, xb + s / 2 + 8.0, yd - 260, yd - 220, 0.0, bk["pivot"][1] + 22.0,
                                            holes=[("x", bk["pivot"][0], bk["pivot"][1], 12.5)], edge=1.0))
    WF("lever plate to rail", sp.weld_bead((xb + s / 2, yd - 220, 2.0), (xb + s / 2, yd - 220, s), 4.0, (1, 0, 0), (0, 1, 0)))
    for xs, sgn in ((xa, -1), (xb, 1)):
        for yy in M.STAKE_Y(yd):
            xo = xs + sgn * (s / 2 + 16.85)
            FR(f"stake tube {'-X' if sgn < 0 else '+X'} at y {yy - yd:+.0f}", sp.tube_between((xo, yy, 0.0), (xo, yy, 80.0), 33.7, 3.2))
            WF(f"stake tube {'-X' if sgn < 0 else '+X'} {yy - yd:+.0f}", sp.weld_bead((xs + sgn * s / 2, yy - 10, 0.0), (xs + sgn * s / 2, yy - 10, s), 3.0, (sgn, 0, 0), (0, -1, 0)))
    # chain guard clip angles on the -X post (a leaf the guard screws to, a web welded to the post)
    g0, g1 = D["x_guard"]
    for zt in M.GUARD_TABS:
        clip = bx(g1, g1 + 3.0, yc - 20, yc + 20, zt - 12, zt + 26) + bx(g1 + 3.0, xa - s / 2, yc - 20, yc + 20, zt, zt + 3)
        clip = break_edges(clip, 0.6) - xcyl(yc, zt + 12, 3.3, g1 - 1, g1 + 4)
        FR(f"guard clip angle at {zt:.0f}", clip)
    # ---------------------------------------------------------------- winding drum (line 2) and big sprocket (line 23)
    DR = lambda n, sh, mat=PAINT: out.append(mk(f"Winding drum: {n}", sh, mat, "made", 2, "drum", G))  # noqa: E731
    core_o, core_t = P["core"]
    half = P["drum_w"] / 2
    fo, ft = P["flange"]
    DR("core 168.3 x 4.5 pipe", sp.tube_between((-half, yd, hd), (half, yd, hd), core_o, core_t))
    for (x0, x1), nm in zip(D["x_flange"], ("-X", "+X")):
        fl = xcyl(yd, hd, fo / 2, x0, x1)
        fl = break_edges(fl, 1.0) - xcyl(yd, hd, P["drum_shaft"] / 2 + 0.1, x0 - 1, x1 + 1)
        for k in range(6):
            a = math.radians(30 + 60 * k)
            fl -= xcyl(yd + 50 * math.cos(a), hd + 50 * math.sin(a), 18.0, x0 - 1, x1 + 1)
        if nm == "-X":
            fl -= xcyl(yd, hd - 92.0, 5.5, x0 - 1, x1 + 1)              # rope hole for the dead end
        DR(f"flange {nm}", fl)
    bo, bw, bt = P["brake_drum"]
    x0, x1 = D["x_brake"]
    DR("brake drum ring", xcyl(yd, hd, bo / 2, x0, x1) - xcyl(yd, hd, bo / 2 - bt, x0 - 1, x1 + 1))
    web = xcyl(yd, hd, bo / 2 - bt, x0, x0 + 6.0) - xcyl(yd, hd, P["drum_shaft"] / 2 + 0.1, x0 - 1, x0 + 7)
    for k in range(6):
        a = math.radians(60 * k)
        web -= xcyl(yd + 75 * math.cos(a), hd + 75 * math.sin(a), 28.0, x0 - 1, x0 + 7)
    DR("brake drum web", web)
    xf1 = D["x_flange"][1][1]
    DR("spacer ring", xcyl(yd, hd, bo / 2 - bt, xf1, x0) - xcyl(yd, hd, bo / 2 - bt - 6, xf1 - 1, x0 + 1))
    rat = M._ratchet(P, yd, hd, D["x_ratchet"][0])
    DR("ratchet wheel, 20 teeth", rat - xcyl(yd, hd, P["drum_shaft"] / 2 + 0.1, r0 - 1, r1 + 1))
    DR("collar between brake drum and ratchet", xcyl(yd, hd, 22.0, x1, r0) - xcyl(yd, hd, P["drum_shaft"] / 2 + 0.1, x1 - 1, r0 + 1))
    xs0, xs1 = D["drum_shaft_x"]
    DR("shaft 30 mm, S355", sp.bar_between((xs0, yd, hd), (xs1, yd, hd), P["drum_shaft"], 1.0), MILD)
    xsp = D["x_spr"]
    DR("sprocket hub", xcyl(yd, hd, 25.0, xsp + 4, xsp + 30) - xcyl(yd, hd, P["drum_shaft"] / 2 + 0.1, xsp + 3, xsp + 31))
    out.append(mk("Big sprocket, 48 teeth, ISO 08B (bought)", sp.sprocket(P["z_big"], xsp - 4, xsp + 4, yd, hd, P["drum_shaft"] + 0.2),
                  MILD, "bought", 23, "drum", G))
    # rope clamp on the -X flange: a plate and a U-bolt over the dead end
    xcl = D["x_flange"][0][0]
    boss = sp.plate(xcl - 10, xcl, yd - 30, yd + 30, hd - 112, hd - 82, holes=[("x", yd - 20, hd - 97, 8.0), ("x", yd + 20, hd - 97, 8.0)], edge=1.0)
    DR("rope clamp boss, 10 mm, tapped M8", boss)
    strap = sp.plate(xcl - 10 - 8 - 6, xcl - 10 - 8, yd - 30, yd + 30, hd - 112, hd - 82, holes=[("x", yd - 20, hd - 97, 9.0), ("x", yd + 20, hd - 97, 9.0)], edge=1.0)
    DR("rope clamp strap, 6 mm", strap)
    for yy in (yd - 20, yd + 20):
        out += fasteners([(f"M8x20 hex bolt (ISO 4017), rope clamp", sp.between(sp.hex_bolt(8, 20), (xcl - 24.0, yy, hd - 97), (xcl - 30.0, yy, hd - 97)))], "drum", G)
    out.append(weld("winding drum: rope clamp boss to flange", sp.weld_bead((xcl, yd - 30, hd - 82), (xcl, yd + 30, hd - 82), 4.0, (-1, 0, 0), (0, 0, 1)), "drum", G))
    for k, (xx, nm) in enumerate(((-half, "-X"), (half, "+X"))):
        sg = -1 if nm == "-X" else 1
        WF_ = sp.ring_weld((xx, yd, hd), (-sg, 0, 0), core_o / 2, 4.0)
        out.append(weld(f"winding drum: flange {nm} to core", WF_, "drum", G))
        xo = D["x_flange"][k][0] if nm == "-X" else D["x_flange"][k][1]
        if nm == "-X":
            out.append(weld("winding drum: flange -X to shaft", sp.ring_weld((xo, yd, hd), (-1, 0, 0), P["drum_shaft"] / 2, 4.0), "drum", G))
    out.append(weld("winding drum: brake web to shaft", sp.ring_weld((x0 + 6.0, yd, hd), (1, 0, 0), P["drum_shaft"] / 2, 4.0), "drum", G))
    out.append(weld("winding drum: ratchet to shaft", sp.ring_weld((r1, yd, hd), (1, 0, 0), P["drum_shaft"] / 2, 4.0), "drum", G))
    out.append(weld("winding drum: sprocket hub to shaft", sp.ring_weld((xsp + 30, yd, hd), (1, 0, 0), P["drum_shaft"] / 2, 4.0), "drum", G))
    # ---------------------------------------------------------------- bearings (lines 21, 22) with their bolts
    for xs, side in ((xa, "-X"), (xb, "+X")):
        out.append(mk(f"Drum bearing UCP206 {side} (bought)", sp.pillow_block("UCP206", xs, yd, hd, P["drum_shaft"]), MILD, "bought", 21, "drum_bearings", G))
        out.append(mk(f"Crank bearing UCP205 {side} (bought)", sp.pillow_block("UCP205", xs, yc, hc, P["crank_shaft"]), MILD, "bought", 22, "crank_bearings", G))
        for sg in (-1, 1):
            # M14 bolts pushed up through the pad before it is welded on, heads inside the pad posts (D3 detail)
            out += fasteners(sp.captive_bolt(14, 50, (xs, yd + sg * u6["J"] / 2, pad_top - 8.0), clamp=8.0 + u6["H1"],
                                             label=f", drum bearing {side}"), "drum_bearings", G)
            out += fasteners(sp.bolt_set(12, 8.0 + u5["H1"], (xs, yc + sg * u5["J"] / 2, top_top + u5["H1"]), label=f", crank bearing {side}"),
                             "crank_bearings", G)
    # ---------------------------------------------------------------- crank shaft, driven member and slip clutch (lines 4, 24)
    # Amish's decision O4 of 2026-10-25 (SKG-DEC-001): a friction slip clutch replaces the 3 mm shear pin. The sprocket
    # and two driven discs are welded to a sleeve that runs on the shaft; woven facings bonded to an inner flange
    # (welded to the shaft) and to a keyed pressure plate grip the discs, clamped by two disc springs and a KM5 locknut.
    c0, c1 = D["crank_shaft_x"]
    cd, cf, ct, cpt, cft = P["clutch"]
    r_sh = P["crank_shaft"] / 2
    cs = sp.bar_between((c0, yc, hc), (c1, yc, hc), P["crank_shaft"], 0.8)
    for xe0, xe1 in ((c0 - 1, c0 + 40), (c1 - 40, c1 + 1)):
        ring = xcyl(yc, hc, 14.0, xe0, xe1) - bx(xe0 - 1, xe1 + 1, yc - 10, yc + 10, hc - 10, hc + 10)
        cs -= ring
    for xb_ in (c0 + 9.0, c1 - 5.0):
        cs -= sp.yhole(xb_, hc, 6.2, yc - 20, yc + 20)
    cs -= bx(xsp - 37.0, xsp - 19.0, yc - 4.0, yc + 4.0, hc + r_sh - 4.0, hc + r_sh + 1.0)          # 8 x 4 keyway
    out.append(mk("Crank shaft 25 mm, S355, square ends, keyway, M25 x 1.5 thread for the clutch nut", cs, MILD, "made", 4, "crank_shaft", G))
    sl = xcyl(yc, hc, 18.0, xsp - 20.0, xsp + 20.0) - xcyl(yc, hc, r_sh + 0.1, xsp - 21, xsp + 21)
    out.append(mk("Driven sleeve 36 mm, bored to run on the shaft", break_edges(sl, 0.5), PAINT, "made", 4, "small_sprocket", G))
    out.append(mk("Small sprocket, 12 teeth, ISO 08B (bought)", sp.sprocket(P["z_small"], xsp - 4, xsp + 4, yc, hc, 36.1), MILD, "bought", 23, "small_sprocket", G))
    out.append(weld("crank: small sprocket to sleeve", sp.ring_weld((xsp + 4, yc, hc), (1, 0, 0), 18.0, 3.0), "small_sprocket", G))
    for x0, nm, wx, wd in ((xsp - 17.0, "outboard", xsp - 17.0, -1), (xsp + 11.0, "inboard", xsp + 17.0, 1)):
        dsc = xcyl(yc, hc, cd / 2, x0, x0 + ct) - xcyl(yc, hc, 18.1, x0 - 1, x0 + ct + 1)
        out.append(mk(f"Clutch driven disc {nm}, 6 mm, 84 mm, ground faces", break_edges(dsc, 0.6), MILD, "made", 24, "small_sprocket", G))
        out.append(weld(f"crank: driven disc {nm} to sleeve", sp.ring_weld((wx, yc, hc), (wd, 0, 0), 18.0, 3.0), "small_sprocket", G))

    def _ring(ro, ri, x0, x1):
        return xcyl(yc, hc, ro, x0, x1) - xcyl(yc, hc, ri, x0 - 1, x1 + 1)
    out.append(mk("Clutch facing, inboard, 4 mm woven lining 84 x 44, bonded to the flange", _ring(cd / 2, cf / 2 + 2.0, xsp + 17.0, xsp + 17.0 + cft),
                  "rubber_belt", "bought", 24, "clutch", G))
    fl = _ring(cd / 2, r_sh + 0.05, xsp + 21.0, xsp + 21.0 + cpt)
    out.append(mk("Clutch inner flange, 8 mm, 84 mm, welded to the shaft", break_edges(fl, 0.6), MILD, "made", 24, "clutch", G))
    out.append(weld("crank: clutch inner flange to shaft", sp.ring_weld((xsp + 29.0, yc, hc), (1, 0, 0), r_sh, 4.0), "clutch", G))
    out.append(mk("Clutch facing, outboard, 4 mm woven lining 84 x 44, bonded to the pressure plate", _ring(cd / 2, cf / 2 + 2.0, xsp - 17.0 - cft, xsp - 17.0),
                  "rubber_belt", "bought", 24, "clutch", G))
    pp = _ring(cd / 2, r_sh + 0.1, xsp - 29.0, xsp - 29.0 + cpt) - bx(xsp - 30, xsp - 20, yc - 4.05, yc + 4.05, hc + r_sh - 1.0, hc + r_sh + 3.3)
    out.append(mk("Clutch pressure plate, 8 mm, 84 mm, keyed to slide", break_edges(pp, 0.6), MILD, "made", 24, "clutch", G))
    key = bx(xsp - 28.9, xsp - 21.1, yc - 4.0, yc + 4.0, hc + r_sh - 4.0, hc + r_sh + 3.0)
    out += fasteners([("Parallel key 8 x 7 x 8 (ISO 773), clutch", key)], "clutch", G, bom=24, mat=MILD)
    for k, x0 in enumerate((xsp - 32.05, xsp - 35.1)):
        out += fasteners([(f"Disc spring 50 x 25.4 x 2.0 (DIN EN 16983, series B), clutch, {k + 1} of 2", _ring(25.0, 12.75, x0, x0 + 3.05))], "clutch", G, bom=24, mat=MILD)
    tab = _ring(21.0, r_sh + 0.1, xsp - 36.35, xsp - 35.1) + bx(xsp - 36.35, xsp - 35.1, yc - 3.0, yc + 3.0, hc + r_sh - 3.5, hc + r_sh + 0.2)
    out += fasteners([("Tab washer MB5 (ISO 2982-2), clutch", tab)], "clutch", G, bom=24, mat=MILD)
    nut = _ring(19.0, r_sh + 0.05, xsp - 43.35, xsp - 36.35)
    for k in range(4):
        a_ = math.radians(45 + 90 * k)
        nut -= Pos(xsp - 39.85, yc + 18.5 * math.cos(a_), hc + 18.5 * math.sin(a_)) * Rot(a_ * 180 / math.pi, 0, 0) * Box(8, 5, 4)
    out += fasteners([("Locknut KM5, M25 x 1.5 (ISO 2982-2), clutch setting", nut)], "clutch", G, bom=24)
    # cranks: arm with a square socket, handle tube turning on a welded 20 mm stub axle, washer and split pin
    for (x0_, x1_), sgn, ang, hl, nm in ((D["x_crank"][0], -1, 90.0, P["handle"][1], "-X"), (D["x_crank"][1], 1, -90.0, P["handle_long"], "+X")):
        a = math.radians(ang)
        ey, ez = yc + P["crank_r"] * math.cos(a), hc + P["crank_r"] * math.sin(a)
        arm = prism_yz(_hull([(yc + 22 * math.cos(t), hc + 22 * math.sin(t)) for t in [2 * math.pi * k / 24 for k in range(24)]] +
                             [(ey + 18 * math.cos(t), ez + 18 * math.sin(t)) for t in [2 * math.pi * k / 24 for k in range(24)]]), x0_, x1_)
        arm = break_edges(arm, 1.0) - bx(x0_ - 1, x1_ + 1, yc - 10.1, yc + 10.1, hc - 10.1, hc + 10.1)
        out.append(mk(f"Crank arm {nm}, 12 mm plate, square socket", arm, PAINT, "made", 4, "cranks", G))
        xo = x0_ if sgn < 0 else x1_
        stub_end = xo + sgn * (hl + 22.0)
        stub, hclips = sp.pin_with_clips(20.0, (xo, ey, ez), (stub_end, ey, ez), clip_axis=(0, 0, 1), inset=6.0)
        out.append(mk(f"Crank handle stub axle {nm}, 20 mm", stub, MILD, "made", 4, "cranks", G))
        out.append(weld(f"crank: stub axle {nm} to arm", sp.ring_weld((xo, ey, ez), (sgn, 0, 0), 10.0, 4.0), "cranks", G))
        h0 = xo + sgn * 5.0
        h1 = xo + sgn * (5.0 + hl)
        handle = sp.between(cp.round_tube(32.0, 5.75, hl), (min(h0, h1), ey, ez), (max(h0, h1), ey, ez))
        out.append(mk(f"Crank handle {nm}, 32 mm tube {hl:.0f} long", break_edges(handle, 0.8), "hdpe_black", "made", 4, "cranks", G))
        out += fasteners([(f"M20 washer (ISO 7089), handle {nm}", sp.between(sp.washer(20), (h1, ey, ez), (h1 + sgn * 5, ey, ez))),
                          (f"Handle split pin {nm}", hclips[1])], "cranks", G)
        # ball-lock pin through the shaft end, outboard of the arm
        xb_ = c0 + 9.0 if sgn < 0 else c1 - 5.0
        blp = sp.bar_between((xb_, yc - 22, hc), (xb_, yc + 22, hc), 6.0, 0.5) + Pos(xb_, yc - 24, hc) * Rot(90, 0, 0) * Cylinder(7, 4)
        blp += Pos(xb_, yc - 30, hc) * Rot(0, 90, 0) * (Cylinder(10, 2.5) - Cylinder(8, 3))
        out += fasteners([(f"Ball-lock pin 6 mm, crank {nm}", blp)], "cranks", G)
    # ---------------------------------------------------------------- roller chain (line 23), chain guard (line 5)
    rb, rs = D["pd_big"] / 2, D["pd_small"] / 2
    ch = M.capstan_parts(P)["chain"]
    out.append(mk("Roller chain ISO 08B-1, 1.6 m (bought)", ch, MILD, "bought", 23, "chain", G))
    guard = M.capstan_parts(P)["guard"]
    for zt in M.GUARD_TABS:
        guard = guard - xcyl(yc, zt + 12, 3.3, g1 - 3, g1 + 1)
    out.append(mk("Chain guard, 1.5 mm sheet", guard, YELLOW, "made", 5, "guard", G))
    for zt in M.GUARD_TABS:
        out += fasteners(sp.bolt_set(6, 4.5, (g1 + 3.0, yc, zt + 12), axis=(1, 0, 0), label=f", guard at {zt:.0f}"), "guard", G)
    # ---------------------------------------------------------------- pawl (line 3)
    pawl = M.capstan_parts(P)["pawl"]
    out.append(mk("Pawl, 8 mm plate", break_edges(pawl, 0.6), PAINT, "made", 3, "pawl", G))
    # ---------------------------------------------------------------- band brake with weighted lever (line 6)
    out += brake_parts(P, bk)
    # ---------------------------------------------------------------- ground stakes (line 7)
    for xs, sgn in ((xa, -1), (xb, 1)):
        for yy in M.STAKE_Y(yd):
            xo = xs + sgn * (s / 2 + 16.85)
            st = Pos(xo, yy, -140.0) * Cylinder(12.5, 440.0)
            st = st + _cone_at((xo, yy, -420.0), 1.0, 12.5, 60.0) + Pos(xo, yy, 83.0) * Cylinder(17.0, 6.0)
            out.append(mk(f"Ground stake {'-X' if sgn < 0 else '+X'} at y {yy - yd:+.0f}", break_edges(st, 0.5), MILD, "made", 7, "stakes", G))
    return out


def _cone_at(base, r0, r1, h):
    from build123d import Solid
    return Solid.make_cone(r0, r1, h, Plane(origin=base))


def brake_geometry(P):
    """Band brake layout. The kit 1.7 model hung the live-end link on a pin 25 mm below the lever pivot on the
    well side, so the falling weight slackened the band. Here (SKG-DEC-001, D3 detail fix) the link leaves the
    band's live end on the tangent and runs to a pin on a short upright arm 60 mm above the lever pivot, so the
    falling weight pulls the band tight; the lever ratio stays about 10:1 (SKG-CAL-001, F1)."""
    M = _M()
    D = M.derived(P)
    yd, hd = D["y_d"], P["hd"]
    rr = P["brake_drum"][0] / 2
    ro = rr + 8.5                                         # lining 5 mm and band 3 mm on the 250 mm drum
    a = math.radians(-100.0)
    A = (yd + ro * math.cos(a), hd + ro * math.sin(a))    # live end on the band's outer face
    tdir = (math.sin(a), -math.cos(a))                    # tangent leaving the live end toward -Y
    yB = yd - 240.0
    t = (yB - A[0]) / tdir[0]
    B = (yB, A[1] + t * tdir[1])                          # link pin on the lever's upright arm
    pivot = (yB, B[1] - 60.0)
    ae = math.radians(172.0)
    eye = (yd + 141.0 * math.cos(ae), hd + 141.0 * math.sin(ae))   # anchor-end eye, pinned between two posts
    return dict(A=A, B=B, pivot=pivot, end=(yd - 890.0, 300.0), eye=eye, ro=ro, rr=rr, link_len=t)


def brake_parts(P, bk):
    M = _M()
    D = M.derived(P)
    bx, xcyl, prism_yz = M.bx, M.xcyl, M.prism_yz
    yd, hd = D["y_d"], P["hd"]
    s = P["shs"][0]
    xb = P["x_brg"][1]
    G = "capstan"
    out = []
    rr, ro = bk["rr"], bk["ro"]
    bxm = (D["x_brake"][0] + 3.0, D["x_brake"][1] - 3.0)

    def arc(r0, r1, a0=-100, a1=170):
        po = [(yd + r1 * math.cos(math.radians(a)), hd + r1 * math.sin(math.radians(a))) for a in range(a0, a1 + 1, 5)]
        pi = [(yd + r0 * math.cos(math.radians(a)), hd + r0 * math.sin(math.radians(a))) for a in range(a1, a0 - 1, -5)]
        return prism_yz(po + pi, bxm[0], bxm[1])
    out.append(mk("Brake lining, 5 mm bonded", arc(rr + 0.5, rr + 5.5), "rubber_belt", "made", 6, "brake", G))
    out.append(mk("Brake band, 40 x 3 spring steel", arc(rr + 5.5, ro), MILD, "made", 6, "brake", G))
    # anchor end: a 16 mm eye welded across the band end, pinned with a 10 mm pin between two 6 mm posts
    ey = bk["eye"]
    eye = sp.between(cp.round_tube(16.0, 2.75, bxm[1] - bxm[0]), (bxm[0], ey[0], ey[1]), (bxm[1], ey[0], ey[1]))
    out.append(mk("Brake band anchor eye, 16 mm tube", eye, MILD, "made", 6, "brake", G))
    out.append(weld("brake: anchor eye to band", sp.weld_bead((bxm[0], ey[0] + 6.0, ey[1] - 4.0), (bxm[1], ey[0] + 6.0, ey[1] - 4.0), 3.0, (0, 1, 0), (0, 0, -1)), "brake", G))
    apn, aclips = sp.pin_with_clips(10.0, (bxm[0] - 16.0, ey[0], ey[1]), (bxm[1] + 16.0, ey[0], ey[1]), clip_axis=(0, 0, 1), inset=4.0)
    out.append(mk("Brake anchor pin 10 mm", apn, MILD, "made", 6, "brake", G))
    out += fasteners([("Brake anchor split pin -X", aclips[0]), ("Brake anchor split pin +X", aclips[1])], "brake", G)
    # live end: 25 x 6 link welded on the band's outer face, eye at the lever's upright arm
    A, B, pv = bk["A"], bk["B"], bk["pivot"]
    xlc = 146.0
    ux, uz = (B[0] - A[0]), (B[1] - A[1])
    L = math.hypot(ux, uz)
    ux, uz = ux / L, uz / L
    link = sp.flat_between((xlc, A[0] - 4.0 * uz, A[1] + 4.0 * ux), (xlc, B[0] + 14.0 * ux, B[1] + 14.0 * uz), 25.0, 6.0, up=(1, 0, 0))
    link = link - xcyl(B[0], B[1], 6.25, xlc - 20, xlc + 20)
    out.append(mk("Brake link, 25 x 6 flat", link, PAINT, "made", 6, "brake", G))
    # lever: 40 x 12 flat with a short upright arm at the pivot carrying the link pin
    xL0, xL1 = xb + s / 2 + 9.0, xb + s / 2 + 21.0
    xLc = (xL0 + xL1) / 2
    vx, vz = bk["end"][0] - pv[0], bk["end"][1] - pv[1]
    Lv = math.hypot(vx, vz)
    vx, vz = vx / Lv, vz / Lv
    lv = sp.flat_between((xLc, pv[0] - 12.0 * vx, pv[1] - 12.0 * vz), (xLc, bk["end"][0], bk["end"][1]), 40.0, 12.0, up=(0, -vz, vx))
    lv = lv + sp.plate(xL0, xL1, pv[0] - 15, pv[0] + 15, pv[1] - 10, B[1] + 16, edge=1.0)
    wc = (pv[0] + 610.0 * vx, pv[1] + 610.0 * vz)
    lv = lv - xcyl(pv[0], pv[1], 6.25, xL0 - 1, xL1 + 1) - xcyl(B[0], B[1], 6.25, xL0 - 1, xL1 + 1) - xcyl(wc[0], wc[1], 6.5, xL0 - 1, xL1 + 1)
    out.append(mk("Brake lever, 40 x 12 flat with upright arm", lv, PAINT, "made", 6, "brake", G))
    wx, wy, wz = P["brake_weight"]
    wt = sp.plate(xL1 + 0.5, xL1 + 0.5 + wx, wc[0] - wy / 2, wc[0] + wy / 2, wc[1] - wz / 2, wc[1] + wz / 2, holes=[("x", wc[0], wc[1], 13.0)], edge=3.0)
    out.append(mk("Brake weight, 6 kg steel block", wt, PAINT, "made", 6, "brake", G))
    out += fasteners(sp.bolt_set(12, 12.0 + 0.5 + wx, (xL0, wc[0], wc[1]), axis=(-1, 0, 0), label=", brake weight"), "brake", G)
    cpn, cclips = sp.pin_with_clips(12.0, (xlc - 12.5 - 9.0, B[0], B[1]), (xL1 + 9.0, B[0], B[1]), clip_axis=(0, 0, 1), inset=4.5)
    out.append(mk("Brake link cross pin 12 mm", cpn, MILD, "made", 6, "brake", G))
    out += fasteners([("Link cross pin split pin, inner", cclips[0]), ("Link cross pin split pin, outer", cclips[1])], "brake", G)
    ppn, pclips = sp.pin_with_clips(12.0, (xb + s / 2 - 9.0, pv[0], pv[1]), (xL1 + 9.0, pv[0], pv[1]), clip_axis=(0, 0, 1), inset=4.5)
    out.append(mk("Brake lever pivot pin 12 mm", ppn, MILD, "made", 6, "brake", G))
    out += fasteners([("Lever pivot split pin, inner", pclips[0]), ("Lever pivot split pin, outer", pclips[1])], "brake", G)
    return out


def _clevis(d, grip, head_at, axis, label):
    """ISO 2341 clevis pin with its split pin; head bearing at head_at, pin running along -axis."""
    pl = Plane(origin=Vector(*head_at), z_dir=Vector(*axis))
    pin = pl * cp.clevis_pin(int(d) if d == int(d) else d, grip)
    clip = pl * (Pos(0, 0, -grip - d) * cp.split_pin(d))
    return [(f"Clevis pin {d:.0f} mm (ISO 2341), {label}", pin), (f"Split pin (ISO 1234), {label}", clip)]


# ================================================================================================ lead cradle and drawbar
def lead(P=None):
    M = _M()
    P = P or M.PARAMS
    D = M.derived(P)
    bx, xcyl, ycyl, prism_yz, fuse = M.bx, M.xcyl, M.ycyl, M.prism_yz, M.fuse
    ly, lz = P["lead_y"], P["lead_z"]
    fa, fl, fh = P["hs_foot"]
    yf = -P["hs_r_foot"]
    so, spd, sw, sb = P["sheave"]
    G = "lead"
    out = []
    CR = lambda n, sh: out.append(mk(f"Foot cradle: {n}", sh, PAINT, "made", 8, "cradle", G))  # noqa: E731
    base = fuse([bx(-160, 160, yf - fl / 2 - 30, yf + fl / 2 + 20, 0.0, 10.0), bx(-60, 60, ly - 200, yf - fl / 2 - 30 + 1, 0.0, 10.0)])
    CR("base plate 10 mm, profile cut", break_edges(base, 1.0))
    z_foot_top = 10.0 + fh
    CR("rim flat, rear", sp.plate(-fa / 2 - 6, fa / 2 + 6, yf - fl / 2 - 6, yf - fl / 2 - 2, 10.0, z_foot_top, edge=0.8))
    CR("rim flat, -X", sp.plate(-fa / 2 - 6, -fa / 2 - 2, yf - fl / 2 - 2, yf + fl / 2, 10.0, z_foot_top, edge=0.8))
    CR("rim flat, +X", sp.plate(fa / 2 + 2, fa / 2 + 6, yf - fl / 2 - 2, yf + fl / 2, 10.0, z_foot_top, edge=0.8))
    for yy, nm in ((yf - 70.0, "rear"), (yf + 70.0, "front")):
        # clamp bars sit on top of the foot plate (z 28 to 38; the kit 1.7 model had them inside it)
        CR(f"clamp bar {nm}", sp.plate(-130, 130, yy - 20, yy + 20, z_foot_top, z_foot_top + 10.0,
                                        holes=[("z", -110.0, yy, 13.0), ("z", 110.0, yy, 13.0)], edge=1.0))
        for xx in (-110.0, 110.0):
            out += fasteners(sp.stud_set(12, 45.0, (xx, yy, 10.0), clamp=z_foot_top + 10.0 - 10.0, label=f", clamp bar {nm} x {xx:+.0f}"), "cradle", G, bom=8)
            out.append(weld(f"foot cradle: stud {nm} {xx:+.0f}", sp.ring_weld((xx, yy, 10.0), (0, 0, 1), 6.0, 3.0), "cradle", G))
    for x0 in (-sw / 2 - 1 - 8, sw / 2 + 1):
        ch = prism_yz([(ly - 110, 10.0), (ly + 110, 10.0), (ly + 60, lz + 85), (ly - 60, lz + 85)], x0, x0 + 8)
        ch = break_edges(ch, 1.0) - xcyl(ly, lz, sb / 2 + 0.25, x0 - 1, x0 + 9)
        CR(f"sheave cheek at x {x0 + 4:+.0f}", ch)
        sg = -1 if x0 < 0 else 1
        out.append(weld(f"foot cradle: cheek {x0 + 4:+.0f} outer", sp.weld_bead((x0 + (8 if sg > 0 else 0), ly - 100, 10.0), (x0 + (8 if sg > 0 else 0), ly + 100, 10.0), 5.0, (sg, 0, 0), (0, 0, 1)), "cradle", G))
    dz = P["draw_z"]
    for x0 in (-20.0, 12.0):
        CR(f"drawbar clevis plate at x {x0 + 4:+.0f}", sp.plate(x0, x0 + 8, ly - 190, ly - 110, 10.0, 70.0, holes=[("x", ly - 160, dz, 21.0)], edge=1.0))
    out.append(weld("foot cradle: rim to base", sp.weld_bead((-fa / 2 - 6, yf - fl / 2 - 6, 10.0), (fa / 2 + 6, yf - fl / 2 - 6, 10.0), 3.0, (0, -1, 0), (0, 0, 1)), "cradle", G))
    out.append(mk("Lead sheave 150 mm for 8 mm rope (bought)", sp.sheave(so * 2, spd * 2, sw, sb, P["rope_d"], (0, ly, lz), (1, 0, 0)), ZINC, "bought", 25, "lead_sheave", G))
    ax_, aclips = sp.pin_with_clips(sb - 0.2, (-sw / 2 - 22, ly, lz), (sw / 2 + 22, ly, lz), clip_axis=(0, 0, 1), inset=6.0)
    out.append(mk("Lead sheave axle 20 mm", ax_, MILD, "made", 8, "lead_axle", G))
    out += fasteners([("Lead axle split pin -X", aclips[0]), ("Lead axle split pin +X", aclips[1])], "lead_axle", G)
    # drawbar (line 9): two halves of 48.3 x 3.2 with a 41 mm spigot, 12 mm tongues slotted in and welded
    do, dt = P["draw_tube"]
    y_front = D["y_d"] + P["rail_half"] + 40.0
    y_back = ly - 160.0
    ym = (y_front + y_back) / 2
    DB = lambda n, sh, mat=PAINT: out.append(mk(f"Drawbar: {n}", sh, mat, "made", 9, "drawbar", G))  # noqa: E731
    DB("half at the capstan, 48.3 x 3.2", sp.tube_between((0, y_front + 36, dz), (0, ym, dz), do, dt))
    DB("half at the cradle, 48.3 x 3.2", sp.tube_between((0, ym, dz), (0, y_back - 36, dz), do, dt))
    DB("spigot 41 mm bar", sp.bar_between((0, ym - 100, dz), (0, ym + 100, dz), do - 2 * dt - 1.0, 1.0), MILD)
    tg1 = sp.plate(-6, 6, y_front - 25, y_front + 60, dz - 20, dz + 20, holes=[("x", y_front, dz, 21.0)], edge=1.5)
    tg2 = sp.plate(-6, 6, y_back - 60, y_back + 25, dz - 20, dz + 20, holes=[("x", y_back, dz, 21.0)], edge=1.5)
    DB("tongue at the capstan, 12 mm", tg1)
    DB("tongue at the cradle, 12 mm", tg2)
    out.append(weld("drawbar: tongue to tube, capstan end", sp.ring_weld((0, y_front + 36, dz), (0, -1, 0), do / 2, 3.0), "drawbar", G))
    out.append(weld("drawbar: tongue to tube, cradle end", sp.ring_weld((0, y_back - 36, dz), (0, 1, 0), do / 2, 3.0), "drawbar", G))
    for yy, nm in ((y_front, "capstan"), (y_back, "cradle")):
        out += fasteners(_clevis(20.0, 40.0, (20.0, yy, dz), (1, 0, 0), f"drawbar at the {nm}"), "draw_pins", G, bom=9)
    return out


# Contacts that are meant to overlap: weld beads fuse into the parts they join; chain rollers sit in sprocket
# teeth; split pins fill their holes; the line lies in sheave grooves and on the drum; band, eye and link are
# welded together. Name pairs as cad_check.py reads them (substring match on both names).
ALLOWED = [
    ("Weld, capstan frame", "Capstan frame"), ("Weld, winding drum", "Winding drum"), ("Weld, winding drum", "shaft"),
    ("Weld, crank: stub", "Crank arm"), ("Weld, crank: stub", "stub axle"), ("Weld, crank: small sprocket", "sprocket"),
    ("Weld, crank: small sprocket", "Sprocket hub"), ("Weld, brake", "Brake"), ("Brake link", "Brake band"),
    ("Weld, foot cradle", "Foot cradle"), ("Weld, foot cradle", "welded stud"), ("Weld, drawbar", "Drawbar"),
    ("sprocket", "Roller chain"), ("split pin", "pin"), ("split pin", "stub axle"),
]


# ================================================================================================ grab (local frame)
def grab_geometry(P):
    """Grab frame numbers shared by the detail and the drawings. The head box sits 19 mm below the head pin axis
    (15 mm in the kit 1.7 model, where the 25 mm pins cut into the 6 mm bottom plate; D3 detail fix)."""
    M = _M()
    D = M.derived(P)
    zh = D["head_pin_z"]
    hx, hy, hz = P["head_block"]
    z0 = zh - 19.0
    so, rp, sw, sb = P["sheave"]
    return dict(zh=zh, z0=z0, z1=z0 + hz, zu=z0 - 85.0, zs=120.0, rp=rp, sw=sw, sb=sb, so=so, hx=hx, hy=hy,
                yA=P["shell_B"] / 2 + P["end_t"], yB=P["shell_B"] / 2 + 2 * P["end_t"] + 1.0, yd_=2 * rp,
                xa0=rp - 4, xa1=rp + 6, zl=197.0)


def grab(P=None):
    M = _M()
    P = P or M.PARAMS
    D = M.derived(P)
    bx, xcyl, ycyl, zcyl, prism_xz, prism_yz, ring_sector_xz, fuse, _hull = (M.bx, M.xcyl, M.ycyl, M.zcyl, M.prism_xz,
                                                                             M.prism_yz, M.ring_sector_xz, M.fuse, M._hull)
    g = grab_geometry(P)
    R, B, t, et, tt = P["shell_R"], P["shell_B"], P["shell_t"], P["end_t"], P["top_t"]
    hp = P["hinge_pin"]
    sx, sz = P["shell_pin"]
    G = "grab"
    out = []
    # ---------------------------------------------------------------- shells (line 12)
    for side, key, nm in ((1, "shell_a", "A"), (-1, "shell_b", "B")):
        yi = B / 2 if side > 0 else B / 2 + et + 1.0
        rot = (lambda sh: sh) if side > 0 else (lambda sh: Rot(0, 0, 180) * sh)
        skin = ring_sector_xz(R, R + t, -90, 0, -yi, yi)
        out.append(mk(f"Grab shell {nm}: skin, 4 mm rolled to 230 mm radius", rot(skin), PAINT, "made", 12, key, G))
        out.append(mk(f"Grab shell {nm}: top cover, 4 mm", rot(sp.plate(50, R - 0.6, -yi, yi, -tt, 0.0, edge=0.8) - skin), PAINT, "made", 12, key, G))
        for sgn in (-1, 1):
            y0, y1 = (yi, yi + et) if sgn > 0 else (-yi - et, -yi)
            q = [(0.0, 0.0)] + [((R + t) * math.cos(math.radians(a)), (R + t) * math.sin(math.radians(a))) for a in range(-90, 1, 5)]
            ep = prism_xz(q, y0, y1) + ycyl(0, 0, 35.0, y0, y1) + prism_xz([(150, -5), (sx + 30, -5), (sx + 30, sz + 25), (150, sz + 25)], y0, y1)
            ep = break_edges(ep.clean(), 1.0)
            ep = ep - ycyl(0, 0, hp / 2 + 0.25, y0 - 1, y1 + 1) - ycyl(sx, sz, 10.25, y0 - 1, y1 + 1)
            out.append(mk(f"Grab shell {nm}: end plate {'+Y' if sgn > 0 else '-Y'}, 6 mm with boss and lug", rot(ep), PAINT, "made", 12, key, G))
            out.append(weld(f"grab shell {nm}: cover to end plate {'+Y' if sgn > 0 else '-Y'}",
                            rot(sp.weld_bead((60, sgn * yi, -tt), (R - 10, sgn * yi, -tt), 4.0, (0, 0, -1), (0, -sgn, 0))), key, G))
        lip = break_edges(bx(1.0, 11.0, -yi, yi, -R - t, -R + 45), 0.8) - skin
        out.append(mk(f"Grab shell {nm}: cutting lip 10 x 50, wear-resistant", rot(lip), "mild_steel", "made", 12, key, G))
        zr = -math.sqrt(R * R - 11.0 * 11.0)
        out.append(weld(f"grab shell {nm}: lip to skin", rot(sp.weld_bead((11.0, -yi + 5, zr + 0.3), (11.0, yi - 5, zr + 0.3), 4.0, (0, 0, 1), (1, 0, 0.05))), key, G))
    yA, yB = g["yA"], g["yB"]
    # ---------------------------------------------------------------- hinge pin, set collars (line 13)
    hpin, hclips = sp.pin_with_clips(hp, (0, -yB - 20, 0), (0, yB + 20, 0), clip_axis=(0, 0, 1), inset=8.0)
    out.append(mk("Grab hinge pin 30 mm, S355", hpin, MILD, "made", 13, "hinge_pin", G))
    out += fasteners([("Hinge pin split pin -Y", hclips[0]), ("Hinge pin split pin +Y", hclips[1])], "hinge_pin", G)
    so, rp, sw, sb, zs = g["so"], g["rp"], g["sw"], g["sb"], g["zs"]
    for sgn in (-1, 1):
        y0 = sgn * (sw / 2 + 11 + 0.5)
        col = sp.between(cp.round_tube(50.0, 9.9, 16.0), (0, y0, 0), (0, y0 + sgn * 16.0, 0))
        col = break_edges(col, 0.8) + Pos(0, y0 + sgn * 8.0, 25.0) * Cylinder(4.0, 6.0)
        out.append(mk(f"Set collar 30 mm on the hinge pin {'+Y' if sgn > 0 else '-Y'} (bought)", col, ZINC, "bought", 13, "hinge_pin", G))
    # ---------------------------------------------------------------- crosshead plates, dead end, sheave, axle (lines 13, 25)
    yd_, xa0, xa1, zl = g["yd_"], g["xa0"], g["xa1"], g["zl"]
    for y0, nm in ((-sw / 2 - 1 - 10, "-Y"), (sw / 2 + 1, "+Y")):
        pl = prism_xz(_hull([(40 * math.cos(a), 40 * math.sin(a)) for a in [2 * math.pi * k / 24 for k in range(24)]] +
                            [(45 * math.cos(a), zs + 45 * math.sin(a)) for a in [2 * math.pi * k / 24 for k in range(24)]]), y0, y0 + 10)
        if nm == "+Y":
            pl = fuse([pl, bx(20.0, xa1, sw / 2 + 1, sw / 2 + 11, 130.0, 185.0), bx(xa0, xa1, sw / 2 + 11, yd_ + 20, 140.0, 185.0),
                       bx(xa0, xa1, yd_ - 18, yd_ + 18, 185.0, 210.0)])
            pl = pl - xcyl(yd_, zl, 8.25, xa0 - 1, xa1 + 1)
        pl = break_edges(pl, 0.8)
        pl = pl - ycyl(0, 0, hp / 2 + 0.25, y0 - 1, y0 + 11) - ycyl(0, zs, sb / 2 + 0.25, y0 - 1, y0 + 11)
        out.append(mk(f"Crosshead plate {nm}, 10 mm{' with dead-end arm and lug' if nm == '+Y' else ''}", pl, PAINT, "made", 13, "crosshead", G))
    out.append(weld("crosshead: dead-end arm to stub", sp.weld_bead((xa0, sw / 2 + 11, 185.0), (xa1, sw / 2 + 11, 185.0), 4.0, (0, 1, 0), (0, 0, 1)), "crosshead", G))
    out.append(mk("Crosshead sheave 150 mm (bought)", sp.sheave(so * 2, rp * 2, sw, sb, P["rope_d"], (0, 0, zs), (0, 1, 0)), ZINC, "bought", 25, "cross_sheave", G))
    cax, cclips = sp.pin_with_clips(sb - 0.2, (0, -sw / 2 - 11 - 15, zs), (0, sw / 2 + 11 + 15, zs), clip_axis=(1, 0, 0), inset=6.0)
    out.append(mk("Crosshead sheave axle 20 mm", cax, MILD, "made", 13, "cross_axle", G))
    out += fasteners([("Crosshead axle split pin -Y", cclips[0]), ("Crosshead axle split pin +Y", cclips[1])], "cross_axle", G)
    # ---------------------------------------------------------------- tie rods with closed eyes, and their pins (line 11)
    zh, xh = g["zh"], P["head_pin_x"]
    rb_w, rb_t = P["rod_bar"]
    for side, yo, nm in ((1, yA, "A"), (-1, yB, "B")):
        for sgn in (-1, 1):
            y0 = yo if sgn > 0 else -yo - rb_t
            a2, b2 = (side * sx, sz), (side * xh, zh)
            circ = lambda c, r: [(c[0] + r * math.cos(2 * math.pi * k / 32), c[1] + r * math.sin(2 * math.pi * k / 32)) for k in range(32)]  # noqa: E731
            rod = prism_xz(_hull(circ(a2, rb_w / 2) + circ(b2, rb_w / 2)), y0, y0 + rb_t)
            rod = break_edges(rod, 0.8) - ycyl(a2[0], a2[1], 10.25, y0 - 1, y0 + rb_t + 1) - ycyl(b2[0], b2[1], 12.75, y0 - 1, y0 + rb_t + 1)
            out.append(mk(f"Tie rod, shell {nm} {'+Y' if sgn > 0 else '-Y'}, 30 x 10 flat", rod, PAINT, "made", 11, "tie_rods", G))
            # 20 mm pin through the shell lug and the rod, split pins both sides
            yin = (yo - et) if sgn > 0 else (-yo - rb_t)
            yout = (yo + rb_t) if sgn > 0 else (-yo + et)
            ya, yb_ = (yin - 14.0, yout + 12.0) if sgn > 0 else (yin - 12.0, yout + 14.0)
            pn, pc = sp.pin_with_clips(20.0, (side * sx, ya, sz), (side * sx, yb_, sz), clip_axis=(0, 0, 1), inset=5.0)
            out.append(mk(f"Tie rod pin 20 mm, shell {nm} {'+Y' if sgn > 0 else '-Y'}", pn, MILD, "made", 11, "shell_pins", G))
            out += fasteners([(f"Tie rod pin split pin, shell {nm} {'+Y' if sgn > 0 else '-Y'} inner", pc[0]),
                              (f"Tie rod pin split pin, shell {nm} {'+Y' if sgn > 0 else '-Y'} outer", pc[1])], "shell_pins", G)
    # ---------------------------------------------------------------- head (line 10)
    hx, hy, z0, z1, zu = g["hx"], g["hy"], g["z0"], g["z1"], g["zu"]
    box = bx(-hx / 2, hx / 2, -hy / 2, hy / 2, z0, z1) - bx(-hx / 2 + 6, hx / 2 - 6, -hy / 2 + 6, hy / 2 - 6, z0 + 6, z1 - 6)
    box = break_edges(box, 1.0)
    for sgn in (-1, 1):
        box = box - ycyl(sgn * xh, zh, 12.7, -hy, hy)
    box = box - zcyl(-rp, 0, 15.2, z0 - 1, z1 + 1)
    out.append(mk("Grab head box 300 x 120 x 40, 6 mm plate", box, PAINT, "made", 10, "head", G))
    yp = 209.0
    for sgn in (-1, 1):
        hpn, hpc = sp.pin_with_clips(25.0, (sgn * xh, -yp, zh), (sgn * xh, yp, zh), clip_axis=(0, 0, 1), inset=6.0)
        out.append(mk(f"Grab head pin 25 mm at x {sgn * xh:+.0f}", hpn, MILD, "made", 10, "head", G))
        out += fasteners([(f"Head pin split pin {sgn * xh:+.0f} -Y", hpc[0]), (f"Head pin split pin {sgn * xh:+.0f} +Y", hpc[1])], "head", G)
        for yy in (-hy / 2, hy / 2):
            out.append(weld(f"grab head: pin {sgn * xh:+.0f} at y {yy:+.0f}", sp.ring_weld((sgn * xh, yy, zh), (0, 1 if yy > 0 else -1, 0), 12.5, 4.0), "head", G))
    gt = sp.tube_between((-rp, 0, z0 - 25), (-rp, 0, z1 + 20), 30.0, 8.0)
    out.append(mk("Grab head rope guide tube 30 x 8", gt, MILD, "made", 10, "head", G))
    out.append(weld("grab head: guide tube top", sp.ring_weld((-rp, 0, z1), (0, 0, 1), 15.0, 4.0), "head", G))
    out.append(weld("grab head: guide tube bottom", sp.ring_weld((-rp, 0, z0), (0, 0, -1), 15.0, 4.0), "head", G))
    xu0, xu1 = rp - sw / 2 - 1 - 6, rp + sw / 2 + 1
    circ = [(rp + 22 * math.cos(a), zu + 22 * math.sin(a)) for a in [2 * math.pi * k / 24 for k in range(24)]]
    for xc0 in (xu0, xu1):
        ch = prism_yz(_hull([(20.0, z0), (58.0, z0)] + circ), xc0, xc0 + 6)
        ch = break_edges(ch, 0.6) - xcyl(rp, zu, sb / 2 + 0.25, xc0 - 1, xc0 + 7)
        out.append(mk(f"Grab head sheave cheek at x {xc0 + 3:.0f}, 6 mm", ch, PAINT, "made", 10, "head", G))
        out.append(weld(f"grab head: cheek {xc0 + 3:.0f} to box", sp.weld_bead((xc0 + (6 if xc0 > rp else 0), 22.0, z0), (xc0 + (6 if xc0 > rp else 0), 56.0, z0), 4.0,
                                                                         (1 if xc0 > rp else -1, 0, 0), (0, 0, -1)), "head", G))
    eye = sp.plate(-30, 30, -6, 6, z1, z1 + 50, holes=[("y", 0.0, z1 + 28, 20.0)], edge=1.0)
    out.append(mk("Grab head recovery-line eye, 12 mm", eye, PAINT, "made", 10, "head", G))
    out.append(weld("grab head: eye to box", sp.weld_bead((-30, 6, z1), (30, 6, z1), 4.0, (0, 1, 0), (0, 0, 1)), "head", G))
    bpx, bpy, bpt = P["ballast_plate"]
    for sgn in (-1, 1):
        y0, y1 = (hy / 2, hy / 2 + bpt) if sgn > 0 else (-hy / 2 - bpt, -hy / 2)
        # bolts at x +/- 40, clear of the line rising from the guide tube at x -65 (D3 detail; were at +/- 75)
        bp = sp.plate(-bpx / 2, bpx / 2, y0, y1, z0, z0 + bpy, holes=[("y", -40.0, z0 + 75, 11.0), ("y", 40.0, z0 + 75, 11.0)], edge=1.5)
        out.append(mk(f"Grab ballast plate {'+Y' if sgn > 0 else '-Y'}, 16 mm", bp, PAINT, "made", 10, "ballast", G))
    for xx in (-40.0, 40.0):
        out.append(mk(f"Ballast spacer tube at x {xx:+.0f}", sp.tube_between((xx, -hy / 2, z0 + 75), (xx, hy / 2, z0 + 75), 16.0, 2.4), MILD, "made", 10, "ballast", G))
        out += fasteners(sp.bolt_set(10, 2 * bpt + hy, (xx, -hy / 2 - bpt, z0 + 75), axis=(0, -1, 0), label=f", ballast at x {xx:+.0f}"), "ballast", G)
    out.append(mk("Upper sheave 150 mm (bought)", sp.sheave(so * 2, rp * 2, sw, sb, P["rope_d"], (rp, rp, zu), (1, 0, 0)), ZINC, "bought", 25, "upper_sheave", G))
    uax, uclips = sp.pin_with_clips(sb - 0.2, (xu0 - 16, rp, zu), (xu1 + 6 + 16, rp, zu), clip_axis=(0, 0, 1), inset=6.0)
    out.append(mk("Upper sheave axle 20 mm", uax, MILD, "made", 10, "upper_axle", G))
    out += fasteners([("Upper axle split pin, inner", uclips[0]), ("Upper axle split pin, outer", uclips[1])], "upper_axle", G)
    # ---------------------------------------------------------------- dead-end load indicator (line 14)
    # Amish's decision O4 of 2026-10-25 (SKG-DEC-001): a peak-reading spring link replaces the shear link. Two 6 mm straps
    # hang on the 16 mm clevis pin through the dead-end lug, held off the lug by spacers; a housing plate is welded
    # across their tops. The line's pull lifts the fork, which draws the M8 rod up through the housing and squeezes a
    # stack of 14 disc springs between the rod's nut and the housing; an O-ring tell-tale on the rod above the housing
    # is pushed down the rod as the load comes off and stays at the peak travel, read against rings on the rod.
    xc = (xa0 + xa1) / 2
    zp = zl + 74.0
    for x0, nm in ((xc - 21.0, "-X"), (xc + 15.0, "+X")):
        st = sp.plate(x0, x0 + 6, yd_ - 15, yd_ + 15, zl - 12, zl + 48, holes=[("x", yd_, zl, 16.5)], edge=0.8)
        out.append(mk(f"Load indicator strap {nm}, 6 mm", st, RED, "made", 14, "load_link", G))
    hp = sp.plate(xc - 15, xc + 15, yd_ - 15, yd_ + 15, zl + 42, zl + 48, holes=[("z", xc, yd_, 8.5)], edge=0.8)
    out.append(mk("Load indicator housing plate, 6 mm", hp, RED, "made", 14, "load_link", G))
    for sg in (-1, 1):
        out.append(weld(f"load indicator: housing to strap {'+X' if sg > 0 else '-X'}",
                        sp.weld_bead((xc + sg * 15, yd_ - 13, zl + 42), (xc + sg * 15, yd_ + 13, zl + 42), 3.0, (-sg, 0, 0), (0, 0, -1)), "load_link", G))
    for x0, x1, nm in ((xc - 15, xa0, "-X"), (xa1, xc + 15, "+X")):
        out.append(mk(f"Load indicator spacer {nm}, 26 x 4.75 tube", sp.between(cp.round_tube(26.0, 4.75, x1 - x0 - 0.2), (x0 + 0.1, yd_, zl), (x1 - 0.1, yd_, zl)),
                      MILD, "made", 14, "load_link", G))
    for k in range(14):
        z0_ = zl + 22.1 + k * (19.9 / 14)
        out += fasteners([(f"Disc spring 18 x 9.2 x 1.0 (DIN EN 16983, series A), load indicator, {k + 1} of 14",
                           Pos(xc, yd_, z0_ + 19.9 / 28) * (Cylinder(9.0, 19.9 / 14) - Cylinder(4.6, 2.0)))], "load_link", G, bom=14, mat=MILD)
    rod = sp.bar_between((xc, yd_, zl + 14.0), (xc, yd_, zl + 54.0), 8.0, 0.5)
    out.append(mk("Load indicator rod M8, stainless, with scale rings", rod, "stainless", "made", 14, "load_link", G))
    out += fasteners([("M8 washer (ISO 7089), load indicator", Pos(xc, yd_, zl + 20.5) * sp.washer(8)),
                      ("M8 hex nut (ISO 4032), load indicator", Pos(xc, yd_, zl + 13.7) * sp.hex_nut(8))], "load_link", G, mat="stainless")
    from build123d import Torus
    out.append(mk("Load indicator tell-tale O-ring 8 x 2", Pos(xc, yd_, zl + 49.0) * Torus(5.0, 1.0), "epdm", "bought", 14, "load_link", G))
    fb = sp.plate(xc - 11.5, xc + 11.5, yd_ - 12, yd_ + 12, zl + 51, zl + 57, edge=0.8) - sp.zhole(xc, yd_, 6.8, zl + 50, zl + 58)
    out.append(mk("Load indicator fork base, 6 mm, tapped M8", fb, RED, "made", 14, "load_link", G))
    for x0, nm in ((xc - 9.5, "-X"), (xc + 4.5, "+X")):
        ch = sp.plate(x0, x0 + 5, yd_ - 10, yd_ + 10, zl + 57, zl + 85, holes=[("x", yd_, zp, 8.5)], edge=0.6)
        out.append(mk(f"Load indicator fork cheek {nm}, 5 mm", ch, RED, "made", 14, "load_link", G))
        out.append(weld(f"load indicator: cheek {nm} to fork base", sp.weld_bead((x0 + (0 if x0 < xc else 5), yd_ - 9, zl + 57), (x0 + (0 if x0 < xc else 5), yd_ + 9, zl + 57),
                                                                            3.0, (-1 if x0 < xc else 1, 0, 0), (0, 0, 1)), "load_link", G))
    sleeve = sp.between(cp.round_tube(16.0, 3.8, 8.6), (xc - 4.3, yd_, zp), (xc + 4.3, yd_, zp))
    out.append(mk("Thimble sleeve 16 mm on the fork pin", break_edges(sleeve, 0.4), MILD, "made", 14, "load_link", G))
    fpn, fcl = sp.pin_with_clips(8.0, (xc - 14.0, yd_, zp), (xc + 14.0, yd_, zp), clip_axis=(0, 0, 1), inset=2.6)
    out.append(mk("Load indicator fork pin 8 mm", fpn, MILD, "made", 14, "load_link", G))
    out += fasteners([("Fork pin split pin -X", fcl[0]), ("Fork pin split pin +X", fcl[1])], "load_link", G, bom=14)
    out += fasteners(_clevis(16.0, 42.0, (xc + 21.0, yd_, zl), (1, 0, 0), "load indicator"), "load_link", G, bom=14)
    thimble = Pos(xc, yd_, zp) * Rot(0, 90, 0) * (Torus(12.5, 4.0) - Cylinder(8.6, 20) - Pos(-17.5, 0, 0) * Box(6, 30, 30))
    out.append(mk("Rope thimble for 8 mm line (bought)", thimble, ZINC, "bought", 26, "rope", G))
    # ---------------------------------------------------------------- the line inside the grab (3:1 reeving)
    pts = [(-rp, 0, z1 + 20)]
    pts += [(-rp, 0, zs + 1)]
    pts += [(rp * math.cos(math.radians(a)), 0, zs + rp * math.sin(math.radians(a))) for a in range(180, 361, 15)]
    pts += [(rp, 0, zu)]
    pts += [(rp, rp + rp * math.cos(math.radians(a)), zu + rp * math.sin(math.radians(a))) for a in range(180, -1, -15)]
    pts += [(rp, 2 * rp, zp + 12.5 + 4.0 + 6.0)]
    out.append(mk("Closing line in the grab, 8 mm polyester (3:1 reeving)", cp.rope(pts, P["rope_d"]), "rope", "bought", 26, "rope", G))
    return out


# ================================================================================================ scraper (local frame)
def scraper(P=None):
    M = _M()
    P = P or M.PARAMS
    D = M.derived(P)
    bx, xcyl, ycyl, zcyl, prism_xz, fuse, _hull = M.bx, M.xcyl, M.ycyl, M.zcyl, M.prism_xz, M.fuse, M._hull
    po, pt = P["pole"]
    px, pz = P["pivot"]
    hub_d, hub_h = P["hub"]
    aw, at = P["arm_bar"]
    z_top = P["head_len"]
    z_bot = D["sleeve_z"][0] - 120.0
    G = "scraper"
    out = []
    SC = lambda n, sh, mat=PAINT: out.append(mk(f"Scraper head: {n}", sh, mat, "made", 15, "scraper_pole", G))  # noqa: E731
    pole = sp.tube_between((0, 0, z_bot + 50), (0, 0, z_top), po, pt)
    pole = pole - ycyl(0, D["cross_pin_z"], P["cross_pin"][0] / 2 + 0.25, -po, po) - xcyl(0, z_top - 75.0, 6.5, -po, po)
    SC("bottom pole 42.4 x 2.6", pole)
    spike = zcyl(0, 0, po / 2, z_bot + 12, z_bot + 50) + _cone_at((0, 0, z_bot), 4.0, po / 2, 12.0) + zcyl(0, 0, po / 2 - pt - 0.1, z_bot + 50, z_bot + 90)
    SC("spike, 50 mm bar turned", break_edges(spike, 0.5), MILD)
    out.append(weld("scraper head: spike to pole", sp.ring_weld((0, 0, z_bot + 50), (0, 0, 1), po / 2, 3.0), "scraper_pole", G))
    hub = sp.tube_between((0, 0, pz - hub_h / 2), (0, 0, pz + hub_h / 2), hub_d, (hub_d - po - 0.4) / 2)
    SC("arm hub 70 mm", break_edges(hub, 0.8))
    for zz, ax in ((pz - hub_h / 2, -1), (pz + hub_h / 2, 1)):
        out.append(weld(f"scraper head: hub {'bottom' if ax < 0 else 'top'} to pole", sp.ring_weld((0, 0, zz), (0, 0, ax), po / 2, 4.0), "scraper_pole", G))
    hubc = zcyl(0, 0, hub_d / 2, pz - hub_h, pz + hub_h)
    for s_ in (-1, 1):
        x0, x1 = (hub_d / 2 - 4, px + 18) if s_ > 0 else (-(px + 18), -(hub_d / 2 - 4))
        for y0 in (-at / 2 - 8, at / 2):
            lug = sp.plate(x0, x1, y0, y0 + 8, pz - 22, pz + 22, edge=1.0) - hubc - ycyl(s_ * px, pz, 8.25, y0 - 1, y0 + 9)
            SC(f"arm lug {'+X' if s_ > 0 else '-X'} {'+Y' if y0 > 0 else '-Y'}", lug)
    cz = P["cent_z"]
    SC("centralizer collar", sp.tube_between((0, 0, cz - 30), (0, 0, cz + 30), 64.0, (64.0 - po - 0.4) / 2))
    sk_w, sk_h, sk_t = P["skid"]
    r_end = P["cent_r"] - sk_t
    colc = zcyl(0, 0, 32.0, cz - 40, cz + 40)
    for k in range(3):
        a = 90 + 120 * k
        arm = bx(30, r_end, -4, 4, cz - 20, cz + 20)
        arm = break_edges(arm, 0.8) - colc
        for rr in (275.0, 305.0, 375.0, 405.0):
            arm = arm - ycyl(rr, cz, 5.5, -10, 10)
        SC(f"centralizer arm {k + 1}, 40 x 8", Rot(0, 0, a) * arm)
        out.append(weld(f"scraper head: centralizer arm {k + 1}", Rot(0, 0, a) * sp.weld_bead((32.0, 4.0, cz + 20), (32.0, 4.0, cz - 20), 3.0, (0, 1, 0), (1, 0, 0)), "scraper_pole", G))
        brk = sp.plate(355.0, r_end, 4.0, 12.0, cz - 20, cz + 20, holes=[("y", 375.0, cz, 11.0), ("y", 405.0, cz, 11.0)], edge=0.8)
        SC(f"skid bracket {k + 1}, 8 mm", Rot(0, 0, a) * brk)
        skid = sp.plate(r_end, P["cent_r"], -sk_w / 2, sk_w / 2 + 12.0, cz - sk_h / 2, cz + sk_h / 2, edge=2.0)
        SC(f"skid {k + 1}, 10 mm", Rot(0, 0, a) * skid)
        out.append(weld(f"scraper head: skid {k + 1} to bracket", Rot(0, 0, a) * sp.weld_bead((r_end, 12.0, cz - 20), (r_end, 12.0, cz + 20), 4.0, (-1, 0, 0), (0, 1, 0)), "scraper_pole", G))
        for rr in (375.0, 405.0):
            out += fasteners([(n, Rot(0, 0, a) * sh) for n, sh in sp.bolt_set(10, 16.0, (rr, 12.0, cz), axis=(0, 1, 0), label=f", skid {k + 1}")], "scraper_pole", G, bom=15)
    for zz, ax in ((cz - 30, -1), (cz + 30, 1)):
        out.append(weld(f"scraper head: collar {'bottom' if ax < 0 else 'top'}", sp.ring_weld((0, 0, zz), (0, 0, ax), po / 2, 3.0), "scraper_pole", G))
    # ---------------------------------------------------------------- arms with toes and blades (line 15)
    ex, ez = D["arm_end"]
    tw, th, tt = P["toe"]
    stx, stz = D["strut_top"]
    for s_ in (-1, 1):
        def c(cx, cz_, r, n=24):
            return [(cx + r * math.cos(2 * math.pi * k / n), cz_ + r * math.sin(2 * math.pi * k / n)) for k in range(n)]
        ux, uz = ex - px, ez - pz
        L = math.hypot(ux, uz)
        ux, uz = ux / L, uz / L
        nx, nz = -uz, ux
        far = [(ex + aw / 2 * nx, ez + aw / 2 * nz), (ex - aw / 2 * nx, ez - aw / 2 * nz)]
        prof = _hull(c(px, pz, 18.0) + far)
        if s_ < 0:
            prof = [(-x, z) for x, z in prof]
        arm = prism_xz(prof, -at / 2, at / 2)
        arm = break_edges(arm, 0.8) - ycyl(s_ * px, pz, 8.25, -at, at) - ycyl(s_ * stx, stz, 6.25, -at, at)
        arm = arm - (bx(ex, ex + 200, -60, 60, ez - 200, ez + 200) if s_ > 0 else bx(-ex - 200, -ex, -60, 60, ez - 200, ez + 200))
        out.append(mk(f"Scraper arm {'+X' if s_ > 0 else '-X'}, 50 x 10 flat on edge", arm, PAINT, "made", 15, "arms", G))
        xa0_, xa1_ = (ex, ex + tt) if s_ > 0 else (-(ex + tt), -ex)
        toe = sp.plate(xa0_, xa1_, -tw / 2, tw / 2, ez - th + 15, ez + 15, edge=1.0)
        out.append(mk(f"Scraper toe plate {'+X' if s_ > 0 else '-X'}, 10 mm wear-resistant", toe, "mild_steel", "made", 15, "arms", G))
        xb0, xb1 = (ex + tt, ex + tt + P["toe_ext"]) if s_ > 0 else (-(ex + tt + P["toe_ext"]), -(ex + tt))
        blade = sp.plate(xb0, xb1, -tw / 2, tw / 2, ez - 10.0, ez, edge=0.8)
        out.append(mk(f"Scraper toe blade {'+X' if s_ > 0 else '-X'}, 10 mm wear-resistant", blade, "mild_steel", "made", 15, "arms", G))
        xe = ex + tt if s_ > 0 else -(ex + tt)
        out.append(weld(f"scraper arm {'+X' if s_ > 0 else '-X'}: blade to toe", sp.weld_bead((xe, -tw / 2, ez), (xe, tw / 2, ez), 4.0, (s_, 0, 0), (0, 0, 1)), "arms", G))
        out.append(weld(f"scraper arm {'+X' if s_ > 0 else '-X'}: toe to arm", sp.weld_bead((s_ * ex, at / 2, ez + 15), (s_ * ex, at / 2, ez - 20), 5.0, (0, 1, 0), (-s_, 0, 0)), "arms", G))
        pn, pc = sp.pin_with_clips(16.0, (s_ * px, -at / 2 - 8 - 12, pz), (s_ * px, at / 2 + 8 + 12, pz), clip_axis=(0, 0, 1), inset=5.0)
        out.append(mk(f"Arm pivot pin 16 mm {'+X' if s_ > 0 else '-X'}", pn, MILD, "made", 15, "arm_pins", G))
        out += fasteners([(f"Arm pivot split pin {'+X' if s_ > 0 else '-X'} -Y", pc[0]), (f"Arm pivot split pin {'+X' if s_ > 0 else '-X'} +Y", pc[1])], "arm_pins", G, bom=15)
        pn, pc = sp.pin_with_clips(12.0, (s_ * stx, -at / 2 - 6 - 10, stz), (s_ * stx, at / 2 + 6 + 10, stz), clip_axis=(0, 0, 1), inset=4.5)
        out.append(mk(f"Strut pin 12 mm at the arm {'+X' if s_ > 0 else '-X'}", pn, MILD, "made", 15, "arm_pins", G))
        out += fasteners([(f"Strut pin split pin, arm {'+X' if s_ > 0 else '-X'} -Y", pc[0]), (f"Strut pin split pin, arm {'+X' if s_ > 0 else '-X'} +Y", pc[1])], "arm_pins", G, bom=15)
    # ---------------------------------------------------------------- slotted sleeve, foot, lugs, struts, pins (line 15)
    s0, s1 = D["sleeve_z"]
    s2 = D["sleeve_top"]
    sbx, sbz = D["strut_bot"]
    sl = sp.tube_between((0, 0, s0), (0, 0, s2), P["sleeve"][0], (P["sleeve"][0] - po - 1.0) / 2)
    swd = P["slot"][0]
    z_s0, z_s1 = D["slot_z"]
    slot = bx(-swd / 2, swd / 2, -P["sleeve"][0], P["sleeve"][0], z_s0, z_s1 - swd / 2) + ycyl(0, z_s1 - swd / 2, swd / 2, -P["sleeve"][0], P["sleeve"][0])
    out.append(mk("Sliding sleeve 54 x 340 with two 13 x 312 slots", sl - slot, PAINT, "made", 15, "sleeve", G))
    foot = zcyl(0, 0, P["foot_d"] / 2, s0 - 10, s0)
    foot = break_edges(foot, 1.5) - zcyl(0, 0, po / 2 + 0.5, s0 - 11, s0 + 1)
    out.append(mk("Sleeve foot plate 250 mm, 10 mm", foot, PAINT, "made", 15, "sleeve", G))
    out.append(weld("scraper sleeve: foot to sleeve", sp.ring_weld((0, 0, s0), (0, 0, 1), P["sleeve"][0] / 2, 5.0), "sleeve", G))
    slc = zcyl(0, 0, P["sleeve"][0] / 2, s0, s2)
    for s_ in (-1, 1):
        x0, x1 = (P["sleeve"][0] / 2 - 3, sbx + 14) if s_ > 0 else (-(sbx + 14), -(P["sleeve"][0] / 2 - 3))
        lug = sp.plate(x0, x1, -at / 2, at / 2, sbz - 16, sbz + 16, edge=1.0) - slc - ycyl(s_ * sbx, sbz, 6.25, -at, at)
        out.append(mk(f"Sleeve strut lug {'+X' if s_ > 0 else '-X'}, 10 mm", lug, PAINT, "made", 15, "sleeve", G))
        for y0 in (-at / 2 - 6, at / 2):
            def c(cx, cz_, r, n=24):
                return [(cx + r * math.cos(2 * math.pi * k / n), cz_ + r * math.sin(2 * math.pi * k / n)) for k in range(n)]
            st = prism_xz(_hull(c(s_ * sbx, sbz, 15.0) + c(s_ * stx, stz, 15.0)), y0, y0 + 6)
            st = break_edges(st, 0.6) - ycyl(s_ * sbx, sbz, 6.25, y0 - 1, y0 + 7) - ycyl(s_ * stx, stz, 6.25, y0 - 1, y0 + 7)
            out.append(mk(f"Strut {'+X' if s_ > 0 else '-X'} {'+Y' if y0 > 0 else '-Y'}, 30 x 6 flat", st, PAINT, "made", 15, "struts", G))
        pn, pc = sp.pin_with_clips(12.0, (s_ * sbx, -at / 2 - 6 - 10, sbz), (s_ * sbx, at / 2 + 6 + 10, sbz), clip_axis=(0, 0, 1), inset=4.5)
        out.append(mk(f"Strut pin 12 mm at the sleeve {'+X' if s_ > 0 else '-X'}", pn, MILD, "made", 15, "sleeve_pins", G))
        out += fasteners([(f"Strut pin split pin, sleeve {'+X' if s_ > 0 else '-X'} -Y", pc[0]), (f"Strut pin split pin, sleeve {'+X' if s_ > 0 else '-X'} +Y", pc[1])], "sleeve_pins", G, bom=15)
    cpd, cpl = P["cross_pin"]
    pn, pc = sp.pin_with_clips(cpd, (0, -38.0, D["cross_pin_z"]), (0, 38.0, D["cross_pin_z"]), clip_axis=(1, 0, 0), inset=4.5)
    out.append(mk("Sleeve cross pin 12 mm", pn, MILD, "made", 15, "cross_pin", G))
    out += fasteners([("Cross pin R-clip", pc[1]), ("Cross pin keeper split pin", pc[0])], "cross_pin", G, bom=15)
    # ---------------------------------------------------------------- one 2 m pole section (line 16), joint bolt
    Ls = P["pole_sec"]
    sec = sp.tube_between((0, 0, z_top), (0, 0, z_top + Ls), po, pt)
    sec = sec - xcyl(0, z_top + 75.0, 6.5, -po, po) - xcyl(0, z_top + Ls - 75.0, 6.5, -po, po)
    out.append(mk("Pole section 2 m, 42.4 x 2.6", sec, PAINT, "made", 16, "pole_section", G))
    spg = sp.bar_between((0, 0, z_top - P["spigot"][1]), (0, 0, z_top + 100), P["spigot"][0], 1.0)
    spg = spg - xcyl(0, z_top - 75.0, 6.5, -po, po) - xcyl(0, z_top + 75.0, 6.5, -po, po)
    out.append(mk("Pole section spigot 36 mm bar, 250 long", spg, MILD, "made", 16, "pole_section", G))
    for zz in (z_top - 75.0, z_top + 75.0):
        out += fasteners(sp.bolt_set(12, po, (po / 2, 0, zz), axis=(1, 0, 0), label=f", pole joint at {zz:.0f}"), "pole_section", G, bom=16)
    # ---------------------------------------------------------------- T-bar (line 17)
    zt = z_top + Ls
    so_d, so_l = P["socket"]
    TB = lambda n, sh, mat=PAINT: out.append(mk(f"T-bar: {n}", sh, mat, "made", 17, "tbar", G))  # noqa: E731
    sock = sp.tube_between((0, 0, zt - 20), (0, 0, zt + so_l - 20), so_d, 2.7)
    hz = zt + so_l - 60
    TB("socket 48.3 x 2.7", sock - xcyl(0, hz, P["tbar"][0] / 2 + 0.2, -so_d, so_d))
    TB("cap plate 6 mm", break_edges(zcyl(0, 0, so_d / 2, zt + so_l - 20, zt + so_l - 14), 1.0))
    tsp = sp.bar_between((0, 0, zt - 100), (0, 0, zt + 120), P["spigot"][0], 1.0)
    TB("spigot 36 mm bar", tsp - xcyl(0, zt - 75, 6.5, -so_d, so_d), MILD)
    out += fasteners(sp.bolt_set(12, po, (po / 2, 0, zt - 75), axis=(1, 0, 0), label=", T-bar joint"), "tbar", G, bom=17)
    hd_ = sp.tube_between((-P["tbar"][1] / 2, 0, hz), (P["tbar"][1] / 2, 0, hz), P["tbar"][0], 3.2)
    TB("handle 33.7 x 3.2, 1.4 m", hd_)
    for sx_ in (-1, 1):
        out.append(weld(f"T-bar: handle to socket {'+X' if sx_ > 0 else '-X'}", sp.ring_weld((sx_ * so_d / 2, 0, hz), (sx_, 0, 0), P["tbar"][0] / 2, 3.0), "tbar", G))
    eye = sp.plate(-6, 6, -25, 25, zt + so_l - 14, zt + so_l + 40, holes=[("x", 0.0, zt + so_l + 18, 18.0)], edge=1.0)
    TB("eye plate 12 mm", eye)
    return out


# ================================================================================================ well-head frame and doors
def wellhead(P=None):
    M = _M()
    P = P or M.PARAMS
    bx, xcyl, zcyl = M.bx, M.xcyl, M.zcyl
    a_in, a_leg, a_t = P["wh_frame"]
    zc = P["collar_h"]
    h = a_in / 2
    G = "wellhead"
    out = []
    WH = lambda n, sh: out.append(mk(f"Well-head frame: {n}", sh, GALV, "made", 18, "wh_frame", G))  # noqa: E731
    ang = lambda L: cp.angle(a_leg, a_leg, a_t, L)  # noqa: E731
    # +Y and -Y angles run the full width; +X and -X angles fit between them. Leg 1 horizontal outward, leg 2 up.
    WH("angle +Y, 50 x 50 x 5", sp.between(ang(a_in + 2 * a_leg), (h + a_leg, h, zc), (-h - a_leg, h, zc), up=(0, 1, 0)))
    WH("angle -Y, 50 x 50 x 5", sp.between(ang(a_in + 2 * a_leg), (-h - a_leg, -h, zc), (h + a_leg, -h, zc), up=(0, -1, 0)))
    WH("angle +X, 50 x 50 x 5", sp.between(ang(a_in), (h, -h, zc), (h, h, zc), up=(1, 0, 0)))
    WH("angle -X, 50 x 50 x 5", sp.between(ang(a_in), (-h, h, zc), (-h, -h, zc), up=(-1, 0, 0)))
    # welded corners (+X,+Y) and (-X,-Y); bolted corners (+X,-Y) and (-X,+Y) with a cleat and two M12 bolts
    for sx_, sy_ in ((1, 1), (-1, -1)):
        out.append(weld(f"well-head frame: corner {sx_:+d}{sy_:+d}", sp.weld_bead((sx_ * h, sy_ * h, zc + a_t), (sx_ * h, sy_ * h, zc + a_leg), 4.0, (-sx_, 0, 0), (0, -sy_, 0)), "wh_frame", G))
    for sx_, sy_ in ((1, -1), (-1, 1)):
        cl = cp.angle(50.0, 50.0, 5.0, 40.0)
        cl = Pos(sx_ * h, sy_ * h, zc + a_t + 2.0) * Rot(0, 0, 0 if (sx_, sy_) == (-1, -1) else (90 if (sx_, sy_) == (1, -1) else -90)) * cl
        cl = break_edges(cl, 0.8)
        hs = [sp.xhole(sy_ * (h - 25.0), zc + a_t + 22.0, 13.0, sx_ * h - 10, sx_ * h + 10), sp.yhole(sx_ * (h - 25.0), zc + a_t + 22.0, 13.0, sy_ * h - 10, sy_ * h + 10)]
        for hh in hs:
            cl = cl - hh
        WH(f"corner cleat {sx_:+d}{sy_:+d}, 50 x 50 x 5", cl)
        out += fasteners(sp.bolt_set(12, 10.0, (sx_ * (h - 5.0), sy_ * (h - 25.0), zc + a_t + 22.0), axis=(-sx_, 0, 0), label=f", corner {sx_:+d}{sy_:+d} x"), "wh_frame", G, bom=18)
        out += fasteners(sp.bolt_set(12, 10.0, (sx_ * (h - 25.0), sy_ * (h - 5.0), zc + a_t + 22.0), axis=(0, -sy_, 0), label=f", corner {sx_:+d}{sy_:+d} y"), "wh_frame", G, bom=18)
    rd = P["ring"][0] / 2 + P["ring"][1] / 2
    for k in range(4):
        a = 90.0 * k
        br = sp.plate(rd - 25, h + 1.0, -25, 25, zc + a_t, zc + a_t + 6, holes=[("z", rd, 0.0, 10.0)], edge=1.0)
        br = br - bx(h - 0.01, h + 2, -26, 26, zc, zc + 20)
        WH(f"datum bracket {k + 1}, 6 mm", Rot(0, 0, a) * br)
    for s_ in (-1, 1):
        for xk in (-500.0, 500.0):
            kn = sp.between(cp.round_tube(24.0, 3.5, 80.0), (xk - 40, s_ * (h + 15), zc + a_leg + 12), (xk + 40, s_ * (h + 15), zc + a_leg + 12))
            WH(f"hinge knuckle {'+Y' if s_ > 0 else '-Y'} x {xk:+.0f}", kn)
            sup = sp.plate(xk - 40, xk + 40, s_ * (h + a_t) if s_ > 0 else -h - 15, s_ * (h + 15) if s_ > 0 else -h - a_t, zc + a_leg - 5, zc + a_leg, edge=0.8)
            WH(f"knuckle support {'+Y' if s_ > 0 else '-Y'} x {xk:+.0f}", sup)
    # doors (line 19): 40 x 40 x 4 angle frame, perforated 3 mm mesh sheet, pole notch and doubler, hinge pins on tabs
    da, dt = P["door_angle"]
    zd = zc + a_leg
    for s_ in (-1, 1):
        nm = "+Y" if s_ > 0 else "-Y"
        DO = lambda n, sh, mat=GALV: out.append(mk(f"Door {nm}: {n}", sh, mat, "made", 19, "doors", G))  # noqa: E731
        y_in, y_out = s_ * 4.0, s_ * (h + 2.0)
        x0, x1 = -h - 2.0, h + 2.0
        dang = lambda L: cp.angle(da, da, dt, L)  # noqa: E731
        notch = zcyl(0, 0, P["pole_hole"], zd - 1, zd + da + 1)
        if s_ > 0:
            me = sp.between(dang(x1 - x0), (x0, y_in, zd), (x1, y_in, zd), up=(0, 1, 0))
            oe = sp.between(dang(x1 - x0), (x1, y_out, zd), (x0, y_out, zd), up=(0, -1, 0))
            se0 = sp.between(dang(abs(y_out - y_in) - 2 * da), (x0, y_out - da, zd), (x0, y_in + da, zd), up=(1, 0, 0))
            se1 = sp.between(dang(abs(y_out - y_in) - 2 * da), (x1, y_in + da, zd), (x1, y_out - da, zd), up=(-1, 0, 0))
        else:
            me = sp.between(dang(x1 - x0), (x1, y_in, zd), (x0, y_in, zd), up=(0, -1, 0))
            oe = sp.between(dang(x1 - x0), (x0, y_out, zd), (x1, y_out, zd), up=(0, 1, 0))
            se0 = sp.between(dang(abs(y_out - y_in) - 2 * da), (x0, y_in - da, zd), (x0, y_out + da, zd), up=(1, 0, 0))
            se1 = sp.between(dang(abs(y_out - y_in) - 2 * da), (x1, y_out + da, zd), (x1, y_in - da, zd), up=(-1, 0, 0))
        DO("meeting-edge angle 40 x 40 x 4 with the pole notch", me - notch)
        DO("outer angle 40 x 40 x 4", oe)
        DO("side angle -X, 40 x 40 x 4", se0)
        DO("side angle +X, 40 x 40 x 4", se1)
        ym0, ym1 = sorted((y_in + s_ * dt, y_out - s_ * dt))
        mesh = bx(x0 + dt, x1 - dt, ym0, ym1, zd + dt, zd + dt + P["mesh_t"])
        holes = []
        pitch, op = 60.0, 50.0                         # 3 mm sheet, 69 % open: about 7 kg/m2, the BOM's expanded mesh
        nx_ = int((x1 - x0 - 2 * da) // pitch)
        ny_ = int((ym1 - ym0 - 2 * da) // pitch)
        for i in range(nx_):
            for j in range(ny_):
                cx = x0 + da + pitch / 2 + i * pitch + ((x1 - x0 - 2 * da) - nx_ * pitch) / 2
                cy = ym0 + da + pitch / 2 + j * pitch - (da - dt) + ((ym1 - ym0 - 2 * da) - ny_ * pitch) / 2
                if abs(cx) < 75 and abs(cy) < 80:
                    continue
                holes.append(Pos(cx, cy, zd + dt + P["mesh_t"] / 2) * Box(op, op, P["mesh_t"] + 2))
        mesh = mesh - Compound(holes) - zcyl(0, 0, P["pole_hole"] + 31, zd, zd + 20)
        DO("perforated mesh sheet 3 mm", mesh)
        dbl = (zcyl(0, 0, P["pole_hole"] + 30, zd + dt, zd + dt + 6) - zcyl(0, 0, P["pole_hole"], zd, zd + 20)) & bx(-80, 80, min(y_in, s_ * 80), max(y_in, s_ * 80), zd, zd + 20)
        dbl = dbl - bx(-80, 80, min(y_in, y_in + s_ * da), max(y_in, y_in + s_ * da), zd, zd + da + 1) if False else dbl
        DO("doubler round the notch, 6 mm", dbl)
        for xk in (-500.0, 500.0):
            pin = sp.bar_between((xk - 60, s_ * (h + 15), zc + a_leg + 12), (xk + 60, s_ * (h + 15), zc + a_leg + 12), 16.0, 0.8)
            DO(f"hinge pin x {xk:+.0f}, 16 mm", pin, MILD)
            for xt in (xk - 55, xk + 41):
                tab = sp.plate(xt, xt + 14, min(s_ * (h + 2), s_ * (h + 25)), max(s_ * (h + 2), s_ * (h + 25)), zd, zd + 22, holes=[("x", s_ * (h + 15), zc + a_leg + 12, 16.0)], edge=0.8)
                DO(f"hinge tab x {xt + 7:+.0f}, 14 mm", tab)
    return out


# ================================================================================================ ballast saddle (local frame)
def saddle(P=None):
    M = _M()
    P = P or M.PARAMS
    w, ti, hi, to, ho, tb, slot = P["saddle"]
    xi, xo = -slot / 2, slot / 2
    G = "saddle"
    out = []
    SD_ = lambda n, sh: out.append(mk(f"Ballast saddle: {n}", sh, PAINT, "made", 20, "saddles", G))  # noqa: E731
    SD_("inner leg 25 mm", sp.plate(xi - ti, xi, -w / 2, w / 2, -hi + tb, 0.0, edge=2.0))
    SD_("outer leg 20 mm", sp.plate(xo, xo + to, -w / 2, w / 2, -ho + tb, 0.0, edge=2.0))
    SD_("bridge 25 mm", sp.plate(xi - ti, xo + to, -w / 2, w / 2, 0.0, tb, edge=2.0))
    SD_("lifting eye 16 mm", sp.plate(-30, 30, -8, 8, tb, tb + 50, holes=[("y", 0.0, tb + 28, 20.0)], edge=1.0))
    for xx, sg in ((xi, 1), (xo, -1)):
        out.append(weld(f"ballast saddle: leg at x {xx:+.0f}", sp.weld_bead((xx, -w / 2 + 5, 0.0), (xx, w / 2 - 5, 0.0), 5.0, (sg, 0, 0), (0, 0, -1)), "saddles", G))
    out.append(weld("ballast saddle: eye", sp.weld_bead((-30, 8, tb), (30, 8, tb), 4.0, (0, 1, 0), (0, 0, 1)), "saddles", G))
    return out


ALLOWED += [
    ("Weld, grab shell A", "Grab shell A"), ("Weld, grab shell B", "Grab shell B"), ("Weld, crosshead", "Crosshead plate"),
    ("Weld, grab head", "Grab head"), ("Weld, grab head", "head pin"), ("Closing line", "sheave"), ("Closing line", "thimble"),
    ("Closing line", "guide tube"), ("thimble", "Thimble sleeve"), ("Weld, scraper head", "Scraper head"), ("Weld, scraper arm", "Scraper"),
    ("Weld, scraper sleeve", "Sleeve foot"), ("Weld, scraper sleeve", "Sliding sleeve"), ("Weld, T-bar", "T-bar"),
    ("Weld, well-head frame", "Well-head frame"), ("Weld, ballast saddle", "Ballast saddle"), ("Load indicator", "Load indicator"), ("Disc spring", "Load indicator"), ("Disc spring", "Disc spring"), ("Clutch", "Clutch"), ("Clutch", "Disc spring"), ("Clutch", "Parallel key"), ("Tab washer", "Crank shaft"), ("Parallel key", "Crank shaft"), ("Locknut KM5", "Crank shaft"), ("Clutch driven disc", "Driven sleeve"), ("Weld, crank: driven disc", "Clutch driven disc"), ("Weld, crank: driven disc", "Driven sleeve"), ("Weld, crank: clutch", "Clutch inner flange"), ("Weld, crank: clutch", "Crank shaft"), ("Weld, load indicator", "Load indicator"), ("Thimble sleeve", "Load indicator fork pin"),
    ("Door +Y", "Door +Y"), ("Door -Y", "Door -Y"), ("split pin", "R-clip"),
]
