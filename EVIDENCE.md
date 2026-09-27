# Evidence and interpretation boundary

This repository is an interactive navigation layer over a research-software
portfolio. It is not a paper, a citation index, or evidence that every linked
project has passed peer review.

## Versioned graph

The deployed graph is a checked-in snapshot containing 182 nodes and 393 typed
edges, including 85 project records. Its exact source commit and SHA-256 digest
are recorded in `data/provenance.json`. The build fails if the graph digest or
declared counts change without a deliberate provenance update.

Graph edges encode curated portfolio relationships such as “uses instrument”
or “uses method.” They support discovery and navigation; they do not establish
causation, priority, correctness, or publication status.

## Quantitative records shown on the site

- **HD 189733 b:** the linked notebook reports a 2.266% median depth across 11
  locally normalized TESS transit events and a 2.247–2.307% central 68%
  event-bootstrap interval. It is an ephemeris-conditioned, one-sector,
  first-order estimate—not an independent discovery or full physical fit.
- **Radial-velocity recovery:** 35/100 recovery at K = 1.5 m/s and 100/100 from
  K = 3 m/s under one declared synthetic cadence, signal family, search grid,
  noise model, and joint decision rule. It is not survey completeness.
- **21-cm candidates:** 290 of 356 baseline local maxima persist across all 12
  declared detector settings in 73 stored LAB sightlines. They are descriptive
  spectral candidates, not a cloud or spiral-arm catalogue.
- **Doppler-information experiment:** 15 controlled synthetic scenarios test
  resolving power against intrinsic line width under fixed photon
  normalization. The resulting local bounds are not commissioned instrument
  performance.

For each result, the linked repository is the authoritative location for
methods, generated artifacts, tests, and limitations.

## EXOhSPEC wording

EXOhSPEC is described here as an instrumentation design and control programme.
The interface does not present unlinked stability figures or design goals as
measured on-sky or commissioned performance.
