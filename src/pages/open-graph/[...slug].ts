import { getCollection } from 'astro:content';
import { OGImageRoute } from 'astro-og-canvas';
import { hasGeneratedOG } from '../../lib/og-image';

const docs = await getCollection('docs');

const pages = Object.fromEntries(
	docs.filter((entry) => hasGeneratedOG(entry.id))
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
