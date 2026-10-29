import { getCollection } from 'astro:content';
import { englishId } from './og-image';

export type Crumb = { href: string; label: string };

function titleCase(seg: string): string {
	return seg
		.split('-')
		.map((w) => (w.length ? w[0].toUpperCase() + w.slice(1) : w))
		.join(' ');
}

// In Astro content collections an index file's id is the directory name
// (e.g. `releases/index.mdx` → id `releases`). One collection scan per build
// instead of a `getEntry` per ancestor — `getEntry` logs a warning for every
// id it can't find, and most locale ancestors are untranslated.
let titles: Promise<Map<string, string>> | null = null;
function getTitles() {
	titles ??= getCollection('docs').then((all) => new Map(all.map((e) => [e.id, e.data.title])));
	return titles;
}

// Build-time cache so Head.astro and PageTitle.astro share a single
// crumb-walk per page instead of doing it twice.
const cache = new Map<string, Promise<Crumb[]>>();

/**
 * Build the breadcrumb trail for a Starlight page. Walks ancestors
 * (everything except the leaf) and labels each with its index page's title
 * — the translated one when it exists, else the English one — falling back
 * to a title-cased slug segment when no index exists. On a locale page
 * (`locale` from Starlight route data, undefined for English) the crumbs
 * link within that locale.
 */
export function buildCrumbs(id: string, locale?: string): Promise<Crumb[]> {
	const key = `${locale ?? ''}:${id}`;
	const hit = cache.get(key);
	if (hit) return hit;
	const promise = (async () => {
		const byId = await getTitles();
		const prefix = locale ? `${locale}/` : '';
		const ancestors = englishId(id).split('/').filter(Boolean).slice(0, -1);
		const crumbs: Crumb[] = [];
		let acc = '';
		for (const segment of ancestors) {
			acc = acc ? `${acc}/${segment}` : segment;
			const label = byId.get(`${prefix}${acc}`) ?? byId.get(acc) ?? titleCase(segment);
			crumbs.push({ href: `/${prefix}${acc}/`, label });
		}
		return crumbs;
	})();
	cache.set(key, promise);
	return promise;
}
