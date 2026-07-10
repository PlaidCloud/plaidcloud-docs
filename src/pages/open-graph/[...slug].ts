// Generates a branded 1200×630 Open Graph card for every docs page that opts
// in (see `hasGeneratedOG`), plus a shared `_default` card for deep reference
// leaves. The design mirrors the marketing site's cards (plaidcloud.com):
// navy field with a warm orange/amber + cyan glow, PlaidCloud logo, an
// uppercase section eyebrow, the page title, and an orange→amber accent bar.
//
// Rendering: hand-built SVG rasterized by @resvg/resvg-js with the vendored
// Inter TTFs in scripts/assets/og/ (resvg needs real font files, not a remote
// stylesheet — the previous astro-og-canvas config pointed at a Google Fonts
// CSS URL, which returns CSS rather than a typeface, so every card rendered
// blank). resvg emits a barely-compressed PNG (~150 KB); a lossless sharp
// re-encode drops it to ~30 KB (pixel-identical) so 300+ cards don't bloat the
// Workers Assets upload. `Head.astro` writes the matching `<slug>.png` URL.
import type { APIContext } from 'astro';
import { getCollection } from 'astro:content';
import { readFileSync } from 'node:fs';
import { join } from 'node:path';
import { Resvg } from '@resvg/resvg-js';
import sharp from 'sharp';
import { hasGeneratedOG } from '../../lib/og-image';

// Anchor to the project root (cwd during `astro build`) rather than
// `import.meta.url` — the endpoint runs from a Vite-bundled chunk whose
// output depth is bundler-dependent, so a relative climb isn't reliable.
const asset = (name: string) => join(process.cwd(), 'scripts/assets/og', name);

const FONTS = [asset('Inter-400.ttf'), asset('Inter-700.ttf')];
const LOGO_B64 = readFileSync(asset('PlaidCloudLogo_White.png')).toString('base64');

const SECTION_EYEBROWS: Record<string, string> = {
	'get-started': 'Get Started',
	guides: 'Guides',
	reference: 'Reference',
	integrations: 'Integrations',
	administration: 'Administration',
	releases: "What's New",
};

// Root (empty id) and the fallback card read as "Documentation".
function eyebrowFor(id: string): string {
	const top = id.split('/')[0];
	return SECTION_EYEBROWS[top] ?? 'Documentation';
}

const esc = (s: string) =>
	s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

// Greedy word-wrap using a rough Inter-Bold advance width. Conservative on
// purpose: a slightly early wrap beats an overflowing line.
function wrap(text: string, fontSize: number, maxWidth: number): string[] {
	const perLine = Math.floor(maxWidth / (fontSize * 0.56));
	const lines: string[] = [];
	let line = '';
	for (const word of text.split(/\s+/)) {
		const cand = line ? `${line} ${word}` : word;
		if (cand.length > perLine && line) {
			lines.push(line);
			line = word;
		} else {
			line = cand;
		}
	}
	if (line) lines.push(line);
	return lines;
}

function card(title: string, eyebrow: string): string {
	let fontSize = 64;
	let lines = wrap(title, fontSize, 1040);
	if (lines.length > 2) {
		fontSize = 52;
		lines = wrap(title, fontSize, 1040);
	}
	if (lines.length > 3) {
		lines = lines.slice(0, 3);
		lines[2] = lines[2].replace(/\s+\S*$/, '') + '…';
	}
	const lineHeight = fontSize * 1.18;
	const titleBlockH = lines.length * lineHeight;
	const titleY = 340 - titleBlockH / 2 + fontSize; // vertically centered around y=340
	const tspans = lines
		.map((l, i) => `<tspan x="80" y="${(titleY + i * lineHeight).toFixed(0)}">${esc(l)}</tspan>`)
		.join('');
	return `<svg width="1200" height="630" viewBox="0 0 1200 630" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <radialGradient id="glowA" cx="100%" cy="100%" r="90%">
      <stop offset="0%" stop-color="#FF7514" stop-opacity="0.55"/>
      <stop offset="35%" stop-color="#FDC20D" stop-opacity="0.28"/>
      <stop offset="75%" stop-color="#041E4B" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glowB" cx="0%" cy="0%" r="80%">
      <stop offset="0%" stop-color="#2EBDF1" stop-opacity="0.30"/>
      <stop offset="65%" stop-color="#041E4B" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="bar" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#FF7514"/>
      <stop offset="100%" stop-color="#FDC20D"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="630" fill="#041E4B"/>
  <rect width="1200" height="630" fill="url(#glowA)"/>
  <rect width="1200" height="630" fill="url(#glowB)"/>
  <image x="80" y="64" width="196" height="52" preserveAspectRatio="xMinYMid meet" xlink:href="data:image/png;base64,${LOGO_B64}"/>
  <text x="80" y="228" font-family="Inter" font-size="26" font-weight="700" letter-spacing="4" fill="#FDC20D">${esc(eyebrow.toUpperCase())}</text>
  <text font-family="Inter" font-size="${fontSize}" font-weight="700" fill="#FFFFFF">${tspans}</text>
  <text x="80" y="566" font-family="Inter" font-size="26" font-weight="400" fill="#FFFFFF" fill-opacity="0.6">docs.plaidcloud.com</text>
  <rect x="0" y="618" width="1200" height="12" fill="url(#bar)"/>
</svg>`;
}

interface CardProps {
	title: string;
	eyebrow: string;
}

export async function getStaticPaths() {
	const docs = await getCollection('docs');
	const paths = docs
		.filter((entry) => hasGeneratedOG(entry.id || 'index'))
		.map((entry) => ({
			// The `.png` extension is part of the slug so the emitted file is
			// `<slug>.png` — this keeps a page card (e.g. `administration.png`)
			// from colliding with a child section's directory (`administration/`).
			// Root page has an empty id; `Head.astro` points it at `index.png`.
			params: { slug: `${entry.id || 'index'}.png` },
			props: { title: entry.data.title, eyebrow: eyebrowFor(entry.id) } as CardProps,
		}));
	paths.push({
		params: { slug: '_default.png' },
		props: { title: 'PlaidCloud Documentation', eyebrow: 'Documentation' },
	});
	return paths;
}

export async function GET({ props }: APIContext): Promise<Response> {
	const { title, eyebrow } = props as CardProps;
	const rendered = new Resvg(card(title, eyebrow), {
		fitTo: { mode: 'width', value: 1200 },
		font: { fontFiles: FONTS, defaultFontFamily: 'Inter', loadSystemFonts: false },
	})
		.render()
		.asPng();
	// Lossless re-encode: resvg's PNG deflate is weak; max-compression sharp
	// shrinks each card ~5× with no pixel change.
	const png = await sharp(rendered).png({ compressionLevel: 9, effort: 10 }).toBuffer();
	return new Response(new Uint8Array(png), {
		headers: { 'Content-Type': 'image/png' },
	});
}
