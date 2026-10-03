"""SinkGrab concept media (TRL 3, constructable design SKG-DDR-002), generated from the parametric model.

Run from the repo root:  python cad/src/concept_media.py
Takes every component from cad/src/model.py at the well head and renders the media set with
.kit/concept.py: hero, exploded view with BOM callouts, concept blueprint (SKG-DWG-010), energy and
material flow per cycle, and the web model (model.glb with viewer.html, coarse tessellation).
Coloured parts carry the BOM line numbers of bom/bom.csv; grey parts (HatchSide tripod, well collar
and ground, spoil tub, person) are context only. Figures come from docs/04-calcs/sizing.py
(SKG-CAL-001). CONCEPT, NOT FOR FABRICATION.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
from build123d import Compound, Color, export_gltf  # noqa: E402
import matplotlib.colors as mc  # noqa: E402
from concept import Part, render_all, human_figure  # noqa: E402
from model import (PARAMS as P, derived, build_components, tripod_context, well_context,  # noqa: E402
                   barrow_context, bx)

C = build_components(P)
D = derived(P)

STYLE = {  # key: (colour, exploded offset in mm)
    "frame": ("#0F766E", (0, 0, 0)), "drum": ("#C2410C", (0, 0, 700)), "drum_bearings": ("#374151", (0, 0, 450)),
    "crank_bearings": ("#374151", (0, 0, 1250)), "crank_shaft": ("#6B7280", (0, 0, 1450)),
    "small_sprocket": ("#B45309", (-350, 0, 1450)), "shear_pin": ("#DC2626", (-350, 0, 1550)),
    "chain": ("#78716C", (-600, 0, 900)), "guard": ("#FACC15", (-900, 0, 900)), "cranks": ("#111827", (0, 0, 1700)),
    "pawl": ("#1D4ED8", (450, 0, 700)), "brake": ("#9333EA", (450, -300, 300)), "stakes": ("#57534E", (0, 0, 0)),
    "cradle": ("#0E7490", (0, 0, 0)), "lead_sheave": ("#D4A017", (0, 0, 350)), "lead_axle": ("#374151", (0, 0, 500)),
    "drawbar": ("#64748B", (0, 0, 250)), "draw_pins": ("#111827", (0, 0, 400)),
    "head": ("#2563EB", (0, 0, 650)), "ballast": ("#1E3A8A", (0, 0, 850)), "tie_rods": ("#475569", (0, 0, 420)),
    "shell_pins": ("#111827", (0, 0, 300)), "shell_a": ("#EA580C", (0, 250, 0)), "shell_b": ("#F59E0B", (0, -250, 0)),
    "crosshead": ("#15803D", (0, 0, 220)), "hinge_pin": ("#111827", (0, 0, 120)), "cross_sheave": ("#D4A017", (0, 0, 300)),
    "cross_axle": ("#374151", (0, 0, 360)), "shear_link": ("#DC2626", (0, 0, 520)), "link_pin": ("#DC2626", (0, 0, 560)),
    "scraper_pole": ("#0369A1", (0, 0, 0)), "arms": ("#E11D48", (0, 0, 300)), "arm_pins": ("#111827", (0, 0, 400)),
    "sleeve": ("#7C3AED", (0, 0, -300)), "sleeve_pins": ("#111827", (0, 0, -400)), "struts": ("#A16207", (0, 0, -150)),
    "pole_section": ("#0284C7", (0, 300, 0)), "tbar": ("#1E40AF", (0, 600, 0)),
    "wh_frame": ("#0F766E", (0, 0, 0)), "doors": ("#9CA3AF", (0, 0, 500)), "saddles": ("#57534E", (0, 0, 0)),
    "hs_sheave": ("#D4A017", (0, 0, 0)), "rope": ("#E11D48", (0, 0, 0)),
}
SHORT = {1: "Capstan frame", 2: "Winding drum", 3: "Pawl", 4: "Crank shaft, hub and cranks", 5: "Chain guard",
         6: "Band brake and lever", 7: "Ground stakes", 8: "Foot cradle", 9: "Drawbar", 10: "Grab head and ballast",
         11: "Tie rods", 12: "Grab shells", 13: "Crosshead and hinge pin", 14: "Shear link", 15: "Scraper head",
         16: "Pole section", 17: "T-bar", 18: "Well-head frame", 19: "Folding doors", 20: "Ballast saddles",
         21: "Drum bearings", 22: "Crank bearings", 23: "Roller chain", 24: "Crank shear pin", 25: "Sheaves",
         26: "Closing line"}
parts = []
for k, c in C.items():
    shape = c.shape
    if k == "stakes":                       # show only the parts above ground in the pictures
        shape = shape & bx(-3000, 3000, -9000, 9000, 0, 200)
    parts.append(Part(SHORT[c.bom], shape, STYLE[k][0], c.bom, STYLE[k][1]))

collar, ground = well_context(P, depth=0.0)
person = human_figure(1750.0, x=D["x_crank"][0][0] - 700.0, y=D["y_c"], z=0.0)
context = [Part("HatchSide tripod (shared block, not in this kit)", tripod_context(P), "#D1D5DB"),
           Part("Well collar (site)", collar, "#D6D3D1"),
           Part("Spoil tub (bought, line 32)", barrow_context(P), "#A8A29E"), person]

flow = {"title": "energy and material per bite at 10 m (SKG-CAL-001 estimates)", "unit": "kJ",
        "stages": [("Two people at the cranks", 11.1), ("Drum and line", 10.1), ("Full grab lifted 11 m", 10.1),
                   ("Sand into the tub", "21 L, 42 kg")],
        "losses": [(0, "Chain and bearings", 1.0), (1, "Lifting the grab itself", 5.2), (2, "Water in the shells", 0.3)]}

outs = render_all(
    parts, project="SinkGrab", title="Rope grab and under-curb scraper well-deepening kit", dwg_no="SKG-DWG-010",
    key_figures=["Bite 21 L (28 L closed shells); grab 48 kg, 93 kg full",
                 "One 8 mm line, 2:1 tackle; head weight opens the shells",
                 "Capstan 4:1, two 250 mm cranks: 52 N each at the rated load",
                 "Line limited to 1.2 to 1.5 kN by a shear link (tripod 150 kg)",
                 "Scraper toes 15 mm past the ring; arms fold to 364 mm radius",
                 "Cycle 3.7 min at 10 m (target 3 min); parts USD 2,506"],
    scale_figure=False, context=context, cut=False, web_model=False, flow=flow)

# Web model at a coarse tessellation (a few MB), with the kit's viewer page
md = ROOT / "media"
kids = []
for p in parts:
    sh = p.shape
    sh.color = Color(*mc.to_rgb(p.color))
    sh.label = p.name
    kids.append(sh)
export_gltf(Compound(kids), str(md / "model.glb"), binary=True, linear_deflection=1.0, angular_deflection=0.35)
(md / "viewer.html").write_text("""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>SinkGrab: rope grab and under-curb scraper concept</title>
<script type="module" src="https://cdn.jsdelivr.net/npm/@google/model-viewer@3/dist/model-viewer.min.js"></script>
<style>body{margin:0;font-family:system-ui,sans-serif;background:#F9FAFB}model-viewer{width:100vw;height:100vh}
.tag{position:fixed;left:12px;top:10px;font-size:12px;color:#B45309;letter-spacing:.06em}</style></head>
<body><div class="tag">CONCEPT, NOT FOR FABRICATION</div>
<model-viewer src="model.glb" poster="hero.png" alt="SinkGrab: rope grab and under-curb scraper concept" camera-controls auto-rotate shadow-intensity="0.6"
  exposure="1.0" camera-orbit="-35deg 70deg auto" interaction-prompt="auto"></model-viewer></body></html>
""")
print({k: str(v) for k, v in outs.items()}, "model.glb", round((md / "model.glb").stat().st_size / 1e6, 2), "MB")
