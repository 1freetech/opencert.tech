# Open CERT Electrical Curriculum

Offline electrical lessons are organized by role. **Tier is archive metadata, not part of the lesson title.**

## Technician — Tier 1

Technician lessons emphasize field skills, measurement, equipment, safety, operation, maintenance, and troubleshooting.

### Shared foundations
1. [Article 0 — Program Foundation](shared/article-00-program-foundation.md)
2. [Article 1 — Codes, Standards, Laws, and Jurisdictions](shared/article-01-codes-standards-laws-jurisdictions.md)
3. [Article 2 — Voltage, Current, Resistance, and Power](shared/article-02-voltage-current-resistance-power.md)
4. [Article 3 — Series and Parallel Circuits](shared/article-03-series-parallel-circuits.md)

### Technician lessons
- [Electrical Engineering Tech Doc #1 – Digital Multimeter Basics](technician/digital-multimeter-basics.md)
- [OSET.001: Real, Reactive, and Apparent Power](technician/oset-001-real-reactive-apparent-power.md)

## Engineer — Tier 2

Use `OSEEC.004: Lesson Title` naming for the Open-Source Electrical Engineer Certification, with sequential three-digit lesson numbers. Technician lessons use OSETC and keep their separate sequence.

Engineer study inherits the shared electrical foundations above. Engineer-specific lessons build beyond those prerequisites into analysis, design, power systems, protection, distribution, three-phase systems, transformers, controls, and electronics.

### Required shared prerequisites
1. Article 0 — Program Foundation
2. Article 1 — Codes, Standards, Laws, and Jurisdictions
3. Article 2 — Voltage, Current, Resistance, and Power
4. Article 3 — Series and Parallel Circuits

Engineer-specific lessons are stored under `engineer/` as they are classified or created.

- [OSEEC.004: Kirchhoff’s Laws: KVL and KCL](engineer/oseec-004-kirchhoffs-laws-kvl-kcl.md) — published September 30, 2026. The next engineer lesson is OSEEC.005; verify live numbering before publishing.

Rotation: Networking → Python → Linux → Windows → Electrical Engineering → OSETC → C++ → Networking. OSETC is next after OSEEC.004.

## Archive rules

- Public lesson titles are preserved; tier labels are not added to titles.
- `tier: 1` = Technician.
- `tier: 2` = Engineer.
- Shared prerequisites live once under `shared/` and are referenced by both pathways.
- Complete published lesson content is retained for offline study.
- New electrical lessons must be assigned to Technician, Engineer, or Shared before the archive is considered organized.
