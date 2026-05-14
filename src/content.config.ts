import { defineCollection, z } from 'astro:content';
import { docsLoader } from '@astrojs/starlight/loaders';
import { docsSchema } from '@astrojs/starlight/schema';

/* `description` stays optional during migration so the build doesn't block
 * on legacy pages with missing or thin descriptions. Tighten to required
 * after the description audit pass post-migration. */
export const collections = {
	docs: defineCollection({
		loader: docsLoader(),
		schema: docsSchema({
			extend: z.object({
				description: z.string().min(20).max(160).optional(),
			}),
		}),
	}),
};
