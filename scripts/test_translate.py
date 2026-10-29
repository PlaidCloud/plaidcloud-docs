# /// script
# requires-python = ">=3.11"
# dependencies = ["anthropic", "pyyaml", "markdown-it-py"]
# ///
"""Offline tests for scripts/translate.py (no API calls): `uv run scripts/test_translate.py`. Exits 1 on any failure."""
import sys, re, shutil, tempfile
from pathlib import Path
REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / 'scripts'))
import translate as t

ok = lambda name, cond: print(("PASS " if cond else "FAIL ") + name) or cond
results = []

# ---- slugger (node github-slugger) + heading text extraction
hs = [t.heading_text(x) for x in ["Schritt 1: `foo` **anlegen**", "Übersicht & Ports", "Übersicht & Ports", "[Link](/x/) テキスト", "手順の概要", "Données (v2) &amp; plus"]]
sl = t.slugify_pages([hs])[0]
results.append(ok(f"slugger {sl}", sl == ["schritt-1-foo-anlegen", "übersicht--ports", "übersicht--ports-1", "link-テキスト", "手順の概要", "données-v2--plus"]))

# ---- hand-made translation of a real page
rel = "guides/workflows/create-a-macro.mdx"
src = (t.DOCS / rel).read_text()
fm, body = t.split_frontmatter(src)
def fake_translate(text):
    """Translate prose only: headings, frontmatter title/description, aria-label, figcaption text."""
    out = re.sub(r"^title: .*$", "title: Ein Makro erstellen", text, count=1, flags=re.M)
    out = re.sub(r"^description: .*$", "description: \"Definieren Sie ein Makro: wiederverwendbar.\"", out, count=1, flags=re.M)
    out = re.sub(r"^(#{2,6}) (.*)$", lambda m: f"{m.group(1)} DE {m.group(2)} Übersicht", out, flags=re.M)
    out = re.sub(r'aria-label="[^"]*"', 'aria-label="Ein Diagramm."', out)
    out = out.replace("A **Macro** is a reusable", "Ein **Makro** ist ein wiederverwendbarer")
    return out
good = t.localize_links(fake_translate(src), "de")
r = t.validate(rel, src, good)
results.append(ok(f"valid translation accepted {r}", r == []))
results.append(ok("internal link localized", "](/de/reference/workflow-steps/workflow-control/run-macro/)" in good))

def mutate(name, fn, expect):
    bad = fn(good)
    assert bad != good, name
    r = t.validate(rel, src, bad)
    results.append(ok(f"reject {name}: {r[:1]}", any(expect in x for x in r)))

fence = t.fences(body)[0] if t.fences(body) else None
mutate("YAML broken", lambda s: s.replace("title: Ein Makro erstellen", "title: Ein: Makro: erstellen", 1), "YAML")
mutate("sidebar.order changed", lambda s: s.replace("order: 12", "order: 13", 1), "sidebar.order")
mutate("frontmatter key added", lambda s: s.replace("sidebar:\n", "draft: true\nsidebar:\n", 1), "keys differ")
mutate("inline code translated", lambda s: s.replace("`month`", "`Monat`", 1), "inline code")
mutate("heading dropped", lambda s: re.sub(r"^## DE .*\n", "", s, count=1, flags=re.M), "heading levels")
mutate("link target changed", lambda s: s.replace("/de/reference/workflow-steps/workflow-control/run-macro/", "/de/reference/workflow-steps/run-macro/", 1), "link targets")
mutate("import changed", lambda s: s.replace("import { Aside }", "import { Aside, Steps }", 1), "import")
mutate("tag attr changed", lambda s: s.replace('type="note"', 'type="tip"', 1), "tag sequence")
mutate("svg coordinate changed", lambda s: re.sub(r'viewBox="0 0 (\d+)', lambda m: f'viewBox="0 0 {int(m.group(1))+1}', s, count=1), "tag sequence")
mutate("bare brace in MDX", lambda s: s.replace("Ein **Makro** ist", "Ein **Makro** {ist}", 1), "bare '{'")
mutate("list item dropped", lambda s: re.sub(r"^6\. .*\n", "", s, count=1, flags=re.M), "list items")
mutate("frontmatter missing", lambda s: s.split("---\n", 2)[2], "frontmatter missing")
if fence:
    mutate("code fence edited", lambda s: s.replace(fence, fence.replace("\n", "\n# Kommentar\n", 1), 1), "code fences")
else:
    print("note: page has no code fences")

# ---- code fence check on a page with fences + table rows
rel2 = next(p for p in t.english_pages() if "```" in (t.DOCS / p).read_text() and "\n|" in (t.DOCS / p).read_text() and p.endswith(".md"))
src2 = (t.DOCS / rel2).read_text()
f2 = t.fences(t.split_frontmatter(src2)[1])[0]
results.append(ok(f"[{rel2}] identity accepted", t.validate(rel2, src2, t.localize_links(src2, "ja")) == []))
results.append(ok("code fence edit rejected", any("code fences" in x for x in t.validate(rel2, src2, src2.replace(f2, f2.replace("\n", "\n-- x\n", 1), 1)))))
results.append(ok("table row dropped rejected", any("table rows" in x for x in t.validate(rel2, src2, re.sub(r"^\|.*\n", "", src2, count=1, flags=re.M)))))

# ---- link localization rules
s = ('---\ntitle: X\nhero:\n  actions:\n    - text: Go\n      link: /get-started/\n    - text: Trial\n      link: https://app.plaidcloud.com\n---\n'
     '[a](/guides/) [b](/images/x.png) [c](https://x.com/guides/) [d](/guides/launcher/#pin) [e](../foo/) [f](/no-such-page/) [g](#local)\n'
     '<LinkCard title="T" href="/reference/" />\n`[x](/guides/)`\n```\n[y](/guides/)\n```\n[ref]: /guides/launcher/\n')
o = t.localize_links(s, "fr")
for frag in ["link: /fr/get-started/", "link: https://app.plaidcloud.com", "[a](/fr/guides/)", "[b](/images/x.png)", "[c](https://x.com/guides/)",
             "[d](/fr/guides/launcher/#pin)", "[e](../foo/)", "[f](/no-such-page/)", "[g](#local)", 'href="/fr/reference/"', "`[x](/guides/)`", "[y](/guides/)", "[ref]: /fr/guides/launcher/"]:
    results.append(ok(f"localize: {frag}", frag in o))
results.append(ok("localize idempotent", t.localize_links(o, "fr") == o))

# ---- anchor rewrite in a temp docs tree
tmp = Path(tempfile.mkdtemp())
(tmp / "guides").mkdir(parents=True)
(tmp / "guides/a.md").write_text("---\ntitle: A\ndescription: d\n---\n\n## Getting Started\n\nSee [b](/guides/b/#step-two) and [here](#getting-started) and [rel](../b/#step-two) and [x](/guides/c/#keep-me).\n")
(tmp / "guides/b.md").write_text("---\ntitle: B\ndescription: d\n---\n\n## Step One\n\n## Step Two\n")
(tmp / "guides/c.md").write_text("---\ntitle: C\ndescription: d\n---\n\n## Keep Me\n")
(tmp / "de/guides").mkdir(parents=True)
(tmp / "de/guides/a.md").write_text("---\ntitle: A\ndescription: d\n---\n\n## Erste Schritte\n\nSiehe [b](/de/guides/b/#step-two) und [hier](#getting-started) und [rel](../b/#step-two) und [x](/de/guides/c/#keep-me).\n")
(tmp / "de/guides/b.md").write_text("---\ntitle: B\ndescription: d\n---\n\n## Schritt eins\n\n## Schritt zwei\n")
t.DOCS, t.PAGE_URLS = tmp, None
t.rewrite_anchors("de")
a = (tmp / "de/guides/a.md").read_text()
for frag in ["(/de/guides/b/#schritt-zwei)", "(#erste-schritte)", "(../b/#schritt-zwei)", "(/de/guides/c/#keep-me)"]:
    results.append(ok(f"anchor: {frag}", frag in a))
before = a
t.rewrite_anchors("de")
results.append(ok("anchor rewrite idempotent", (tmp / "de/guides/a.md").read_text() == before))
shutil.rmtree(tmp)

# ---- output cleanup
results.append(ok("strip wrapping fence", t.clean_output("---\n", "```markdown\n---\ntitle: x\n---\nbody\n```") == "---\ntitle: x\n---\nbody\n"))
# ---- frontmatter quoting: a translated value gains ": " and stops being valid YAML
import yaml
broken = "---\ntitle: CLI-Tools\ndescription: Referenz für Tools: PlaidLink und PlaidXL\nsidebar:\n  label: CLI\n---\n\nText\n"
fixed = t.quote_frontmatter(broken)
fmq = yaml.safe_load(t.split_frontmatter(fixed)[0])
results.append(ok("quote_frontmatter repairs ': ' value", fmq["description"] == "Referenz für Tools: PlaidLink und PlaidXL" and fmq["sidebar"]["label"] == "CLI"))
results.append(ok("quote_frontmatter leaves valid YAML untouched", t.quote_frontmatter(src) == src))
hashy = yaml.safe_load(t.split_frontmatter(t.quote_frontmatter("---\ntitle: Tools: A\nsidebar:\n  label: Schritt #2\n---\n"))[0])
results.append(ok("quote_frontmatter keeps ' #' out of a YAML comment", hashy["sidebar"]["label"] == "Schritt #2"))
# ---- inline code wrapped across a line break: compared with the break normalized
wsrc = "---\ntitle: X\ndescription: d\n---\n\nRun `plaid run --project\nfoo` first, then save.\n"
results.append(ok("wrapped inline code re-wrapped accepted", t.validate("a.md", wsrc, "---\ntitle: X\ndescription: d\n---\n\nFühren Sie zuerst\n`plaid run --project foo` aus.\n") == []))
results.append(ok("wrapped inline code edited rejected", any("inline code" in x for x in t.validate("a.md", wsrc, "---\ntitle: X\ndescription: d\n---\n\nFühren Sie zuerst `plaid run --projekt\nfoo` aus.\n"))))

# ---- bold flanking: CJK text around **…** that ends/starts with punctuation
ja = "---\ntitle: T\n---\n\n**「設定」**を開き、次に**（任意）**の欄を確認します。`**literal**`はそのまま。\n"
fj = t.fix_bold_flanking(ja)
results.append(ok(f"fix_bold_flanking renders all bold: {fj.splitlines()[-1]}", t.unrendered_bold(t.split_frontmatter(fj)[1]) == 0 and "`**literal**`" in fj))
results.append(ok("fix_bold_flanking no-op on rendering bold", t.fix_bold_flanking("A **bold** word.\n") == "A **bold** word.\n"))

print(f"\n{sum(results)}/{len(results)} passed")

# ---- snippets: units, identity validation, import linking, pruning
t.DOCS, t.SNIPPETS, t.PAGE_URLS = REPO / 'src/content/docs', REPO / 'src/snippets', None
bad = [k for k in t.english_snippets() for lc in ("de", "ja") if t.validate(k, t.src_path(k).read_text(), t.localize_links(t.src_path(k).read_text(), lc))]
results.append(ok(f"all {len(t.english_snippets())} used snippets pass identity validation {bad}", not bad))
k = "@snippets/common-data-filter.mdx"
ssrc = t.src_path(k).read_text()
results.append(ok("snippet: frontmatter added rejected", any("frontmatter added" in x for x in t.validate(k, ssrc, "---\ntitle: x\n---\n" + ssrc))))
results.append(ok("snippet: link localized", "](/de/reference/" in t.localize_links(t.src_path("@snippets/common-data-mapper.mdx").read_text(), "de")))
results.append(ok("paths: mkey/out_path", t.mkey("de", k) == "snippets/de/common-data-filter.mdx" and t.out_path("de", k) == t.SNIPPETS / "de/common-data-filter.mdx"
                  and t.mkey("de", "guides/x.md") == "de/guides/x.md"))

tmp = Path(tempfile.mkdtemp())
docs, snips = tmp / "docs", tmp / "snippets"
(docs / "ref").mkdir(parents=True); (snips / "sub").mkdir(parents=True)
page = "---\ntitle: P\ndescription: d\n---\n\nimport SnippetA from '@snippets/a.mdx';\nimport SnippetB from '@snippets/sub/b.mdx';\n\nIntro.\n\n<SnippetA />\n\n<SnippetB />\n"
(docs / "ref/p.mdx").write_text(page)
(snips / "a.mdx").write_text("import SnippetB from '@snippets/sub/b.mdx';\n\n#### Filter\n\nText.\n\n<SnippetB />\n")
(snips / "sub/b.mdx").write_text("Nested text.\n")
(snips / "unused.mdx").write_text("Unused.\n")
t.DOCS, t.SNIPPETS, t.PAGE_URLS, t.MANIFEST = docs, snips, None, tmp / "manifest.json"
results.append(ok(f"units include nested, skip unused: {t.english_units()}", t.english_units() == ["ref/p.mdx", "@snippets/a.mdx", "@snippets/sub/b.mdx"]))
(docs / "de/ref").mkdir(parents=True)
tr_page = page.replace("Intro.", "Einleitung.").replace("title: P", "title: S")
(docs / "de/ref/p.mdx").write_text(tr_page)
t.link_snippets("de")
results.append(ok("import kept English when no translated snippet", (docs / "de/ref/p.mdx").read_text() == tr_page))
(snips / "de/sub").mkdir(parents=True)
(snips / "de/a.mdx").write_text((snips / "a.mdx").read_text().replace("Text.", "Text DE."))
(snips / "de/sub/b.mdx").write_text("Verschachtelt.\n")
t.link_snippets("de")
pg = (docs / "de/ref/p.mdx").read_text()
results.append(ok("page imports rewritten to translated snippets", "'@snippets/de/a.mdx'" in pg and "'@snippets/de/sub/b.mdx'" in pg))
results.append(ok("nested snippet import rewritten", "'@snippets/de/sub/b.mdx'" in (snips / "de/a.mdx").read_text()))
results.append(ok("validator accepts localized snippet import", t.validate("ref/p.mdx", page, pg) == []))
t.link_snippets("de")
results.append(ok("link_snippets idempotent", (docs / "de/ref/p.mdx").read_text() == pg))
results.append(ok("stale pairs include snippets", {k for _, k, _ in t.stale_pairs(["de"], t.english_units())} == {"ref/p.mdx", "@snippets/a.mdx", "@snippets/sub/b.mdx"}))
# English drops snippet b everywhere -> translation pruned, imports relinked
(docs / "ref/p.mdx").write_text(page.replace("import SnippetB from '@snippets/sub/b.mdx';\n", "").replace("<SnippetB />\n", ""))
(snips / "a.mdx").write_text("#### Filter\n\nText.\n")
t.save_json(t.MANIFEST, {"snippets/de/sub/b.mdx": "x", "snippets/de/a.mdx": "y", "de/ref/p.mdx": "z"})
removed = t.prune_deleted()
results.append(ok(f"prune removes unused translated snippet {removed}", removed == ["snippets/de/sub/b.mdx"] and not (snips / "de/sub/b.mdx").exists()
                  and set(t.load_json(t.MANIFEST, {})) == {"snippets/de/a.mdx", "de/ref/p.mdx"}))
# translated snippet deleted -> page import falls back to English
(snips / "de/a.mdx").unlink(); t.link_snippets("de")
results.append(ok("import reverts to English when translated snippet is gone", "'@snippets/a.mdx'" in (docs / "de/ref/p.mdx").read_text()))
shutil.rmtree(tmp)
print(f"\n{sum(results)}/{len(results)} passed (final)")

# ---- editUrl on translated pages
t.DOCS, t.SNIPPETS, t.PAGE_URLS = REPO / 'src/content/docs', REPO / 'src/snippets', None
import yaml
for rel in ("guides/workflows/create-a-macro.mdx", "index.mdx"):
    src = (t.DOCS / rel).read_text()
    out = t.set_edit_url(t.localize_links(src, "de"), rel)
    fm = yaml.safe_load(t.split_frontmatter(out)[0])
    results.append(ok(f"editUrl set on {rel}", fm["editUrl"] == f"https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/{rel}"))
    results.append(ok(f"validator allows exactly that editUrl ({rel})", t.validate(rel, src, out) == []))
    results.append(ok("set_edit_url idempotent", t.set_edit_url(out, rel) == out))
    wrong = out.replace(f"docs/{rel}", "docs/de/" + rel)
    results.append(ok("validator rejects a wrong editUrl", any("editUrl" in x for x in t.validate(rel, src, wrong))))
    other = out.replace("editUrl:", "draft: true\neditUrl:")
    results.append(ok("validator still rejects other added keys", any("keys differ" in x for x in t.validate(rel, src, other))))
k = "@snippets/common-data-filter.mdx"
results.append(ok("no editUrl on snippets", t.set_edit_url(t.src_path(k).read_text(), k) == t.src_path(k).read_text()))
print(f"\n{sum(results)}/{len(results)} passed (with editUrl)")

# ---- prepare / ingest (worker-subagent flow) in a temp repo root
import argparse, json as _json
REAL = REPO
tmp = Path(tempfile.mkdtemp())
docs, snips = tmp / "src/content/docs", tmp / "src/snippets"
(docs / "guides").mkdir(parents=True); snips.mkdir(parents=True)
for rel in ("guides/workflows/create-a-macro.mdx", "reference/workflow-steps/import/import-csv.mdx"):
    (docs / rel).parent.mkdir(parents=True, exist_ok=True); shutil.copy(REAL / "src/content/docs" / rel, docs / rel)
for f in re.findall(r"@snippets/([^']+)'", (docs / "reference/workflow-steps/import/import-csv.mdx").read_text()):
    shutil.copy(REAL / "src/snippets" / f, snips / f)
(docs / "guides/small.md").write_text("---\ntitle: Small\ndescription: d\n---\n\nSee [macro](/guides/workflows/create-a-macro/#steps).\n\n## Steps\n\nClick **Save**.\n")
t.ROOT, t.DOCS, t.SNIPPETS, t.PAGE_URLS = tmp, docs, snips, None
t.I18N = tmp / "i18n"; t.MANIFEST, t.JOBS, t.STAGING = t.I18N / "manifest.json", t.I18N / "jobs", t.I18N / "staging"
t.GLOSSARY_DIR = REAL / "i18n/glossary"
t.cmd_prepare(argparse.Namespace(locales=["de", "ja"], paths=None, chunk_words=2500, out="i18n/jobs", force_paths=None))
chunks = sorted((t.JOBS / "de").glob("*.json"))
c1 = _json.loads(chunks[0].read_text())
items = [i for c in chunks for i in _json.loads(c.read_text())["items"]]
results.append(ok(f"prepare: {len(chunks)} de chunks, every unit once", sorted(i["path"] for i in items) == sorted(t.english_units())))
results.append(ok("prepare: item shape", set(c1["items"][0]) >= {"path", "kind", "source_file", "glossary", "output_file"} and c1["prompt_file"] == "i18n/jobs/prompts/de.md"))
results.append(ok("prepare: snippet kind + staging path", any(i["kind"] == "snippet" and i["output_file"].startswith("i18n/staging/de/@snippets/") for i in items)))
results.append(ok("prepare: chunks respect word budget (big page alone)", all(sum(i["words"] for i in _json.loads(c.read_text())["items"]) <= 2500 or len(_json.loads(c.read_text())["items"]) == 1 for c in chunks)))
pr = (t.JOBS / "prompts/de.md").read_text()
results.append(ok("prepare: prompt has system prompt + per-file rules", pr.startswith(t.system_prompt("de")) and t.MDX_RULE in pr and t.SNIPPET_NOTE.strip() in pr))
results.append(ok("prepare: WORKER.md written", (t.JOBS / "WORKER.md").read_text() == t.WORKER_MD))
# worker output: one good page (with preamble + fence), one good snippet, one broken page, one good ja page
st = t.STAGING
(st / "de/guides").mkdir(parents=True); (st / "de/@snippets").mkdir(parents=True); (st / "ja/guides").mkdir(parents=True)
small = (docs / "guides/small.md").read_text()
(st / "de/guides/small.md").write_text("Here is the translation:\n\n```markdown\n" + small.replace("title: Small", "title: Klein").replace("## Steps", "## Schritte") + "```\n")
(st / "ja/guides/small.md").write_text(small.replace("## Steps", "## 手順"))
macro = (docs / "guides/workflows/create-a-macro.mdx").read_text()
(st / "de/guides/workflows").mkdir(parents=True)
(st / "de/guides/workflows/create-a-macro.mdx").write_text(macro.replace("## Steps", "## Schritte").replace("`month`", "`Monat`"))
sn = (snips / "no-examples.mdx").read_text()
(st / "de/@snippets/no-examples.mdx").write_text(sn)
t.cmd_ingest(argparse.Namespace(locales=["de", "ja"]))
de_small = (docs / "de/guides/small.md").read_text()
results.append(ok("ingest: preamble + fence stripped, written", de_small.startswith("---\ntitle: Klein") and "```" not in de_small))
results.append(ok("ingest: editUrl + localized link", "editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/small.md" in de_small
                  and "(/de/guides/workflows/create-a-macro/#steps)" in de_small))
results.append(ok("ingest: staging file deleted on success", not (st / "de/guides/small.md").exists() and (snips / "de/no-examples.mdx").exists()))
rej = _json.loads((st / "_rejects.json").read_text())
results.append(ok(f"ingest: invalid kept in staging + logged {[r['path'] for r in rej]}", (st / "de/guides/workflows/create-a-macro.mdx").exists()
                  and rej == [{"locale": "de", "path": "guides/workflows/create-a-macro.mdx", "reasons": rej[0]["reasons"]}] and "inline code" in rej[0]["reasons"][0]))
results.append(ok("ingest: anchor kept English (target not translated)", "#steps)" in de_small))
man = t.load_json(t.MANIFEST, {})
results.append(ok(f"ingest: manifest {sorted(man)}", sorted(man) == ["de/guides/small.md", "ja/guides/small.md", "snippets/de/no-examples.mdx"]))
# now fix the macro and re-ingest: anchors in small.md get the translated slug, snippet import relinked
(st / "de/guides/workflows/create-a-macro.mdx").write_text(macro.replace("## Steps", "## Schritte"))
t.cmd_ingest(argparse.Namespace(locales=["de"]))
results.append(ok("re-ingest: anchor rewritten to translated slug", "(/de/guides/workflows/create-a-macro/#schritte)" in (docs / "de/guides/small.md").read_text()))
results.append(ok("check passes on ingested output", not any(t.validate(k, t.src_path(k).read_text(), p.read_text()) for lc in ("de", "ja") for k, p in t.translated_units(lc))))
shutil.rmtree(tmp)
print(f"\n{sum(results)}/{len(results)} passed (with prepare/ingest)")

# ---- a staged file made from older English never installs as current
tmp = Path(tempfile.mkdtemp())
t.ROOT, t.DOCS, t.SNIPPETS, t.PAGE_URLS = tmp, tmp / "src/content/docs", tmp / "src/snippets", None
t.I18N = tmp / "i18n"; t.MANIFEST, t.JOBS, t.STAGING = t.I18N / "manifest.json", t.I18N / "jobs", t.I18N / "staging"
(t.DOCS / "guides").mkdir(parents=True); t.SNIPPETS.mkdir(parents=True)
eng = t.DOCS / "guides/s.md"
eng.write_text("---\ntitle: S\ndescription: d\n---\n\nClick **Save** once.\n")
prep = lambda: t.cmd_prepare(argparse.Namespace(locales=["de"], paths=None, chunk_words=2500, out="i18n/jobs", force_paths=None))
prep()
staged = t.STAGING / "de/guides/s.md"
staged.parent.mkdir(parents=True); staged.write_text("---\ntitle: S\ndescription: d\n---\n\nKlicken Sie einmal auf **Speichern**.\n")
eng.write_text("---\ntitle: S\ndescription: d\n---\n\nNever click **Save**; it deletes everything.\n")
t.cmd_ingest(argparse.Namespace(locales=["de"]))
results.append(ok("stale staged file rejected after English edit", staged.exists() and not (t.DOCS / "de/guides/s.md").exists()))
prep()
results.append(ok("re-prepare deletes the stale staged file", not staged.exists()))
staged.parent.mkdir(parents=True, exist_ok=True); staged.write_text("---\ntitle: S\ndescription: d\n---\n\nKlicken Sie einmal auf **Speichern**.\n")
shutil.rmtree(t.JOBS)
t.cmd_ingest(argparse.Namespace(locales=["de"]))
results.append(ok("staged file with no prepare chunk rejected", not (t.DOCS / "de/guides/s.md").exists() and "de/guides/s.md" not in t.load_json(t.MANIFEST, {})))
shutil.rmtree(tmp)

# ---- review round: termbase, overrides, recall, typography, emphasis rendering, schema limits, force-paths
t.ROOT, t.DOCS, t.SNIPPETS, t.PAGE_URLS, t.STEP_NAMES = REAL, REAL / "src/content/docs", REAL / "src/snippets", None, None
t.I18N = REAL / "i18n"; t.MANIFEST, t.JOBS, t.STAGING = t.I18N / "manifest.json", t.I18N / "jobs", t.I18N / "staging"
t.GLOSSARY_DIR, t.OVERRIDES_DIR, t.TERMBASE_DIR = t.I18N / "glossary", t.I18N / "glossary_overrides", t.I18N / "termbase"
rel = "guides/workflows/create-a-macro.mdx"; src = (t.DOCS / rel).read_text()
good = t.set_edit_url(t.localize_links(fake_translate(src), "fr"), rel)
def nbsp(text):
    fm, body = t.split_frontmatter(text)
    lines = []
    for line in body.split("\n"):
        if (not any(c in line for c in "`<[:|") or line.startswith(("#", "-", "1"))) and not line.startswith("import "):
            line = re.sub(r" ?([;!?])", " \\1", re.sub(r" ?:(?=\s)", " :", line))
        lines.append(line)
    return f"---\n{fm}\n---\n" + "\n".join(lines)
fr = nbsp(good)
results.append(ok(f"fr NBSP/NNBSP typography accepted ({fr.count(chr(0xa0)) + fr.count(chr(0x202f))} inserted)", fr != good and t.validate(rel, src, fr) == []))
bad = good.replace("Ein **Makro** ist", "Ein **Makro **ist", 1)
results.append(ok("unrendered bold rejected", any("literal **" in x for x in t.validate(rel, src, bad))))
ko_src = "---\ntitle: X\ndescription: d\n---\n\nSelect **English (US)** in the list.\n"
results.append(ok("ko **English (US)**를 rejected", any("literal **" in x for x in t.validate("a.md", ko_src, "---\ntitle: X\ndescription: d\n---\n\n목록에서 **English (US)**를 선택합니다.\n"))))
results.append(ok("ko **English (US)** 를 accepted", t.validate("a.md", ko_src, "---\ntitle: X\ndescription: d\n---\n\n목록에서 **English (US)** 를 선택합니다.\n") == []))
results.append(ok("ja **保存**をクリック accepted", t.validate("a.md", ko_src.replace("English (US)", "Save"), "---\ntitle: X\ndescription: d\n---\n\n**保存**をクリックします。\n") == []))
long = good.replace("description: \"Definieren Sie ein Makro: wiederverwendbar.\"", "description: \"" + "x" * 501 + "\"")
results.append(ok("description over content-schema max rejected", any("outside content schema" in x for x in t.validate(rel, src, long))))
results.append(ok("schema limits read from content.config", t.schema_limits().get("description") == (0, 500)))
de, pl = t.load_glossary("de"), t.load_glossary("pl")
results.append(ok("override applied (de Load sample, Run)", de["Load sample"] == "Beispiel laden" and de["Run"] == "Ausführen"))
results.append(ok("null override drops entry (pl Driver)", "Driver" not in pl and pl["Readable"] == "Dostępne do odczytu"))
lower = {k.lower(): k for k in de}
for label, want in (("Dismiss onboarding", "Dismiss onboarding?"), ("Skip Rows", "Skip Rows:"), ("load sample", "Load sample"), ("Workspace Members", "Workspace Member")):
    hit = t.lookup_label(label, de, lower)
    results.append(ok(f"recall: **{label}** -> {hit}", hit is not None and hit[0] == want))
pg = t.page_glossary((["Scalar / Dimension"], []), de)
results.append(ok(f"joined label built from parts {pg}", pg.get("Scalar / Dimension") == f"{de['Scalar']} / {de['Dimension']}"))
sp = t.system_prompt("de")
results.append(ok("termbase in system prompt", "  - trial balance → Saldenliste" in sp and "one term per concept" in sp))
results.append(ok("step names in prompt (English kept, glossary form shown)", "\n- Allocation Split\n" in sp and " → " in sp.split("## Workflow step names")[1]))
results.append(ok("prompt: link-target line + description cap", "the build adds language prefixes" in sp and "under 480 characters" in sp and "Do not add a language prefix" not in sp))
results.append(ok("fr/pl/pt-pt/es voice rules", "U+202F" in t.system_prompt("fr") and "skończyłeś" in t.system_prompt("pl")
                  and "Never use \"você\"" in t.system_prompt("pt-pt") and "virgulilla" in t.system_prompt("es")))
results.append(ok("CJK bold rule + ja noun rule", "never a bare particle" in t.system_prompt("ja") and "Never put a space between `**`" in t.system_prompt("zh-cn")))
# force-paths
tmp = Path(tempfile.mkdtemp())
t.save_json(tmp / "m.json", {f"{lc}/{rel}": t.sha(src) for lc in t.LOCALES})
t.MANIFEST = tmp / "m.json"
real_prune, t.prune_deleted = t.prune_deleted, lambda: None  # prepare would prune the real repo's translations
t.cmd_prepare(argparse.Namespace(locales=["de"], paths=[rel], chunk_words=12000, out=str(tmp / "jobs"), force_paths=None))
results.append(ok("current unit not prepared without force", not list((tmp / "jobs/de").glob("*.json"))))
t.cmd_prepare(argparse.Namespace(locales=["de"], paths=[rel], chunk_words=12000, out=str(tmp / "jobs"), force_paths=[rel]))
results.append(ok("--force-paths re-queues a current unit", [i["path"] for i in _json.loads((tmp / "jobs/de/001.json").read_text())["items"]] == [rel]))
t.prune_deleted = real_prune
shutil.rmtree(tmp)
print(f"\n{sum(results)}/{len(results)} passed (review round)")

# ---- anchors into translated snippet headings (snippets slugged separately)
tmp = Path(tempfile.mkdtemp())
docs, snips = tmp / "docs", tmp / "snippets"
(docs / "g").mkdir(parents=True); snips.mkdir(parents=True)
(docs / "g/p.mdx").write_text("---\ntitle: P\ndescription: d\n---\n\nimport S from '@snippets/s.mdx';\n\n## Overview\n\n<S />\n")
(snips / "s.mdx").write_text("#### Overview\n\n#### Source Columns No Longer Listed\n")
(docs / "g/q.md").write_text("---\ntitle: Q\ndescription: d\n---\n\nSee [x](/g/p/#source-columns-no-longer-listed) and [y](/g/p/#overview).\n")
(docs / "de/g").mkdir(parents=True); (snips / "de").mkdir(parents=True)
(docs / "de/g/p.mdx").write_text("---\ntitle: P\ndescription: d\n---\n\nimport S from '@snippets/de/s.mdx';\n\n## Überblick\n\n<S />\n")
(snips / "de/s.mdx").write_text("#### Übersicht\n\n#### Nicht mehr aufgeführte Quellspalten\n")
(docs / "de/g/q.md").write_text("---\ntitle: Q\ndescription: d\n---\n\nSiehe [x](/de/g/p/#source-columns-no-longer-listed) und [y](/de/g/p/#overview).\n")
t.DOCS, t.SNIPPETS, t.PAGE_URLS = docs, snips, None
t.rewrite_anchors("de")
q = (docs / "de/g/q.md").read_text()
results.append(ok(f"anchor into translated snippet heading: {q.strip().splitlines()[-1]}", "(/de/g/p/#nicht-mehr-aufgeführte-quellspalten)" in q))
results.append(ok("page heading wins over same-slug snippet heading", "(/de/g/p/#überblick)" in q))
(snips / "s2.mdx").write_text("See [y](/g/p/#overview).\n"); (snips / "de/s2.mdx").write_text("Siehe [y](/de/g/p/#overview).\n")
(docs / "g/r.md").write_text("---\ntitle: R\ndescription: d\n---\n\nimport S2 from '@snippets/s2.mdx';\n\n[x](/g/p/#source-columns-no-longer-listed)\n\n<S2 />\n")
(docs / "de/g/r.md").write_text("---\ntitle: R\ndescription: d\n---\n\nimport S2 from '@snippets/de/s2.mdx';\n\n[x](/de/g/p/#nicht-mehr-aufgefuehrte-quellspalten)\n\n<S2 />\n")
t.PAGE_URLS = None
t.rewrite_anchors("de")
results.append(ok("link inside a translated snippet is mapped", "(/de/g/p/#überblick)" in (snips / "de/s2.mdx").read_text()))
results.append(ok("translator-guessed anchor restored from English", "(/de/g/p/#nicht-mehr-aufgeführte-quellspalten)" in (docs / "de/g/r.md").read_text()))
(docs / "g/u.md").write_text("---\ntitle: U\ndescription: d\n---\n\n## Alpha\n\n## Beta\n")
(docs / "g/v.md").write_text("---\ntitle: V\ndescription: d\n---\n\n[a](/g/u/#alpha) [b](/g/u/#beta)\n")
(docs / "de/g/v.md").write_text("---\ntitle: V\ndescription: d\n---\n\n[a](/de/g/u/#altes-alpha) [b](/de/g/u/#altes-beta)\n")
t.PAGE_URLS = None
t.rewrite_anchors("de")
results.append(ok("anchors into an English-fallback target revert to English, by position", "(/de/g/u/#alpha) [b](/de/g/u/#beta)" in (docs / "de/g/v.md").read_text()))
shutil.rmtree(tmp)
# ---- ESM detection: wrapped prose starting with "export" is not an export statement
results.append(ok("ESM_RE ignores prose 'export it as CSV'", not t.ESM_RE.match("export it as CSV or PDF.") and bool(t.ESM_RE.match("export const x = 1;")) and bool(t.ESM_RE.match("import { Aside } from '@astrojs/starlight/components';"))))

print(f"\n{sum(results)}/{len(results)} passed (all)")
sys.exit(0 if all(results) else 1)
