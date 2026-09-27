from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_site"
GRAPH = ROOT / "data" / "research-graph.json"
EXPECTED_GRAPH_SHA256 = (
    "fed48ff1f7ad78a346c805492f17b7dd74f57ba3268a8bee2aae94c6f751ce0d"
)


def sha256(path: Path) -> str:
    canonical_bytes = path.read_bytes().replace(b"\r\n", b"\n")
    return hashlib.sha256(canonical_bytes).hexdigest()


graph = json.loads(GRAPH.read_text(encoding="utf-8"))
actual_hash = sha256(GRAPH)
if actual_hash != EXPECTED_GRAPH_SHA256:
    raise SystemExit(
        "Pinned graph checksum changed; update provenance and validation deliberately."
    )
if len(graph.get("nodes", [])) != 182 or len(graph.get("edges", [])) != 393:
    raise SystemExit("Pinned graph does not match the declared 182-node/393-edge snapshot.")
if sum(node.get("type") == "Project" for node in graph["nodes"]) != 85:
    raise SystemExit("Pinned graph does not contain the declared 85 project records.")

if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir()

for name in (
    "index.html",
    "styles.css",
    "theme-observatory.css",
    "app.js",
    "LICENSE",
    "README.md",
    "EVIDENCE.md",
):
    shutil.copy2(ROOT / name, OUT / name)

shutil.copytree(ROOT / "data", OUT / "data")
print(
    "Built self-contained site with "
    f"{len(graph['nodes'])} nodes, {len(graph['edges'])} edges, "
    f"SHA-256 {actual_hash}."
)
