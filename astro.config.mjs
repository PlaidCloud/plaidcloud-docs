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
			logo: {
				light: './src/assets/logo.svg',
				dark: './src/assets/logo-dark.svg',
				replacesTitle: true,
			},
			favicon: '/favicon.ico',
			customCss: ['./src/styles/brand.css'],
			editLink: {
				baseUrl: 'https://github.com/PlaidCloud/plaidcloud-docs/edit/main/',
			},
			lastUpdated: true,
			components: {
				PageTitle: './src/components/PageTitle.astro',
			},
			social: [
				{ icon: 'github', label: 'GitHub', href: 'https://github.com/PlaidCloud/plaidcloud-docs' },
			],
			sidebar: [
				{
					label: 'Get started',
					items: [
						{ label: 'Overview',   link: '/get-started/' },
						{ label: 'Quickstart', link: '/get-started/quickstart/' },
						{ label: 'Concepts',   link: '/get-started/concepts/' },
						{ label: 'Tutorials',  link: '/get-started/tutorials/' },
					],
				},
				{
					label: 'Guides',
					items: [
						{ label: 'Overview',          link: '/guides/' },
						{ label: 'AI Assistant',      collapsed: true, items: [{ autogenerate: { directory: 'guides/ai-assistant' } }] },
						{
							label: 'Allocations',
							collapsed: true,
							items: [
								{ label: 'Overview',                 link: '/guides/allocations/' },
								{ label: 'Getting started',          collapsed: true, items: [{ autogenerate: { directory: 'guides/allocations/getting-started' } }] },
								{ label: 'Setup',                    collapsed: true, items: [{ autogenerate: { directory: 'guides/allocations/setup' } }] },
								{ label: 'Results & troubleshooting', collapsed: true, items: [{ autogenerate: { directory: 'guides/allocations/results' } }] },
							],
						},
						{ label: 'Connections',       collapsed: true, items: [{ autogenerate: { directory: 'guides/connections' } }] },
						{ label: 'Dashboards',        collapsed: true, items: [{ autogenerate: { directory: 'guides/dashboards' } }] },
						{ label: 'Data',              collapsed: true, items: [{ autogenerate: { directory: 'guides/data' } }] },
						{ label: 'Dimensions',        collapsed: true, items: [{ autogenerate: { directory: 'guides/dimensions' } }] },
						{
							label: 'Documents',
							collapsed: true,
							items: [
								{ label: 'Overview',           link: '/guides/documents/' },
								{ label: 'Account management', collapsed: true, items: [{ autogenerate: { directory: 'guides/documents/account-management' } }] },
								{ label: 'Adding accounts',    collapsed: true, items: [{ autogenerate: { directory: 'guides/documents/adding-accounts' } }] },
								{ label: 'Searching documents', link: '/guides/documents/searching-documents/' },
								{ label: 'Using documents',     link: '/guides/documents/using-document/' },
							],
						},
						{ label: 'Email',             collapsed: true, items: [{ autogenerate: { directory: 'guides/email' } }] },
						{ label: 'Panel apps',        collapsed: true, items: [{ autogenerate: { directory: 'guides/panel-apps' } }] },
						{ label: 'Projects',          collapsed: true, items: [{ autogenerate: { directory: 'guides/projects' } }] },
						{ label: 'Sandbox',           collapsed: true, items: [{ autogenerate: { directory: 'guides/sandbox' } }] },
						{ label: 'Workflows',         collapsed: true, items: [{ autogenerate: { directory: 'guides/workflows' } }] },
					],
				},
				// Reference is top-level only — full tree (1,200+ entries from
				// expressions/workflow-steps) would inline into every page and
				// blow past Workers Assets size limits. Users navigate references
				// via landing pages + search (Pagefind).
				{
					label: 'Reference',
					collapsed: true,
					items: [
						{ label: 'Overview',       link: '/reference/' },
						{ label: 'Connectors',     link: '/reference/connectors/' },
						{ label: 'Workflow steps', link: '/reference/workflow-steps/' },
						{ label: 'Expressions',    link: '/reference/expressions/' },
						{ label: 'CLI',            link: '/reference/cli/' },
						{ label: 'Glossary',       link: '/reference/glossary/' },
					],
				},
				{
					label: 'Integrations',
					items: [
						{ label: 'Overview',          link: '/integrations/' },
						{ label: 'AI coding agents',  collapsed: true, items: [{ autogenerate: { directory: 'integrations/ai-coding-agents' } }] },
						{ label: 'PySpark',           collapsed: true, items: [{ autogenerate: { directory: 'integrations/pyspark' } }] },
					],
				},
				{
					label: 'Administration',
					items: [
						{ label: 'Overview', link: '/administration/' },
						{
							label: 'Access management',
							collapsed: true,
							items: [
								{ label: 'Overview',                link: '/administration/access/' },
								{ label: 'Organization & workspaces', collapsed: true, items: [{ autogenerate: { directory: 'administration/access/overview' } }] },
								{ label: 'Member authentication',   collapsed: true, items: [{ autogenerate: { directory: 'administration/access/member-authentication' } }] },
								{ label: 'Member management',       collapsed: true, items: [{ autogenerate: { directory: 'administration/access/member-management' } }] },
								{ label: 'Member identity',         collapsed: true, items: [{ autogenerate: { directory: 'administration/access/member-user-identity' } }] },
								{ label: 'Security groups',         collapsed: true, items: [{ autogenerate: { directory: 'administration/access/managing-security-groups-and-assignments' } }] },
								{ label: 'Advanced (SSO/SAML)',     collapsed: true, items: [{ autogenerate: { directory: 'administration/access/advanced' } }] },
							],
						},
						{ label: 'Scheduled events', collapsed: true, items: [{ autogenerate: { directory: 'administration/scheduled-events' } }] },
					],
				},
				{ label: "What's new", link: '/releases/' },
			],
			plugins: [starlightLlmsTxt()],
		}),
	],
});
