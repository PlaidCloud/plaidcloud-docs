#!/usr/bin/env python3
"""
Hugo -> Astro Starlight content migration.

One-shot tool. Run per-section to land content in batches:
    python3 scripts/migrate.py --sections connectors
    python3 scripts/migrate.py --sections workflows allocations

Reads:  content/en/docs/<section>/...
Writes: src/content/docs/<remapped-path>/...
Appends new redirects to: public/_redirects
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path
from typing import Optional

REPO_ROOT = Path(__file__).resolve().parent.parent
HUGO_DOCS = REPO_ROOT / "content" / "en" / "docs"
ASTRO_DOCS = REPO_ROOT / "src" / "content" / "docs"
REDIRECTS_FILE = REPO_ROOT / "public" / "_redirects"

# Top-level section moves
SECTION_MAP = {
    "AI_Assistant":        "guides/ai-assistant",
    "Access_Management":   "administration/access",
    "Dashboards":          "guides/dashboards",
    "Document Management": "guides/documents",
    "Email":               "guides/email",
    "Jupyter_CLI":         "reference/cli/jupyter",
    "Panel Apps":          "guides/panel-apps",
    "PySpark":             "integrations/pyspark",
    "Sandbox":             "guides/sandbox",
    "ai-agents":           "integrations/ai-coding-agents",
    "allocations":         "guides/allocations",
    "data":                "guides/data",
    "dimensions":          "guides/dimensions",
    "expressions":         "reference/expressions",
    "plaidlink":           "reference/cli/plaidlink",
    "plaidxl":             "reference/cli/plaidxl",
    "projects":            "guides/projects",
    "scheduled-events":    "administration/scheduled-events",
    "workflow-steps":      "reference/workflow-steps",
    "workflows":           "guides/workflows",
}

# connectors/ splits across guides/connections (tasks) and reference/connectors (provider refs)
CONNECTORS_SPLIT = {
    "_index.md":                  "reference/connectors/_index.md",
    "clone-connection.md":        "guides/connections/clone-connection.md",
    "cloud-services-connections": "reference/connectors/cloud-services",
    "collaboration-connections":  "reference/connectors/collaboration",
    "database-connections":       "reference/connectors/databases",
    "erp-connections":            "reference/connectors/erp",
    "git-connections":            "reference/connectors/git",
    "google-connections":         "reference/connectors/google",
    "open-table-connections":     "reference/connectors/open-tables",
    "rest-connections":           "reference/connectors/rest",
}

DROP = {"markdown_example.md", "how-to/_index.md", "how-to/selecting-latest-record-in-large-history-table.md"}

# how-to is a one-page section; relocate that page into guides/data
HOWTO_MOVE = {
    "how-to/selecting-latest-record-in-large-history-table.md":
        "guides/data/selecting-latest-record-in-large-history-table.md",
}

# Hugo-only front matter keys to strip outright
# `slug` is stripped so Starlight derives URLs from folder structure
# (Hugo's slug was per-segment; Astro's slug overrides the whole URL).
STRIP_KEYS = {
    "type", "layout", "headless", "main_menu", "sitemap",
    "title_includes", "cid", "priority", "categories", "tags",
    "id", "date", "slug",
}


def normalize_segment(seg: str) -> str:
    """kebab-case folder/file segment."""
    seg = seg.replace("_", "-").replace(" ", "-").lower()
    seg = re.sub(r"-+", "-", seg)
    return seg


def remap_path(rel: Path) -> Path | None:
    """
    Map a path relative to content/en/docs/ to its new location under
    src/content/docs/. Returns None if file should be dropped.
    """
    parts = rel.parts
    posix = rel.as_posix()

    # Drop list
    if posix in DROP:
        return None

    # how-to relocations
    if posix in HOWTO_MOVE:
        new_rel = HOWTO_MOVE[posix]
        return Path(_normalize_path(new_rel))

    top = parts[0]

    # connectors splits across two roots
    if top == "connectors":
        if len(parts) == 1:
            return None
        sub = parts[1]
        rest = parts[2:] if len(parts) > 2 else ()
        if sub in CONNECTORS_SPLIT:
            mapped = CONNECTORS_SPLIT[sub]
            new = Path(mapped, *rest) if rest else Path(mapped)
            return Path(_normalize_path(new.as_posix()))
        # Unmapped connectors subpath
        return None

    if top in SECTION_MAP:
        new_prefix = SECTION_MAP[top]
        rest = parts[1:]
        new = Path(new_prefix, *rest) if rest else Path(new_prefix)
        return Path(_normalize_path(new.as_posix()))

    return None


def _normalize_path(posix: str) -> str:
    """Apply kebab-case to each path segment except the filename's extension.
    Hugo's _index.md becomes Astro's index.md (handled outside this function)."""
    p = Path(posix)
    stem = p.stem
    suffix = p.suffix
    parent_parts = [normalize_segment(s) for s in p.parent.parts] if p.parent.parts else []
    if stem == "_index":
        new_stem = "index"
    else:
        new_stem = normalize_segment(stem)
    return str(Path(*parent_parts, new_stem + suffix))


def split_front_matter(text: str) -> tuple[dict, str]:
    """
    Parse YAML front matter into a dict (string values only) plus the body.
    Returns ({}, text) if no front matter.
    """
    if not text.startswith("---"):
        return {}, text
    lines = text.splitlines(keepends=True)
    if not lines:
        return {}, text
    # Find closing ---
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        return {}, text

    fm_text = "".join(lines[1:end_idx])
    body = "".join(lines[end_idx + 1:])

    fm: dict[str, str] = {}
    current_key = None
    for raw in fm_text.splitlines():
        if not raw.strip() or raw.strip().startswith("#"):
            continue
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*)\s*:\s*(.*)$", raw)
        if m:
            key = m.group(1).strip()
            val = m.group(2).strip()
            fm[key] = val
            current_key = key
        else:
            # Multi-line continuation — append to current value
            if current_key:
                fm[current_key] = (fm[current_key] + " " + raw.strip()).strip()
    return fm, body


def normalize_fm(fm: dict) -> dict:
    """Lowercase keys, map Hugo->Starlight, strip dead keys."""
    out: dict = {}
    sidebar: dict = {}

    for raw_key, val in fm.items():
        key = raw_key.lower()
        if key in STRIP_KEYS:
            continue
        if key == "linktitle":
            sidebar["label"] = val
            continue
        if key == "weight":
            try:
                sidebar["order"] = float(val)
            except ValueError:
                pass
            continue
        out[key] = val

    if sidebar:
        out["sidebar"] = sidebar
    return out


def render_fm(fm: dict) -> str:
    """Emit YAML front matter. Handles nested sidebar dict."""
    lines = ["---"]
    for k, v in fm.items():
        if k == "sidebar" and isinstance(v, dict):
            lines.append("sidebar:")
            for sk, sv in v.items():
                if isinstance(sv, float) and sv.is_integer():
                    sv = int(sv)
                lines.append(f"  {sk}: {_yaml_scalar(sv)}")
        else:
            lines.append(f"{k}: {_yaml_scalar(v)}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def _yaml_scalar(v) -> str:
    if isinstance(v, (int, float)):
        return str(v)
    s = str(v).strip()
    if s.startswith(("'", '"')):
        return s
    # Quote if contains special characters
    if any(c in s for c in [":", "#", "&", "*", "?", "|", ">", "<", "!", "%", "@", "`"]):
        s_esc = s.replace('"', '\\"')
        return f'"{s_esc}"'
    return s


# --- Body transforms ---

CALLOUT_PATTERN = re.compile(
    r"\{\{[<%]\s*(note|caution|warning)\s*[%>]\}\}(.*?)\{\{[<%]\s*/\1\s*[%>]\}\}",
    re.DOTALL | re.IGNORECASE,
)

CALLOUT_TYPES = {
    "note":    "note",
    "caution": "caution",
    "warning": "danger",
}


def transform_callouts(body: str) -> tuple[str, bool]:
    used = False

    def repl(m: re.Match) -> str:
        nonlocal used
        used = True
        tag = m.group(1).lower()
        inner = m.group(2).strip()
        ast_type = CALLOUT_TYPES[tag]
        if ast_type == "note":
            return f"<Aside>\n{inner}\n</Aside>"
        return f'<Aside type="{ast_type}">\n{inner}\n</Aside>'

    return CALLOUT_PATTERN.sub(repl, body), used


INCLUDE_PATTERN = re.compile(r'\{\{<\s*include\s+"([^"]+)"\s*>\}\}')


def transform_includes(body: str) -> tuple[str, list[str]]:
    """Convert {{< include "foo.md" >}} to MDX component reference. Returns body + names."""
    names: list[str] = []

    def repl(m: re.Match) -> str:
        name = m.group(1)
        stem = Path(name).stem
        component = "Snippet" + "".join(p.capitalize() for p in re.split(r"[-_]", stem))
        names.append(component + ":" + stem)
        return f"<{component} />"

    return INCLUDE_PATTERN.sub(repl, body), names


SWAGGERUI_PATTERN = re.compile(r"\{\{<\s*swaggerui\s*>\}\}")
MERMAID_PATTERN = re.compile(r"\{\{<\s*mermaid\s*>\}\}(.*?)\{\{<\s*/mermaid\s*>\}\}", re.DOTALL)
FIGURE_PATTERN = re.compile(r'\{\{<\s*figure\s+src="([^"]+)"(?:\s+caption="([^"]*)")?[^>]*>\}\}')


def transform_misc(body: str) -> tuple[str, set[str]]:
    used_components: set[str] = set()

    def swagger_repl(_):
        used_components.add("SwaggerUI")
        return "<SwaggerUI />"

    body = SWAGGERUI_PATTERN.sub(swagger_repl, body)
    body = MERMAID_PATTERN.sub(lambda m: f"```mermaid\n{m.group(1).strip()}\n```", body)
    body = FIGURE_PATTERN.sub(
        lambda m: f"![{m.group(2) or ''}]({m.group(1)})", body
    )
    return body, used_components


def strip_duplicate_h1(body: str, title: str) -> str:
    """Strip a leading `# Title` line if it matches front matter title."""
    if not title:
        return body
    body_stripped = body.lstrip("\n")
    pattern = re.compile(r"^#\s+" + re.escape(title) + r"\s*$", re.MULTILINE)
    first_line_match = re.match(r"^#\s+(.+?)\s*$", body_stripped, re.MULTILINE)
    if first_line_match and first_line_match.group(1).strip().lower() == title.strip().lower():
        return body_stripped.split("\n", 1)[1].lstrip("\n") if "\n" in body_stripped else ""
    # Also strip if found anywhere very near the top
    return pattern.sub("", body_stripped, count=1).lstrip("\n")


def escape_remaining_hugo_syntax(body: str) -> tuple[str, list[str]]:
    """
    Find any leftover {{< ... >}} or {{% ... %}} (unrecognized shortcodes) and
    wrap them in HTML comments so MDX doesn't parse them. Logs them for review.
    """
    leftovers: list[str] = []
    pattern = re.compile(r"\{\{[<%][^}]+[%>]\}\}")

    def repl(m: re.Match) -> str:
        leftovers.append(m.group(0))
        return f"{{/* TODO migration: {m.group(0)} */}}"

    return pattern.sub(repl, body), leftovers


def needs_mdx(body: str, used_components: set[str], include_names: list[str]) -> bool:
    return (
        bool(used_components)
        or bool(include_names)
        or "<Aside" in body
        or "{/*" in body
    )


def build_import_block(used: set[str], include_names: list[str]) -> str:
    lines: list[str] = []
    starlight_imports: list[str] = []
    if "<Aside" in "\n".join([*used, "placeholder"]) or any("Aside" in u for u in used):
        pass  # handled below by checking body
    return ""  # imports are added by the caller using context


def transform_file(src: Path, dst: Path, log) -> dict:
    text = src.read_text(encoding="utf-8")
    fm_raw, body = split_front_matter(text)
    # Capture the Hugo slug (if any) before STRIP_KEYS drops it.
    hugo_slug = (fm_raw.get("slug") or fm_raw.get("Slug") or "").strip().strip("'\"")
    fm = normalize_fm(fm_raw)

    title = fm.get("title", "").strip().strip("'\"")
    body = strip_duplicate_h1(body, title)

    body, callouts_used = transform_callouts(body)
    body, include_components = transform_includes(body)
    body, misc_components = transform_misc(body)
    body, leftover_hugo = escape_remaining_hugo_syntax(body)

    # Determine extension
    is_mdx = (
        callouts_used
        or include_components
        or misc_components
        or "<Aside" in body
        or "{/*" in body
    )
    if dst.name == "index.md" and is_mdx:
        dst = dst.with_name("index.mdx")
    elif is_mdx:
        dst = dst.with_suffix(".mdx")

    # Build import block for components used
    imports: list[str] = []
    starlight_components: list[str] = []
    if callouts_used:
        starlight_components.append("Aside")
    if starlight_components:
        imports.append(
            "import { " + ", ".join(starlight_components) + " } from '@astrojs/starlight/components';"
        )
    if include_components:
        seen = set()
        for entry in include_components:
            comp, stem = entry.split(":", 1)
            if comp in seen:
                continue
            seen.add(comp)
            imports.append(f"import {comp} from '@snippets/{stem}.mdx';")
    if "SwaggerUI" in misc_components:
        imports.append("import SwaggerUI from '~/components/SwaggerUI.astro';")

    front_matter_text = render_fm(fm)
    parts = [front_matter_text]
    if imports:
        parts.append("\n".join(imports) + "\n")
    parts.append(body.lstrip("\n"))
    out = "\n".join(parts).rstrip() + "\n"

    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(out, encoding="utf-8")

    return {
        "src": src,
        "dst": dst,
        "leftover_hugo": leftover_hugo,
        "hugo_slug": hugo_slug,
    }


def _to_old_url(rel: Path, hugo_slug: str) -> str:
    """Reconstruct the URL Hugo would have served for this file.
    Hugo's slug overrides only the leaf segment."""
    posix = rel.as_posix()
    if posix.endswith("/_index.md"):
        return "/docs/" + posix[: -len("/_index.md")] + "/"
    if hugo_slug:
        parent = rel.parent.as_posix()
        prefix = f"/docs/{parent}/" if parent != "." else "/docs/"
        return prefix + hugo_slug + "/"
    return "/docs/" + re.sub(r"\.md$", "/", posix)


def _to_new_url(rel: Path) -> str:
    posix = rel.as_posix()
    return "/docs/" + re.sub(r"/index\.mdx?$|\.mdx?$", "/", posix)


def generate_redirect(old_rel: Path, new_rel: Path, hugo_slug: str = "") -> Optional[str]:
    old_url = _to_old_url(old_rel, hugo_slug)
    new_url = _to_new_url(new_rel)
    if old_url == new_url:
        return None
    return f"{old_url}   {new_url}   301"


def migrate_section(section: str, log):
    section_dir = HUGO_DOCS / section
    if not section_dir.is_dir():
        print(f"skip: {section} (no source dir)", file=sys.stderr)
        return 0, [], []

    count = 0
    all_leftovers = []
    pairs = []

    for md in sorted(section_dir.rglob("*.md")):
        rel = md.relative_to(HUGO_DOCS)
        target = remap_path(rel)
        if target is None:
            print(f"drop: {rel}", file=sys.stderr)
            continue

        dst = ASTRO_DOCS / target
        result = transform_file(md, dst, log)
        actual_dst = result["dst"].relative_to(ASTRO_DOCS)
        pairs.append((rel, actual_dst, result["hugo_slug"]))
        all_leftovers.extend(result["leftover_hugo"])
        count += 1
        if result["leftover_hugo"]:
            print(f"  ⚠ {rel}: {len(result['leftover_hugo'])} unrecognized shortcode(s)", file=sys.stderr)

    return count, all_leftovers, pairs


def append_redirects(pairs) -> int:
    if not pairs:
        return 0
    REDIRECTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    existing = REDIRECTS_FILE.read_text(encoding="utf-8") if REDIRECTS_FILE.exists() else ""
    new_lines = []
    if not existing.endswith("\n"):
        new_lines.append("")
    new_lines.append("# --- migration redirects (auto-generated) ---")
    added = 0
    for old, new, hugo_slug in pairs:
        line = generate_redirect(old, new, hugo_slug)
        if line and line not in existing:
            new_lines.append(line)
            added += 1
    REDIRECTS_FILE.write_text(existing + "\n".join(new_lines) + "\n", encoding="utf-8")
    return added


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sections", nargs="+", required=True, help="Section names under content/en/docs/")
    args = ap.parse_args()

    log = []
    grand_total = 0
    all_leftovers = []
    all_pairs = []

    for section in args.sections:
        n, leftovers, pairs = migrate_section(section, log)
        grand_total += n
        all_leftovers.extend(leftovers)
        all_pairs.extend(pairs)
        print(f"section {section}: migrated {n} files", file=sys.stderr)

    redirects_added = append_redirects(all_pairs)

    print(f"\nTOTAL: {grand_total} files migrated, {redirects_added} redirects added", file=sys.stderr)
    if all_leftovers:
        leftover_summary: dict[str, int] = {}
        for l in all_leftovers:
            tag = re.match(r"\{\{[<%]\s*([a-zA-Z_-]+)", l)
            t = tag.group(1) if tag else l
            leftover_summary[t] = leftover_summary.get(t, 0) + 1
        print(f"  unrecognized shortcodes: {leftover_summary}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
