import { getCollection } from 'astro:content';
import { OGImageRoute } from 'astro-og-canvas';

const docs = await getCollection('docs');

// Skip OG image generation for deep reference pages (workflow step pages
// and expression function pages) — they're rarely shared on social media
// and they account for most of the page count. Reference category and
// sub-category landing pages still get OG images. Pages without a generated
// OG fall back to the site's default OG image declared in the layout.
function shouldGenerate(id: string): boolean {
	if (id.startsWith('reference/workflow-steps/') && id.split('/').length > 3) return false;
	if (id.startsWith('reference/expressions/') && id.split('/').length > 3) return false;
	return true;
}

const pages = Object.fromEntries(
	docs.filter((entry) => shouldGenerate(entry.id))
		.map((entry) => [entry.id, { data: entry.data }]),
);

// Add a generic default OG image used as a fallback by reference pages
// that opt out of per-page generation.
pages['_default'] = {
	data: {
		title: 'PlaidCloud Documentation',
		description: 'Unified financial analytics platform — workflows, allocations, dashboards.',
	},
};

export const { getStaticPaths, GET } = await OGImageRoute({
	param: 'slug',
	pages,
	getImageOptions: (_path, page) => ({
		title: page.data.title,
		description: page.data.description ?? '',
		bgGradient: [
			[0, 26, 61],   // #001a3d navy deep
			[0, 47, 108],  // #002f6c primary navy
		],
		border: { color: [0, 163, 224], width: 8, side: 'inline-start' },
		padding: 60,
		font: {
			title: {
				size: 72,
				families: ['Inter', 'sans-serif'],
				weight: 'Bold',
				color: [255, 255, 255],
				lineHeight: 1.1,
			},
			description: {
				size: 32,
				families: ['Inter', 'sans-serif'],
				color: [180, 200, 230],
				lineHeight: 1.4,
			},
		},
		fonts: [
			'https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap',
		],
	}),
});
