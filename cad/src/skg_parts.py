"""SinkGrab repo-specific CAD helpers (kit 1.9 parts library extensions, STANDARDS section 24).

These sit beside .kit/cad_parts.py and are candidates for a future kit release (see docs/REVIEW.md):

    between()       place any stock built along +Z between two points, with its cross-section turned by 'up'
    shs_between(), tube_between(), bar_between(), flat_between()   real stock (cad_parts) between two points
    plate()         a plate given by its box extents, edges broken, with round holes along X, Y or Z
    weld_bead()     a fillet weld bead along a segment with its two legs on any two faces
    ring_weld()     a round fillet weld (tube or shaft into a plate)
    bolt_set()      ISO 4017 bolt, two ISO 7089 washers and an ISO 4032 nut on any axis (adds M14, which the
                    kit table lacks: s 21, k 8.8, m 12.8, washer 28 x 2.5)
    captive_bolt()  a bolt pushed up from below and tacked under a plate, with washer and nut on top
    stud_set()      a welded stud with washer and nut
    pillow_block()  a UCP2xx pillow block ball bearing: cast housing with two bolt holes, insert, grease nipple
    sprocket()      ISO 606 roller-chain sprocket (08B by default) with teeth
    sheave()        grooved rope sheave with a bearing boss
    pin_clip()      R-clip or split pin through a pin end

All sizes in millimetres. CONCEPT, NOT FOR FABRICATION.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / ".kit"))
from build123d import (Box, Cylinder, Plane, Polygon, Pos, Rot, Solid, Sketch, Circle, Vector, Compound,  # noqa: E402
                       Location, extrude, revolve, Axis, RegularPolygon, chamfer, fillet)
import cad_parts as cp  # noqa: E402
from cad_parts import break_edges  # noqa: E402

ISO = dict(cp.ISO)
ISO[14] = (21, 8.8, 12.8, 28, 2.5, 2.0)


# --------------------------------------------------------------------------------------------- placement
def _v(p):
    return Vector(*p) if not isinstance(p, Vector) else p


def frame_at(a, b, up=(0, 0, 1)):
    """A plane with its origin at a, z along a->b and x as near to 'up' as the direction allows."""
    a, b = _v(a), _v(b)
    z = (b - a).normalized()
    u = _v(up)
    if abs(u.normalized().dot(z)) > 0.98:
        u = Vector(1, 0, 0) if abs(z.X) < 0.9 else Vector(0, 1, 0)
    x = (u - z * u.dot(z)).normalized()
    return Plane(origin=a, x_dir=x, z_dir=z)


def between(shape, a, b, up=(0, 0, 1)):
    """Place a shape built along +Z from z = 0 so it runs from a to b."""
    return frame_at(a, b, up) * shape


def length(a, b):
    return (_v(b) - _v(a)).length


def shs_between(a, b, s, t, up=(0, 0, 1)):
    return between(cp.shs(s, t, length(a, b)), a, b, up)


def rhs_between(a, b, w, h, t, up=(0, 0, 1)):
    return between(cp.rhs(w, h, t, length(a, b)), a, b, up)


def tube_between(a, b, od, t):
    return between(cp.round_tube(od, t, length(a, b)), a, b)


def bar_between(a, b, d, chamfer_ends=0.8):
    return between(cp.round_bar(d, length(a, b), chamfer_ends), a, b)


def flat_between(a, b, w, t, up=(0, 0, 1), r=0.8):
    """Flat bar w x t from a to b; the w side lies along 'up' (projected square to the bar)."""
    return between(cp.flat_bar(w, t, length(a, b), r=r), a, b, up)


# --------------------------------------------------------------------------------------------- plates
def plate(x0, x1, y0, y1, z0, z1, holes=(), edge=1.0, slots=()):
    """Box plate with edges broken by 'edge' (capped at a third of the thinnest side) and round holes
    holes = [(axis, c1, c2, d), ...]: axis 'x' -> (y, z), 'y' -> (x, z), 'z' -> (x, y)."""
    xs, ys, zs = sorted((x0, x1)), sorted((y0, y1)), sorted((z0, z1))
    w, h, t = xs[1] - xs[0], ys[1] - ys[0], zs[1] - zs[0]
    s = Pos(sum(xs) / 2, sum(ys) / 2, sum(zs) / 2) * Box(w, h, t)
    if edge:
        s = break_edges(s, min(edge, min(w, h, t) / 3.2))
    for ax, c1, c2, d in holes:
        s = s - hole(ax, c1, c2, d, (xs, ys, zs))
    return s


def hole(ax, c1, c2, d, ext):
    xs, ys, zs = ext
    if ax == "x":
        return Pos(sum(xs) / 2, c1, c2) * Rot(0, 90, 0) * Cylinder(d / 2, xs[1] - xs[0] + 2)
    if ax == "y":
        return Pos(c1, sum(ys) / 2, c2) * Rot(90, 0, 0) * Cylinder(d / 2, ys[1] - ys[0] + 2)
    return Pos(c1, c2, sum(zs) / 2) * Cylinder(d / 2, zs[1] - zs[0] + 2)


def xhole(y, z, d, x0, x1):
    return Pos((x0 + x1) / 2, y, z) * Rot(0, 90, 0) * Cylinder(d / 2, abs(x1 - x0) + 2)


def yhole(x, z, d, y0, y1):
    return Pos(x, (y0 + y1) / 2, z) * Rot(90, 0, 0) * Cylinder(d / 2, abs(y1 - y0) + 2)


def zhole(x, y, d, z0, z1):
    return Pos(x, y, (z0 + z1) / 2) * Cylinder(d / 2, abs(z1 - z0) + 2)


# --------------------------------------------------------------------------------------------- welds
def weld_bead(a, b, leg, n1, n2):
    """Fillet weld bead from point a to point b (the joint root line), legs 'leg' along the unit directions
    n1 and n2 (each square to the line, pointing along the two faces away from the root)."""
    a, b = _v(a), _v(b)
    d = (b - a)
    L = d.length
    z = d.normalized()
    x = _v(n1).normalized()
    x = (x - z * x.dot(z)).normalized()
    y = z.cross(x)
    n2 = _v(n2).normalized()
    p2 = (leg * n2.dot(x), leg * n2.dot(y))
    pts = [(0.0, 0.0), (leg, 0.0), p2]
    area = (pts[1][0] * pts[2][1] - pts[2][0] * pts[1][1])
    if area < 0:
        pts = [pts[0], pts[2], pts[1]]
    pl = Plane(origin=a, x_dir=x, z_dir=z)
    return pl * extrude(Polygon(*pts, align=None), L)


def ring_weld(center, axis, r, leg):
    """Round fillet weld: a cone ring of leg 'leg' round a tube or shaft of radius r where it meets a face at
    'center', the weld standing up along 'axis'."""
    pl = Plane(origin=_v(center), z_dir=_v(axis))
    cone = Solid.make_cone(r + leg, r, leg, pl)
    cyl = Solid.make_cylinder(r, leg, pl)
    return cone - cyl


# --------------------------------------------------------------------------------------------- fasteners
def _hex(s, h):
    return cp._hex(s, h)


def hex_bolt(d, L):
    s, k = ISO[d][0], ISO[d][1]
    head = _hex(s, k)
    shank = Pos(0, 0, -L / 2) * Cylinder(d / 2, L)
    try:
        shank = chamfer(shank.edges().sort_by(Axis.Z)[0], d * 0.08)
    except Exception:
        pass
    return head + shank


def hex_nut(d):
    s, m = ISO[d][0], ISO[d][2]
    return _hex(s, m) - Pos(0, 0, m / 2) * Cylinder(d / 2, m)


def washer(d):
    d2, h = ISO[d][3], ISO[d][4]
    return extrude(Sketch() + Circle(d2 / 2) - Circle(d * 0.54), h)


def bolt_length(d, grip, extra=None):
    s, k, m, d2, h, p = ISO[d]
    return math.ceil((grip + 2 * h + m + (extra if extra is not None else 2.5 * p)) / 5) * 5


def bolt_set(d, grip, top, axis=(0, 0, 1), label="", extra=None):
    """Bolt, two washers and a nut clamping a joint 'grip' thick. 'top' is the point on the bolt axis at the
    face the head bears on; the bolt shank runs along -axis. Returns [(name, shape), ...]."""
    s, k, m, d2, h, p = ISO[d]
    L = bolt_length(d, grip, extra)
    pl = Plane(origin=_v(top), z_dir=_v(axis))
    return [(f"M{d}x{L} hex bolt (ISO 4017){label}", pl * (Pos(0, 0, h) * hex_bolt(d, L))),
            (f"M{d} washer (ISO 7089){label}", pl * washer(d)),
            (f"M{d} washer (ISO 7089){label}", pl * (Pos(0, 0, -grip - h) * washer(d))),
            (f"M{d} hex nut (ISO 4032){label}", pl * (Pos(0, 0, -grip - h - m) * hex_nut(d)))]


def captive_bolt(d, L, under, axis=(0, 0, 1), clamp=0.0, label=""):
    """A bolt pushed up from below a plate (its head tacked to the underside at 'under'), the shank standing
    up along 'axis'; washer and nut on top of a clamped thickness 'clamp' measured from 'under'."""
    s, k, m, d2, h, p = ISO[d]
    pl = Plane(origin=_v(under), z_dir=_v(axis))
    bolt = pl * (Rot(180, 0, 0) * hex_bolt(d, L))
    return [(f"M{d}x{L} hex bolt (ISO 4017), captive{label}", bolt),
            (f"M{d} washer (ISO 7089){label}", pl * (Pos(0, 0, clamp) * washer(d))),
            (f"M{d} hex nut (ISO 4032){label}", pl * (Pos(0, 0, clamp + h) * hex_nut(d)))]


def stud_set(d, L, base, axis=(0, 0, 1), clamp=0.0, label=""):
    """Threaded stud welded on at 'base', standing L along 'axis', with washer and nut on a clamped
    thickness 'clamp' measured from the base."""
    s, k, m, d2, h, p = ISO[d]
    pl = Plane(origin=_v(base), z_dir=_v(axis))
    rod = Pos(0, 0, L / 2) * Cylinder(d / 2, L)
    try:
        rod = chamfer(rod.edges().sort_by(Axis.Z)[-1], d * 0.08)
    except Exception:
        pass
    return [(f"M{d}x{L:.0f} welded stud{label}", pl * rod),
            (f"M{d} washer (ISO 7089){label}", pl * (Pos(0, 0, clamp) * washer(d))),
            (f"M{d} hex nut (ISO 4032){label}", pl * (Pos(0, 0, clamp + h) * hex_nut(d)))]


def pin_clip(d_pin, at_pt, pin_axis, clip_axis=(0, 0, 1)):
    """Split pin (or R-clip leg) across a pin of diameter d_pin at 'at_pt', lying along clip_axis."""
    pl = Plane(origin=_v(at_pt), x_dir=_v(clip_axis), z_dir=_v(pin_axis))
    return pl * cp.split_pin(d_pin)


def pin_with_clips(d, a, b, clip_axis=(0, 0, 1), inset=None, chamfer_ends=None):
    """A plain pin from a to b with a cross hole near each end for a split pin; returns (pin, [clip, clip]).
    'inset' is the distance from each end to the clip hole centre."""
    a, b = _v(a), _v(b)
    L = (b - a).length
    z = (b - a).normalized()
    inset = inset if inset is not None else max(4.0, 0.5 * d)
    pin = bar_between(a, b, d, chamfer_ends if chamfer_ends is not None else max(0.5, 0.06 * d))
    dp = d * 0.32
    clips = []
    for c in (a + z * inset, b - z * inset):
        pl = Plane(origin=c, x_dir=_v(clip_axis), z_dir=z)
        pin = pin - pl * (Rot(0, 90, 0) * Cylinder(dp / 2 + 0.15, d * 2))
        clips.append(pin_clip(d, c, z, clip_axis))
    return pin, clips


# --------------------------------------------------------------------------------------------- bought parts
UCP = {  # h centre height, L base length, J bolt spacing, A base width, H1 base thickness, bolt d, housing dia, housing width
    "UCP205": dict(h=36.5, L=140.0, J=105.0, A=38.0, H1=15.0, bolt=12, D=70.0, W=34.0),
    "UCP206": dict(h=42.9, L=165.0, J=121.0, A=48.0, H1=17.0, bolt=14, D=80.0, W=38.0),
}


def pillow_block(kind, x, y, zc, shaft):
    """UCP2xx pillow block ball bearing, shaft along X at (y, zc), base on the plane z = zc - h."""
    u = UCP[kind]
    h, L, J, A, H1, D, W = u["h"], u["L"], u["J"], u["A"], u["H1"], u["D"], u["W"]
    zb = zc - h
    base = plate(x - A / 2, x + A / 2, y - L / 2, y + L / 2, zb, zb + H1, edge=2.0)
    for sgn in (-1, 1):
        base = base - zhole(x, y + sgn * J / 2, u["bolt"] + 1.5, zb - 1, zb + H1 + 1)
    web = Pos(x, y, (zb + H1 + zc) / 2) * Box(W * 0.8, D * 0.78, zc - zb - H1 + 1)
    housing = Pos(x, y, zc) * Rot(0, 90, 0) * Cylinder(D / 2, W)
    body = base + web + housing
    body = body - Pos(x, y, zc) * Rot(0, 90, 0) * Cylinder(D / 2 - 7, W + 2)
    insert = Pos(x, y, zc) * Rot(0, 90, 0) * (Cylinder(D / 2 - 7, W + 8) - Cylinder(shaft / 2 + 0.05, W + 10))
    insert = break_edges(insert, 0.8)
    nipple = Pos(x, y, zc + D / 2 + 4) * (Cylinder(4, 8) + Pos(0, 0, 6) * _hex(8, 4))
    return break_edges(body, 1.0) + insert + nipple


def sprocket(z, x0, x1, y, zc, bore, pitch=12.7, roller=8.51):
    """Roller-chain sprocket (ISO 606) in the plane x0..x1, centred at (y, zc), with z teeth and a bore."""
    pd = pitch / math.sin(math.pi / z)
    ra = pd / 2 + 0.3 * roller
    rr = pd / 2 - roller / 2
    pts = []
    n = z
    for k in range(n):
        a0 = 2 * math.pi * k / n
        da = 2 * math.pi / n
        for f, r in ((0.0, rr), (0.22, rr + 0.25 * roller), (0.36, ra), (0.64, ra), (0.78, rr + 0.25 * roller)):
            a = a0 + f * da
            pts.append((y + r * math.cos(a), zc + r * math.sin(a)))
    face = Plane.YZ.offset(x0) * Polygon(*pts, align=None)
    s = extrude(face, amount=x1 - x0)
    if s.volume < 0 or s.bounding_box().min.X < min(x0, x1) - 1:
        s = extrude(face, amount=-(x1 - x0))
    s = s - Pos((x0 + x1) / 2, y, zc) * Rot(0, 90, 0) * Cylinder(bore / 2, abs(x1 - x0) + 2)
    return s


def sheave(od, pd, w, bore, rope_d, center, axis):
    """Rope sheave: grooved rim od, groove bottom at the pitch radius less half a rope, width w, an 8 mm web
    with six lightening holes, and a bearing boss of 2.2 x bore; 'axis' is the axle direction."""
    r_out, r_g = od / 2, pd / 2 - rope_d / 2
    gw = rope_d * 1.15
    r_rim_in = r_g - 7.0
    r_boss = bore * 1.1
    tw = 4.0
    webbed = r_rim_in - r_boss > 16.0
    groove = [(r_out - 3, -w / 2), (r_out, -w / 2 + 3), (r_out, -gw / 2 - 2), (r_g + gw / 2, -gw / 2), (r_g, 0.0),
              (r_g + gw / 2, gw / 2), (r_out, gw / 2 + 2), (r_out, w / 2 - 3), (r_out - 3, w / 2)]
    if webbed:
        prof = ([(bore / 2, -w / 2), (r_boss, -w / 2), (r_boss + 3, -tw), (r_rim_in - 3, -tw), (r_rim_in, -w / 2 + 2)] + groove +
                [(r_rim_in, w / 2 - 2), (r_rim_in - 3, tw), (r_boss + 3, tw), (r_boss, w / 2), (bore / 2, w / 2)])
    else:
        prof = [(bore / 2, -w / 2)] + groove + [(bore / 2, w / 2)]
    face = Plane.XZ * Polygon(*prof, align=None)
    s = revolve(face, Axis.Z, 360)
    rh = (r_boss + r_rim_in) / 2
    dh = min(0.8 * (r_rim_in - r_boss - 6), 2 * rh * math.sin(math.pi / 6) - 6)
    for k in range(6 if webbed and dh > 4 else 0):
        a = 2 * math.pi * k / 6
        s = s - Pos(rh * math.cos(a), rh * math.sin(a), 0) * Cylinder(dh / 2, w + 2)
    pl = Plane(origin=_v(center), z_dir=_v(axis))
    return pl * s


def hlr_safe(shape):
    """Copy of a shape for hidden-line views and concept pictures only. OCCT's hidden-line projection hangs on the
    ISO 2341 clevis pins as cadquery builds them (found on the shear link's 16 x 26 pin and the drawbar's 20 x 40
    pins), so each round pin-like solid (section 10 to 40 mm, longer than 20 mm, under 60 cm3) lying along X, Y or Z
    is drawn as a plain cylinder of its head diameter and length. Never used for the model, STEP or masses."""
    from build123d import Compound
    out = []
    for sol in shape.solids():
        bb = sol.bounding_box()
        sz = (bb.size.X, bb.size.Y, bb.size.Z)
        c = bb.center()
        done = False
        if sol.volume < 60000:
            for ax in range(3):
                a, b = [sz[k] for k in range(3) if k != ax]
                if sz[ax] > 20.0 and 10.0 < a < 40.0 and abs(a - b) < 0.5 and sz[ax] > a:
                    lo = (bb.min.X, bb.min.Y, bb.min.Z)[ax]
                    out.append(_rod(ax, (c.X, c.Y, c.Z), a / 2, lo, lo + sz[ax]))
                    done = True
                    break
        if not done:
            out.append(sol)
    return Compound(out)


def _rod(ax, c, r, lo, hi):
    from build123d import Cylinder, Pos, Rot
    mid = [c[0], c[1], c[2]]
    mid[ax] = (lo + hi) / 2
    rot = (Rot(0, 90, 0), Rot(90, 0, 0), Rot(0, 0, 0))[ax]
    return Pos(*mid) * rot * Cylinder(r, hi - lo)
