// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import sitemap from '@astrojs/sitemap';
import starlightLlmsTxt from 'starlight-llms-txt';
import { fileURLToPath } from 'node:url';

export default defineConfig({
	site: 'https://docs.plaidcloud.com',
	vite: {
		resolve: {
			alias: {
				'@snippets': fileURLToPath(new URL('./src/snippets', import.meta.url)),
			},
		},
	},
	integrations: [
		sitemap({
			serialize(item) {
				if (item.url.endsWith('/')) item.priority = 1.0;
				else if (item.url.includes('/get-started/')) item.priority = 1.0;
				else if (item.url.includes('/guides/'))      item.priority = 0.8;
				else if (item.url.includes('/reference/'))   item.priority = 0.6;
				else if (item.url.includes('/releases/'))    item.priority = 0.5;
				return item;
			},
		}),
		starlight({
			title: 'PlaidCloud',
			logo: { src: './src/assets/logo.svg', replacesTitle: true },
			favicon: '/favicon.ico',
			customCss: ['./src/styles/brand.css'],
			editLink: {
				baseUrl: 'https://github.com/PlaidCloud/plaidcloud-docs/edit/main/',
			},
			lastUpdated: true,
			social: [
				{ icon: 'github', label: 'GitHub', href: 'https://github.com/PlaidCloud/plaidcloud-docs' },
			],
			sidebar: [
				{ label: 'Get started',    items: [{ autogenerate: { directory: 'get-started' } }] },
				{ label: 'Guides',         items: [{ autogenerate: { directory: 'guides' } }] },
				{ label: 'Reference',      collapsed: true, items: [{ autogenerate: { directory: 'reference' } }] },
				{ label: 'Integrations',   items: [{ autogenerate: { directory: 'integrations' } }] },
				{ label: 'Administration', items: [{ autogenerate: { directory: 'administration' } }] },
				{ label: 'Releases',       items: [{ autogenerate: { directory: 'releases' } }] },
			],
			plugins: [starlightLlmsTxt()],
		}),
	],
});
