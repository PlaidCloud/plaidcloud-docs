import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

/**
 * Structured per-page corpus for the docs AI assistant's retriever
 * (sc-22943 — BM25 shortlist + fetch, replacing the embeddings/Chroma path).
 *
 * One doc page = one JSON object { slug, title, description, text }. The
 * consumer (plaid `docs_retrieval`) fetches this once from the CDN
 * (`/pages.json`) and builds a BM25 index over it — no embeddings, no vector
 * store. Reliable per-page boundaries and real slugs come for free from the
 * content collection, unlike parsing the monolithic `llms-full.txt`.
 */

/** Starlight page id → canonical slug. The root landing page has id `index`;
 * nested index files are already stripped by Starlight (e.g. `guides`). */
function toSlug(id: string): string {
	return !id || id === 'index' ? '/' : `/${id}/`;
}

/**
 * Strip MDX/JSX noise to plain retrieval text. Mirrors the sc-22943 eval's
 * corpus cleaning so the published corpus matches what the retriever was
 * evaluated on. Frontmatter is already parsed out into `data`.
 */
function cleanBody(raw: string): string {
	return raw
		.replace(/^\s*import\s.+$/gm, '')        // MDX import lines
		.replace(/<\/?[A-Za-z][^>]*\/?>/g, '')   // JSX / HTML tags (keep inner text)
		.replace(/\[([^\]]+)\]\([^)]*\)/g, '$1') // [text](url) → text
		.replace(/^```.*$/gm, '')                // code-fence markers
		.replace(/\n{3,}/g, '\n\n')
		.trim();
}

export const GET: APIRoute = async () => {
	const entries = await getCollection('docs');
	const pages = entries
		.filter((entry) => entry.id !== '404')
		.map((entry) => ({
			slug: toSlug(entry.id),
			title: entry.data.title ?? '',
			description: entry.data.description ?? '',
			text: cleanBody(entry.body ?? ''),
		}))
		.sort((a, b) => a.slug.localeCompare(b.slug));

	return new Response(JSON.stringify(pages), {
		headers: { 'content-type': 'application/json; charset=utf-8' },
	});
};
