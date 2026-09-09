import { defineCollection, z } from 'astro:content';
import { docsLoader } from '@astrojs/starlight/loaders';
import { docsSchema } from '@astrojs/starlight/schema';

/* `description` is permissive during migration to avoid blocking on legacy
 * pages with long or thin descriptions. Tighten (min 20, max 160) after
 * the description audit pass post-migration.
 *
 * The max is here ahead of that audit because the release pages regress without
 * it: every PR adding a What's New entry appended its outcome to the month's
 * description as well, growing one month's to 4,469 characters on a single line
 * — a meta description no search result can use, and a line that three
 * concurrent docs PRs conflict on by construction. */
export const collections = {
	docs: defineCollection({
		loader: docsLoader(),
		schema: docsSchema({
			extend: z.object({
				description: z.string().max(500).optional(),
			}),
		}),
	}),
};
