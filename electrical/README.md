# Open CERT Electrical Curriculum

Offline electrical lessons are organized by role. **Tier is archive metadata, not part of the lesson title.**

## Technician — Tier 1

Technician lessons emphasize field skills, measurement, equipment, safety, operation, maintenance, and troubleshooting.

### Shared foundations
1. [OSEEC.000 — Program Foundation](shared/article-00-program-foundation.md)
2. [OSEEC.001 — Codes, Standards, Laws, and Jurisdictions](shared/article-01-codes-standards-laws-jurisdictions.md)
3. [OSEEC.002 — Voltage, Current, Resistance, and Power](shared/article-02-voltage-current-resistance-power.md)
4. [OSEEC.003 — Series and Parallel Circuits](shared/article-03-series-parallel-circuits.md)

### Technician lessons
- [Electrical Engineering Tech Doc #1 – Digital Multimeter Basics](technician/digital-multimeter-basics.md)
- [OSET.001: Real, Reactive, and Apparent Power](technician/oset-001-real-reactive-apparent-power.md)

- [OSETC.011: Lockout/Tagout and Energy Isolation](../lessons/electrical/OSETC/OSETC.011-lockout-tagout-energy-isolation.md) — published September 30, 2026.
- [OSETC.012: Grounding and Bonding Basics](../lessons/electrical/OSETC/OSETC.012-grounding-bonding-basics.md) — published October 1, 2026.
- [OSETC.013: Ground-Fault Circuit Interrupters (GFCIs)](../lessons/electrical/OSETC/OSETC.013-ground-fault-circuit-interrupters.md) — published October 1, 2026.

## Engineer — Tier 2

Use `OSEEC.004: Lesson Title` naming for the Open-Source Electrical Engineer Certification, with sequential three-digit lesson numbers. Technician lessons use OSETC and keep their separate sequence.

Engineer study inherits the shared electrical foundations above. Engineer-specific lessons build beyond those prerequisites into analysis, design, power systems, protection, distribution, three-phase systems, transformers, controls, and electronics.

### Required shared prerequisites
1. OSEEC.000 — Program Foundation
2. OSEEC.001 — Codes, Standards, Laws, and Jurisdictions
3. OSEEC.002 — Voltage, Current, Resistance, and Power
4. OSEEC.003 — Series and Parallel Circuits

Engineer-specific lessons are stored under `engineer/` as they are classified or created.

- [OSEEC.004: Kirchhoff’s Laws: KVL and KCL](engineer/oseec-004-kirchhoffs-laws-kvl-kcl.md) — published September 30, 2026. [OSEEC.005: AC Fundamentals](engineer/oseec-005-ac-fundamentals.md) was published October 1, 2026. OSEEC.006: Capacitance, Inductance, and Reactance is a draft; verify its content before the next engineer publication.

Rotation: Networking → Python → Linux → Windows → Electrical Engineering → OSETC → C++ → Networking. OSETC.011: Lockout/Tagout and Energy Isolation was published September 30, 2026. OSC++.011: Range-Based For Loops was published September 30, 2026. OSNTC.004: VLAN Basics was published September 30, 2026. OSPython.009: Virtual Environments was published October 1, 2026. Linux Command #31 – stat (Linux OS) was published October 1, 2026. Windows Command #19 – arp (Windows OS) was published October 1, 2026. OSEEC.005: AC Fundamentals was published October 1, 2026. OSETC.012: Grounding and Bonding Basics was published October 1, 2026. OSETC.013: Ground-Fault Circuit Interrupters (GFCIs) was published October 1, 2026. C++ is next in the rotation.

## Archive rules

- Public lesson titles are preserved; tier labels are not added to titles.
- `tier: 1` = Technician.
- `tier: 2` = Engineer.
- Shared prerequisites live once under `shared/` and are referenced by both pathways.
- Complete published lesson content is retained for offline study.
- New electrical lessons must be assigned to Technician, Engineer, or Shared before the archive is considered organized.

OSEEC titles use three-digit numbering throughout: OSEEC.000–OSEEC.005 are published. Published, scheduled, and draft engineer article titles and existing archive title metadata/headings were standardized September 30, 2026. Existing URLs, archive paths, and cover artwork are retained.
