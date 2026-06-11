#!/usr/bin/env python3
"""Generate a polished, customer-facing PlaidCloud platform architecture diagram (SVG)."""

from html import escape
import base64
from pathlib import Path
import shutil
import subprocess

# ----------------------------------------------------------------------------- palette
NAVY      = "#16243D"   # primary ink / structure
SLATE     = "#5B6B82"   # secondary text
TEAL      = "#0F9B86"   # brand / platform
TEAL_DK   = "#0B7768"
PURPLE    = "#6F57D9"   # AI / agents / programmatic
AMBER     = "#D98324"   # external systems / integration
BLUE      = "#2D6CDF"   # consumers
CARD_BG   = "#FFFFFF"
CARD_BRD  = "#DCE3EC"
PAGE_BG   = "#F5F8FB"
LANE_BRD  = "#E2E8F1"
FONT      = "'Helvetica Neue', Helvetica, Arial, sans-serif"

W, H = 1680, 1200

svg = []
def add(s): svg.append(s)

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "public" / "images"
LOGO_PATH = ROOT / "src" / "assets" / "logo.svg"
LOGO_DATA = base64.b64encode(LOGO_PATH.read_bytes()).decode("ascii")

def tint(hexcolor, amt):
    """Lighten a hex color toward white by amt (0..1)."""
    h = hexcolor.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    r = int(r + (255 - r) * amt)
    g = int(g + (255 - g) * amt)
    b = int(b + (255 - b) * amt)
    return f"#{r:02X}{g:02X}{b:02X}"

# ----------------------------------------------------------------------------- icons
# Each icon is drawn into a 24x24 viewbox, stroked in `color`. Returns an SVG <g>.
def icon(name, cx, cy, color, size=24):
    s = size / 24.0
    t = f'transform="translate({cx},{cy}) scale({s})"'
    st = f'fill="none" stroke="{color}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"'
    P = {
        "users": '<circle cx="9" cy="8" r="3.2"/><path d="M3.5 19c0-3 2.5-5 5.5-5s5.5 2 5.5 5"/><circle cx="17" cy="8.5" r="2.4"/><path d="M15 14.4c2.6.2 4.8 2.1 4.8 4.6"/>',
        "engineer": '<path d="M8 16l-4-4 4-4"/><path d="M16 8l4 4-4 4"/><path d="M13 5l-2 14"/>',
        "agent": '<rect x="5" y="8" width="14" height="10" rx="2.5"/><path d="M12 8V4"/><circle cx="12" cy="3" r="1.3"/><circle cx="9.5" cy="13" r="1.1"/><circle cx="14.5" cy="13" r="1.1"/>',
        "extapp": '<rect x="4" y="5" width="16" height="14" rx="2"/><path d="M4 9h16"/><circle cx="6.7" cy="7" r=".7"/><circle cx="9" cy="7" r=".7"/>',
        "web": '<rect x="4" y="5" width="16" height="14" rx="2"/><path d="M4 9h16"/><path d="M8 13h6M8 16h4"/>',
        "xl": '<rect x="4" y="4" width="16" height="16" rx="2"/><path d="M4 9h16M4 14h16M10 4v16"/>',
        "chart": '<path d="M4 4v16h16"/><rect x="7" y="11" width="2.6" height="6" rx="0.6"/><rect x="12" y="7" width="2.6" height="10" rx="0.6"/><rect x="17" y="13" width="2.6" height="4" rx="0.6"/>',
        "notebook": '<rect x="6" y="3.5" width="13" height="17" rx="2"/><path d="M6 8h13M6 12h13M6 16h8"/><path d="M5 6.5v12"/>',
        "panel": '<rect x="4" y="4" width="16" height="16" rx="2"/><path d="M4 10h16M11 10v10"/>',
        "rest": '<path d="M9 6l-5 6 5 6"/><path d="M15 6l5 6-5 6"/>',
        "mcp": '<path d="M9 14V8a3 3 0 0 1 6 0v6"/><rect x="7" y="14" width="10" height="5" rx="2"/><path d="M10 8V5M14 8V5"/>',
        "workflow": '<circle cx="6" cy="7" r="2.3"/><circle cx="6" cy="17" r="2.3"/><circle cx="18" cy="12" r="2.3"/><path d="M8.2 7.6l7.6 3.2M8.2 16.4l7.6-3.2"/>',
        "spark": '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/>',
        "git": '<circle cx="7" cy="6" r="2.2"/><circle cx="7" cy="18" r="2.2"/><circle cx="17" cy="9" r="2.2"/><path d="M7 8.2v7.6M9 7.4c5 .6 6 1.6 6 4.4"/>',
        "shield": '<path d="M12 3l7 3v5c0 4.5-3 7.6-7 9-4-1.4-7-4.5-7-9V6z"/><path d="M9 12l2 2 4-4"/>',
        "lakehouse": '<ellipse cx="12" cy="6" rx="7" ry="2.6"/><path d="M5 6v8c0 1.4 3.1 2.6 7 2.6s7-1.2 7-2.6V6"/><path d="M5 10c0 1.4 3.1 2.6 7 2.6s7-1.2 7-2.6"/>',
        "objstore": '<path d="M5 7c0-1.4 3.1-2.6 7-2.6S19 5.6 19 7v10c0 1.4-3.1 2.6-7 2.6S5 18.4 5 17z"/><ellipse cx="12" cy="7" rx="7" ry="2.6"/><path d="M5 12c0 1.4 3.1 2.6 7 2.6s7-1.2 7-2.6"/>',
        "catalog": '<rect x="5" y="4" width="14" height="16" rx="2"/><path d="M9 8h6M9 12h6M9 16h4"/><path d="M5 4v16"/>',
        "erp": '<path d="M4 20h16"/><rect x="6" y="6" width="12" height="14" rx="1"/><path d="M9 10h2M13 10h2M9 14h2M13 14h2"/><path d="M10 6V3h4v3"/>',
        "database": '<ellipse cx="12" cy="6" rx="6.5" ry="2.4"/><path d="M5.5 6v12c0 1.3 2.9 2.4 6.5 2.4s6.5-1.1 6.5-2.4V6"/><path d="M5.5 12c0 1.3 2.9 2.4 6.5 2.4s6.5-1.1 6.5-2.4"/>',
        "api": '<rect x="3.5" y="6" width="17" height="12" rx="2"/><path d="M8 10l-2 2 2 2M16 10l2 2-2 2M13 9l-2 6"/>',
        "cloud": '<path d="M7 17h9.5a3.5 3.5 0 0 0 .4-7 5 5 0 0 0-9.6-1.2A3.8 3.8 0 0 0 7 17z"/>',
        "files": '<path d="M7 3.5h6l4 4V20a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V4.5a1 1 0 0 1 1-1z"/><path d="M13 3.5V8h4"/><path d="M9 13h6M9 16h6"/>',
    }
    body = P.get(name, "")
    return f'<g {t} {st}>{body}</g>'

# ----------------------------------------------------------------------------- primitives
def text(x, y, s, size=14, color=NAVY, weight="400", anchor="start", spacing=None, opacity=1):
    sp = f' letter-spacing="{spacing}"' if spacing is not None else ""
    op = f' opacity="{opacity}"' if opacity != 1 else ""
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
            f'fill="{color}" font-weight="{weight}" text-anchor="{anchor}"{sp}{op}>{escape(s)}</text>')

def wrap_words(s, max_width, size):
    max_chars = max(8, int(max_width / (size * 0.54)))
    lines = []
    line = ""
    for word in s.split():
        candidate = f"{line} {word}".strip()
        if len(candidate) <= max_chars:
            line = candidate
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines[:2]

def text_lines(x, y, lines, size=14, color=NAVY, weight="400", line_height=15):
    return "".join(
        text(x, y + i*line_height, line, size=size, color=color, weight=weight)
        for i, line in enumerate(lines)
    )

def card(x, y, w, h, title, sub, icon_name, accent, title_size=15.5, sub_size=11.5, href=None):
    g = []
    if href:
        g.append(f'<a href="{escape(href)}" class="arch-card">')
        g.append(f'<title>{escape(title)}</title>')
    g.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{CARD_BG}" '
             f'stroke="{CARD_BRD}" stroke-width="1.2"/>')
    # left accent rail
    g.append(f'<rect x="{x}" y="{y}" width="5" height="{h}" rx="2.5" fill="{accent}"/>')
    g.append(f'<rect x="{x+2.5}" y="{y}" width="3" height="{h}" fill="{accent}"/>')
    # icon tile
    iy = y + h/2 - 21
    g.append(f'<rect x="{x+16}" y="{iy}" width="42" height="42" rx="11" fill="{tint(accent,0.86)}"/>')
    g.append(icon(icon_name, x+16+9, iy+9, accent, size=24))
    tx = x + 70
    if sub:
        sub_lines = wrap_words(sub, w - 82, sub_size)
        title_y = y + h/2 - (9 if len(sub_lines) > 1 else 4)
        g.append(text(tx, title_y, title, size=title_size, weight="600", color=NAVY))
        g.append(text_lines(tx, title_y + 19, sub_lines, size=sub_size, weight="400", color=SLATE, line_height=14))
    else:
        g.append(text(tx, y + h/2 + 5, title, size=title_size, weight="600", color=NAVY))
    if href:
        g.append('</a>')
    return "".join(g)

def lane_heading(x, y, label, accent):
    return (f'<rect x="{x}" y="{y-11}" width="4" height="15" rx="2" fill="{accent}"/>'
            + text(x+12, y, label, size=13, weight="700", color=NAVY, spacing="1.4"))

def header_label_bg(x, y, w):
    return f'<rect x="{x-8}" y="{y-18}" width="{w}" height="26" rx="8" fill="url(#page)"/>'

# ----------------------------------------------------------------------------- canvas
add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{FONT}">')
add('<defs>')
add('<style>'
    '.arch-card{cursor:pointer}'
    '.arch-card:hover rect:first-of-type,.arch-card:focus rect:first-of-type{stroke:#0F9B86;stroke-width:2.4}'
    '.arch-card:focus{outline:none}'
    '</style>')
add(f'<linearGradient id="page" x1="0" y1="0" x2="0" y2="1">'
    f'<stop offset="0" stop-color="#FBFCFE"/><stop offset="1" stop-color="{PAGE_BG}"/></linearGradient>')
add(f'<linearGradient id="platform" x1="0" y1="0" x2="0" y2="1">'
    f'<stop offset="0" stop-color="{tint(TEAL,0.95)}"/><stop offset="1" stop-color="{tint(TEAL,0.90)}"/></linearGradient>')
add('<filter id="soft" x="-20%" y="-20%" width="140%" height="140%">'
    '<feDropShadow dx="0" dy="2" stdDeviation="6" flood-color="#1B2A44" flood-opacity="0.10"/></filter>')
add('<marker id="arrow" markerWidth="9" markerHeight="9" refX="6.5" refY="4" orient="auto">'
    f'<path d="M1 1 L7 4 L1 7" fill="none" stroke="{SLATE}" stroke-width="1.6" '
    'stroke-linecap="round" stroke-linejoin="round"/></marker>')
add('<marker id="arrowA" markerWidth="9" markerHeight="9" refX="6.5" refY="4" orient="auto-start-reverse">'
    f'<path d="M1 1 L7 4 L1 7" fill="none" stroke="{AMBER}" stroke-width="1.7" '
    'stroke-linecap="round" stroke-linejoin="round"/></marker>')
add('</defs>')
add(f'<rect width="{W}" height="{H}" fill="url(#page)"/>')

# ----------------------------------------------------------------------------- header
add(f'<image x="58" y="31" width="204" height="59" href="data:image/svg+xml;base64,{LOGO_DATA}"/>')
add(text(300, 61, "Platform Architecture", size=30, weight="300", color=TEAL_DK))
add(text(300, 87, "Unified data integration, transformation, analytics & AI - securely connected to your enterprise systems.",
         size=15, color=SLATE))

# =========================================================================== BAND A: consumers
ax, aw = 60, W-120
A_y = 116
add(lane_heading(ax, A_y, "WHO CONNECTS", BLUE))
consumers = [
    ("Business & Finance Users", "Self-service models & reports", "users", BLUE, "/guides/dashboards/"),
    ("Data & Analytics Engineers", "Pipelines, transforms, code", "engineer", TEAL, "/guides/workflows/"),
    ("AI Agents & Copilots", "Automated analysis via MCP", "agent", PURPLE, "/integrations/ai-coding-agents/"),
    ("External Apps & Services", "Programmatic integration", "extapp", AMBER, "/reference/connectors/rest/"),
]
cw = (aw - 3*40) / 4
cy0 = A_y + 14
for i,(t,s,ic,ac,href) in enumerate(consumers):
    cx = ax + i*(cw+40)
    add(f'<g filter="url(#soft)">{card(cx, cy0, cw, 96, t, s, ic, ac, href=href)}</g>')

# connectors: consumers -> platform
plat_top = 286
for i in range(4):
    cx = ax + i*(cw+40) + cw/2
    add(f'<path d="M{cx} {cy0+96} L{cx} {plat_top}" stroke="{SLATE}" stroke-width="1.6" '
        f'opacity="0.55" marker-end="url(#arrow)"/>')

# =========================================================================== PLATFORM CONTAINER
px, pw = 60, W-120
py, ph = plat_top, 590
add(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="22" fill="url(#platform)" '
    f'stroke="{TEAL}" stroke-width="1.6" filter="url(#soft)"/>')
# platform title badge
add(f'<rect x="{px+26}" y="{py-16}" width="226" height="32" rx="16" fill="{NAVY}"/>')
add(f'<circle cx="{px+46}" cy="{py}" r="5" fill="{TEAL}"/>')
add(text(px+60, py+5, "PlaidCloud Platform", size=14.5, weight="700", color="#FFFFFF", spacing="0.4"))
add(f'<rect x="{px+pw-396}" y="{py+17}" width="362" height="26" rx="13" fill="{tint(TEAL,0.90)}" '
    f'stroke="{tint(TEAL,0.68)}" stroke-width="1"/>')
add(text(px+pw-215, py+35, "Multi-tenant · Cloud-native · enterprise-grade security",
         size=11.5, color=TEAL_DK, weight="600", anchor="middle"))

INX = px + 24
INW = pw - 48

# ---- sub-lane 1: Experience & Interfaces
s1y = py + 40
add(lane_heading(INX, s1y, "EXPERIENCE & INTERFACE LAYER", TEAL))
interfaces = [
    ("Web UI", "Analyze & Workflow Designer", "web", TEAL, "/get-started/quickstart/"),
    ("PlaidXL", "Excel Add-in", "xl", TEAL, "/reference/cli/plaidxl/"),
    ("Superset", "Dashboards & BI", "chart", TEAL, "/guides/dashboards/"),
    ("Jupyter", "Notebooks & code", "notebook", TEAL, "/reference/cli/jupyter/"),
    ("Panel Apps", "WASM / server data apps", "panel", TEAL, "/guides/panel-apps/"),
    ("REST API", "Programmatic access", "rest", PURPLE, "/reference/connectors/rest/"),
    ("MCP Server", "AI tool & agent access", "mcp", PURPLE, "/get-started/tutorials/mcp-with-ai-agent/"),
]
n = len(interfaces); gap = 22
iw = (INW - (n-1)*gap) / n
iy = s1y + 14
for i,(t,s,ic,ac,href) in enumerate(interfaces):
    cx = INX + i*(iw+gap)
    add(card(cx, iy, iw, 100, t, s, ic, ac, title_size=14.5, sub_size=10.8, href=href))

# ---- sub-lane 2: Core Platform Services
s2y = iy + 100 + 38
add(lane_heading(INX, s2y, "CORE PLATFORM SERVICES", TEAL_DK))
services = [
    ("Workflow & Transform Engine", "Visual + SQL data pipelines at scale", "workflow", TEAL_DK, "/guides/workflows/"),
    ("AI Agents & Automation", "Agentic analysis, copilots, orchestration", "spark", PURPLE, "/guides/ai-assistant/"),
    ("Project Git Versioning", "Branch, review & audit every change", "git", AMBER, "/guides/git/"),
    ("Security & Governance", "SSO · RBAC · isolated tenancy", "shield", NAVY, "/administration/access/"),
]
n2 = len(services); gap2 = 30
sw = (INW - (n2-1)*gap2) / n2
sy = s2y + 14
for i,(t,s,ic,ac,href) in enumerate(services):
    cx = INX + i*(sw+gap2)
    add(card(cx, sy, sw, 100, t, s, ic, ac, title_size=14.5, sub_size=11, href=href))

# ---- sub-lane 3: Data Foundation
s3y = sy + 100 + 38
add(lane_heading(INX, s3y, "DATA FOUNDATION", TEAL_DK))
data = [
    ("Lakehouse", "High-performance columnar analytics engine", "lakehouse", TEAL_DK, "/guides/data/"),
    ("Object Storage", "Governed, elastic data lake", "objstore", BLUE, "/reference/connectors/cloud-services/"),
    ("Data Catalog & Lineage", "Discovery, metadata & audit trail", "catalog", PURPLE, "/guides/data/table-explorer/"),
]
n3 = len(data); gap3 = 24
dw = (INW - (n3-1)*gap3) / n3
dy = s3y + 14
for i,(t,s,ic,ac,href) in enumerate(data):
    cx = INX + i*(dw+gap3)
    add(card(cx, dy, dw, 100, t, s, ic, ac, title_size=15.5, sub_size=11.5, href=href))

# internal flow arrows (interfaces -> services -> data), subtle & centered per group
def vflow(y1, y2, xs):
    for x in xs:
        add(f'<path d="M{x} {y1} L{x} {y2}" stroke="{TEAL_DK}" stroke-width="1.5" '
            f'opacity="0.35" marker-end="url(#arrow)"/>')
xs_a = [INX + INW*f for f in (0.18,0.5,0.82)]
vflow(iy+100, sy-3, xs_a)
vflow(sy+100, dy-3, xs_a)

# =========================================================================== BAND E: external systems
plat_bottom = py + ph
E_head_y = plat_bottom + 40
external = [
    ("ERP Systems", "SAP · Oracle · NetSuite · Workday", "erp", AMBER, "/reference/connectors/erp/"),
    ("Databases & Warehouses", "Postgres · SQL Server · Snowflake · BigQuery", "database", AMBER, "/reference/connectors/databases/"),
    ("REST & SaaS APIs", "Salesforce · HTTP · custom services", "api", AMBER, "/reference/connectors/rest/"),
    ("Cloud Object Storage", "Amazon S3 · Azure Blob · GCS", "cloud", AMBER, "/reference/connectors/cloud-services/"),
    ("Files & Spreadsheets", "Excel · CSV · Parquet · JSON", "files", AMBER, "/guides/connections/"),
]
ne = len(external); gape = 28
ew = (aw - (ne-1)*gape) / ne
ey = E_head_y + 46

# bi-directional connectors across platform boundary
for i in range(ne):
    cx = ax + i*(ew+gape) + ew/2
    add(f'<path d="M{cx} {E_head_y+18} L{cx} {ey-12}" stroke="{AMBER}" stroke-width="1.7" '
        f'opacity="0.7" marker-end="url(#arrowA)"/>')
    add(f'<path d="M{cx} {E_head_y-20} L{cx} {plat_bottom}" stroke="{AMBER}" stroke-width="1.7" '
        f'opacity="0.7" marker-end="url(#arrowA)"/>')

add(header_label_bg(px, E_head_y, 636))
add(f'<rect x="{px}" y="{E_head_y-13}" width="4" height="17" rx="2" fill="{AMBER}"/>')
add(text(px+12, E_head_y, "ENTERPRISE SYSTEMS & DATA SOURCES", size=13, weight="700", color=NAVY, spacing="1.4"))
add(text(px+352, E_head_y, "secure, bi-directional connectors - read & write-back", size=12.5, color=SLATE, weight="400"))

for i,(t,s,ic,ac,href) in enumerate(external):
    cx = ax + i*(ew+gape)
    add(f'<g filter="url(#soft)">{card(cx, ey, ew, 104, t, s, ic, ac, title_size=14.5, sub_size=10.6, href=href)}</g>')

# =========================================================================== footer / legend
fy = ey + 104 + 34
add(f'<line x1="{px}" y1="{fy-20}" x2="{px+pw}" y2="{fy-20}" stroke="{LANE_BRD}" stroke-width="1.2"/>')
# legend
lx = px
add(f'<path d="M{lx} {fy} L{lx+34} {fy}" stroke="{SLATE}" stroke-width="1.6" marker-end="url(#arrow)"/>')
add(text(lx+44, fy+4, "Data & request flow", size=12, color=SLATE))
lx2 = lx + 230
add(f'<path d="M{lx2} {fy} L{lx2+34} {fy}" stroke="{AMBER}" stroke-width="1.7" '
    f'marker-start="url(#arrowA)" marker-end="url(#arrowA)"/>')
add(text(lx2+44, fy+4, "Bi-directional integration", size=12, color=SLATE))
add(text(px+pw, fy+4, "Copyright 2026 PlaidCloud, Inc.", size=12, color=SLATE, anchor="end"))

add('</svg>')

OUT_DIR.mkdir(parents=True, exist_ok=True)
svg_path = OUT_DIR / "platform-architecture.svg"
png_path = OUT_DIR / "platform-architecture.png"
pdf_path = OUT_DIR / "platform-architecture.pdf"

with open(svg_path, "w") as f:
    f.write("\n".join(svg))
print(f"wrote {svg_path}")

rsvg = shutil.which("rsvg-convert")
if rsvg:
    subprocess.run([rsvg, "-w", "3360", "-h", "2400", "-f", "png", "-o", str(png_path), str(svg_path)], check=True)
    subprocess.run([rsvg, "-f", "pdf", "-o", str(pdf_path), str(svg_path)], check=True)
    print(f"wrote {png_path}")
    print(f"wrote {pdf_path}")
else:
    print("skipped PNG/PDF export: rsvg-convert not found")
