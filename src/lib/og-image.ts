/**
 * Decide whether a page gets its own per-page OG image or shares the
 * default fallback. Used by both `pages/open-graph/[...slug].ts` (which
 * generates the PNGs) and `components/Head.astro` (which writes the
 * `og:image` URL into the page head). Must stay in sync.
 *
 * Deep reference pages (workflow-step and expression-function leaves)
 * share `/open-graph/_default.png` — there are ~1,400 of them, so a
 * per-page card each would meaningfully grow the file count against the
 * Workers Assets 20,000-file limit for little SEO gain.
 */
export function hasGeneratedOG(id: string): boolean {
	if (id.startsWith('reference/workflow-steps/') && id.split('/').length > 3) return false;
	if (id.startsWith('reference/expressions/') && id.split('/').length > 3) return false;
	return true;
}
