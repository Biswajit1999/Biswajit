from pathlib import Path
import shutil
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_site"

if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir()

for name in ("index.html", "styles.css", "app.js", "LICENSE", "README.md"):
    src = ROOT / name
    if src.exists():
        shutil.copy2(src, OUT / name)

# Apply the cool deep-observatory CSS after the base stylesheet.
base_css = (OUT / "styles.css").read_text(encoding="utf-8")
theme_css = (ROOT / "theme-observatory.css").read_text(encoding="utf-8")
(OUT / "styles.css").write_text(base_css + "\n\n/* Deep Observatory Theme */\n" + theme_css + "\n", encoding="utf-8")

# Keep the Three.js scene in the same palette as the interface.
app_path = OUT / "app.js"
app = app_path.read_text(encoding="utf-8")
replacements = {
    "scene.fog=new THREE.FogExp2(0x090706,.021);": "scene.fog=new THREE.FogExp2(0x050914,.021);",
    "const C={amber:0xe3a35a,rust:0xc66743,cyan:0x7fcad2,green:0x85bd8b,ivory:0xf3eadc,blue:0x78a7ff,dim:0x826f59};": "const C={amber:0x6f9bff,rust:0x9a7cff,cyan:0x2fd0c2,green:0x6fe3a1,ivory:0xeaf1ff,blue:0x8fb3ff,dim:0x46607f};",
    "g.addColorStop(0,'rgba(255,247,229,1)');g.addColorStop(.13,'rgba(255,205,139,.95)');g.addColorStop(.42,'rgba(227,142,70,.28)');": "g.addColorStop(0,'rgba(244,249,255,1)');g.addColorStop(.13,'rgba(169,197,255,.96)');g.addColorStop(.42,'rgba(111,155,255,.28)');",
    "const GRAPH_URL='https://raw.githubusercontent.com/Biswajit1999/Biswajit_Jana.github.io/main/data/research-graph.json';": "const GRAPH_URL='data/research-graph.json';",
}
for old, new in replacements.items():
    if old not in app:
        raise SystemExit(f"Expected app.js palette marker not found: {old[:70]}")
    app = app.replace(old, new)
app_path.write_text(app, encoding="utf-8")

# Mirror the current research graph into this deployment so the new site is self-contained.
data_dir = OUT / "data"
data_dir.mkdir(exist_ok=True)
graph_url = "https://raw.githubusercontent.com/Biswajit1999/Biswajit_Jana.github.io/main/data/research-graph.json"
try:
    urllib.request.urlretrieve(graph_url, data_dir / "research-graph.json")
    print("Mirrored research graph")
except Exception as exc:
    # app.js has a built-in fallback project set, so deployment remains usable.
    print(f"Research graph mirror unavailable: {exc}")

print("Built themed site in _site")
