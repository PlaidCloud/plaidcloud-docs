import { getEntry } from 'astro:content';

export type Crumb = { href: string; label: string };

function titleCase(seg: string): string {
	return seg
		.split('-')
		.map((w) => (w.length ? w[0].toUpperCase() + w.slice(1) : w))
		.join(' ');
}

// Build-time cache so Head.astro and PageTitle.astro share a single
// crumb-walk per page id instead of doing 2× the getEntry lookups.
const cache = new Map<string, Promise<Crumb[]>>();

/**
 * Build the breadcrumb trail for a Starlight page id. Walks ancestors
 * (everything except the leaf), looks up each ancestor's index page in
 * the docs collection for a friendly label, and falls back to a
 * title-cased slug segment when no index exists.
 */
export function buildCrumbs(id: string): Promise<Crumb[]> {
	const hit = cache.get(id);
	if (hit) return hit;
	const promise = (async () => {
		const parts = id.split('/').filter(Boolean);
		const ancestors = parts.slice(0, -1);
		const crumbs: Crumb[] = [];
		let acc = '';
		for (const segment of ancestors) {
			acc = acc ? `${acc}/${segment}` : segment;
			// In Astro v6 content collections an index file's id is the
			// directory name (e.g. `releases/index.mdx` → id `releases`),
			// so look that up directly. Astro's `getEntry` logs a warning
			// when it can't find an id even if the rejection is caught, so
			// the previous `/index`-first fallback flooded the build log.
			const entry = await getEntry('docs', acc).catch(() => undefined);
			const label = entry?.data?.title ?? titleCase(segment);
			crumbs.push({ href: `/${acc}/`, label });
		}
		return crumbs;
	})();
	cache.set(id, promise);
	return promise;
}
