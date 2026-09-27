# Biswajit Research Universe

An immersive, interactive evidence map for **Biswajit Jana** — astrophysics,
astronomical instrumentation, exoplanets, scientific computing, and precision-
control systems.

The visual layer is backed by a versioned portfolio graph: **182 nodes, 393
typed edges, and 85 project records**. The snapshot is checked into this
repository with source-commit provenance and a SHA-256 integrity check.

## Experience

- Three.js GPU particle field with section-specific topology morphing
- Scroll-driven camera choreography
- Interactive 3D research nodes and camera fly-to focus
- Floating labels anchored to scene objects
- Animated information paths through the research graph
- EXOhSPEC optical/instrumentation visualization
- Exoplanet research constellation and orbital scenes
- Scientific-software network view
- Mobile and reduced-motion fallbacks
- Semantic HTML content beneath the WebGL layer
- Evidence cards with estimands, sensitivity results, and interpretation limits
- Deterministic, network-independent graph deployment

## Research graph

The visual experience is backed by a curated portfolio knowledge graph
connecting projects, instruments, methods, planet classes, molecules, and
analysis types. See [EVIDENCE.md](EVIDENCE.md) for its scope and the scientific
interpretation boundary.

## Architecture

The site is intentionally static-host friendly: HTML, CSS, ES modules,
Three.js, and JSON data. `scripts/build_site.py` validates and copies a
self-contained deployment without downloading mutable portfolio data.

```bash
node --check app.js
node scripts/validate_site.mjs
python scripts/build_site.py
```

## Author

**Biswajit Jana**

Astrophysics · Astronomical Instrumentation · Scientific Computing
