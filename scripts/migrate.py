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
from urllib.parse import quote

REPO_ROOT = Path(__file__).resolve().parent.parent
HUGO_DOCS = REPO_ROOT / "content" / "en" / "docs"
HUGO_INCLUDES = REPO_ROOT / "content" / "en" / "includes"
ASTRO_DOCS = REPO_ROOT / "src" / "content" / "docs"
ASTRO_SNIPPETS = REPO_ROOT / "src" / "snippets"
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

DROP = {"markdown_example.md", "how-to/_index.md"}

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
    r"^([ \t]*)\{\{[<%]\s*(note|caution|warning)\s*[%>]\}\}(.*?)\{\{[<%]\s*/\2\s*[%>]\}\}",
    re.DOTALL | re.IGNORECASE | re.MULTILINE,
)

CALLOUT_TYPES = {
    "note":    "note",
    "caution": "caution",
    "warning": "danger",
}


def transform_callouts(body: str) -> tuple[str, bool]:
    """
    Convert Hugo note/caution/warning shortcodes into Starlight <Aside>.
    Emits a compact single-line form to avoid MDX list-item boundary issues.
    Preserves the leading whitespace of the original shortcode so nested
    list contexts retain correct indentation.
    """
    used = False

    def repl(m: re.Match) -> str:
        nonlocal used
        used = True
        indent = m.group(1)
        tag = m.group(2).lower()
        inner = " ".join(m.group(3).split())  # collapse whitespace; single line
        ast_type = CALLOUT_TYPES[tag]
        if ast_type == "note":
            return f"{indent}<Aside>{inner}</Aside>"
        return f'{indent}<Aside type="{ast_type}">{inner}</Aside>'

    return CALLOUT_PATTERN.sub(repl, body), used


INCLUDE_PATTERN = re.compile(r'\{\{<\s*include\s+"([^"]+)"\s*>\}\}')


def transform_includes(body: str) -> tuple[str, list[str]]:
    """Convert {{< include "foo.md" >}} or {{< include "sub/foo.md" >}} to
    MDX component reference. Returns body + entries of form
    "ComponentName:relative/path-without-ext"."""
    names: list[str] = []

    def repl(m: re.Match) -> str:
        name = m.group(1)
        p = Path(name)
        stem = p.stem
        rel_no_ext = str(p.with_suffix(""))
        # Component name from stem only (with directory prefix to avoid collisions)
        prefix = "".join(part.capitalize() for part in p.parent.parts) if str(p.parent) != "." else ""
        body_part = "".join(part.capitalize() for part in re.split(r"[-_]", stem))
        component = "Snippet" + prefix + body_part
        names.append(component + ":" + rel_no_ext)
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


# Common HTML elements MDX accepts as plain HTML (no escaping needed).
_HTML_WHITELIST = {
    "a", "abbr", "address", "area", "article", "aside", "audio", "b",
    "base", "bdi", "bdo", "blockquote", "body", "br", "button", "canvas",
    "caption", "cite", "code", "col", "colgroup", "data", "datalist",
    "dd", "del", "details", "dfn", "dialog", "div", "dl", "dt", "em",
    "embed", "fieldset", "figcaption", "figure", "footer", "form",
    "h1", "h2", "h3", "h4", "h5", "h6", "head", "header", "hr", "html",
    "i", "iframe", "img", "input", "ins", "kbd", "label", "legend",
    "li", "link", "main", "map", "mark", "meta", "meter", "nav",
    "noscript", "object", "ol", "optgroup", "option", "output", "p",
    "param", "picture", "pre", "progress", "q", "rb", "rp", "rt", "rtc",
    "ruby", "s", "samp", "script", "section", "select", "slot", "small",
    "source", "span", "strong", "style", "sub", "summary", "sup", "svg",
    "table", "tbody", "td", "template", "textarea", "tfoot", "th",
    "thead", "time", "title", "tr", "track", "u", "ul", "var", "video",
    "wbr",
}

# Autolink: <http(s)://...> -> [url](url). Handle double-bracket too.
AUTOLINK_DOUBLE = re.compile(r"<<(https?://[^>\s]+)>>")
AUTOLINK_SINGLE = re.compile(r"<(https?://[^>\s]+)>")
# Bare placeholder: <name-or_with_punct> where it's not a real HTML tag.
PLACEHOLDER_TAG = re.compile(r"<([a-z][a-zA-Z0-9_-]*)>")


def _wrap_placeholder(m: re.Match) -> str:
    name = m.group(1)
    if name.lower() in _HTML_WHITELIST:
        return m.group(0)
    return f"`<{name}>`"


def _transform_outside_code_spans(line: str) -> str:
    """Apply MDX safety transforms only to text outside backtick code spans."""
    # Split on backticks; even-indexed pieces are outside code spans.
    parts = line.split("`")
    for i in range(0, len(parts), 2):
        s = parts[i]
        # Strip backslash escapes inside <...> first (Hugo md residue).
        s = re.sub(
            r"<([^>]*\\[_*][^>]*)>",
            lambda m: "<" + m.group(1).replace("\\_", "_").replace("\\*", "*") + ">",
            s,
        )
        # Autolinks -> plain URL text.
        s = AUTOLINK_DOUBLE.sub(lambda m: m.group(1), s)
        s = AUTOLINK_SINGLE.sub(lambda m: m.group(1), s)
        # Wrap non-HTML placeholder tags in backticks.
        s = PLACEHOLDER_TAG.sub(_wrap_placeholder, s)
        # Escape bare `<` that can't start an HTML/JSX tag (e.g. `n <= 1`, `< 5`).
        # MDX requires the character after `<` to be a letter, `!`, or `/`.
        s = re.sub(r"<(?=[^a-zA-Z!/])", "&lt;", s)
        # Escape bare `{` that MDX would parse as JS expression
        # (text like `{Column -> Value}`). Allow `{/*` MDX comment marker.
        s = re.sub(r"\{(?!/\*)", r"\\{", s)
        parts[i] = s
    return "`".join(parts)


def mdx_safety(body: str) -> str:
    """Escape constructs that look like JSX/HTML but aren't.

    Skips fenced code blocks (```...```) entirely and skips inline code
    spans (`...`) within text lines.
    """
    out_lines: list[str] = []
    in_code_block = False
    for line in body.splitlines(keepends=True):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_code_block = not in_code_block
            out_lines.append(line)
            continue
        if in_code_block:
            out_lines.append(line)
            continue
        out_lines.append(_transform_outside_code_spans(line))
    return "".join(out_lines)


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
    body = mdx_safety(body)
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
    Hugo's slug overrides only the leaf segment. URL-encode the path so
    Cloudflare's _redirects parser (whitespace-tokenized) doesn't choke
    on legacy paths with spaces like /Document Management/."""
    posix = rel.as_posix()
    if posix.endswith("/_index.md"):
        url = "/docs/" + posix[: -len("/_index.md")] + "/"
    elif hugo_slug:
        parent = rel.parent.as_posix()
        prefix = f"/docs/{parent}/" if parent != "." else "/docs/"
        url = prefix + hugo_slug + "/"
    else:
        url = "/docs/" + re.sub(r"\.md$", "/", posix)
    return quote(url, safe="/")


def _to_new_url(rel: Path) -> str:
    """Astro Starlight serves from src/content/docs/ at root URLs (no /docs/ prefix)."""
    posix = rel.as_posix()
    return "/" + re.sub(r"/index\.mdx?$|\.mdx?$", "/", posix)


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


def migrate_snippets() -> int:
    """Migrate content/en/includes/* (recursively) into src/snippets/ as MDX-importable components."""
    if not HUGO_INCLUDES.is_dir():
        return 0
    ASTRO_SNIPPETS.mkdir(parents=True, exist_ok=True)
    count = 0
    for src in sorted(HUGO_INCLUDES.rglob("*.md")):
        text = src.read_text(encoding="utf-8")
        _, body = split_front_matter(text)
        body, _ = transform_callouts(body)
        body, _ = transform_misc(body)
        body = mdx_safety(body)
        body, _ = escape_remaining_hugo_syntax(body)
        body = body.strip("\n") + "\n"

        imports: list[str] = []
        if "<Aside" in body:
            imports.append("import { Aside } from '@astrojs/starlight/components';")
        prefix = ("\n".join(imports) + "\n\n") if imports else ""

        rel = src.relative_to(HUGO_INCLUDES).with_suffix(".mdx")
        dst = ASTRO_SNIPPETS / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(prefix + body, encoding="utf-8")
        count += 1
    return count


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sections", nargs="+", help="Section names under content/en/docs/")
    ap.add_argument("--snippets", action="store_true", help="Also migrate content/en/includes/ to src/snippets/")
    args = ap.parse_args()

    log = []
    grand_total = 0
    all_leftovers = []
    all_pairs = []

    if args.snippets:
        n = migrate_snippets()
        print(f"snippets: migrated {n} files", file=sys.stderr)

    if not args.sections:
        return 0

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
