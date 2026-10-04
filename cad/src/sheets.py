"""SinkGrab drawing sheets: SKG-DWG-001 Rev P3, SKG-DWG-002 Rev P4 (TRL 3, constructable design SKG-DDR-002).

Run from the repo root:  python cad/src/sheets.py
Writes cad/drawings/SKG-DWG-001 (well-head layout: capstan, lead cradle, drawbar, well-head frame
and doors, grab at the dump position) and SKG-DWG-002 (clamshell grab and under-curb scraper) as
SVG, PDF and PNG from cad/src/model.py with .kit/drawing.py. Overall sizes are dimensioned by the
kit; main dimensions and interfaces are listed in the notes from PARAMS and derived(). The concept
blueprint in media/ is SKG-DWG-010; the making sketches for the build plan are SKG-DWG-101 onward.
"""
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
from build123d import Compound, Pos  # noqa: E402
from drawing import Sheet  # noqa: E402
from model import PARAMS as P, derived, build_components, grab_parts, scraper_parts  # noqa: E402

DATE = "2026-10-03"
REVS = [("P1", "Preliminary GA for TRL 3 (from cad/src/model.py)", DATE, "AC"),
        ("P2", "SKG-DDR-002: design for construction", DATE, "AC"),
        ("P3", "SKG-DDR-003: 3:1 tackle, long crank handle, toe blades", DATE, "AC")]
REVS_002 = REVS + [("P4", "SKG-DDR-004: slotted scraper sleeve and cross pin", "2026-10-04", "AC")]


def safe_project_views(part, workdir, line_weight=0.35):
    """Front, top, right and iso views, edge by edge, so a degenerate edge is skipped."""
    from build123d import ExportSVG, LineType, Unit
    workdir = Path(workdir)
    workdir.mkdir(parents=True, exist_ok=True)
    bb = part.bounding_box()
    c = bb.center()
    d = max(bb.size.X, bb.size.Y, bb.size.Z) * 10
    setups = {"front": ((c.X, c.Y - d, c.Z), (0, 0, 1)), "top": ((c.X, c.Y, c.Z + d), (0, 1, 0)),
              "right": ((c.X + d, c.Y, c.Z), (0, 0, 1)), "iso": ((c.X + d, c.Y - d, c.Z + d * 0.8), (0, 0, 1))}
    out = {}
    for name, (origin, up) in setups.items():
        visible, hidden = part.project_to_viewport(origin, up, (c.X, c.Y, c.Z))
        ex = ExportSVG(unit=Unit.MM, line_weight=line_weight)
        ex.add_layer("Visible", line_color=0x111827)
        ex.add_layer("Hidden", line_color=0x6B7280, line_type=LineType.ISO_DASH, line_weight=line_weight / 2)
        for layer, edges in (("Visible", visible), ("Hidden", hidden if name != "iso" else [])):
            for e in edges:
                try:
                    ex.add_shape(e, layer=layer)
                except (AssertionError, ValueError, ZeroDivisionError):
                    pass
        p = workdir / f"{name}.svg"
        ex.write(str(p))
        out[name] = p
    return out


def layout_sheet():
    C = build_components(P)
    D = derived(P)
    keys = ["frame", "drum", "drum_bearings", "crank_bearings", "crank_shaft", "small_sprocket", "chain", "guard",
            "cranks", "pawl", "brake", "cradle", "lead_sheave", "lead_axle", "drawbar", "draw_pins", "wh_frame", "doors",
            "head", "ballast", "tie_rods", "shell_a", "shell_b", "crosshead", "cross_sheave", "rope", "hs_sheave"]
    work = ROOT / "cad" / "drawings" / "_views1"
    views = safe_project_views(Compound([C[k].shape for k in keys]), work, line_weight=0.25)
    s = Sheet(project="SinkGrab", title="Rope grab well-deepening kit: well-head layout", dwg_no="SKG-DWG-001", rev="P3",
              author="Amish Chadha", date=DATE, scale=1 / 60, theme="technical",
              material="Layout only; parts per SKG-DWG-002 and SKG-DWG-101 to 117. HatchSide tripod not shown. PRELIMINARY, NOT FOR FABRICATION",
              revisions=REVS)
    s.add_ortho(views)
    s.add_svg(views["iso"], 276, 32, 140, 92, label="Isometric view", sublabel="Not to scale; tripod not shown")
    s.add_notes("Main dimensions and interfaces (mm)", [
        f"Well axis at x = y = 0; collar top {P['collar_h']:.0f} above ground; lining ID {P['lining'][0]:.0f}",
        f"Lead sheave at the HatchSide leg A foot: centre {abs(P['lead_y']):.0f} out, {P['lead_z']:.0f} up",
        f"Drum axis {P['cap_gap']:,.0f} beyond the lead sheave, {P['hd']:.0f} up; fleet {D['fleet_deg']:.1f} deg",
        f"Drawbar 48.3 x 3.2, pins {abs((D['y_d'] + P['rail_half'] + 40) - (P['lead_y'] - 160)):,.0f} apart, {P['draw_z']:.0f} up",
        f"Line 8 mm: drum underwound, horizontal at {D['rope_z_low']:.0f}, up leg A at {D['up_angle']:.0f} deg",
        "Head sheave 150 OD for 8 mm rope in the HatchSide cheeks; line drops on the well axis",
        f"Well-head frame: 50 x 50 x 5 angle, opening {P['wh_frame'][0]:.0f} square, on the collar",
        "Doors 1,364 x 680, hinged at y = +/- 695; 64 mm pole hole when closed",
        f"Grab shown closed at the dump position, hinge {D['grab_hinge_site']:,.0f} up",
        "Capstan: 4:1 chain, 3 mm shear pin, pawl, weighted band brake; +X handle 240 for two",
        "Third-angle; front view from -Y",
    ], x=276, y=135, width=146)
    out = s.save(ROOT / "cad" / "drawings" / "SKG-DWG-001")
    shutil.rmtree(work, ignore_errors=True)
    print("wrote", out)


def tools_sheet():
    D = derived(P)
    G = grab_parts(P)
    S = scraper_parts(P)
    grab = Compound(list(G.values()))
    scr = Compound([v for k, v in S.items() if k not in ("pole_section", "tbar")])
    both = Compound([Pos(-900, 0, 0) * grab, Pos(500, 0, 300) * scr])
    work = ROOT / "cad" / "drawings" / "_views2"
    views = safe_project_views(both, work, line_weight=0.3)
    s = Sheet(project="SinkGrab", title="Clamshell grab and under-curb scraper: general arrangement", dwg_no="SKG-DWG-002", rev="P4",
              author="Amish Chadha", date="2026-10-04", scale=1 / 20, theme="technical",
              material="Steel plate and section, wear-resistant lips and toes; bought sheave and pins per bom/bom.csv. PRELIMINARY, NOT FOR FABRICATION",
              revisions=REVS_002)
    s.add_ortho(views)
    s.add_svg(views["iso"], 276, 40, 140, 84, label="Isometric view", sublabel="Not to scale; grab left (closed), scraper head right (arms open)")
    s.add_notes("Main dimensions and interfaces (mm)", [
        f"Grab shells R {P['shell_R']:.0f} x {P['shell_B']:.0f} wide; closed span {2 * (P['shell_R'] + P['shell_t']):.0f}; 28.3 L",
        f"Hinge pin {P['hinge_pin']:.0f}; tie rods 30 x 10 at {P['rod_len']:.0f} centres; head pins at x +/- {P['head_pin_x']:.0f}",
        f"Head to crosshead stroke {D['stroke']:.0f}; open {P['open_deg']:.0f} deg, lips {D['lip_span_open']:.0f} apart",
        "Line: guide tube, crosshead sheave, upper sheave, shear link on crosshead (3:1)",
        "Shear link pin about 1.9 mm, releases 1.20 to 1.47 kN (break-tested)",
        f"Toe blades at {P['toe_r']:.0f} radius, {P['toe_r'] - P['ring'][0] / 2 - P['ring'][1]:.0f} beyond a 1.0 m ring's outer face",
        f"Arms fold to {D['fold_toe_r']:.0f} radius: sleeve slides {D['sleeve_travel']:.0f} on a 12 cross pin",
        f"Sleeve 54 x {P['sleeve_len']:.0f}, slot 13 x {P['slot'][1]:.0f} each side; no stop collar",
        f"Centralizer skids at {P['cent_r']:.0f} radius, {P['cent_z']:.0f} above the toes",
        f"Foot plate {P['foot_d']:.0f} dia; sump {P['sump']:.0f} below the toe line",
        "Pole 42.4 x 2.6 in 2 m sections, 36 spigot and M12 cross bolt",
        "Third-angle; front view from -Y",
    ], x=276, y=135, width=146)
    out = s.save(ROOT / "cad" / "drawings" / "SKG-DWG-002")
    shutil.rmtree(work, ignore_errors=True)
    print("wrote", out)


if __name__ == "__main__":
    what = sys.argv[1:] or ["layout", "tools"]
    if "layout" in what:
        layout_sheet()
    if "tools" in what:
        tools_sheet()
