import { getCollection } from 'astro:content';

/**
 * Returns the set of entry IDs that act as "landings" — pages whose
 * job is to introduce a subtree rather than be a self-contained article.
 *
 * In Astro content collections an index file's id is the directory name
 * (e.g. `guides/allocations/index.md` → `guides/allocations`), and any
 * sibling files under that directory have ids prefixed with `${id}/`.
 * So a landing is any entry whose id is a strict prefix of another
 * entry's id.
 *
 * Cached at module scope so the scan runs once per build.
 */
let cache: Promise<Set<string>> | null = null;

export function getLandingIds(): Promise<Set<string>> {
	if (!cache) {
		cache = (async () => {
			const all = await getCollection('docs');
			const ids = all.map((e) => e.id);
			const parents = new Set<string>();
			// The home page (id '') is a landing by definition.
			parents.add('');
			for (const a of ids) {
				for (const b of ids) {
					if (a !== b && b.startsWith(`${a}/`)) {
						parents.add(a);
						break;
					}
				}
			}
			return parents;
		})();
	}
	return cache;
}
