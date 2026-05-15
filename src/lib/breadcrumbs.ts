import { getEntry } from 'astro:content';

export type Crumb = { href: string; label: string };

function titleCase(seg: string): string {
	return seg
		.split('-')
		.map((w) => (w.length ? w[0].toUpperCase() + w.slice(1) : w))
		.join(' ');
}

/**
 * Build the breadcrumb trail for a Starlight page id. Walks ancestors
 * (everything except the leaf), looks up each ancestor's index page in
 * the docs collection for a friendly label, and falls back to a
 * title-cased slug segment when no index exists.
 */
export async function buildCrumbs(id: string): Promise<Crumb[]> {
	const parts = id.split('/').filter(Boolean);
	const ancestors = parts.slice(0, -1);
	const crumbs: Crumb[] = [];
	let acc = '';
	for (const segment of ancestors) {
		acc = acc ? `${acc}/${segment}` : segment;
		let entry = await getEntry('docs', `${acc}/index`).catch(() => undefined);
		if (!entry) {
			entry = await getEntry('docs', acc).catch(() => undefined);
		}
		const label = entry?.data?.title ?? titleCase(segment);
		crumbs.push({ href: `/${acc}/`, label });
	}
	return crumbs;
}
