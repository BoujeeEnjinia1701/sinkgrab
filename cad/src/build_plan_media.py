"""SinkGrab prototype build plan pictures (SKG-BLD-001, STANDARDS section 18).

Run from the repo root:  python cad/src/build_plan_media.py [overview|sheets|joints|steps ...]
With no argument it draws everything. Every picture is drawn from cad/src/model.py, so the
pictures and the model never disagree:
    docs/05-build-plan/overview.png       every component pulled apart, numbered in build order
    cad/drawings/SKG-DWG-101 to 117       making sketches for the made components
    docs/05-build-plan/joint-NN.png       close-ups of the joints that need explaining
    docs/05-build-plan/step-NN.png        one picture per assembly step
Uses .kit/build_views.py. BUILD PLAN ILLUSTRATION, PLAN NOT YET BUILT.
"""
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
import build_views as bv  # noqa: E402
from build_views import Part  # noqa: E402
from build123d import Compound, Pos, Rot  # noqa: E402
from model import (PARAMS as P, derived, capstan_parts, lead_parts, grab_parts, scraper_parts,  # noqa: E402
                   wellhead_parts, saddle_part, tripod_context, well_context, head_sheave, rope_shape,
                   bx, zcyl, annulus_z)

OUT = ROOT / "docs" / "05-build-plan"
DWG = ROOT / "cad" / "drawings"
DATE = "2026-10-03"
D = derived(P)
CAP = capstan_parts(P)
LEAD = lead_parts(P)
GRAB = grab_parts(P)
SCR = scraper_parts(P)
WH = wellhead_parts(P)
SAD = saddle_part(P)
GREY = "#D1D5DB"

COL = {"frame": "#0F766E", "drum": "#C2410C", "drum_bearings": "#374151", "crank_bearings": "#4B5563",
       "crank_shaft": "#6B7280", "small_sprocket": "#B45309", "shear_pin": "#DC2626", "chain": "#78716C",
       "guard": "#CA8A04", "cranks": "#111827", "pawl": "#1D4ED8", "brake": "#9333EA", "stakes": "#57534E",
       "cradle": "#0E7490", "lead_sheave": "#D4A017", "lead_axle": "#374151", "drawbar": "#64748B", "draw_pins": "#111827",
       "head": "#2563EB", "ballast": "#1E3A8A", "tie_rods": "#475569", "shell_pins": "#111827", "shell_a": "#EA580C",
       "shell_b": "#F59E0B", "crosshead": "#15803D", "hinge_pin": "#111827", "cross_sheave": "#D4A017",
       "cross_axle": "#374151", "shear_link": "#DC2626", "link_pin": "#B91C1C", "scraper_pole": "#0369A1",
       "arms": "#E11D48", "arm_pins": "#111827", "sleeve": "#7C3AED", "sleeve_pins": "#111827", "struts": "#A16207",
       "pole_section": "#0284C7", "tbar": "#1E40AF", "wh_frame": "#0F766E", "doors": "#9CA3AF", "saddle": "#57534E",
       "rope": "#E11D48", "hs_sheave": "#D4A017"}

ALL = {**CAP, **LEAD, **GRAB, **SCR, **WH}


def part(name, shape, key, explode=(0, 0, 0)):
    return Part(name, shape, COL[key], None, tuple(explode))


def crop(shape, x0, x1, y0, y1, z0, z1):
    s = shape & bx(x0, x1, y0, y1, z0, z1)
    return s


def moved(shape, dx, dy, dz):
    return Pos(dx, dy, dz) * shape


# ----------------------------------------------------------------- overview
def overview():
    cy = -D["y_d"]                                   # capstan moved to y = 0
    ly = 1760.0 + 1100.0                             # lead cradle to y = +1100
    gx, sx = 1700.0, 2900.0
    items = [
        ("Capstan frame", moved(CAP["frame"], 0, cy, 0), "frame", (0, 0, 0)),
        ("Winding drum with brake drum and ratchet", moved(CAP["drum"], 0, cy, 0), "drum", (0, 0, 650)),
        ("Pawl", moved(CAP["pawl"], 0, cy, 0), "pawl", (350, 0, 650)),
        ("Crank shaft, sprocket hub and cranks", moved(CAP["crank_shaft"] + CAP["small_sprocket"] + CAP["cranks"], 0, cy, 0), "crank_shaft", (0, 0, 650)),
        ("Chain guard", moved(CAP["guard"], 0, cy, 0), "guard", (-550, 0, 350)),
        ("Band brake and weighted lever", moved(CAP["brake"], 0, cy, 0), "brake", (500, -250, 0)),
        ("Ground stakes (4)", moved(CAP["stakes"] & bx(-2000, 2000, -9000, 9000, 0, 200), 0, cy, 0), "stakes", (0, 0, -100)),
        ("Foot cradle", moved(LEAD["cradle"], 0, ly, 0), "cradle", (0, 0, 0)),
        ("Drawbar, two halves", Pos(-1100, 3300, 0) * LEAD["drawbar"], "drawbar", (0, 0, 0)),
        ("Grab head and ballast plates", moved(GRAB["head"] + GRAB["ballast"], gx, 0, 300), "head", (0, 0, 450)),
        ("Tie rods (4)", moved(GRAB["tie_rods"], gx, 0, 300), "tie_rods", (0, 0, 220)),
        ("Grab shell A", moved(GRAB["shell_a"], gx, 0, 300), "shell_a", (250, 0, 0)),
        ("Grab shell B", moved(GRAB["shell_b"], gx, 0, 300), "shell_b", (-250, 0, 0)),
        ("Crosshead and hinge pin", moved(GRAB["crosshead"] + GRAB["hinge_pin"], gx, 0, 300), "crosshead", (0, 0, 120)),
        ("Shear link", moved(GRAB["shear_link"], gx, 0, 300), "shear_link", (300, 0, 300)),
        ("Scraper head (pole, hub, centralizer)", moved(SCR["scraper_pole"], sx, 0, 450), "scraper_pole", (0, 0, 0)),
        ("Scraper arms and struts", moved(SCR["arms"] + SCR["struts"], sx, 0, 450), "arms", (0, 0, 250)),
        ("Sliding sleeve and foot", moved(SCR["sleeve"], sx, 0, 450), "sleeve", (0, 0, -150)),
        ("Pole section, 2 m", Pos(sx + 700, -1300, 60) * Rot(90, 0, 0) * Pos(0, 0, -P["head_len"]) * SCR["pole_section"], "pole_section", (0, 0, 0)),
        ("T-bar", Pos(sx + 400, 1200, -3500 + 2000) * SCR["tbar"], "tbar", (0, 0, 0)),
        ("Well-head frame", Pos(0, -2700, -300) * WH["wh_frame"], "wh_frame", (0, 0, 0)),
        ("Folding doors (2)", Pos(0, -2700, -300) * WH["doors"], "doors", (0, 0, 450)),
        ("Ballast saddle (1 of 8)", Pos(1900, -1700, 300) * SAD, "saddle", (0, 0, 0)),
        ("Bearings (4), bought", moved(CAP["drum_bearings"] + CAP["crank_bearings"], 0, cy, 0), "drum_bearings", (0, 0, 350)),
        ("Chain and sprockets, bought", moved(CAP["chain"], 0, cy, 0), "chain", (-350, 0, 450)),
        ("Sheaves (3), bought", moved(LEAD["lead_sheave"], 0, ly, 0) + moved(GRAB["cross_sheave"], gx, 0, 300), "lead_sheave", (0, 0, 300)),
    ]
    parts = [part(n, s, k, e) for n, s, k, e in items]
    bv.overview(parts, OUT / "overview.png", "SinkGrab prototype: every component in build order",
                subtitle="Made parts first (1 to 23), then bought parts (24 to 26); ropes, pins and fasteners not shown",
                key=True, size=(12, 8.5))
    print("overview")


# ----------------------------------------------------------------- making sketches
def sheets():
    cap_all = [Part(k, v, GREY) for k, v in CAP.items() if k != "stakes"]
    grab_all = [Part(k, v, GREY) for k, v in GRAB.items()]
    scr_all = [Part(k, v, GREY) for k, v in SCR.items()]
    lead_all = [Part(k, v, GREY) for k, v in LEAD.items()]
    wh_all = [Part(k, v, GREY) for k, v in WH.items()]
    OWN = {"SKG-DWG-103": {"crank_shaft", "small_sprocket", "cranks"}, "SKG-DWG-105": {"pawl", "brake"},
           "SKG-DWG-110": {"head", "ballast"}, "SKG-DWG-111": {"crosshead", "tie_rods", "shear_link", "hinge_pin"},
           "SKG-DWG-113": {"arms", "struts", "sleeve"}, "SKG-DWG-114": {"pole_section", "tbar"},
           "SKG-DWG-116": {"doors"}, "SKG-DWG-109": {"shell_a"}}
    rw = P["ring"][1]
    ring_piece = bx(-rw / 2, rw / 2, -260, 260, -500, 0)
    S = [
        ("SKG-DWG-101", "Capstan frame: making sketch", CAP["frame"], "frame", cap_all,
         "40 x 40 x 2 SHS; 8 mm plate; 33.7 x 3.2 tube; 12 mm bar",
         ["Two side frames 430 apart (bearing planes at -200 and +230 from the drum centre)",
          "Each: base rail 660, post 150 behind the drum axis up to the top plate (805 to top)",
          "Two pad posts 60 either side of the drum axis; pad 180 x 50 x 8, top at 169",
          "Front brace from the rail front to the post at 640; rear brace to the post at 560",
          "Front and rear cross rails; top tie at 700; brake anchor bar 125 behind the axis",
          "Drawbar clevis: two 8 mm plates on the front rail, 21 mm hole 40 up, 32 apart",
          "Pawl bracket under the +X front brace, 12 mm pin; brake post and lever plate",
          "Four stake tubes 33.7 x 80, 200 either side of the drum axis, outside the rails",
          "Tack on a flat table; diagonals within 3 mm; pads level and in line within 1 mm"]),
        ("SKG-DWG-102", "Winding drum: making sketch", CAP["drum"], "drum", cap_all,
         "168.3 x 4.5 pipe; 6 mm plate; 250 x 6 ring; 8 mm plate; 30 mm S355 shaft",
         ["Core 200 long between 6 mm flanges 260 OD (six 36 mm lightening holes)",
          "Holds 23 turns a layer of 8 mm rope; three layers, 41.7 m",
          "Brake drum 250 OD x 50 wide on a 6 mm web, 6 mm outboard of the +X flange",
          "Ratchet wheel 20 teeth, 200 OD, 168 root, 8 mm, 8 mm outboard of the brake drum",
          "Shaft 30 x 549 through all; weld in short stitches, turning the drum",
          "48-tooth sprocket on a hub at the -X end, outboard of the bearing",
          "Rope clamp with a U-bolt on the -X flange",
          "Check: flanges run true within 1.5 mm; brake drum within 0.5 mm"]),
        ("SKG-DWG-103", "Crank shaft, sprocket hub and cranks: making sketch",
         CAP["crank_shaft"] + CAP["small_sprocket"] + CAP["cranks"], "crank_shaft", cap_all,
         "25 mm S355 shaft; 36 mm tube hub; 12 mm plate arms; 32 mm handle tube",
         ["Shaft 25 x 633; square ends 20 across flats, 40 long, for the cranks",
          "Hub 26 long, bored to slide on the shaft; 12-tooth sprocket welded to it",
          "Drill hub and shaft together for the 3 mm shear pin, 12 from the sprocket face",
          "Crank arms 250 between centres with a square socket and a ball-lock pin",
          "Handles 32 x 120 turn on M12 bolts; arms 180 deg apart",
          "Check: hub turns freely with the pin out, locks with it in"]),
        ("SKG-DWG-104", "Chain guard: making sketch", CAP["guard"], "guard", cap_all,
         "1.5 mm steel sheet",
         ["Two side sheets cut to the outline: 22 clear of the big sprocket, 30 of the small",
          "Band 46 wide round the outline, stitch welded or riveted",
          "Holes 60 (drum hub) and 44 (crank shaft), clear of both",
          "Two M6 screws into the frame tabs at 560 and 780",
          "Check: no finger reaches the chain with the guard on"]),
        ("SKG-DWG-105", "Pawl and band brake with weighted lever: making sketch",
         CAP["pawl"] + CAP["brake"], "brake", cap_all,
         "8 mm plate; 40 x 3 spring steel band with lining; 40 x 12 flat; 6 kg block",
         ["Pawl: 12 mm pivot hole, nose radius 3, 150 from the drum axis at the pivot",
          "Pawl stops the drum turning to pay out; flip it up to lower",
          "Band 270 deg round the brake drum, lining bonded on, 6 mm thick in all",
          "Anchor end pinned to the post behind the drum (the tight end when lowering)",
          "Live end by a 25 x 6 link to the lever, 60 from the pivot",
          "Lever 650 long, 6 kg block at the end: brake on when let go",
          "Check: lever lifts 30 mm to free the drum; 300 N m holding"]),
        ("SKG-DWG-106", "Ground stake: making sketch",
         CAP["stakes"] & bx(-1000, 0, -4800, -4500, -600, 200), "stakes", cap_all,
         "25 mm round bar, 34 mm washer",
         ["Four stakes 25 x 500, ground to a point",
          "34 mm washer welded on top; rests on the stake tube",
          "Stop the capstan skating; the drawbar is the anchor",
          "Check: straight within 3 mm"]),
        ("SKG-DWG-107", "Foot cradle: making sketch", LEAD["cradle"], "cradle", lead_all,
         "10 mm plate; 4 mm flat rim; 10 mm clamp bars; 8 mm cheeks",
         ["Base 320 wide under the HatchSide leg A foot, tongue to the sheave",
          "Rim 30 high on three sides; the foot plate drops in",
          "Two clamp bars 260 x 40 x 10 across the foot plate, four M12 bolts",
          "Cheeks 8 mm, 30 apart, 20.5 mm axle hole 185 up, 260 beyond the foot centre",
          "Drawbar clevis: two 8 mm plates, 21 mm hole 40 up, 160 beyond the sheave",
          "Check: the foot sits flat; sheave turns between the cheeks"]),
        ("SKG-DWG-108", "Drawbar: making sketch",
         Rot(0, 0, 90) * Pos(0, -(P["lead_y"] + D["y_d"]) / 2, 0) * LEAD["drawbar"], "drawbar", lead_all,
         "48.3 x 3.2 tube; 41 mm bar spigot; 12 mm plate tongues",
         ["Two halves, 2,470 between pin centres in all",
          "Spigot 41 x 200 welded 100 into one half; slides into the other",
          "Tongue 12 mm with a 21 mm hole welded into each outer end",
          "20 mm clevis pins with R-clips at both ends",
          "Check: straight within 3 mm; pins slide in by hand"]),
        ("SKG-DWG-109", "Grab shell: making sketch", GRAB["shell_a"], "shell_a", grab_all,
         "4 mm plate rolled to 230 radius; 6 mm end plates; 10 x 50 wear-resistant lip",
         ["Skin quarter circle, inside radius 230, 340 wide (shell B 353)",
          "End plates: quarter discs 234 radius with a hinge boss 70 and a lug at 190, 25",
          "Hinge hole 30.5 at the corner; tie rod pin hole 20.5 in the lug",
          "Top cover 4 mm from 50 out to 230, the full width",
          "Lip 10 x 50 welded inside the bottom edge, ground square to the open face",
          "Shell B: same, end plates outside A's (13 mm wider between them)",
          "Check: both shells meet along the lips within 2 mm when pinned"]),
        ("SKG-DWG-110", "Grab head with ballast plates: making sketch",
         GRAB["head"] + GRAB["ballast"], "head", grab_all,
         "6 mm plate box; 25 mm S355 bar; 30 mm tube; 12 and 16 mm plate",
         ["Box 300 x 120 x 40 from 6 mm plate, welded all round",
          "Two head pins 25 dia through the box ends at +/- 120, 418 long",
          "Rope guide tube 30 OD, 14 bore, 65 from the centre on the -X side",
          "Dead-end lug 12 mm under the box at +65, 16.5 mm hole across",
          "Recovery-line eye on top, 20 mm hole",
          "Ballast plates 190 x 110 x 16 bolted to both faces (M10)",
          "Check: 13.3 kg with the plates"]),
        ("SKG-DWG-111", "Crosshead, tie rods and shear link: making sketch",
         GRAB["crosshead"] + GRAB["tie_rods"] + GRAB["shear_link"] + GRAB["hinge_pin"], "crosshead", grab_all,
         "10 mm plate; 30 x 10 flat; 6 mm plate; 30 mm bar",
         ["Crosshead plates 10 mm, 50 apart: hinge hole 30.5, axle hole 20.5 120 above",
          "Hinge pin 30 x 404, R-clips both ends; sheave on a 20 mm axle",
          "Tie rods 30 x 10, 420 between 20.5 and 25.5 holes; two per shell",
          "Shear link: two 6 mm plates 87 x 30, 16 mm pin at the top",
          "Calibrated link pin about 1.9 mm, 62 below the top pin",
          "Check: crosshead turns on the pin; rods swing freely"]),
        ("SKG-DWG-112", "Scraper head (pole, hub and centralizer): making sketch",
         SCR["scraper_pole"], "scraper_pole", scr_all,
         "42.4 x 2.6 tube; 70 mm tube hub; 8 mm plate lugs; 40 x 8 flat; 10 mm skids",
         ["Bottom pole 42.4 x 2.6, 1,420 long, solid 50 mm spike end and stop collar",
          "Hub 70 OD x 90 at 80 above the toe line; two pairs of lugs, 16.5 holes at 45",
          "Centralizer collar at 700 up; three arms 120 deg apart; skids at 440 radius",
          "Skid arms drilled for 340, 440 and 590 radius (0.8, 1.0 and 1.3 m rings)",
          "Top end takes the next section's spigot, 13 mm cross hole",
          "Check: pole straight within 3 mm; skids on a 880 circle"]),
        ("SKG-DWG-113", "Scraper arms, struts and sleeve: making sketch",
         SCR["arms"] + SCR["struts"] + SCR["sleeve"], "arms", scr_all,
         "50 x 10 flat; 10 mm wear plate; 30 x 6 flat; 54 mm tube; 10 mm plate",
         ["Arms 50 x 10, 540 from pivot to toe; toe plate 100 x 80 x 10",
          "Toes reach 590 radius open: 15 beyond a 1.0 m ring's outer face",
          "Struts 30 x 6 in pairs, 398 between 12.5 holes",
          "Sleeve 54 x 110 slides on the pole; foot plate 250 dia below it",
          "Lifting the pole 300 on the sleeve folds the toes to 364 radius",
          "Longer arm pair (660) for 1.2 to 1.3 m rings",
          "Check: arms open and fold freely by hand"]),
        ("SKG-DWG-114", "Pole section and T-bar: making sketch",
         Pos(0, 0, -P["head_len"]) * (SCR["pole_section"] + SCR["tbar"]), "pole_section", scr_all,
         "42.4 x 2.6 tube; 36 mm bar; 48.3 x 2.7 tube; 33.7 x 3.2 tube",
         ["Section 2,000 long; 36 spigot 250 long, 150 out of the bottom",
          "13 mm cross holes 75 from each end; M12 bolt and nyloc nut",
          "T-bar socket 48.3 x 200 fits over a spigot; handle 1,400 across",
          "Eye plate 12 mm on top, 18 mm hole for the closing line shackle",
          "Check: sections join straight within 5 mm over 4 m"]),
        ("SKG-DWG-115", "Well-head frame: making sketch", WH["wh_frame"], "wh_frame", wh_all,
         "50 x 50 x 5 angle; 6 mm plate; 24 mm tube knuckles",
         ["Square opening 1,360, horizontal legs on the collar, vertical legs inside",
          "Made in two halves, bolted at two corners with M12",
          "Four datum brackets 6 mm with 10 mm holes at 537 radius",
          "Four hinge knuckles on the +Y and -Y sides, 1,000 apart",
          "Check: sits on the collar without rocking; datum holes square within 3 mm"]),
        ("SKG-DWG-116", "Folding door: making sketch",
         WH["doors"] & bx(-2000, 2000, 0, 2000, 0, 2000), "doors", wh_all,
         "40 x 40 x 4 angle; expanded steel mesh; 16 mm bar pins",
         ["Frame 1,364 x 680 from 40 x 40 x 4 angle, mesh welded inside",
          "Semicircular notch 32 radius at the middle of the meeting edge",
          "6 mm doubler round the notch; two doors make a 64 mm pole hole",
          "Two hinge pins 16 on the outer edge, into the frame knuckles",
          "Check: both doors close flat and meet within 5 mm"]),
        ("SKG-DWG-117", "Ballast saddle: making sketch", SAD, "saddle",
         [Part("ring wall", ring_piece, GREY)],
         "25 and 20 mm plate offcuts; 12 mm eye plate",
         ["Inner leg 200 x 300 x 25, outer leg 200 x 150 x 20, bridge 25",
          "Slot 95 wide over a 75 mm ring wall",
          "Lifting eye on the bridge, 20 mm hole, its own 6 mm line",
          "20.6 kg; make eight",
          "Check: drops over a 75 mm board without binding"]),
    ]
    for dwg, title, shape, key, nb, mat, notes in S:
        own = OWN.get(dwg, {key})
        if dwg == "SKG-DWG-116":
            nb = [n for n in nb if n.name != "doors"] + [Part("other door", WH["doors"] & bx(-2000, 2000, -2000, 0, 0, 2000), GREY)]
        else:
            nb = [n for n in nb if n.name not in own]
        bv.component_sheet(Part(title, shape, COL[key]), nb[:14], "SinkGrab", dwg, title, mat, notes, DATE, out_dir=str(DWG))
        print("sheet", dwg)


# ----------------------------------------------------------------- joints
def joints():
    yd, hd, yc, hc = D["y_d"], P["hd"], D["y_c"], P["hc"]
    xa, xb = P["x_brg"]
    # 1 drum bearing on its pad
    r = (xa - 60, xa + 60, yd - 120, yd + 120, 100, 300)
    bv.joint([part("Bearing pad on the frame", crop(CAP["frame"], *r), "frame"),
              part("Drum bearing, 2 x M14", crop(CAP["drum_bearings"], *r), "drum_bearings"),
              part("Drum shaft", crop(CAP["drum"], *r), "drum")],
             OUT / "joint-01.png", "Joint 1: drum bearing on its pad", "Two M14 bolts through the pad; set screws lock the shaft")
    # 2 shear pin hub
    xs = D["x_spr"]
    r2 = (xs - 30, xs + 40, yc - 60, yc + 60, hc - 60, hc + 60)
    bv.joint([part("Crank shaft", crop(CAP["crank_shaft"], *r2), "crank_shaft"),
              part("Small sprocket on its hub", crop(CAP["small_sprocket"], *r2), "small_sprocket"),
              part("3 mm shear pin", CAP["shear_pin"], "shear_pin")],
             OUT / "joint-02.png", "Joint 2: shear pin through the sprocket hub", "Cut through the shaft; the hub turns on the shaft and only the pin drives it", cut="+Y")
    # 3 ratchet and pawl
    r3 = (D["x_ratchet"][0] - 5, D["x_ratchet"][1] + 40, yd - 120, yd + 120, hd - 40, hd + 230)
    bv.joint([part("Ratchet wheel on the drum shaft", crop(CAP["drum"], *r3), "drum"),
              part("Pawl", CAP["pawl"], "pawl"),
              part("Pawl bracket and pin", crop(CAP["frame"], *r3), "frame")],
             OUT / "joint-03.png", "Joint 3: ratchet wheel and pawl", "Seen from the +X side; the pawl stops the drum paying out", azim=0, elev=8)
    # 4 band brake
    r4 = (D["x_brake"][0] - 10, xb + 120, yd - 1000, yd + 160, 0, 400)
    bv.joint([part("Brake drum", crop(CAP["drum"], D["x_brake"][0], D["x_brake"][1], yd - 200, yd + 200, 0, 500), "drum"),
              part("Band, link, lever and weight", CAP["brake"], "brake"),
              part("Anchor post and lever plate", crop(CAP["frame"], *r4), "frame")],
             OUT / "joint-04.png", "Joint 4: weighted band brake", "Lift the lever to lower; let go and the weight sets the brake", azim=20, elev=18)
    # 5 drawbar clevis at the capstan
    yf = yd + P["rail_half"] + 40
    r5 = (-80, 80, yf - 90, yf + 160, 0, 100)
    bv.joint([part("Front cross rail and clevis", crop(CAP["frame"], *r5), "frame"),
              part("Drawbar tongue", crop(LEAD["drawbar"], *r5), "drawbar"),
              part("20 mm clevis pin", crop(LEAD["draw_pins"], *r5), "draw_pins")],
             OUT / "joint-05.png", "Joint 5: drawbar on the capstan", "The tongue sits between the clevis plates; the pin carries the pull")
    # 6 foot cradle with the HatchSide foot and lead sheave
    yfoot = -P["hs_r_foot"]
    foot = Pos(0, yfoot, 0) * bx(-P["hs_foot"][0] / 2, P["hs_foot"][0] / 2, -P["hs_foot"][1] / 2, P["hs_foot"][1] / 2, 10.0, 10.0 + P["hs_foot"][2])
    r6 = (-200, 200, P["lead_y"] - 260, yfoot + 200, 0, 300)
    bv.joint([Part("HatchSide leg A foot (shared)", foot, "#9CA3AF"),
              part("Foot cradle", LEAD["cradle"], "cradle"),
              part("Lead sheave", LEAD["lead_sheave"], "lead_sheave"),
              part("Axle", LEAD["lead_axle"], "lead_axle"),
              part("Drawbar end", crop(LEAD["drawbar"], *r6), "drawbar")],
             OUT / "joint-06.png", "Joint 6: HatchSide foot in the cradle", "Clamp bars hold the foot; the line turns up leg A over the sheave")
    # 7 grab hinge: shells' end plates, crosshead and pin near the hinge
    r7 = (-110, 110, -215, 215, -70, 70)
    bv.joint([part("Shell A end plates and boss", crop(GRAB["shell_a"], *r7), "shell_a"),
              part("Shell B end plates (outside A's)", crop(GRAB["shell_b"], *r7), "shell_b"),
              part("Crosshead plates", crop(GRAB["crosshead"], *r7), "crosshead"),
              part("30 mm hinge pin", GRAB["hinge_pin"], "hinge_pin")],
             OUT / "joint-07.png", "Joint 7: grab hinge and crosshead", "One 30 mm pin carries shell A, shell B outside it, and the crosshead between", azim=-35, elev=28)
    # 8 tie rod on the shell lug
    sx, sz = P["shell_pin"]
    r8 = (sx - 70, sx + 50, 120, 230, sz - 60, sz + 120)
    bv.joint([part("Shell A end plate and lug", crop(GRAB["shell_a"], *r8), "shell_a"),
              part("Tie rod", crop(GRAB["tie_rods"], *r8), "tie_rods"),
              part("20 mm pin", crop(GRAB["shell_pins"], *r8), "shell_pins")],
             OUT / "joint-08.png", "Joint 8: tie rod on the shell lug", "Pin through the rod and lug, R-clip outside", azim=-40, elev=20)
    # 9 shear link at the dead end
    zh = D["head_pin_z"]
    rp = P["sheave"][1]
    r9 = (rp - 40, rp + 40, -40, 40, zh - 160, zh + 30)
    bv.joint([part("Dead-end lug under the head", crop(GRAB["head"], *r9), "head"),
              part("Shear link plates", GRAB["shear_link"], "shear_link"),
              part("Calibrated link pin", GRAB["link_pin"], "link_pin")],
             OUT / "joint-09.png", "Joint 9: shear link at the tackle dead end", "The line's thimble hangs on the small pin; if it shears the grab opens", azim=-30)
    # 10 scraper linkage
    r10 = (0, 420, -60, 60, -340, 140)
    bv.joint([part("Pole and hub", crop(SCR["scraper_pole"], *r10), "scraper_pole"),
              part("Arm", crop(SCR["arms"], *r10), "arms"),
              part("Struts", crop(SCR["struts"], *r10), "struts"),
              part("Sleeve and foot", crop(SCR["sleeve"], *r10), "sleeve")],
             OUT / "joint-10.png", "Joint 10: arm, strut and sliding sleeve", "The pole's weight slides it down through the sleeve and opens the arm", azim=-90, elev=5)
    # 11 pole spigot joint
    z0 = P["head_len"]
    r11 = (-40, 40, -40, 40, z0 - 220, z0 + 220)
    bv.joint([part("Scraper head pole", crop(SCR["scraper_pole"], *r11), "scraper_pole"),
              part("Next section with its spigot", crop(SCR["pole_section"], *r11), "pole_section")],
             OUT / "joint-11.png", "Joint 11: pole section joint", "Cut open: 36 mm spigot in the tube, M12 bolt through both", cut="+Y")
    # 12 door hinge and pole hole
    h = P["wh_frame"][0] / 2
    r12 = (-600, 100, 0, h + 60, 280, 420)
    bv.joint([part("Frame and hinge knuckle", crop(WH["wh_frame"], *r12), "wh_frame"),
              part("Door", crop(WH["doors"], *r12), "doors")],
             OUT / "joint-12.png", "Joint 12: door hinge and pole notch", "Hinge pin in the frame knuckle at the outer edge; notch at the meeting edge", azim=-60, elev=35)
    # 13 saddle on the ring wall
    rw = P["ring"][1]
    ring = bx(-rw / 2, rw / 2, -260, 260, -500, 0)
    bv.joint([Part("Top caisson ring wall (site)", ring, "#A8A29E"),
              part("Ballast saddle", SAD, "saddle")],
             OUT / "joint-13.png", "Joint 13: saddle astride the top ring", "Inner leg inside the ring, outer leg in the gap to the lining", azim=-20, elev=15)
    # 14 toe under the cutting edge
    ri, wall, hr = P["ring"][0] / 2, P["ring"][1], P["ring"][2]
    ringc = annulus_z(ri, ri + wall, 20.0, 20.0 + hr) & bx(0, 900, 20, 400, -600, 900)
    bv.joint([Part("Bottom caisson ring (site, cut)", ringc, "#A8A29E"),
              part("Scraper head", crop(SCR["scraper_pole"], -100, 700, -400, 400, -500, 900), "scraper_pole"),
              part("Arm and toe", crop(SCR["arms"], 0, 700, -100, 100, -100, 200), "arms"),
              part("Sleeve and foot", crop(SCR["sleeve"], 0, 700, -400, 400, -500, 200), "sleeve"),
              part("Struts", crop(SCR["struts"], 0, 700, -100, 100, -500, 200), "struts")],
             OUT / "joint-14.png", "Joint 14: toe under the cutting edge", "Toe 15 mm past the ring's outer face, just below the edge; skid on the bore", azim=-90, elev=8)
    print("joints 14")


# ----------------------------------------------------------------- steps
def steps():
    n = 0

    def go(done, new, title, sub, context=(), size=(8, 6), elev=24, azim=-58):
        nonlocal n
        n += 1
        bv.step(done, new, OUT / f"step-{n:02d}.png", title, sub, context=context, label_done=False, size=size, elev=elev, azim=azim)

    g = lambda k, nm, e=(0, 0, 0), src=CAP: Part(nm, src[k], COL[k], None, e)  # noqa: E731
    fr, dr = g("frame", "Frame"), g("drum", "Drum")
    db, cb = g("drum_bearings", "Drum bearings"), g("crank_bearings", "Crank bearings")
    cs, ss, sp = g("crank_shaft", "Crank shaft"), g("small_sprocket", "Sprocket hub"), g("shear_pin", "Shear pin")
    ch, gd, ck, pw, bk = g("chain", "Chain"), g("guard", "Guard"), g("cranks", "Cranks"), g("pawl", "Pawl"), g("brake", "Brake")

    def mv(p, e):
        return Part(p.name, p.shape, p.color, None, e)
    go([dr], [mv(db, (0, 0, 0))], "Step 1: drum bearings onto the drum shaft", "Slide a UCP206 onto each shaft end, grease nipples up; set screws loose")
    go([fr], [mv(dr, (0, 0, 450)), mv(db, (0, 0, 450))], "Step 2: lower the drum onto the pads", "Two people; two M14 bolts each; centre the drum; tighten the set screws")
    go([fr, dr, db], [mv(cb, (0, 0, 350)), mv(cs, (0, 0, 350)), mv(ss, (-150, 0, 350))], "Step 3: crank shaft, hub and bearings onto the top plates", "Hub on the -X end; M12 bolts; sprockets in line within 1 mm")
    go([fr, dr, db, cb, cs, ss], [mv(ch, (-250, 0, 0))], "Step 4: fit the chain", "Over both sprockets; connecting link clip closed end leading")
    go([fr, dr, db, cb, cs, ss, ch], [mv(sp, (0, 0, 200))], "Step 5: fit the shear pin", "3 mm mild steel pin through hub and shaft, split pin; spares on the frame")
    go([fr, dr, db, cb, cs, ss, ch, sp], [mv(gd, (-300, 0, 0))], "Step 6: chain guard on", "Two M6 screws into the tabs; never turn the cranks with it off")
    go([fr, dr, db, cb, cs, ss, ch, sp, gd], [mv(pw, (250, 0, 150))], "Step 7: pawl on its pin", "Washer and R-clip; it drops into the ratchet by its own weight", azim=-30)
    go([fr, dr, db, cb, cs, ss, ch, sp, gd, pw], [mv(bk, (300, 0, 0))], "Step 8: band brake and weighted lever", "Pin the anchor end, then the link and lever; weight on", azim=-30)
    go([fr, dr, db, cb, cs, ss, ch, sp, gd, pw, bk], [mv(ck, (0, 0, 250))], "Step 9: cranks on", "Square sockets onto the shaft ends, 180 deg apart; ball-lock pins in")
    # grab
    G = lambda k, nm, e=(0, 0, 0): Part(nm, GRAB[k], COL[k], None, e)  # noqa: E731
    sa, sb_ = G("shell_a", "Shell A"), G("shell_b", "Shell B")
    go([sa, sb_], [G("crosshead", "Crosshead", (0, 0, 300)), G("hinge_pin", "Hinge pin", (0, 450, 0)),
                   G("cross_sheave", "Crosshead sheave", (0, 0, 300)), G("cross_axle", "Sheave axle", (0, 0, 300))],
       "Step 10: crosshead and hinge pin into the shells", "Shells lip to lip; crosshead between them; pin through all; R-clips")
    base = [sa, sb_, G("crosshead", "Crosshead"), G("hinge_pin", "Hinge pin"), G("cross_sheave", "Sheave")]
    go(base, [G("tie_rods", "Tie rods (4)", (0, 150, 150)), G("shell_pins", "Rod pins (4)", (0, 250, 0))],
       "Step 11: tie rods onto the shell lugs", "Shell A's rods outside A's end plates, shell B's outside B's")
    base += [G("tie_rods", "Tie rods"), G("shell_pins", "Pins")]
    go(base, [G("head", "Head", (0, 0, 350))], "Step 12: head onto the tie rods", "Head pins through the upper rod holes; R-clips")
    base += [G("head", "Head")]
    go(base, [G("ballast", "Ballast plates", (0, 0, 300)), G("shear_link", "Shear link", (250, 0, -150)), G("link_pin", "Link pin", (250, 0, -150))],
       "Step 13: ballast plates and shear link", "M10 bolts for the plates; link on the dead-end lug, calibrated pin below")
    # scraper
    Sx = lambda k, nm, e=(0, 0, 0): Part(nm, SCR[k], COL[k], None, e)  # noqa: E731
    go([Sx("scraper_pole", "Scraper head")], [Sx("sleeve", "Sleeve and foot", (0, 0, -300)), Sx("arms", "Arms", (0, 0, 250)),
                                              Sx("struts", "Struts", (0, 0, 150)), Sx("arm_pins", "Arm pins", (0, 0, 250)),
                                              Sx("sleeve_pins", "Strut pins", (0, 0, -300))],
       "Step 14: arms, struts and sleeve onto the pole", "Sleeve on from below before the stop collar; pins and R-clips", azim=-80, elev=12)
    go([Sx("scraper_pole", "Scraper head"), Sx("arms", "Arms"), Sx("sleeve", "Sleeve"), Sx("struts", "Struts")],
       [Sx("pole_section", "Pole section", (0, 0, 600)), Sx("tbar", "T-bar", (0, 0, 900))],
       "Step 15: pole section and T-bar", "Spigot into the pole, M12 bolt; T-bar socket over the top spigot", size=(7, 8), azim=-80, elev=12)
    # site
    collar, ground = well_context(P, depth=200.0)
    ctx_well = [Part("Well collar (site)", collar, "#E5E7EB")]
    go([], [Part("Well-head frame", WH["wh_frame"], COL["wh_frame"], None, (0, 0, 400))],
       "Step 16: well-head frame on the collar", "Two halves, bolted at the corners; datum holes on the ring wall line", context=ctx_well)
    go([Part("Frame", WH["wh_frame"], GREY)], [Part("Doors", WH["doors"], COL["doors"], None, (0, 0, 350))],
       "Step 17: hang the doors", "Hinge pins into the knuckles; close both; the pole notch meets", context=ctx_well)
    tri = tripod_context(P)
    ctx_tri = [Part("HatchSide tripod (shared)", tri, "#E5E7EB")] + ctx_well
    lead = [Part("Cradle", LEAD["cradle"], COL["cradle"], None, (0, -300, 0)), Part("Lead sheave", LEAD["lead_sheave"], COL["lead_sheave"], None, (0, -300, 0)),
            Part("Axle", LEAD["lead_axle"], COL["lead_axle"], None, (0, -300, 0))]
    go([Part("Frame and doors", WH["wh_frame"] + WH["doors"], GREY)], lead,
       "Step 18: cradle under the leg A foot", "Lift the foot, slide the cradle under, clamp bars and M12 bolts", context=ctx_tri, size=(8, 6.5))
    capk = ["frame", "drum", "drum_bearings", "crank_bearings", "crank_shaft", "small_sprocket", "chain", "guard", "pawl", "brake", "cranks"]
    capstan = [Part("Capstan", Compound([CAP[k] for k in capk]), COL["frame"], None, (0, -500, 0))]
    go([Part("Cradle and sheave", LEAD["cradle"] + LEAD["lead_sheave"], GREY), Part("Frame and doors", WH["wh_frame"] + WH["doors"], GREY)],
       capstan + [Part("Drawbar", LEAD["drawbar"], COL["drawbar"], None, (0, 0, 300)),
                  Part("Stakes", CAP["stakes"] & bx(-2000, 2000, -9000, 9000, 0, 200), COL["stakes"], None, (0, 0, 300))],
       "Step 19: capstan and drawbar", "Drawbar pinned to both clevises, in line; stakes through the tubes", context=ctx_tri, size=(9, 6), azim=-35)
    grab_site = [Part("Grab", Pos(0, 0, D["grab_hinge_site"]) * Rot(0, 0, 90) * Compound(list(GRAB.values())), COL["shell_a"], None, (0, 0, 150)),
                 Part("Closing line", rope_shape(P), COL["rope"], None, (0, 0, 0)),
                 Part("Head sheave for 8 mm rope", head_sheave(P), COL["hs_sheave"], None, (0, 0, 300))]
    go([Part("Capstan, drawbar and cradle", Compound([CAP[k] for k in capk] + [LEAD["drawbar"], LEAD["cradle"], LEAD["lead_sheave"]]), GREY),
        Part("Frame and doors", WH["wh_frame"] + WH["doors"], GREY)], grab_site,
       "Step 20: reeve the line and hang the grab", "Drum, lead sheave, up leg A, head sheave, down to the grab's guide tube and shear link",
       context=ctx_tri, size=(9, 6.5), azim=-35)
    print("steps", n)


if __name__ == "__main__":
    what = sys.argv[1:] or ["overview", "sheets", "joints", "steps"]
    OUT.mkdir(parents=True, exist_ok=True)
    for w in what:
        globals()[w]()
