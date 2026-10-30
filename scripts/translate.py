# /// script
# dependencies = ["anthropic", "pyyaml", "markdown-it-py"]
# ///
"""Machine-translate the English docs into the site's locales with the Claude Message Batches API, or via
Claude Code worker subagents (prepare / ingest).

Run with its dependencies on demand (no site dependency changes):

    uv run scripts/translate.py <command> ...

Commands:
    glossary                 rebuild i18n/glossary/<locale>.json from the PlaidClient UI catalogs
    plan   [--count N]       list stale page x locale pairs, deletions, and a token/cost estimate
    submit [--locales ...] [--paths GLOB ...] [--limit N]
                             create batch(es) for the stale pairs; records i18n/batches/<id>.json
    collect <batch_id>       poll until the batch ends, post-process, validate, write translations
    check                    re-validate every translated file against its English source
    check-anchors [--dist]   verify every /<locale>/…#anchor link in the built site hits an id
    prepare [--locales ...] [--paths ...] [--force-paths ...] [--chunk-words N]
                             write worker chunks + per-locale prompts to i18n/jobs/ (see i18n/jobs/WORKER.md)
    ingest [--locales ...]   post-process + validate worker output from i18n/staging/, install valid files

Terminology: i18n/termbase/<locale>.json (curated concepts, whole list in every prompt) and the PlaidClient UI
glossary with docs-side fixes from i18n/glossary_overrides/<locale>.json (null drops an entry). Catalog defects
the overrides work around are listed in i18n/CATALOG_FIXES.md.

Credentials come from the SDK's default resolution (ANTHROPIC_API_KEY or an `ant auth login` profile).

State:
    i18n/manifest.json       "<locale>/<path>" -> sha256 of the English source that was translated
    i18n/glossary/*.json     UI msgid -> msgstr per locale (official PlaidClient translations)
    i18n/batches/<id>.json   custom_id -> pair map for a submitted batch, plus per-pair results after collect

Translations land in src/content/docs/<locale>/<same relative path>. A translation that fails the
structural validator is not written (the page falls back to English) and is retried on the next run.
"""

import argparse
import difflib
import fnmatch
import functools
import hashlib
import html
import json
import posixpath
import re
import subprocess
import sys
import time
import unicodedata
import urllib.parse
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "src/content/docs"
SNIPPETS = ROOT / "src/snippets"
I18N = ROOT / "i18n"
MANIFEST = I18N / "manifest.json"
GLOSSARY_DIR = I18N / "glossary"
OVERRIDES_DIR = I18N / "glossary_overrides"
TERMBASE_DIR = I18N / "termbase"
BATCH_DIR = I18N / "batches"
PLAIDCLIENT = Path.home() / "Projects/PlaidClient"

MODEL = "claude-opus-5-5"
EFFORT = "low"
# Opus 5.5 list $/MTok, halved for the Batches API. Cache writes are 1.25x input (5-minute TTL).
PRICE = {"input": 2.0, "output": 10.0, "cache_read": 0.10, "cache_write": 2.50}
MAX_BATCH_REQUESTS = 90_000
MAX_BATCH_BYTES = 200 * 1024 * 1024

# locale dir -> (BCP-47 tag, language name, PlaidClient catalog, register/voice rules)
LOCALES = {
    "de": ("de", "German", "de",
           'Address the reader formally with "Sie" (never "du"). Instructions use the "Sie" imperative '
           '("Klicken Sie auf …"). Follow German software-documentation conventions; keep English IT terms '
           "where German UIs normally keep them (the glossary and termbase show which)."),
    "es": ("es", "Spanish", "es",
           'Address the reader with "usted" forms, matching the PlaidCloud UI ("¿Desea…?", "Haga clic en…", '
           '"Seleccione…"). Use neutral international Spanish that reads naturally in Latin America (período, '
           'costo, pérdidas y ganancias). Quote terms with “…”, never « ». The character "~" is "virgulilla", never "tilde".'),
    "fr": ("fr", "French", "fr",
           'Address the reader with "vous". Instructions use the "vous" imperative ("Cliquez sur…", '
           '"Sélectionnez…"). Follow French software-documentation conventions. French typography in prose only '
           "(never inside code, URLs, link targets, attribute values other than human-readable text, or frontmatter "
           "keys): a no-break space U+00A0 before `:` and inside « » (after « and before »); a narrow no-break space "
           "U+202F before `;`, `!` and `?`. Quote terms with « »."),
    "pt-br": ("pt-BR", "Brazilian Portuguese", "pt_BR",
              'Address the reader as "você". Use Brazilian vocabulary (arquivo, tela, usuário, baixar). '
              'Instructions use the imperative ("Clique em…", "Selecione…").'),
    "pt-pt": ("pt-PT", "European Portuguese", "pt_PT",
              'Use European Portuguese. Never use "você": use third-person verb forms, impersonal constructions '
              '("Pode…", "Selecione…", "É possível…") or "por si", as the PlaidCloud UI does ("Pretende…?"). '
              "Use European vocabulary (ficheiro, ecrã, utilizador, separador, transferir, predefinido) except where the "
              'glossary fixes a UI term; never Brazilian forms such as "tela" or "padrão" for default.'),
    "pl": ("pl", "Polish", "pl",
           "Use a neutral, professional register. Instructions use the standard second-person singular imperative "
           'of Polish software documentation ("Kliknij…", "Wybierz…"); descriptive sentences may use impersonal '
           'constructions ("Można…", "Należy…"). Never use "Pan/Pani". Keep it gender-neutral: never use forms '
           'that assume the reader\'s gender (past tense such as "skończyłeś", adjectives such as "sam", "gotowy").'),
    "ja": ("ja", "Japanese", "ja",
           "Write in です/ます style throughout. Use standard Japanese technical-writing conventions and full-width "
           "Japanese punctuation in prose (、。「」 and full-width （） including around English terms). Do not put "
           "spaces inside Japanese compounds (ワークフローの実行ステップ)."),
    "ko": ("ko", "Korean", "ko",
           "Write in the formal 합니다체 (합니다/하십시오) throughout, following standard Korean spacing rules "
           "and software-documentation conventions."),
    "zh-cn": ("zh-CN", "Simplified Chinese", "zh",
              "Write in Simplified Chinese (简体中文) as used in mainland China software documentation. Use 您 "
              "sparingly; prefer sentences without an explicit pronoun. Use full-width punctuation in prose, "
              "including “ ” quotes and （）, with no space before full-width punctuation."),
}
CJK = {"ja", "ko", "zh-cn"}

# Product and module names that stay English in prose. A bolded UI label still follows the glossary.
KEEP_ENGLISH = [
    "PlaidCloud", "Weave", "Lakehouse", "Panel", "Dash", "Analyze", "PlaidLink", "PlaidXL",
    "Common Finance Model", "Data Foundation", "Jupyter", "Superset",
]

# Frontmatter values the model may change; everything else must survive byte-for-byte (after parsing).
FM_TRANSLATABLE = {("title",), ("description",), ("sidebar", "label"), ("hero", "title"),
                   ("hero", "tagline"), ("hero", "actions", "*", "text")}
# Human-readable attributes inside HTML/JSX tags.
ATTR_TRANSLATABLE = {"alt", "aria-label", "title", "description", "label", "caption", "placeholder", "text"}
EDIT_BASE = "https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/"
NON_PAGE_PREFIXES = ("/images/", "/downloads/", "/open-graph/", "/_astro/", "/fonts/")


# ---------------------------------------------------------------- corpus + manifest
#
# A unit is either a docs page, keyed by its path under src/content/docs ("guides/x.md"), or an imported
# snippet, keyed "@snippets/<file>" exactly as pages import it. Translations live in src/content/docs/<lc>/
# and src/snippets/<lc>/; manifest keys are "<lc>/<path>" and "snippets/<lc>/<file>".

SNIPPET = "@snippets/"
SNIPPET_IMPORT_RE = re.compile(r"""(['"])@snippets/(?:(?:""" + "|".join(map(re.escape, LOCALES)) + r""")/)?([^'"]+)\1""")


def english_pages():
    """Relative paths of every English source page (locale dirs excluded)."""
    return sorted(p.relative_to(DOCS).as_posix() for p in DOCS.rglob("*.md*")
                  if p.is_file() and p.relative_to(DOCS).parts[0] not in LOCALES)


def english_snippets():
    """Snippet keys imported (directly or via another snippet) by English pages; unused snippets are skipped."""
    seen, todo = set(), [(DOCS / rel).read_text() for rel in english_pages()]
    while todo:
        for _, f in SNIPPET_IMPORT_RE.findall(todo.pop()):
            if f not in seen and (SNIPPETS / f).is_file():
                seen.add(f)
                todo.append((SNIPPETS / f).read_text())
    return sorted(SNIPPET + f for f in seen)


def english_units():
    return english_pages() + english_snippets()


def src_path(key):
    return SNIPPETS / key[len(SNIPPET):] if key.startswith(SNIPPET) else DOCS / key


def out_path(lc, key):
    return SNIPPETS / lc / key[len(SNIPPET):] if key.startswith(SNIPPET) else DOCS / lc / key


def mkey(lc, key):
    return f"snippets/{lc}/{key[len(SNIPPET):]}" if key.startswith(SNIPPET) else f"{lc}/{key}"


def translated_units(lc):
    """(key, path) of every translated file of a locale."""
    out = []
    for base, prefix in ((DOCS / lc, ""), (SNIPPETS / lc, SNIPPET)):
        if base.exists():
            out += [(prefix + p.relative_to(base).as_posix(), p) for p in sorted(base.rglob("*.md*"))]
    return out


def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()


def load_json(path, default):
    return json.loads(path.read_text()) if path.exists() else default


def save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1, sort_keys=True) + "\n")


def stale_pairs(locales, keys):
    manifest = load_json(MANIFEST, {})
    hashes = {k: sha(src_path(k).read_text()) for k in keys}
    return [(lc, k, hashes[k]) for lc in locales for k in keys if manifest.get(mkey(lc, k)) != hashes[k]]


def prune_deleted():
    """Delete translations (and manifest entries) whose English source no longer exists or is no longer used."""
    english = set(english_units())
    live = {mkey(lc, k) for lc in LOCALES for k in english}
    manifest = load_json(MANIFEST, {})
    removed = []
    for lc in LOCALES:
        for key, p in translated_units(lc):
            if key not in english:
                p.unlink()
                removed.append(mkey(lc, key))
    for k in [k for k in manifest if k not in live]:
        manifest.pop(k)
        removed.append(k)
    save_json(MANIFEST, manifest)
    if removed:
        for lc in LOCALES:
            link_snippets(lc)
    return sorted(set(removed))


def link_snippets(lc):
    """Point snippet imports in a locale's translated files at the translated snippet when it exists."""
    for _, p in translated_units(lc):
        text = p.read_text()
        new = re.sub(r"^(import .*)$", lambda m: SNIPPET_IMPORT_RE.sub(
            lambda i: f"{i.group(1)}@snippets/{lc + '/' if (SNIPPETS / lc / i.group(2)).is_file() else ''}"
                      f"{i.group(2)}{i.group(1)}", m.group(1)), text, flags=re.M)
        if new != text:
            p.write_text(new)


# ---------------------------------------------------------------- glossary

def parse_po(text):
    """msgid -> msgstr for translated, non-fuzzy, non-plural entries."""
    out = {}
    for block in re.split(r"\n\s*\n", text):
        if "#, fuzzy" in block or "msgid_plural" in block:
            continue
        fields, key = {}, None
        for line in block.splitlines():
            m = re.match(r'(msgctxt|msgid|msgstr)\s+"(.*)"\s*$', line)
            if m:
                key = m.group(1)
                fields[key] = m.group(2)
            elif key and re.match(r'\s*"(.*)"\s*$', line):
                fields[key] += re.match(r'\s*"(.*)"\s*$', line).group(1)
        msgid, msgstr = fields.get("msgid"), fields.get("msgstr")
        if not msgid or not msgstr:
            continue
        unescape = lambda s: re.sub(r"\\(.)", lambda m: {"n": "\n", "t": "\t"}.get(m.group(1), m.group(1)), s)
        out.setdefault(unescape(msgid), unescape(msgstr))
    return out


def build_glossaries():
    for lc, (_, _, po, _) in LOCALES.items():
        text = subprocess.run(
            ["git", "-C", str(PLAIDCLIENT), "show", f"origin/master:plaid/source/translation/{po}.po"],
            check=True, capture_output=True, text=True).stdout
        # Only label-like strings can match a page (bold UI labels, Title-Case phrases).
        entries = {k: v for k, v in parse_po(text).items() if "%" not in k and "\n" not in k and len(k) <= 80}
        save_json(GLOSSARY_DIR / f"{lc}.json", entries)
        print(f"{lc}: {len(entries)} entries")


def load_glossary(lc):
    """PlaidClient catalog with the docs-side overrides applied (a null override drops the entry)."""
    glossary = load_json(GLOSSARY_DIR / f"{lc}.json", {})
    for k, v in load_json(OVERRIDES_DIR / f"{lc}.json", {}).items():
        if v is None:
            glossary.pop(k, None)
        else:
            glossary[k] = v
    return glossary


def page_terms(src):
    """UI strings the page uses: bolded labels plus multi-word Title-Case phrases (locale-independent)."""
    prose = strip_code(split_frontmatter(src)[1])
    bold = re.findall(r"\*\*([^*\n]+?)\*\*", prose)
    words = re.findall(r"[^\s*`\[\]()|<>\"]+", re.sub(r"\]\([^)]*\)", "]", prose))
    phrases = []
    for i in range(len(words)):
        for n in range(2, 7):
            if i + n <= len(words):
                phrases.append(" ".join(words[i:i + n]).rstrip(".,;:"))
    return bold, phrases


def label_variants(label):
    """Catalog spellings a bold label may correspond to: trailing punctuation/ellipsis on or off, singular/plural."""
    base = label.strip().rstrip(":?…. ").strip()
    out = [label, base, base + "…", base + "...", base + ":", base + "?"]
    out += [base[:-1]] if base.endswith("s") else [base + "s"]
    return [v for v in dict.fromkeys(out) if v]


def lookup_label(label, glossary, lower):
    for v in label_variants(label):
        if v in glossary:
            return v, glossary[v]
    for v in label_variants(label):
        if v.lower() in lower:
            return lower[v.lower()], glossary[lower[v.lower()]]
    return None


def page_glossary(terms, glossary, limit=250):
    bold, phrases = terms
    lower = {}
    for k in glossary:
        lower.setdefault(k.lower(), k)
    out = {}
    for label in bold:
        hit = lookup_label(label, glossary, lower)
        if hit:
            out[hit[0]] = hit[1]
        elif " / " in label:  # build a joined label from its parts
            parts = [lookup_label(p, glossary, lower) for p in label.split(" / ")]
            if all(parts):
                out[label] = " / ".join(h[1] for h in parts)
    for ph in phrases:
        if ph in glossary and ph[:1].isupper() and len(out) < limit:
            out[ph] = glossary[ph]
    return dict(list(out.items())[:limit])


STEP_NAMES = None


def step_names():
    """English titles of the workflow-step reference pages (the step type names)."""
    global STEP_NAMES
    if STEP_NAMES is None:
        STEP_NAMES = sorted({yaml.safe_load(split_frontmatter(p.read_text())[0])["title"]
                             for p in (DOCS / "reference/workflow-steps").rglob("*.md*")
                             if p.stem != "index" and p.parent.name != "common"})
    return STEP_NAMES


# ---------------------------------------------------------------- prompt

def system_prompt(lc):
    tag, name, _, voice = LOCALES[lc]
    termbase = load_json(TERMBASE_DIR / f"{lc}.json", {})
    glossary = load_glossary(lc)
    steps = "\n".join(f"- {n} → {glossary[n]}" if n in glossary else f"- {n}" for n in step_names())
    cjk = ("\n- Bold markers: put a space outside a `**` marker only when the bold text starts or ends with punctuation "
           "AND the character on that outer side is a letter or CJK character; otherwise Markdown does not render the bold. "
           "Never put a space between `**` and following punctuation (。、，：）), and never add a sentence-ending mark the "
           "bold text already ends with." if lc in CJK else "")
    if lc in ("ja", "ko"):
        cjk += (" When a bold UI label ends with punctuation (…, ?, ）), follow it with a noun "
                + ("(ボタン, メニュー, タブ)" if lc == "ja" else "(버튼, 메뉴, 옵션, 탭)") + ", never a bare particle.")
    return f"""You are a professional technical translator localizing the PlaidCloud product documentation from English into {name} ({tag}). Each request contains one page of an Astro Starlight documentation site (Markdown or MDX). You return the same page, fully translated, with its structure untouched.

## Register and voice
- {voice}
- Technical-documentation register: clear, concise, natural {name}, as a senior technical writer at a software company would write it. Translate the meaning, not word by word; avoid calques. When a term has two senses (model vs template), choose distinct words.
- Headings, page titles and sidebar labels: use normal {name} capitalization; do not copy English Title Case.{cjk}

## Terminology
- Termbase: use these renderings for these concepts everywhere (prose, lists, tables, bold labels, SVG text), one term per concept across all pages. Adjust capitalization, number and inflection to the sentence.
{chr(10).join(f"  - {k} → {v}" for k, v in termbase.items())}
- Glossary: the request contains a <glossary> of PlaidCloud UI strings with their official {name} translations from the product's own UI catalog. When the English text names an on-screen UI element (a button, menu, tab, panel, field, dialog or option), use the glossary translation exactly, character for character. Apply glossary and termbase translations to UI option values and concept names wherever they appear (plain list items, table cells, SVG text), not only in bold.
- If a glossary entry's sense clearly doesn't fit the context (verb vs noun on a button, geographic location vs file location), use the fitting word in the termbase's style.
- Only exact on-screen labels count as UI labels. Bold concept names, dimension or dataset names (Product, Department, Customer, Budget) and generic elements are prose: translate them. Plain-text table cells are prose: always translate them.
- A bold on-screen label absent from the glossary stays exactly in English, consistently in every occurrence on every page; never translate it in one place and not another. But never leave one item of a list or table in English while its siblings are translated: if a sibling is translated, translate the rest to match, in the termbase's style.
- Workflow step type names (the step names listed below, e.g. Import CSV, Table Extract) stay in English in titles, link text and prose, followed by your language's word for step, unless the list gives a glossary form after →; then use that form everywhere, including link text.
- These product and module names stay in English in prose: {", ".join(KEEP_ENGLISH)}. Third-party product names (Snowflake, SAP, Excel, Databricks, Alteryx, Python, …) also stay as written.
- Technical identifiers stay in English: function, column, table, variable, file and API field names, SQL keywords, and anything in code formatting.

## What to translate
- Prose, headings, list items, table cells, admonition bodies, link text and image alt text.
- Frontmatter: only the values of `title`, `description`, `sidebar.label`, `hero.title`, `hero.tagline` and `hero.actions[].text`. Every other frontmatter key and value stays identical. Keep the YAML valid: quote a value that contains `: ` or starts with a special character. The `description` must stay under 480 characters; condense if the translation runs long.
- Human-readable attribute values in HTML/JSX tags: `title`, `description`, `label`, `alt`, `aria-label`, `caption`, `placeholder`, `text`; and the text content of `<figcaption>` and SVG `<text>`/`<tspan>` elements.

## Never change
- Fenced code blocks (``` or ~~~) and everything inside them, including comments: copy them byte for byte.
- Inline code spans (`like this`): copy them exactly; never translate inside backticks.
- Link targets and URLs, including `#anchor` fragments, in Markdown links, reference definitions and `href`/`src`/`link` values. Translate the link text; copy link targets exactly (the build adds language prefixes and fixes anchors).
- `import`/`export` lines.
- HTML/JSX tag names, attribute names, and every attribute value not listed above (ids, classes, styles, viewBox, coordinates, `type="note"`, `{{expressions}}`).
- HTML entities such as `&lt;` `&gt;` `&amp;` `&#123;` `&#125;`: keep them as entities.
- Markdown structure: the same headings in the same order and levels, the same list items, the same table rows and columns, the same bold and italic spans, the same admonition markers (`:::note` … `:::`), and the same blank lines around HTML/JSX blocks. Never add, remove, merge, split or reorder sections, list items, table rows, links, code or components. Do not add custom heading ids, translator notes or comments.

## Workflow step names
{steps}

## Output
Return only the complete translated file, starting with its first line (the opening `---` when it has frontmatter). No preamble, no explanation, no wrapping code fence. Translate the whole page however long it is."""


MDX_RULE = ("This is an MDX file: never introduce a bare `{`, `}` or `<` in prose (MDX parses them as JSX); "
            "if the translation needs one, use `&#123;`, `&#125;` or `&lt;`. Never add HTML comments.")
MD_RULE = "This is a plain Markdown file."
SNIPPET_NOTE = " It is a reusable fragment that several pages include; it has no frontmatter of its own."


def file_rule(rel):
    return (MDX_RULE if rel.endswith(".mdx") else MD_RULE) + (SNIPPET_NOTE if rel.startswith(SNIPPET) else "")


def user_message(rel, src, gloss):
    rule = file_rule(rel)
    return (f"<glossary>\n{json.dumps(gloss, ensure_ascii=False, indent=0)}\n</glossary>\n\n"
            f"{rule}\n\n<page path=\"{rel}\">\n{src}</page>")


def custom_id(lc, rel):
    # custom_id must match ^[a-zA-Z0-9_-]{1,64}$; the batch record maps it back to (locale, path).
    return f"{lc}-{hashlib.sha1(rel.encode()).hexdigest()[:24]}"


def max_tokens(src):
    return min(64_000, 8_000 + len(src) // 2)


def request_params(lc, rel, src, gloss):
    return {
        "model": MODEL,
        "max_tokens": max_tokens(src),
        "output_config": {"effort": EFFORT},
        "system": [{"type": "text", "text": system_prompt(lc), "cache_control": {"type": "ephemeral"}}],
        "messages": [{"role": "user", "content": user_message(rel, src, gloss)}],
    }


# ---------------------------------------------------------------- markdown parsing helpers

def split_frontmatter(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    return (m.group(1), text[m.end():]) if m else (None, text)


FENCE_RE = re.compile(r"^([ \t]*)(`{3,}|~{3,})[^\n]*\n.*?^[ \t]*\2[`~]*[ \t]*$", re.M | re.S)
# A code span may wrap onto the next line (CommonMark turns the line ending into a space), never past a blank line.
INLINE_CODE_RE = re.compile(r"(?<!`)(`+)(?!`)((?:[^\n]|\n(?![ \t]*\n))+?)(?<!`)\1(?!`)")


def fences(body):
    return [m.group(0) for m in FENCE_RE.finditer(body)]


def strip_code(body):
    """Body with fenced blocks and inline code removed (what the reader sees as prose + markup)."""
    return INLINE_CODE_RE.sub(" ", FENCE_RE.sub("\n", body))


def headings(body):
    """[(level, text-as-rendered)] for ATX headings outside code fences.

    Imported `@snippets/` components are compiled separately with their own slugger, so their headings
    never affect this page's slugs and are not included.
    """
    out = []
    for line in FENCE_RE.sub("\n", body).splitlines():
        m = re.match(r"^(#{1,6})[ \t]+(.*?)(?:[ \t]+#+)?[ \t]*$", line)
        if m:
            out.append((len(m.group(1)), heading_text(m.group(2))))
    return out


def heading_text(md):
    t = INLINE_CODE_RE.sub(lambda m: m.group(2).strip(), md)
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", t)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"</?[A-Za-z][A-Za-z0-9-]*(?:\s[^>]*)?/?>", "", t)  # CommonMark tag names only; <column_name> is text
    t = re.sub(r"(\*\*|__|\*)", "", t)
    t = re.sub(r"\\([\\`*_{}\[\]()#+\-.!])", r"\1", t)
    return html.unescape(t)


def slugify_pages(heading_lists):
    """github-slugger (the exact package Astro uses) over each page's heading list, via node."""
    script = ("import('github-slugger').then(({default: S}) => {"
              "const pages = JSON.parse(require('fs').readFileSync(0, 'utf8'));"
              "console.log(JSON.stringify(pages.map(hs => { const s = new S(); return hs.map(h => s.slug(h)); })));})")
    out = subprocess.run(["node", "-e", script], input=json.dumps(heading_lists), cwd=Path(__file__).resolve().parent,
                         check=True, capture_output=True, text=True).stdout
    return json.loads(out)


LINK_RE = re.compile(r"(\]\()([^)\s]+)((?:\s+\"[^\"]*\")?\))")
REFDEF_RE = re.compile(r"^(\s*\[[^\]]+\]:\s+)(\S+)", re.M)
ATTR_LINK_RE = re.compile(r"(\b(?:href|link)=[\"'])([^\"']+)([\"'])")
FM_LINK_RE = re.compile(r"^(\s*-?\s*link:\s*)(\S+)", re.M)


def link_targets(text):
    body = strip_code(text)
    return ([m.group(2) for m in LINK_RE.finditer(body)] + [m.group(2) for m in REFDEF_RE.finditer(body)]
            + [m.group(2) for m in ATTR_LINK_RE.finditer(body)])


TAG_RE = re.compile(r"<(/?)([A-Za-z][\w.:-]*)((?:[^<>\"'{}]|\"[^\"]*\"|'[^']*'|\{[^{}]*\})*?)(/?)>", re.S)
ATTR_RE = re.compile(r"([\w:.-]+)(?:\s*=\s*(\"[^\"]*\"|'[^']*'|\{[^{}]*\}))?")


def tags(text):
    """Tag sequence with the non-translatable attributes, locale prefixes normalized."""
    out = []
    for m in TAG_RE.finditer(strip_code(text)):
        attrs = tuple(sorted((k, unlocalize(v or "")) for k, v in ATTR_RE.findall(m.group(3))
                             if k not in ATTR_TRANSLATABLE))
        out.append((m.group(1), m.group(2), attrs, m.group(4)))
    return out


LOCALE_PREFIX_RE = re.compile(r"(^|[\"'(])/(?:" + "|".join(map(re.escape, LOCALES)) + r")(?=/)")


def unlocalize(target):
    return LOCALE_PREFIX_RE.sub(r"\1", target)


def normalize_target(t):
    return unlocalize(t).split("#", 1)[0]


# ---------------------------------------------------------------- validator

def fm_values(node, path=()):
    """{path: value} for leaves, with list indexes as '*' wildcard for the translatable check."""
    if isinstance(node, dict):
        out = {}
        for k, v in node.items():
            out.update(fm_values(v, path + (str(k),)))
        return out
    if isinstance(node, list):
        out = {path + ("#len",): len(node)}
        for i, v in enumerate(node):
            out.update(fm_values(v, path + (str(i),)))
        return out
    return {path: node}


def translatable(path):
    generic = tuple("*" if p.isdigit() else p for p in path)
    return generic in FM_TRANSLATABLE


# An ESM line, not a wrapped prose line that happens to start with "export it as CSV…".
ESM_RE = re.compile(r"""import\s+(?:['"]|[\w*{].*\bfrom\s+['"])|export\s+(?:const|let|var|function|class|default|\{|\*)""")


def validate(rel, src, out):
    """Return a list of reasons the translation is structurally unsafe; empty means accept."""
    reasons = []
    sfm, sbody = split_frontmatter(src)
    ofm, obody = split_frontmatter(out)
    if (sfm is None) != (ofm is None):
        return ["frontmatter missing" if ofm is None else "frontmatter added"]
    try:
        so, oo = yaml.safe_load(sfm or "") or {}, yaml.safe_load(ofm or "") or {}
    except yaml.YAMLError as e:
        return [f"frontmatter not valid YAML: {str(e).splitlines()[0]}"]
    if "editUrl" in oo and "editUrl" not in so:
        # The only key post-processing adds: "Edit page" on a translation opens its English source.
        if rel.startswith(SNIPPET) or oo.pop("editUrl") != EDIT_BASE + rel:
            reasons.append("frontmatter editUrl is not the English source's edit URL")
    sv, ov = fm_values(so), fm_values(oo)
    if sv.keys() != ov.keys():
        reasons.append(f"frontmatter keys differ: {sorted(set(map('.'.join, sv.keys() ^ ov.keys())))}")
    else:
        for p in sv:
            if translatable(p):
                if not isinstance(ov[p], str) or not ov[p].strip():
                    reasons.append(f"frontmatter {'.'.join(p)} empty")
            elif unlocalize(str(sv[p])) != unlocalize(str(ov[p])):
                reasons.append(f"frontmatter {'.'.join(p)} changed")
    if fences(sbody) != fences(obody):
        reasons.append(f"code fences differ ({len(fences(sbody))} vs {len(fences(obody))} blocks)")
    spans = lambda b: Counter(re.sub(r"[ \t]*\n[ \t]*", " ", m.group(0)) for m in INLINE_CODE_RE.finditer(FENCE_RE.sub("\n", b)))
    sic, oic = spans(sbody), spans(obody)
    if sic != oic:
        reasons.append(f"inline code differs: missing {list((sic - oic).elements())[:5]} extra {list((oic - sic).elements())[:5]}")
    imports = lambda b: [SNIPPET_IMPORT_RE.sub(r"\1@snippets/\2\1", l)
                         for l in FENCE_RE.sub("\n", b).splitlines() if ESM_RE.match(l)]
    if imports(sbody) != imports(obody):
        reasons.append("import/export lines differ")
    sh, oh = [h[0] for h in headings(sbody)], [h[0] for h in headings(obody)]
    if sh != oh:
        reasons.append(f"heading levels differ: {Counter(sh)} vs {Counter(oh)}")
    sl, ol = Counter(map(normalize_target, link_targets(sbody))), Counter(map(normalize_target, link_targets(obody)))
    if sl != ol:
        reasons.append(f"link targets differ: missing {list((sl - ol).elements())[:5]} extra {list((ol - sl).elements())[:5]}")
    st, ot = tags(sbody), tags(obody)
    if st != ot:
        diff = next((i for i, (a, b) in enumerate(zip(st, ot)) if a != b), min(len(st), len(ot)))
        reasons.append(f"tag sequence differs at #{diff} ({len(st)} vs {len(ot)} tags): "
                       f"{st[diff][1] if diff < len(st) else '-'} vs {ot[diff][1] if diff < len(ot) else '-'}")
    prose_s, prose_o = strip_code(sbody), strip_code(obody)
    for name, rx in (("admonition markers", r"^[ \t>]*:::.*$"), ("table rows", r"^[ \t>]*\|.*$"),
                     ("list items", r"^[ \t>]*(?:[-*+]|\d+[.)])[ \t]+")):
        a, b = len(re.findall(rx, prose_s, re.M)), len(re.findall(rx, prose_o, re.M))
        if a != b:
            reasons.append(f"{name} count differs ({a} vs {b})")
    if rel.endswith(".mdx"):
        no_tags = lambda t: TAG_RE.sub("", t)
        for ch in "{}<":
            a, b = no_tags(prose_s).count(ch), no_tags(prose_o).count(ch)
            if a != b:
                reasons.append(f"bare '{ch}' count differs in MDX prose ({a} vs {b})")
        if "<!--" in obody and "<!--" not in sbody:
            reasons.append("HTML comment added to MDX")
    a, b = unrendered_bold(sbody), unrendered_bold(obody)
    if b > a:
        reasons.append(f"{b - a} bold marker(s) left as literal ** after CommonMark rendering (flanking rules; "
                       "e.g. **English (US)**를 needs a space after **)")
    for key, (lo, hi) in schema_limits().items():
        v = oo.get(key)
        if isinstance(v, str) and not lo <= len(v) <= hi:
            reasons.append(f"frontmatter {key} length {len(v)} outside content schema {lo}..{hi}")
    return reasons


MD = None


@functools.lru_cache(maxsize=4096)  # English sources are re-checked once per locale
def unrendered_bold(body):
    """Literal `**` left in the CommonMark rendering (outside code): a bold that does not render.

    Compared against the English page, since `**` inside raw HTML/JSX blocks is legitimately left for MDX.
    """
    global MD
    if MD is None:
        from markdown_it import MarkdownIt
        MD = MarkdownIt("commonmark", {"html": True})
    html_out = re.sub(r"<code>.*?</code>", "", MD.render(FENCE_RE.sub("\n", body)), flags=re.S)
    return html_out.count("**")


SCHEMA = None


def schema_limits():
    """Top-level frontmatter string limits declared in src/content.config.* (z.string().min(a).max(b))."""
    global SCHEMA
    if SCHEMA is None:
        SCHEMA = {}
        for cfg in ROOT.glob("src/content.config.*"):
            for key, chain in re.findall(r"(\w+):\s*z\.string\(\)((?:\.\w+\([^)]*\))*)", cfg.read_text()):
                lo = re.search(r"\.min\((\d+)\)", chain)
                hi = re.search(r"\.max\((\d+)\)", chain)
                if lo or hi:
                    SCHEMA[key] = (int(lo.group(1)) if lo else 0, int(hi.group(1)) if hi else 10**9)
    return SCHEMA


# ---------------------------------------------------------------- post-processing

PAGE_URLS = None


def page_url(rel):
    stem = re.sub(r"\.mdx?$", "", rel)
    stem = stem[:-len("index")] if stem == "index" or stem.endswith("/index") else stem + "/"
    return "/" + stem


def page_for_url(path):
    """English page rel path for a root-relative docs URL, or None."""
    global PAGE_URLS
    if PAGE_URLS is None:
        PAGE_URLS = {page_url(rel): rel for rel in english_pages()}
    path = path if path.endswith("/") else path + "/"
    return PAGE_URLS.get(path)


def localize_url(target, lc):
    path, frag = (target.split("#", 1) + [None])[:2]
    if (not path.startswith("/") or path.startswith("//") or path.startswith(NON_PAGE_PREFIXES)
            or LOCALE_PREFIX_RE.match(path) or "." in path.rsplit("/", 1)[-1] or page_for_url(path) is None):
        return target
    return f"/{lc}{path}" + (f"#{frag}" if frag is not None else "")


# Fenced blocks or inline spans (inline backreference renumbered to \3; spans stay on one line).
CODE_RE = re.compile(FENCE_RE.pattern + r"|(?<!`)(`+)(?!`)[^\n]+?(?<!`)\3(?!`)", re.M | re.S)


def rewrite_targets(text, fn):
    """Apply fn to every link target in a page body, leaving code untouched."""
    def chunk_fn(chunk):
        for rx in (LINK_RE, REFDEF_RE, ATTR_LINK_RE):
            chunk = rx.sub(lambda m: m.group(1) + fn(m.group(2)) + (m.group(3) if m.lastindex >= 3 else ""), chunk)
        return chunk
    out, i = [], 0
    for m in CODE_RE.finditer(text):
        out += [chunk_fn(text[i:m.start()]), m.group(0)]
        i = m.end()
    return "".join(out) + chunk_fn(text[i:])


def localize_links(text, lc):
    fm, body = split_frontmatter(text)
    body = rewrite_targets(body, lambda t: localize_url(t, lc))
    if fm is None:
        return body
    fm = FM_LINK_RE.sub(lambda m: m.group(1) + localize_url(m.group(2), lc), fm)
    return f"---\n{fm}\n---\n{body}"


def set_edit_url(text, key):
    """Point a translated page's "Edit page" link at its English source (translations are generated)."""
    fm, body = split_frontmatter(text)
    if fm is None or key.startswith(SNIPPET) or re.search(r"^editUrl:", fm, re.M):
        return text
    return f"---\n{fm}\neditUrl: {EDIT_BASE}{key}\n---\n{body}"


def rewrite_anchors(lc):
    """Map English heading slugs to translated ones in every link of every translated page of a locale.

    Fragments are resolved against the target page: an English slug is replaced by the translated slug at
    the same heading position; a fragment already matching a translated slug is kept; a target without a
    translation keeps the English anchor (Starlight serves the English fallback there).
    """
    ldir = DOCS / lc
    translated = sorted(p.relative_to(ldir).as_posix() for p in ldir.rglob("*.md*")) if ldir.exists() else []
    if not translated:
        return 0
    # Each imported snippet is compiled with its own slugger, so its headings are mapped separately and merged
    # into every page that (transitively) imports it.
    snippets = [k[len(SNIPPET):] for k, _ in translated_units(lc) if k.startswith(SNIPPET)]
    hs = lambda p: [h[1] for h in headings(split_frontmatter(p.read_text())[1])]
    lists = ([hs(DOCS / r) for r in translated] + [hs(ldir / r) for r in translated]
             + [hs(SNIPPETS / f) for f in snippets] + [hs(SNIPPETS / lc / f) for f in snippets])
    slugs = slugify_pages(lists)
    n, m = len(translated), len(snippets)
    pair = lambda es, ts: dict(zip(es, ts)) if len(es) == len(ts) else {}
    snip = {f: (pair(slugs[2 * n + i], slugs[2 * n + m + i]), set(slugs[2 * n + m + i])) for i, f in enumerate(snippets)}

    def imported(text, seen):
        for _, f in SNIPPET_IMPORT_RE.findall(text):
            if f not in seen and (SNIPPETS / f).is_file():
                seen.add(f)
                imported((SNIPPETS / f).read_text(), seen)
        return seen

    maps = {}
    for i, rel in enumerate(translated):
        mapping, tslugs = pair(slugs[i], slugs[n + i]), set(slugs[n + i])
        for f in imported((DOCS / rel).read_text(), set()) & snip.keys():
            for es, ts in snip[f][0].items():
                mapping.setdefault(es, ts)
            tslugs |= snip[f][1]
        maps[rel] = (mapping, tslugs)

    def fix(target, rel, english):
        """`english` is the English page's link to the same target at the same position, when the pages line up."""
        if "#" not in target:
            return target
        path, frag = target.split("#", 1)
        frag = urllib.parse.unquote(frag)
        if not path:
            dest = rel
        elif path.startswith("/"):
            dest = page_for_url(unlocalize(path))
        elif re.match(r"[a-z]+:", path) or rel is None:
            return target
        else:
            dest = page_for_url(posixpath.normpath(posixpath.join(page_url(rel), path)) + "/")
        if dest is None:
            return target
        # The English anchor is authoritative: translators sometimes rewrite one, and a target page can change
        # (re-translated with new headings, or back to an English fallback) after this link was mapped.
        if english and "#" in english:
            frag = urllib.parse.unquote(english.split("#", 1)[1])
        if dest not in maps:
            return target if not english else f"{path}#{frag}"
        mapping, tslugs = maps[dest]
        if frag in mapping:
            return f"{path}#{mapping[frag]}"
        if frag in tslugs:
            return f"{path}#{frag}"
        close = difflib.get_close_matches(frag, tslugs, n=1, cutoff=0.75)
        return f"{path}#{close[0]}" if close else target

    def by_path(body):
        seq = defaultdict(list)
        rewrite_targets(body, lambda t: seq[normalize_target(t)].append(t) or t)
        return seq

    # A snippet has no URL of its own (its relative links resolve per importing page), so only its absolute
    # links are mapped; `rel=None` marks it.
    changed = 0
    for p, rel, src in ([(ldir / r, r, DOCS / r) for r in translated]
                        + [(SNIPPETS / lc / f, None, SNIPPETS / f) for f in snippets]):
        text = p.read_text()
        fm, body = split_frontmatter(text)
        eng, ours, seen = by_path(split_frontmatter(src.read_text())[1]), by_path(body), Counter()

        def positional(t, rel=rel, eng=eng, ours=ours, seen=seen):
            k = normalize_target(t)
            i, seen[k] = seen[k], seen[k] + 1
            return fix(t, rel, eng[k][i] if len(eng[k]) == len(ours[k]) else None)

        new = ("" if fm is None else f"---\n{fm}\n---\n") + rewrite_targets(body, positional)
        if new != text:
            p.write_text(new)
            changed += 1
    return changed


def clean_output(src, text):
    """Strip what a translator wraps around the file: a whole-file code fence or a preamble before the frontmatter."""
    text = text.strip("\n")
    m = re.match(r"^(`{3,}|~{3,})[\w-]*\n(.*)\n\1$", text, re.S)
    if m and not src.lstrip().startswith(m.group(1)):
        text = m.group(2).strip("\n")
    if src.startswith("---\n") and not text.startswith("---\n"):
        m = re.search(r"^---\n", text, re.M)
        if m:
            text = text[m.start():]
            m = re.match(r"^(.*)\n(`{3,}|~{3,})[\w-]*\n?$", text, re.S)  # fence opened in the preamble
            text = m.group(1) if m and text.count(m.group(2)) % 2 else text
    return text + "\n"


FM_SCALAR_RE = re.compile(r"^(\s*(?:- )?[\w.-]+:[ \t]+)(?![\"'\[{|>&*!])(.+?)[ \t]*$", re.M)


def quote_frontmatter(text):
    """Translations add ': ' or ' #' to plain YAML scalars (e.g. "Referenz für X: Y"); double-quote those values."""
    fm, body = split_frontmatter(text)
    if fm is None:
        return text
    try:
        yaml.safe_load(fm)
        return text
    except yaml.YAMLError:
        pass
    fm = FM_SCALAR_RE.sub(lambda m: m[1] + (json.dumps(m[2], ensure_ascii=False) if ": " in m[2] or " #" in m[2] else m[2]), fm)
    return f"---\n{fm}\n---\n{body}"


def _punct(c):
    return unicodedata.category(c)[0] in "PS"


def fix_bold_flanking(text):
    """`**「設定」**を` never renders: CommonMark needs a space where a `**` sits between punctuation and a letter.

    CJK has no word spaces, so translations hit this constantly. Add the one space each failing marker needs;
    keep the result only if fewer `**` are left unrendered.
    """
    fm, body = split_frontmatter(text)
    before = unrendered_bold(body)
    if not before:
        return text
    spans = [(m.start(), m.end()) for m in FENCE_RE.finditer(body)]
    out, pos = [], 0
    for line_start, line in ((m.start(), m.group(0)) for m in re.finditer(r"[^\n]*\n?", body) if m.group(0)):
        if any(a <= line_start < b for a, b in spans):
            out.append(line)
            continue
        masked = INLINE_CODE_RE.sub(lambda m: "\0" * len(m.group(0)), line)
        marks = [m.start() for m in re.finditer(r"(?<!\*)\*\*(?!\*)", masked)]
        inserts = []
        for i, at in enumerate(marks[: len(marks) // 2 * 2]):
            prev = line[at - 1] if at else " "
            nxt = line[at + 2] if at + 2 < len(line) else " "
            if i % 2 == 0 and _punct(nxt) and not (prev.isspace() or _punct(prev)):
                inserts.append(at)
            elif i % 2 == 1 and _punct(prev) and not (nxt.isspace() or _punct(nxt)):
                inserts.append(at + 2)
        for at in reversed(inserts):
            line = line[:at] + " " + line[at:]
        out.append(line)
    fixed = "".join(out)
    if unrendered_bold(fixed) >= before:
        return text
    return text if fm is None else f"---\n{fm}\n---\n{fixed}"


def finalize(lc, key, src, raw):
    """Post-process a raw translation exactly as collect/ingest write it; returns (text, rejection reasons)."""
    text = set_edit_url(localize_links(fix_bold_flanking(quote_frontmatter(clean_output(src, raw))), lc), key)
    return text, validate(key, src, text)


# ---------------------------------------------------------------- commands

def select_units(globs):
    """Pages and snippets to consider; globs match page paths or "@snippets/<file>"."""
    keys = english_units()
    return [k for k in keys if any(fnmatch.fnmatch(k, g) for g in globs)] if globs else keys


def cmd_glossary(args):
    build_glossaries()


def cmd_plan(args):
    import anthropic
    pages = select_units(args.paths)
    pairs = stale_pairs(args.locales, pages)
    live = {mkey(lc, k) for lc in LOCALES for k in english_units()}
    orphans = [k for k in load_json(MANIFEST, {}) if k not in live]
    for lc in args.locales:
        print(f"{lc}: {sum(1 for p in pairs if p[0] == lc)} stale of {len(pages)} (pages + snippets)")
    print(f"deletions pending: {len(orphans)}")
    if args.verbose:
        for lc, rel, _ in pairs:
            print(f"  {lc}/{rel}")
    if not pairs or not args.count:
        return
    client = anthropic.Anthropic()
    sample = sorted({rel for _, rel, _ in pairs})[:: max(1, len({r for _, r, _ in pairs}) // args.count)][: args.count]
    glossary = load_glossary(args.locales[0])
    tok = chars = 0
    for rel in sample:
        src = src_path(rel).read_text()
        params = request_params(args.locales[0], rel, src, page_glossary(page_terms(src), glossary))
        tok += client.messages.count_tokens(model=MODEL, system=params["system"], messages=params["messages"]).input_tokens
        chars += len(src)
    per_char = tok / chars
    sys_tok = client.messages.count_tokens(model=MODEL, system=request_params(args.locales[0], "x.md", "", {})["system"],
                                           messages=[{"role": "user", "content": "x"}]).input_tokens
    total_chars = sum(len(src_path(rel).read_text()) for _, rel, _ in pairs)
    page_tok = total_chars * per_char - len(pairs) * sys_tok
    in_tok = page_tok + len(pairs) * sys_tok
    out_tok = page_tok * 1.3  # translation is ~1.0-1.6x the English tokens depending on script; plus low-effort thinking
    cost = (page_tok * PRICE["input"] + len(pairs) * sys_tok * PRICE["cache_read"] + out_tok * PRICE["output"]) / 1e6
    print(f"sampled {len(sample)} pages: {per_char:.3f} tokens/char, system prompt {sys_tok} tokens")
    print(f"estimate: {in_tok / 1e6:.1f}M input, ~{out_tok / 1e6:.1f}M output, ~${cost:,.0f} at batch rates "
          "(the pilot's measured usage is the better number)")


def cmd_submit(args):
    import anthropic
    from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
    from anthropic.types.messages.batch_create_params import Request

    removed = prune_deleted()
    if removed:
        print(f"deleted {len(removed)} translations of removed pages")
    pairs = stale_pairs(args.locales, select_units(args.paths))[: args.limit]
    if not pairs:
        print("nothing stale")
        return
    glossaries = {lc: load_glossary(lc) for lc in args.locales}
    if not all(glossaries.values()):
        sys.exit("missing i18n/glossary/<locale>.json; run `translate.py glossary` first")
    terms = {}
    chunks, chunk, size = [], [], 0
    for lc, rel, h in pairs:
        src = src_path(rel).read_text()
        terms.setdefault(rel, page_terms(src))
        params = request_params(lc, rel, src, page_glossary(terms[rel], glossaries[lc]))
        n = len(json.dumps(params))
        if chunk and (len(chunk) >= MAX_BATCH_REQUESTS or size + n > MAX_BATCH_BYTES):
            chunks.append(chunk)
            chunk, size = [], 0
        chunk.append((lc, rel, h, params))
        size += n
    chunks.append(chunk)
    if args.dry_run:
        for chunk in chunks:
            print(f"dry run: {len(chunk)} requests, {sum(len(json.dumps(c[3])) for c in chunk) / 1e6:.1f} MB")
        return
    client = anthropic.Anthropic()
    for chunk in chunks:
        batch = client.messages.batches.create(requests=[
            Request(custom_id=custom_id(lc, rel), params=MessageCreateParamsNonStreaming(**params))
            for lc, rel, _, params in chunk])
        save_json(BATCH_DIR / f"{batch.id}.json", {
            "created": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "model": MODEL, "effort": EFFORT,
            "pairs": {custom_id(lc, rel): {"locale": lc, "path": rel, "sha": h} for lc, rel, h, _ in chunk}})
        print(f"{batch.id}: {len(chunk)} requests ({batch.processing_status})")


def cmd_collect(args):
    import anthropic
    client = anthropic.Anthropic()
    record_path = BATCH_DIR / f"{args.batch_id}.json"
    record = load_json(record_path, None)
    if record is None:
        sys.exit(f"no record {record_path}")
    while True:
        batch = client.messages.batches.retrieve(args.batch_id)
        if batch.processing_status == "ended":
            break
        c = batch.request_counts
        print(f"{time.strftime('%H:%M:%S')} {batch.processing_status}: processing={c.processing} "
              f"succeeded={c.succeeded} errored={c.errored}", flush=True)
        time.sleep(args.poll)
    manifest = load_json(MANIFEST, {})
    results, usage = {}, Counter()
    touched = {}
    for res in client.messages.batches.results(args.batch_id):
        pair = record["pairs"].get(res.custom_id)
        if pair is None:
            continue
        lc, rel = pair["locale"], pair["path"]
        entry = {"locale": lc, "path": rel, "status": res.result.type}
        if res.result.type != "succeeded":
            err = getattr(res.result, "error", None)
            entry["reasons"] = [str(getattr(err, "error", err))] if err else []
            results[res.custom_id] = entry
            continue
        msg = res.result.message
        u = msg.usage
        entry["usage"] = {"input": u.input_tokens, "output": u.output_tokens,
                          "cache_read": u.cache_read_input_tokens or 0, "cache_write": u.cache_creation_input_tokens or 0}
        usage.update(entry["usage"])
        src = src_path(rel).read_text()
        if sha(src) != pair["sha"]:
            entry.update(status="stale", reasons=["English source changed since submit"])
        elif msg.stop_reason != "end_turn":
            entry.update(status="rejected", reasons=[f"stop_reason {msg.stop_reason}"])
        else:
            text, reasons = finalize(lc, rel, src, "".join(b.text for b in msg.content if b.type == "text"))
            if reasons:
                entry.update(status="rejected", reasons=reasons)
            else:
                dest = out_path(lc, rel)
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(text)
                manifest[mkey(lc, rel)] = pair["sha"]
                touched.setdefault(lc, []).append(rel)
                entry["status"] = "written"
        results[res.custom_id] = entry
    save_json(MANIFEST, manifest)
    # Anchors need every target page's translated headings, so this runs over the whole locale.
    for lc in touched:
        link_snippets(lc)
        rewrite_anchors(lc)
    record["results"] = results
    record["ended"] = batch.ended_at.isoformat() if batch.ended_at else None
    record["usage"] = dict(usage)
    save_json(record_path, record)
    report(record, batch)


def cost(u):
    return sum(u.get(k, 0) * PRICE[k] for k in PRICE) / 1e6


def report(record, batch):
    results = record["results"]
    by_status = Counter(r["status"] for r in results.values())
    print(f"\n{len(results)} results: {dict(by_status)}")
    for r in sorted(results.values(), key=lambda r: (r["path"], r["locale"])):
        if r["status"] != "written":
            print(f"  {r['status']:9} {r['locale']}/{r['path']}: {'; '.join(r.get('reasons', []))}")
    u = record["usage"]
    print(f"usage: {u}  cost ${cost(u):.2f} at batch rates")
    words = Counter()
    for r in results.values():
        if "usage" in r:
            words[r["locale"]] += len(src_path(r["path"]).read_text().split())
    corpus_words = sum(len(src_path(k).read_text().split()) for k in english_units())
    per_locale = Counter()
    for r in results.values():
        if "usage" in r:
            per_locale[r["locale"]] += cost(r["usage"])
    full = sum(per_locale[lc] / words[lc] * corpus_words for lc in per_locale if words[lc])
    print(f"extrapolated full run ({corpus_words:,} English words x {len(per_locale)} locales): ${full:,.0f}")
    if batch.created_at and batch.ended_at:
        print(f"batch wall time: {batch.ended_at - batch.created_at}")


JOBS = I18N / "jobs"
STAGING = I18N / "staging"
WORKER_MD = """# Translation worker

You translate one chunk of PlaidCloud docs. Your task names a chunk file `i18n/jobs/<locale>/<NNN>.json`.

1. Read the chunk JSON, then read its `prompt_file` once. The prompt is your translator instructions; follow
   them exactly. Its per-file rules apply by extension (`.mdx` vs `.md`) and `kind` (`snippet`).
2. For each item, in order:
   - Read `source_file` (repo-relative).
   - Translate it. The item's `glossary` is the <glossary> the prompt refers to; apply it and the prompt's
     termbase exactly as the prompt's Terminology section says (UI labels anywhere, one term per concept).
   - Write ONLY the complete translated file to `output_file` (create parent dirs): no preamble, no commentary,
     no wrapping code fence. Overwrite if it exists.
3. Touch nothing else: no other files, no git, no builds, no scripts.
4. Finish with one line: `<chunk>: <written>/<total> written`, plus the paths of any item you could not finish.
"""


def rel_or_abs(path):
    return path.relative_to(ROOT).as_posix() if path.is_relative_to(ROOT) else str(path)


def cmd_prepare(args):
    out = ROOT / args.out
    removed = prune_deleted()
    if removed:
        print(f"deleted {len(removed)} translations of removed pages")
    pairs = stale_pairs(args.locales, select_units(args.paths))
    if args.force_paths:  # re-translate these even though the manifest says they are current
        have = {(lc, k) for lc, k, _ in pairs}
        pairs += [(lc, k, sha(src_path(k).read_text())) for lc in args.locales
                  for k in select_units(args.force_paths) if (lc, k) not in have]
    glossaries = {lc: load_glossary(lc) for lc in args.locales}
    (out / "prompts").mkdir(parents=True, exist_ok=True)
    (out / "WORKER.md").write_text(WORKER_MD)
    terms = {}
    for lc in args.locales:
        prompt_file = out / "prompts" / f"{lc}.md"
        prompt_file.write_text(system_prompt(lc) + "\n\n## Per-file rules\n"
                               f"- `.mdx` files: {MDX_RULE}\n- `.md` files: {MD_RULE}\n"
                               f"- Snippets (`kind: snippet`):{SNIPPET_NOTE}\n")
        for old in (out / lc).glob("*.json") if (out / lc).exists() else []:
            old.unlink()
        chunks, chunk, words = [], [], 0
        for _, key, h in (p for p in pairs if p[0] == lc):
            # A staged file left from an earlier prepare was made from older English; this chunk's sha must not vouch for it.
            (STAGING / lc / key).unlink(missing_ok=True)
            src = src_path(key).read_text()
            n = len(src.split())
            if chunk and words + n > args.chunk_words:
                chunks.append(chunk)
                chunk, words = [], 0
            terms.setdefault(key, page_terms(src))
            chunk.append({"path": key, "kind": "snippet" if key.startswith(SNIPPET) else "page", "sha": h, "words": n,
                          "source_file": src_path(key).relative_to(ROOT).as_posix(),
                          "glossary": page_glossary(terms[key], glossaries[lc]),
                          "output_file": (STAGING / lc / key).relative_to(ROOT).as_posix()})
            words += n
        if chunk:
            chunks.append(chunk)
        for i, items in enumerate(chunks, 1):
            save_json(out / lc / f"{i:03}.json", {"locale": lc, "prompt_file": rel_or_abs(prompt_file),
                                                   "items": items})
        print(f"{lc}: {len(chunks)} chunks, {sum(map(len, chunks))} units, "
              f"{sum(i['words'] for c in chunks for i in c):,} words")


def cmd_ingest(args):
    manifest = load_json(MANIFEST, {})
    # Every `prepare --out` dir counts; the most recently written chunk names the source a staged file was made from.
    chunks = sorted(JOBS.parent.glob(f"{JOBS.name}*/*/*.json"), key=lambda f: f.stat().st_mtime)
    prepared = {(j["locale"], i["path"]): i["sha"] for f in chunks for j in [load_json(f, {})] for i in j.get("items", [])}
    rejects_file = STAGING / "_rejects.json"
    rejects = load_json(rejects_file, [])
    passed, failed, why, touched = 0, 0, Counter(), set()
    for lc in args.locales:
        for f in sorted((STAGING / lc).rglob("*.md*")) if (STAGING / lc).exists() else []:
            key = f.relative_to(STAGING / lc).as_posix()
            if not src_path(key).is_file():
                reasons = ["no English source"]
            else:
                src = src_path(key).read_text()
                text, reasons = finalize(lc, key, src, f.read_text())
                if (lc, key) not in prepared:
                    reasons.append("not in any prepare chunk")
                elif prepared[(lc, key)] != sha(src):
                    reasons.append("English source changed since prepare")
            if reasons:
                failed += 1
                why.update(re.sub(r" at #\d+", "", r.split(":")[0].split(" (")[0]) for r in reasons)
                rejects = [r for r in rejects if (r["locale"], r["path"]) != (lc, key)]
                rejects.append({"locale": lc, "path": key, "reasons": reasons})
                print(f"  rejected {lc}/{key}: {'; '.join(reasons)}")
                continue
            dest = out_path(lc, key)
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(text)
            manifest[mkey(lc, key)] = sha(src)
            f.unlink()
            rejects = [r for r in rejects if (r["locale"], r["path"]) != (lc, key)]
            passed += 1
            touched.add(lc)
    save_json(MANIFEST, manifest)
    if rejects or rejects_file.exists():
        save_json(rejects_file, rejects)
    # Cross-page anchors need every translated target of the locale, so relink the whole locale, not just new files.
    for lc in args.locales:
        link_snippets(lc)
        rewrite_anchors(lc)
    print(f"ingested {passed} passed, {failed} rejected (kept in staging; see {rejects_file.relative_to(ROOT)})")
    for reason, n in why.most_common():
        print(f"  {n:4} {reason}")


def cmd_check_anchors(args):
    """Every /<locale>/…#frag link in the built site must hit an id on the target page."""
    dist = ROOT / args.dist
    ids, bad, total = {}, Counter(), 0
    href_re = re.compile(r'href="(/(?:' + "|".join(map(re.escape, LOCALES)) + r')/[^"#]*)#([^"]+)"')
    for page in sorted(dist.rglob("index.html")):
        for path, frag in href_re.findall(page.read_text()):
            frag = urllib.parse.unquote(html.unescape(frag))
            target = dist / path.strip("/") / "index.html"
            if target not in ids:
                ids[target] = set(map(html.unescape, re.findall(r'\bid="([^"]+)"', target.read_text()))) if target.exists() else None
            total += 1
            if ids[target] is not None and frag not in ids[target]:
                bad[(path, frag)] += 1
    for (path, frag), n in sorted(bad.items()):
        print(f"missing  {path}#{frag}  ({n} link{'s' if n > 1 else ''})")
    print(f"{total} locale anchor links checked: {sum(bad.values())} broken ({len(bad)} distinct)")
    sys.exit(1 if bad else 0)


def cmd_check(args):
    manifest = load_json(MANIFEST, {})
    english = set(english_units())
    bad = stale = total = 0
    for lc in LOCALES:
        for key, p in translated_units(lc):
            total += 1
            name = mkey(lc, key)
            if key not in english:
                print(f"orphan   {name}")
                bad += 1
                continue
            src, text = src_path(key).read_text(), p.read_text()
            reasons = validate(key, src, text)
            missing = [f for f in re.findall(rf"^import .*['\"]@snippets/{re.escape(lc)}/([^'\"]+)", text, re.M)
                       if not (SNIPPETS / lc / f).is_file()]
            reasons += [f"imports missing translated snippet {f}" for f in missing]
            if not key.startswith(SNIPPET) and set_edit_url(text, key) != text:
                reasons.append("editUrl missing")
            if reasons:
                bad += 1
                print(f"invalid  {name}: {'; '.join(reasons)}")
            if manifest.get(name) != sha(src):
                print(f"stale    {name}")
                stale += 1
    have = {(lc, key) for lc in LOCALES for key, _ in translated_units(lc)}
    missing = [(lc, key) for lc in LOCALES for key in sorted(english) if (lc, key) not in have]
    for lc, key in missing:
        print(f"missing  {mkey(lc, key)}")
    # Every English change ships with its translations: a stale or missing translation fails like an invalid one.
    print(f"{total} translated files: {bad} invalid, {stale} stale, {len(missing)} missing")
    sys.exit(1 if bad or stale or missing else 0)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("glossary").set_defaults(fn=cmd_glossary)
    for name, fn in (("plan", cmd_plan), ("submit", cmd_submit)):
        p = sub.add_parser(name)
        p.add_argument("--locales", nargs="+", default=list(LOCALES), choices=list(LOCALES))
        p.add_argument("--paths", nargs="+", help="globs relative to src/content/docs")
        p.set_defaults(fn=fn)
    sub.choices["plan"].add_argument("--count", type=int, default=5, help="pages to count_tokens (0 = skip API)")
    sub.choices["plan"].add_argument("-v", "--verbose", action="store_true")
    sub.choices["submit"].add_argument("--limit", type=int)
    sub.choices["submit"].add_argument("--dry-run", action="store_true", help="build requests, print sizes, send nothing")
    p = sub.add_parser("collect")
    p.add_argument("batch_id")
    p.add_argument("--poll", type=int, default=60)
    p.set_defaults(fn=cmd_collect)
    sub.add_parser("check").set_defaults(fn=cmd_check)
    p = sub.add_parser("check-anchors", help="verify /<locale>/…#anchor links in the built dist/")
    p.add_argument("--dist", default="dist")
    p.set_defaults(fn=cmd_check_anchors)
    p = sub.add_parser("prepare", help="write chunked jobs for Claude Code worker subagents (no API)")
    p.add_argument("--locales", nargs="+", default=list(LOCALES), choices=list(LOCALES))
    p.add_argument("--paths", nargs="+", help="globs relative to src/content/docs, or @snippets/<file>")
    p.add_argument("--chunk-words", type=int, default=20_000)
    p.add_argument("--force-paths", nargs="+", help="units to include even when current (globs, as --paths)")
    p.add_argument("--out", default="i18n/jobs")
    p.set_defaults(fn=cmd_prepare)
    p = sub.add_parser("ingest", help="post-process, validate and install worker output from i18n/staging/")
    p.add_argument("--locales", nargs="+", default=list(LOCALES), choices=list(LOCALES))
    p.set_defaults(fn=cmd_ingest)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
