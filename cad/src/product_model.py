"""SinkGrab product appearance model for photoreal renders (STANDARDS sections 12 and 24), TRL 3, kit 1.9.1.

Every product part is components(CHOSEN) from cad/src/model.py as it is: the hand capstan with every bolt and
weld, the foot cradle and drawbar, the well-head frame and doors, the grab hanging at the dump position over
the spoil tub, the scraper and one pole section laid on the ground, four of the eight ballast saddles, the
closing line and the head sheave. Only the site is added, as context parts: the HatchSide tripod (a shared
block, in grey), the concrete well collar and lining reaching 0.6 m below ground, a soil spoil heap and a
1.75 m mannequin standing at the -X crank. Ground level is model z = 0 (photoreal --ground-z=0); the stakes and
the collar reach below it.

Views (RENDER_VIEWS): "hero", the kit at a village well on packed soil in late-morning sun, seen from the front
right; "studio", the same kit on a plain studio floor; "grab", the clamshell grab on its own in the studio.
Site structure parts end in "(site)" and are left out of camera framing; the figure ends in "(scale)".
APPEARANCE MODEL ONLY. CONCEPT, NOT FOR FABRICATION.

    from product_model import product_parts
    for p in product_parts(): print(p["name"], p["group"], p["material"])
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / ".kit")]

from build123d import Pos, Rot  # noqa: E402
import model as M  # noqa: E402
from cad_parts import part, break_edges  # noqa: E402

TITLE = "SinkGrab: rope grab and under-curb scraper that deepen village wells under water"

_SITE = ["--scene=outdoor", "--ground=soil", "--ground-z=0", "--sun=48,-20", "--lens=40"]
RENDER_VIEWS = [
    {"name": "hero", "groups": ["shell", "context"], "explode": False, "el": 16, "az": -35, "args": _SITE,
     "note": "Site render at a village well on packed soil, late-morning sun from behind the camera's right shoulder, seen "
             "from the front right and a little above (about 16 deg elevation): hand capstan with a 1.75 m person at the -X "
             "crank, drawbar to the cradle under the HatchSide leg A foot, well-head frame with closed doors, the grab "
             "hanging over the spoil tub, the scraper and saddles on the ground; HatchSide tripod in grey"},
    {"name": "studio", "groups": ["shell"], "explode": False, "el": 24, "az": -40,
     "note": "Studio render of the whole kit from the front right and above (about 24 deg elevation), no site"},
    {"name": "grab", "groups": ["grab"], "explode": False, "el": 18, "az": -30,
     "note": "Studio render of the clamshell grab on its own from the front right (about 18 deg elevation): head with "
             "ballast plates and upper sheave, tie rods, crosshead with set collars and load indicator, two shells"},
]


def site():
    """Site context at a village well: the HatchSide tripod, the collar and lining reaching below ground, a spoil
    heap and a mannequin at the -X crank. Ground level is z = 0."""
    P = M.PARAMS
    D = M.derived(P)
    out = []
    ctx = lambda n, sh, mat: out.append(part(n, sh, mat, kind="context", group="context"))  # noqa: E731
    ctx("HatchSide tripod, shared block (context)", M.tripod_context(P), "aluminium")
    import math
    fa, fl, fh = P["hs_foot"]
    for az in P["hs_leg_az"][1:]:          # legs B and C stand on bearers in the soil; leg A stands in the cradle
        pad = Rot(0, 0, az + 90) * Pos(0, -P["hs_r_foot"], 0) * M.bx(-fa / 2 - 20, fa / 2 + 20, -fl / 2 - 20, fl / 2 + 20, -40.0, 10.0)
        ctx(f"HatchSide foot bearer at {az:.0f} deg (site)", break_edges(pad, 3.0), "hardwood")
    collar, _ground = M.well_context(P, depth=600.0)
    ctx("Well collar and lining (site)", break_edges(collar, 6.0), "concrete")
    heap = Pos(-2300.0, 1500.0, -150.0) * Rot(0, 0, 25) * M.bx(-600, 600, -450, 450, 0, 380)
    ctx("Spoil heap of wet sand (site)", break_edges(heap, 120.0), "sand")
    try:
        from context_parts import mannequin
        xc = D["x_crank"][0][0] - P["handle"][1] - 520.0
        man = Pos(xc, D["y_c"], 0) * Rot(0, 0, 90) * mannequin(1750, "stand", shoulder_flex_r=55, elbow_flex_r=40)
        out.append(part("Person 1.75 m at the crank (scale)", man, "skin", kind="context", group="context"))
    except Exception as e:   # the mannequin is for scale only; never block the product parts
        print("mannequin not added:", e)
    return out


def product_parts():
    import skg_detail as SD
    parts = []
    for p in M.components(M.CHOSEN):
        if p["kind"] == "context":
            continue
        q = dict(p)
        q["group"] = "shell"
        parts.append(q)
    for p in SD.grab(M.PARAMS):
        q = dict(p)
        q["group"] = "grab"
        parts.append(q)
    return parts + site()


if __name__ == "__main__":
    ps = product_parts()
    print(len(ps), "parts;", sum(p["group"] == "shell" for p in ps), "shell,", sum(p["group"] == "grab" for p in ps), "grab,",
          sum(p["group"] == "context" for p in ps), "context")
