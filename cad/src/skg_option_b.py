"""SinkGrab option B at detail level D3: a dart-valve bailer spudded on a jerk line (SKG-OPT-001).

Working principle: a heavy steel tube with a cutting shoe and a dart (flap) valve is lowered into the flooded
rings on the same capstan line. The crew spuds it: with the drum on the pawl, two people pull a jerk bar that
hooks the vertical line above the closed doors sideways, lifting the bailer about 0.24 m, and let go so it drops
back. Each drop drives the shoe into the loose sand, which pushes the dart up and enters the tube; on the lift
the dart closes and holds it. When full the bailer is hoisted like the grab and set down in the spoil tub,
where the dart stem touching the tub floor opens the valve. There is no under-curb scraper: the rings sink as
loose sand from under the cutting edge runs into the crater the bailer leaves, so the option suits sand and
gravel only. The capstan, foot cradle, drawbar, well-head frame and saddles are option A's.

Bailer frame for bailer(): axis Z, the shoe's cutting edge at z = 0. Everything else is in the site frame.
CONCEPT, NOT FOR FABRICATION.
"""
from __future__ import annotations

import math

from build123d import Box, Cylinder, Pos, Rot, Compound, Torus

import cad_parts as cp
from cad_parts import break_edges
import skg_parts as sp
from skg_detail import mk, fasteners, weld, _M, _clevis, PAINT, MILD, ZINC, GALV

B = dict(
    barrel=(219.1, 4.5, 1000.0),   # OD, wall, length; 1.0 m keeps the full bailer under the shear link (SKG-OPT-001)
    shoe=(232.0, 16.5, 100.0),     # OD, wall, height; 6.5 mm proud of the barrel so it cuts clearance
    seat=(10.0, 120.0, 55.0),      # thickness, bore, top height above the cutting edge
    dart=(140.0, 12.0, 25.0, 460.0, 40.0),   # disc OD, disc t, stem d, stem length, stem below the edge
    spider=(8.0, 60.0, 360.0),     # plate t, height, centre height
    bail=(50.0, 12.0, 420.0, 300.0),          # flat w, t, width between legs (outside), height above the barrel top
    jerk=(42.4, 3.2, 1500.0),      # jerk bar tube and length
    roller=(60.0, 40.0, 16.0),     # jerk roller OD, width, axle
    fill=0.50,                     # assumed fill of the bailer volume with sand per run (range 0.3 to 0.7)
    spud_lift=500.0,               # line pulled sideways at mid height above the doors, mm
    spud_span=2000.0,              # head sheave to the fairlead on the doors, mm
)


def geometry(P=None):
    """First-order numbers for option B from its geometry (used by docs/04-calcs/stem_check.py)."""
    M = _M()
    P = P or M.PARAMS
    od, t, L = B["barrel"]
    ri = od / 2 - t
    zs = B["seat"][2]
    top = B["shoe"][2] + L
    vol = math.pi * ri ** 2 * (top - zs) * 1e-6          # litres above the seat
    half = B["spud_span"] / 2
    d = B["spud_lift"]
    stroke = 2 * (math.hypot(half, d) - half)
    sin_t = d / math.hypot(half, d)
    return dict(volume_L=vol, stroke=stroke, pull_factor=2 * sin_t, top=top)


def bailer(P=None):
    M = _M()
    P = P or M.PARAMS
    from build123d import Solid, Plane
    out = []
    G = "bailer"
    od, t, L = B["barrel"]
    sod, st, sh = B["shoe"]
    BL = lambda n, s, mat=PAINT, kind="made": out.append(mk(f"Bailer: {n}", s, mat, kind, None, "bailer", G))  # noqa: E731
    top = sh + L
    BL("barrel 219.1 x 4.5 pipe, 1.0 m", sp.tube_between((0, 0, sh), (0, 0, top), od, t))
    shoe = sp.tube_between((0, 0, 0), (0, 0, sh), sod, st)
    keep = Solid.make_cone(sod / 2 - st + 0.5, sod / 2 + 2.0, 30.0, Plane(origin=(0, 0, 0))) + Pos(0, 0, 65) * Cylinder(sod / 2 + 5, 70)
    BL("cutting shoe 232 x 16.5, bevelled, wear-resistant", break_edges(shoe & keep, 0.5), MILD)
    out.append(weld("bailer: shoe to barrel", sp.ring_weld((0, 0, sh), (0, 0, 1), od / 2, 5.0), "bailer", G))
    stt, sbore, stop = B["seat"]
    BL("valve seat ring 10 mm", break_edges(sp.tube_between((0, 0, stop - stt), (0, 0, stop), sod - 2 * st, (sod - 2 * st - sbore) / 2), 0.8))
    dd, dt_, ds, dl, dbelow = B["dart"]
    BL("dart disc 140 x 12", break_edges(Pos(0, 0, stop + dt_ / 2) * Cylinder(dd / 2, dt_), 1.0) - Pos(0, 0, stop + dt_ / 2) * Cylinder(ds / 2, dt_ + 2), MILD)
    BL("dart stem 25 mm", sp.bar_between((0, 0, -dbelow), (0, 0, -dbelow + dl), ds, 1.5), MILD)
    out.append(weld("bailer: dart disc to stem", sp.ring_weld((0, 0, stop + dt_), (0, 0, 1), ds / 2, 4.0), "bailer", G))
    spt, sph, spz = B["spider"]
    ri = od / 2 - t
    guide_d = ds + 2.0
    p1 = sp.plate(-ri + 0.5, ri - 0.5, -spt / 2, spt / 2, spz - sph / 2, spz + sph / 2, edge=0.8) - Pos(0, 0, spz) * Cylinder(guide_d / 2, sph + 2)
    BL("dart guide spider plate 1, 8 mm", p1)
    p2 = sp.plate(-spt / 2, spt / 2, -ri + 0.5, ri - 0.5, spz - sph / 2, spz + sph / 2, edge=0.8) - Pos(0, 0, spz) * Cylinder(guide_d / 2, sph + 2)
    p2 = p2 - Pos(0, 0, spz) * Box(spt + 0.4, 2 * spt + guide_d, sph + 2)
    BL("dart guide spider plate 2 (two halves), 8 mm", p2)
    for sx_ in (-1, 1):
        out.append(weld(f"bailer: spider to barrel {'+X' if sx_ > 0 else '-X'}", sp.weld_bead((sx_ * (ri - 0.5), spt / 2, spz - sph / 2), (sx_ * (ri - 0.5), spt / 2, spz + sph / 2), 3.0, (0, 1, 0), (-sx_, 0, 0)), "bailer", G))
    bw, btk, bwid, bh = B["bail"]
    for sx_ in (-1, 1):
        x0 = od / 2 if sx_ > 0 else -od / 2 - 12
        BL(f"bail lug {'+X' if sx_ > 0 else '-X'}, 12 mm", sp.plate(x0, x0 + 12, -40, 40, top - 60, top + 60, holes=[("x", 0.0, top + 30, 21.0)], edge=1.0))
        xe = od / 2 + 12 if sx_ > 0 else -od / 2 - 12
        out.append(weld(f"bailer: lug {'+X' if sx_ > 0 else '-X'} to barrel", sp.weld_bead((xe, -40, top - 60), (xe, 40, top - 60), 5.0, (sx_, 0, 0), (0, 0, -1)), "bailer", G))
    xl = od / 2 + 12 + 1
    ztop = top + bh + bw / 2
    for sx_ in (-1, 1):
        x0 = xl if sx_ > 0 else -xl - btk
        BL(f"bail leg {'+X' if sx_ > 0 else '-X'}, 50 x 12 flat", sp.plate(x0, x0 + btk, -bw / 2, bw / 2, top, ztop, holes=[("x", 0.0, top + 30, 21.0)], edge=1.0))
        out += fasteners(_clevis(20.0, 25.0, ((xl + btk) * sx_, 0.0, top + 30), (sx_, 0, 0), f"bail {'+X' if sx_ > 0 else '-X'}"), "bailer", G, bom=None)
    BL("bail top bar with eye, 36 mm", sp.plate(-xl - btk, xl + btk, -18.0, 18.0, ztop, ztop + 60, holes=[("y", 0.0, ztop + 35, 22.0)], edge=1.5))
    for sx_ in (-1, 1):
        xe = (xl + btk) if sx_ > 0 else -xl - btk
        out.append(weld(f"bailer: bail top to leg {'+X' if sx_ > 0 else '-X'}", sp.weld_bead((xe, -18.0, ztop), (xe, 18.0, ztop), 4.0, (sx_, 0, 0), (0, 0, 1)), "bailer", G))
    return out


def jerk_and_fairlead(P=None):
    """Jerk bar hooked on the vertical line above the doors, and the roller fairlead set over the pole hole."""
    M = _M()
    P = P or M.PARAMS
    D = M.derived(P)
    out = []
    G = "jerk"
    y_r = D["drop_y"]
    rd = P["rope_d"]
    zc = P["collar_h"]
    zd = zc + P["wh_frame"][1] + P["door_angle"][0]          # top of the closed doors
    zj = zd + B["spud_span"] / 2 + 60.0
    ro, rw, ra = B["roller"]
    yc_ = y_r - rd / 2 - ro / 2 + 3.0                       # roller behind the line (the crew pulls toward +Y)
    JB = lambda n, s, mat=PAINT, kind="made": out.append(mk(f"Jerk bar: {n}", s, mat, kind, None, "jerk", G))  # noqa: E731
    JB("roller 60 mm, nylon, grooved", sp.sheave(ro, ro - 6.0, rw, ra, rd, (0, yc_, zj), (1, 0, 0)), "hdpe_black", "bought")
    for sx_ in (-1, 1):
        x0 = rw / 2 + 1 if sx_ > 0 else -rw / 2 - 1 - 8
        JB(f"fork cheek {'+X' if sx_ > 0 else '-X'}, 8 mm", sp.plate(x0, x0 + 8, yc_ - 25, y_r + 170, zj - 25, zj + 25, holes=[("x", yc_, zj, ra + 0.5)], edge=1.5))
    ax_, cl = sp.pin_with_clips(ra - 0.2, (-rw / 2 - 1 - 8 - 14, yc_, zj), (rw / 2 + 1 + 8 + 14, yc_, zj), clip_axis=(0, 0, 1), inset=6.0)
    JB("roller axle 16 mm", ax_, MILD)
    out += fasteners([("Jerk roller split pin -X", cl[0]), ("Jerk roller split pin +X", cl[1])], "jerk", G, bom=None)
    jod, jt, jl = B["jerk"]
    yb = y_r + 170.0 + jod / 2
    JB("bar 42.4 x 3.2, 1.5 m", sp.tube_between((-jl / 2, yb, zj), (jl / 2, yb, zj), jod, jt))
    for sx_ in (-1, 1):
        xe = rw / 2 + 9 if sx_ > 0 else -rw / 2 - 9
        out.append(weld(f"jerk bar: cheek {'+X' if sx_ > 0 else '-X'} to bar", sp.weld_bead((xe, y_r + 170, zj - 20), (xe, y_r + 170, zj + 20), 4.0, (sx_, 0, 0), (0, -1, 0)), "jerk", G))
        grip = sp.tube_between((sx_ * (jl / 2 - 150), yb, zj), (sx_ * jl / 2, yb, zj), jod + 7.0, 3.4)
        JB(f"rubber grip {'+X' if sx_ > 0 else '-X'}", break_edges(grip, 1.0), "epdm", "bought")
    FL = lambda n, s, mat=GALV, kind="made": out.append(mk(f"Fairlead: {n}", s, mat, kind, None, "jerk", G))  # noqa: E731
    pl = sp.plate(-110, 110, -110, 110, zd, zd + 6, edge=1.0)
    pl = pl - sp.plate(-6, 6, y_r - 6, 120, zd - 1, zd + 7, edge=0) - Pos(0, y_r, zd + 3) * Cylinder(8, 8)
    FL("base plate 6 mm with a line slot", pl)
    for sx_ in (-1, 1):
        FL(f"locating pin {'+X' if sx_ > 0 else '-X'}", sp.bar_between((sx_ * 80, -80, zd - 25), (sx_ * 80, -80, zd), 12.0, 0.8), MILD)
    rr = 20.0
    for sy_ in (-1, 1):
        yy = y_r + sy_ * (rd / 2 + rr + 0.5)
        for sx_ in (-1, 1):
            x0 = 45.0 if sx_ > 0 else -51.0
            FL(f"roller bracket {'+X' if sx_ > 0 else '-X'} {'+Y' if sy_ > 0 else '-Y'}, 6 mm",
               sp.plate(x0, x0 + 6, yy - 15, yy + 15, zd + 6, zd + 46, holes=[("x", yy, zd + 31, 10.5)], edge=0.8))
            xe = 51.0 if sx_ > 0 else -51.0
            out.append(weld(f"fairlead: bracket {'+X' if sx_ > 0 else '-X'} {'+Y' if sy_ > 0 else '-Y'}",
                            sp.weld_bead((xe, yy - 15, zd + 6), (xe, yy + 15, zd + 6), 3.0, (sx_, 0, 0), (0, 0, 1)), "jerk", G))
        FL(f"roller {'+Y' if sy_ > 0 else '-Y'}, 40 mm HDPE", break_edges(sp.tube_between((-44.0, yy, zd + 31), (44.0, yy, zd + 31), 2 * rr, 9.5), 1.0), "hdpe_black", "bought")
        ax_, cl = sp.pin_with_clips(10.0, (-51 - 16, yy, zd + 31), (51 + 16, yy, zd + 31), clip_axis=(0, 0, 1), inset=5.0)
        FL(f"roller axle {'+Y' if sy_ > 0 else '-Y'}, 10 mm", ax_, MILD)
        out += fasteners([(f"Fairlead axle split pin {'+Y' if sy_ > 0 else '-Y'} -X", cl[0]), (f"Fairlead axle split pin {'+Y' if sy_ > 0 else '-Y'} +X", cl[1])], "jerk", G, bom=None)
    return out
