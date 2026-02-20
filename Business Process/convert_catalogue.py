"""
Convert ProcessCatalogue.csv to a structured JSON format optimized for agent consumption.

Produces two files:
1. ProcessCatalogue.json          - Hierarchical tree structure
2. ProcessCatalogue_flat.json     - Flat indexed array (easy search/filter)
"""

import csv
import json
import re
import html
from pathlib import Path

CSV_PATH = Path(__file__).parent / "ProcessCatalogue.csv"
OUT_TREE = Path(__file__).parent / "ProcessCatalogue.json"
OUT_FLAT = Path(__file__).parent / "ProcessCatalogue_flat.json"


def strip_html(text: str) -> str:
    """Remove HTML tags and decode entities, collapse whitespace."""
    if not text:
        return ""
    text = html.unescape(text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def extract_url(ref: str) -> str:
    """Pull the first URL from an HTML anchor or raw text."""
    if not ref:
        return ""
    m = re.search(r'https?://[^\s<>"]+', ref)
    return m.group(0) if m else ""


def resolve_title(row: dict) -> str:
    """Return the deepest non-empty title from Title 1..7."""
    for i in range(7, 0, -1):
        val = row.get(f"Title {i}", "").strip()
        if val:
            return val
    return ""


def build_item(row: dict) -> dict:
    """Build a clean process item dict from a CSV row."""
    item = {
        # --- Identity & hierarchy ---
        "id": int(row["ID"]) if row["ID"] else None,
        "sequenceId": row.get("Process sequence ID", "").strip() or None,
        "alternateSequenceId": row.get("Alternate process sequence ID", "").strip() or None,
        "type": row.get("Work Item Type", "").strip(),
        "title": resolve_title(row),
        "parentId": int(row["Parent"]) if row.get("Parent", "").strip() else None,
        "microsoftId": row.get("Microsoft ID", "").strip() or None,
        "partnerId": row.get("Partner ID", "").strip() or None,

        # --- Content ---
        "description": strip_html(row.get("Description", "")),
        "microsoftReference": extract_url(row.get("Microsoft references", "")),

        # --- Classification ---
        "areaPath": row.get("Area Path", "").strip() or None,
        "applicationFamily": row.get("Application family", "").strip() or None,
        "products": row.get("Products", "").strip() or None,
        "industries": row.get("Industries", "").strip() or None,
        "module": row.get("Module", "").strip() or None,
        "menuPath": row.get("Menu path", "").strip() or None,
        "menuItemName": row.get("Menu item name", "").strip() or None,
        "apqcId": row.get("APQC ID", "").strip() or None,
        "apqcDescription": row.get("APQC description", "").strip() or None,

        # --- Status & workflow ---
        "scope": row.get("Scope", "").strip() or None,
        "state": row.get("State", "").strip() or None,
        "catalogStatus": row.get("Catalog status", "").strip() or None,
        "articleStatus": row.get("Article status", "").strip() or None,
        "businessProcessFlowStatus": row.get("Business process flow status", "").strip() or None,
        "fitGapStatus": row.get("Fit gap status", "").strip() or None,
        "gapSolutionApproach": row.get("Gap solution approach", "").strip() or None,
        "updateComments": strip_html(row.get("Update comments", "")),
        "assignedTo": row.get("Assigned To", "").strip() or None,
    }
    # Remove None/empty values to keep payload compact
    return {k: v for k, v in item.items() if v is not None and v != ""}


def build_hierarchy(items: list[dict]) -> dict:
    """Build a nested tree from flat items using parentId."""
    lookup = {item["id"]: {**item, "children": []} for item in items}

    roots = []
    for item in items:
        node = lookup[item["id"]]
        pid = item.get("parentId")
        if pid and pid in lookup:
            lookup[pid]["children"].append(node)
        else:
            roots.append(node)

    # Clean up: remove empty children arrays and parentId from tree nodes
    def clean(node):
        node.pop("parentId", None)
        if not node["children"]:
            del node["children"]
        else:
            for child in node["children"]:
                clean(child)

    for root in roots:
        clean(root)

    return roots


def add_hierarchy_path(items: list[dict]) -> None:
    """Add a hierarchyPath field showing the full title breadcrumb."""
    lookup = {item["id"]: item for item in items}
    cache = {}

    def get_path(item_id):
        if item_id in cache:
            return cache[item_id]
        item = lookup.get(item_id)
        if not item:
            return []
        pid = item.get("parentId")
        if pid and pid in lookup:
            path = get_path(pid) + [item["title"]]
        else:
            path = [item["title"]]
        cache[item_id] = path
        return path

    for item in items:
        path = get_path(item["id"])
        item["hierarchyPath"] = " > ".join(path)


def main():
    with open(CSV_PATH, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(f"Read {len(rows)} rows from CSV")

    # Build flat items
    items = [build_item(row) for row in rows]
    items = [i for i in items if i.get("id") is not None]

    print(f"Processed {len(items)} items")

    # Add hierarchy paths to flat items
    add_hierarchy_path(items)

    # --- Flat output ---
    flat_output = {
        "_metadata": {
            "source": "ProcessCatalogue.csv",
            "format": "D365 Finance & Operations Business Process Library",
            "description": "Flat indexed catalogue of business processes. Use 'id' and 'parentId' to traverse hierarchy. 'hierarchyPath' shows the full breadcrumb.",
            "typeHierarchy": "Tree > End to end > Process area > Process > Scenario | System process | Test cases",
            "totalItems": len(items),
            "generatedFrom": "ProcessCatalogue.csv conversion script",
            "fields": {
                "identity": "id, sequenceId, alternateSequenceId, type, title, parentId, microsoftId, partnerId, hierarchyPath",
                "content": "description, microsoftReference",
                "classification": "areaPath, applicationFamily, products, industries, module, menuPath, menuItemName, apqcId, apqcDescription",
                "status": "scope, state, catalogStatus, articleStatus, businessProcessFlowStatus, fitGapStatus, gapSolutionApproach, updateComments, assignedTo",
            },
        },
        "processes": items,
    }

    with open(OUT_FLAT, "w", encoding="utf-8") as f:
        json.dump(flat_output, f, indent=2, ensure_ascii=False)
    print(f"Wrote flat catalogue: {OUT_FLAT} ({OUT_FLAT.stat().st_size / 1024 / 1024:.1f} MB)")

    # --- Hierarchical tree output ---
    tree = build_hierarchy(items)

    tree_output = {
        "_metadata": {
            "source": "ProcessCatalogue.csv",
            "format": "D365 Finance & Operations Business Process Library",
            "description": "Hierarchical tree of business processes. Each node may contain 'children' array.",
            "typeHierarchy": "Tree > End to end > Process area > Process > Scenario | System process | Test cases",
            "totalItems": len(items),
            "generatedFrom": "ProcessCatalogue.csv conversion script",
            "fields": {
                "identity": "id, sequenceId, alternateSequenceId, type, title, microsoftId, partnerId, hierarchyPath",
                "content": "description, microsoftReference",
                "classification": "areaPath, applicationFamily, products, industries, module, menuPath, menuItemName, apqcId, apqcDescription",
                "status": "scope, state, catalogStatus, articleStatus, businessProcessFlowStatus, fitGapStatus, gapSolutionApproach, updateComments, assignedTo",
            },
        },
        "processTree": tree,
    }

    with open(OUT_TREE, "w", encoding="utf-8") as f:
        json.dump(tree_output, f, indent=2, ensure_ascii=False)
    print(f"Wrote tree catalogue:  {OUT_TREE} ({OUT_TREE.stat().st_size / 1024 / 1024:.1f} MB)")


if __name__ == "__main__":
    main()
