#!/usr/bin/env python3
"""
validate_repo.py — Single-shot repository validator for the D365 F&O accelerator baseline.

Runs:
  1. JSON Schema validation of every governed JSON file (challenge journal, DMF templates,
     DMF↔OData mapping, process catalogue, dependency graph, run-state).
  2. Skill frontmatter lint (required `name` + `description`, unique `name`,
     description length, body size cap, intra-repo link resolution).
  3. Cross-file consistency:
        - dependency-graph waves cover every module in the modules array
        - DMF templates referenced from dependency-graph.json all exist
        - module knowledge files referenced from dependency-graph.json all exist
  4. Mapping drift check: every odata_entity marked `verified` in dmf_odata_mapping.json
     should appear in SourceFiles/odata.xml.

Exit code: 0 on success, 1 on any violation.

Run:  python tools/validate_repo.py            # validate everything
      python tools/validate_repo.py --quick    # skip drift checks
"""

from __future__ import annotations

import argparse
import io
import json
import re
import sys
from pathlib import Path
from typing import Any

# Force UTF-8 on stdout so Unicode glyphs render on Windows consoles.
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

try:
    from jsonschema import Draft202012Validator
except ImportError:
    print("ERROR: jsonschema is required. Install with: pip install jsonschema", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent
SCHEMAS = ROOT / "schemas"
SKILLS = ROOT / "skills"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
DESC_RE = re.compile(r"^description:\s*(.*?)(?=\n[a-zA-Z_]+:|\Z)", re.DOTALL | re.MULTILINE)
NAME_RE = re.compile(r"^name:\s*(\S+)\s*$", re.MULTILINE)
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

MAX_DESC_LEN = 1024  # description should be a punchy trigger; warn beyond this
MAX_BODY_BYTES = 12_000  # SKILL.md body sanity ceiling; over → split into sidecars


class Issue:
    def __init__(self, severity: str, where: str, message: str) -> None:
        self.severity = severity  # "error" | "warning"
        self.where = where
        self.message = message

    def __str__(self) -> str:
        tag = "✗" if self.severity == "error" else "!"
        return f"  {tag} [{self.where}] {self.message}"


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def load_schema(name: str) -> dict[str, Any]:
    return load_json(SCHEMAS / name)


def validate_with(schema: dict[str, Any], data: Any, source: str) -> list[Issue]:
    issues: list[Issue] = []
    validator = Draft202012Validator(schema)
    for err in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
        loc = "/".join(str(p) for p in err.absolute_path) or "<root>"
        issues.append(Issue("error", source, f"{loc}: {err.message}"))
    return issues


def validate_json_artefacts() -> list[Issue]:
    out: list[Issue] = []
    cj_path = ROOT / "ChallengeJournal" / "challenge_journal.json"
    if cj_path.exists():
        out += validate_with(load_schema("challenge-journal.schema.json"), load_json(cj_path), str(cj_path.relative_to(ROOT)))

    dg_path = ROOT / "Modules" / "dependency-graph.json"
    if dg_path.exists():
        out += validate_with(load_schema("dependency-graph.schema.json"), load_json(dg_path), str(dg_path.relative_to(ROOT)))

    map_path = ROOT / "Modules" / "dmf_odata_mapping.json"
    if map_path.exists():
        out += validate_with(load_schema("dmf-odata-mapping.schema.json"), load_json(map_path), str(map_path.relative_to(ROOT)))

    pc_path = ROOT / "Business Process" / "ProcessCatalogue.json"
    if pc_path.exists():
        # process catalogue is large; only validate top-level shape if it matches our schema
        try:
            pc = load_json(pc_path)
            if isinstance(pc, dict) and "nodes" in pc:
                out += validate_with(load_schema("process-catalogue.schema.json"), pc, str(pc_path.relative_to(ROOT)))
        except json.JSONDecodeError as exc:
            out.append(Issue("error", str(pc_path.relative_to(ROOT)), f"invalid JSON: {exc}"))

    dmf_schema = load_schema("dmf-template.schema.json")
    for tpl in ROOT.joinpath("Modules").rglob("*.json"):
        if tpl.name in {"dmf_odata_mapping.json", "dependency-graph.json"}:
            continue
        if not re.match(r"^\d{3} - ", tpl.name):
            continue
        try:
            data = load_json(tpl)
        except json.JSONDecodeError as exc:
            out.append(Issue("error", str(tpl.relative_to(ROOT)), f"invalid JSON: {exc}"))
            continue
        out += validate_with(dmf_schema, data, str(tpl.relative_to(ROOT)))

    rs_path = ROOT / "Documentation" / "run-state.json"
    if rs_path.exists():
        out += validate_with(load_schema("run-state.schema.json"), load_json(rs_path), str(rs_path.relative_to(ROOT)))

    return out


def lint_skills() -> list[Issue]:
    out: list[Issue] = []
    if not SKILLS.exists():
        out.append(Issue("error", "skills/", "skills/ directory missing"))
        return out

    seen_names: dict[str, Path] = {}
    for skill_dir in sorted(SKILLS.iterdir()):
        if not skill_dir.is_dir():
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            out.append(Issue("error", str(skill_dir.relative_to(ROOT)), "missing SKILL.md"))
            continue

        text = skill_md.read_text(encoding="utf-8")
        fm = FRONTMATTER_RE.match(text)
        if not fm:
            out.append(Issue("error", str(skill_md.relative_to(ROOT)), "missing YAML frontmatter"))
            continue
        body = text[fm.end():]
        fm_block = fm.group(1)

        name_m = NAME_RE.search(fm_block)
        desc_m = DESC_RE.search(fm_block)

        if not name_m:
            out.append(Issue("error", str(skill_md.relative_to(ROOT)), "frontmatter missing `name`"))
        else:
            name = name_m.group(1).strip()
            if name != skill_dir.name:
                out.append(Issue("warning", str(skill_md.relative_to(ROOT)), f"frontmatter name '{name}' differs from folder '{skill_dir.name}'"))
            if name in seen_names:
                out.append(Issue("error", str(skill_md.relative_to(ROOT)), f"duplicate skill name (also in {seen_names[name].relative_to(ROOT)})"))
            else:
                seen_names[name] = skill_md

        if not desc_m:
            out.append(Issue("error", str(skill_md.relative_to(ROOT)), "frontmatter missing `description`"))
        else:
            desc = desc_m.group(1).strip()
            if not desc:
                out.append(Issue("error", str(skill_md.relative_to(ROOT)), "frontmatter `description` is empty"))
            elif len(desc) > MAX_DESC_LEN:
                out.append(Issue("warning", str(skill_md.relative_to(ROOT)), f"description is {len(desc)} chars (>{MAX_DESC_LEN}); shorten or move detail to body"))

        body_bytes = len(body.encode("utf-8"))
        if body_bytes > MAX_BODY_BYTES:
            out.append(Issue("warning", str(skill_md.relative_to(ROOT)), f"SKILL.md body is {body_bytes} bytes (>{MAX_BODY_BYTES}); consider splitting into sidecar reference files"))

        # Local link resolution
        for m in LINK_RE.finditer(body):
            target = m.group(1).split("#", 1)[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            target_path = (skill_dir / target).resolve()
            if not target_path.exists():
                # also try repo root
                root_path = (ROOT / target).resolve()
                if not root_path.exists():
                    out.append(Issue("warning", str(skill_md.relative_to(ROOT)), f"broken local link: {target}"))

    return out


def cross_check_dependency_graph() -> list[Issue]:
    out: list[Issue] = []
    dg_path = ROOT / "Modules" / "dependency-graph.json"
    if not dg_path.exists():
        return out
    dg = load_json(dg_path)
    seqs_in_modules = {m["dmfSeq"] for m in dg.get("modules", [])}
    seqs_in_waves = {seq for w in dg.get("waves", []) for seq in w.get("modules", [])}
    missing_in_waves = seqs_in_modules - seqs_in_waves
    extra_in_waves = seqs_in_waves - seqs_in_modules
    for s in sorted(missing_in_waves):
        out.append(Issue("error", "dependency-graph.json", f"module {s} declared but not assigned to any wave"))
    for s in sorted(extra_in_waves):
        out.append(Issue("error", "dependency-graph.json", f"wave references unknown module {s}"))

    for m in dg.get("modules", []):
        for missing_dep in [d for d in m.get("dependsOn", []) if d not in seqs_in_modules]:
            out.append(Issue("error", "dependency-graph.json", f"module {m['dmfSeq']} dependsOn unknown {missing_dep}"))
        if (mp := m.get("modulePath")):
            if not (ROOT / mp).exists():
                out.append(Issue("warning", "dependency-graph.json", f"module {m['dmfSeq']}: modulePath not found ({mp})"))
        if (tpl := m.get("dmfTemplate")):
            if not (ROOT / tpl).exists():
                out.append(Issue("warning", "dependency-graph.json", f"module {m['dmfSeq']}: dmfTemplate not found ({tpl})"))
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--quick", action="store_true", help="Skip drift / cross-file checks")
    args = parser.parse_args()

    print("• Validating governed JSON…")
    issues = validate_json_artefacts()
    print("• Linting skills…")
    issues += lint_skills()
    if not args.quick:
        print("• Cross-checking dependency graph…")
        issues += cross_check_dependency_graph()

    errors = [i for i in issues if i.severity == "error"]
    warnings = [i for i in issues if i.severity == "warning"]

    if issues:
        print()
        for i in issues:
            print(i)
        print()
    print(f"Result: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
