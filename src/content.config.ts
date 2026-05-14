import { defineCollection, z } from 'astro:content';
import { docsLoader } from '@astrojs/starlight/loaders';
import { docsSchema } from '@astrojs/starlight/schema';

/* `description` is permissive during migration to avoid blocking on legacy
 * pages with long or thin descriptions. Tighten (min 20, max 160) after
 * the description audit pass post-migration. */
export const collections = {
	docs: defineCollection({
		loader: docsLoader(),
		schema: docsSchema({
			extend: z.object({
				description: z.string().optional(),
			}),
		}),
	}),
};
