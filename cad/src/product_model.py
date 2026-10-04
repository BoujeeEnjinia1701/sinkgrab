"""SinkGrab product appearance model (build123d), TRL 3, constructable design (SKG-DDR-002).

For photoreal renders only (.kit/export_views.py, then .kit/photoreal.py on Amish's Mac). Every
part is the model.py solid itself; colours and materials are added for the look. Three scenes:
    hero      the kit at the well head (group "shell"), the HatchSide tripod, collar, spoil tub and a
              posed 1.75 m mannequin at the capstan crank as context
    exploded  the clamshell grab on its own, pulled apart (group "grab")
    detail    the under-curb scraper head with its arms open under the cutting edge of a cut-away
              bottom caisson ring, and a ballast saddle on a cut-away top ring (group "detail")
Appearance additions not in model.py, recorded in docs/REVIEW.md: the wound rope on the drum
(two layers), the context collar, ground disc, tub, ring pieces and mannequin. CONCEPT, NOT FOR
FABRICATION.

    from product_model import product_parts
    for p in product_parts(): print(p["name"], p["group"], p["material"])
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
from build123d import Pos, Rot  # noqa: E402
from model import (PARAMS as P, derived, build_components, grab_parts, scraper_parts, saddle_part,  # noqa: E402
                   tripod_context, well_context, barrow_context, annulus_z, bx)

TITLE = "SinkGrab: rope grab and under-curb scraper that deepen village wells under water"

RENDER_VIEWS = [
    {"name": "hero", "groups": ["shell", "context"], "explode": False, "el": 20, "az": -35,
     "note": "Product render from the front right and above (about 20 deg elevation). Hand capstan with a person at "
             "the crank, drawbar to the cradle under the tripod foot, well-head frame with closed doors, grab over "
             "the spoil tub; HatchSide tripod in grey"},
    {"name": "exploded", "groups": ["grab"], "explode": True, "el": 22, "az": -40,
     "note": "Exploded clamshell grab from the front right and above (about 22 deg elevation): head with ballast "
             "plates and head sheave, tie rods, crosshead with sheave, hinge pin and shear link, two shells"},
    {"name": "detail", "groups": ["detail"], "explode": False, "el": 15, "az": -60,
     "note": "Detail from the front right, slightly above (about 15 deg elevation): scraper arms open under the "
             "cutting edge of a cut-away bottom ring; ballast saddle astride a cut-away top ring"},
]

LOOK = {  # key: (colour, material)
    "frame": ("#0F766E", "painted steel"), "drum": ("#C2410C", "painted steel"), "drum_bearings": ("#374151", "cast iron"),
    "crank_bearings": ("#374151", "cast iron"), "crank_shaft": ("#9CA3AF", "bright steel"), "small_sprocket": ("#6B7280", "steel"),
    "shear_pin": ("#DC2626", "steel"), "chain": ("#4B5563", "steel"), "guard": ("#FACC15", "painted steel"),
    "cranks": ("#111827", "painted steel"), "pawl": ("#1D4ED8", "painted steel"), "brake": ("#7E22CE", "painted steel"),
    "stakes": ("#57534E", "steel"), "cradle": ("#0E7490", "painted steel"), "lead_sheave": ("#D4A017", "zinc plated steel"),
    "lead_axle": ("#9CA3AF", "steel"), "drawbar": ("#64748B", "painted steel"), "draw_pins": ("#9CA3AF", "zinc plated steel"),
    "head": ("#2563EB", "painted steel"), "ballast": ("#1E3A8A", "painted steel"), "tie_rods": ("#475569", "painted steel"),
    "shell_pins": ("#9CA3AF", "zinc plated steel"), "shell_a": ("#EA580C", "painted steel"), "shell_b": ("#F59E0B", "painted steel"),
    "crosshead": ("#15803D", "painted steel"), "hinge_pin": ("#9CA3AF", "bright steel"), "cross_sheave": ("#D4A017", "zinc plated steel"),
    "cross_axle": ("#9CA3AF", "steel"), "upper_sheave": ("#D4A017", "zinc plated steel"), "upper_axle": ("#9CA3AF", "steel"), "shear_link": ("#DC2626", "painted steel"), "link_pin": ("#B91C1C", "steel"),
    "scraper_pole": ("#0369A1", "painted steel"), "arms": ("#E11D48", "painted steel"), "arm_pins": ("#9CA3AF", "steel"),
    "sleeve": ("#7C3AED", "painted steel"), "sleeve_pins": ("#9CA3AF", "steel"), "struts": ("#A16207", "painted steel"),
    "pole_section": ("#0284C7", "painted steel"), "tbar": ("#1E40AF", "painted steel"), "wh_frame": ("#0F766E", "galvanised steel"),
    "doors": ("#9CA3AF", "galvanised steel"), "saddles": ("#57534E", "steel"), "hs_sheave": ("#D4A017", "zinc plated steel"),
    "rope": ("#E11D48", "polyester rope"),
}
EXPLODE = {"head": (0, 0, 520), "ballast": (0, 0, 640), "shear_link": (0, 0, 380), "link_pin": (0, 0, 380),
           "tie_rods": (0, 0, 260), "shell_pins": (0, 0, 180), "shell_a": (260, 0, -60), "shell_b": (-260, 0, -60),
           "crosshead": (0, 0, 140), "cross_sheave": (0, 0, 200), "cross_axle": (0, 0, 200), "hinge_pin": (0, 420, 0),
           "upper_sheave": (0, -220, 520), "upper_axle": (0, -300, 520)}


def product_parts(P=P):
    D = derived(P)
    out = []

    def add(name, shape, color, material, bom, group, explode=(0, 0, 0)):
        out.append({"name": name, "shape": shape, "color": color, "material": material,
                    "bom": bom, "group": group, "explode": tuple(float(v) for v in explode)})

    # hero: the kit at the well head
    C = build_components(P)
    for k, c in C.items():
        col, mat = LOOK[k]
        shape = c.shape
        if k == "stakes":
            shape = shape & bx(-3000, 3000, -9000, 9000, 0, 200)
        add(c.name, shape, col, mat, c.bom, "shell")
    collar, ground = well_context(P, depth=0.0)
    add("HatchSide tripod (shared block)", tripod_context(P), "#C4C9D0", "anodised aluminium", None, "context")
    add("Well collar (site)", collar, "#D6D3D1", "concrete", None, "context")
    add("Ground (site)", ground, "#B8A98E", "packed earth", None, "context")
    add("Spoil tub (bought)", barrow_context(P), "#78716C", "galvanised steel", 32, "context")
    from context_parts import mannequin
    xc = D["x_crank"][0][0] - P["handle"][1] - 520.0
    person = Pos(xc, D["y_c"], 0) * Rot(0, 0, 90) * mannequin(1750, "stand", shoulder_flex_r=55, elbow_flex_r=40)
    add("Person, 1.75 m (scale)", person, "#D1D5DB", "clay", None, "context")
    # exploded: the grab on its own
    for k, v in grab_parts(P).items():
        col, mat = LOOK[k]
        add(C[k].name, Pos(0, 0, 0) * v, col, mat, C[k].bom, "grab", EXPLODE.get(k, (0, 0, 0)))
    # detail: scraper head open under a cut-away bottom ring; saddle on a cut-away top ring
    ri, wall, hr = P["ring"][0] / 2, P["ring"][1], P["ring"][2]
    cut = bx(-2000, 2000, 0, 2000, -2000, 4000)            # keep the back half (+Y) of the rings
    for k, v in scraper_parts(P).items():
        if k in ("pole_section", "tbar"):
            continue
        col, mat = LOOK[k]
        add(C[k].name, v, col, mat, C[k].bom, "detail")
    ring_bot = annulus_z(ri, ri + wall, 20.0, 20.0 + hr) & cut
    add("Bottom caisson ring (site, cut away)", ring_bot, "#A8A29E", "concrete", None, "detail")
    zt = 20.0 + 2 * hr
    ring_top = annulus_z(ri, ri + wall, 20.0 + hr, zt) & cut
    add("Top caisson ring (site, cut away)", ring_top, "#B5AFA8", "concrete", None, "detail")
    sad = Pos(0, ri + wall / 2, zt) * Rot(0, 0, 90) * saddle_part(P)
    add("Ballast saddle", sad, LOOK["saddles"][0], "steel", 20, "detail")
    return out


if __name__ == "__main__":
    for p in product_parts():
        s = p["shape"]
        print(f"{p['name']:52s} {p['group']:8s} {p['material']:18s} vol={s.volume / 1000:9.1f} cm3")
