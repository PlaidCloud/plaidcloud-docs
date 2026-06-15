// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import sitemap from '@astrojs/sitemap';
import starlightLlmsTxt from 'starlight-llms-txt';
import { fileURLToPath } from 'node:url';
import { execSync } from 'node:child_process';
import { readdirSync, statSync } from 'node:fs';
import { join, relative } from 'node:path';

// Build a `url -> ISO date` map from git log, one walk over the docs tree.
// Fallback to file mtime when the file isn't tracked (or git isn't available).
const DOCS_ROOT = fileURLToPath(new URL('./src/content/docs', import.meta.url));
const SITE_URL = 'https://docs.plaidcloud.com';

function fileToUrl(absPath) {
	let rel = relative(DOCS_ROOT, absPath).replace(/\\/g, '/');
	rel = rel.replace(/\.mdx?$/, '');
	if (rel === 'index') return `${SITE_URL}/`;
	rel = rel.replace(/\/index$/, '');
	return `${SITE_URL}/${rel}/`;
}

function walkDocs(dir, out = []) {
	for (const name of readdirSync(dir)) {
		const p = join(dir, name);
		const stat = statSync(p);
		if (stat.isDirectory()) walkDocs(p, out);
		else if (/\.(mdx?|MD)$/.test(name)) out.push(p);
	}
	return out;
}

function gitLastmod(absPath) {
	try {
		const iso = execSync(`git log -1 --format=%aI -- "${absPath}"`, {
			encoding: 'utf8',
			stdio: ['ignore', 'pipe', 'ignore'],
		}).trim();
		return iso || null;
	} catch {
		return null;
	}
}

const urlToLastmod = new Map();
for (const f of walkDocs(DOCS_ROOT)) {
	const iso = gitLastmod(f) ?? statSync(f).mtime.toISOString();
	urlToLastmod.set(fileToUrl(f), iso);
}

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
				// Per-page lastmod from git history (falls back to file mtime).
				const iso = urlToLastmod.get(item.url);
				if (iso) item.lastmod = iso;
				// Priority by pathname. Every Astro URL ends in `/`, so check
				// the pathname explicitly rather than the trailing slash.
				const pathname = new URL(item.url).pathname;
				if (pathname === '/')                          item.priority = 1.0;
				else if (pathname.startsWith('/get-started/')) item.priority = 1.0;
				else if (pathname.startsWith('/guides/'))      item.priority = 0.8;
				else if (pathname.startsWith('/integrations/')) item.priority = 0.7;
				else if (pathname.startsWith('/administration/')) item.priority = 0.6;
				else if (pathname.startsWith('/reference/'))   item.priority = 0.6;
				else if (pathname.startsWith('/releases/'))    item.priority = 0.5;
				else                                           item.priority = 0.7;
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
				Head: './src/components/Head.astro',
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
						{ label: 'Platform Architecture', link: '/get-started/platform-architecture/' },
						{ label: 'Concepts',   link: '/get-started/concepts/' },
						{ label: 'Tutorials',  link: '/get-started/tutorials/' },
						{ label: 'FAQ',        link: '/get-started/faq/' },
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
						{ label: 'PlaidCloud Git',    collapsed: true, items: [{ autogenerate: { directory: 'guides/git' } }] },
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
						{ label: 'Control plane', collapsed: true, items: [{ autogenerate: { directory: 'administration/control-plane' } }] },
						{ label: 'Scheduled events', collapsed: true, items: [{ autogenerate: { directory: 'administration/scheduled-events' } }] },
					],
				},
				{ label: "What's new", link: '/releases/' },
			],
			plugins: [
				starlightLlmsTxt({
					projectName: 'PlaidCloud',
					description:
						'PlaidCloud is a unified financial analytics platform for finance and data teams: ETL/ELT workflows, allocations, dimensions, a managed Lakehouse (Databend v1 or Iceberg+StarRocks v2), dashboards, and an MCP server for AI agents.',
					details: `Audience: data engineers, analysts, and finance/FP&A users.

Concepts:

- **Workspace**: a tenant — e.g. \`acme.plaid.cloud\`. All access is scoped to a workspace.
- **Project**: holds tables, dimensions, workflows, dashboards, and documents.
- **Workflow**: an ordered sequence of *workflow steps* (import, transform, allocate, export, notify, etc.).
- **Allocation**: distributes a value across a *dimension* using a driver and a method.
- **Lakehouse v1 vs v2**: v1 uses Databend SQL; v2 uses Apache Iceberg tables with StarRocks 4.1 SQL — function names differ.
- **PlaidLink Agent**: outbound proxy that lets workflows reach on-prem databases and file systems.
- **MCP server**: every workspace exposes \`/mcp/\` for AI coding agents (Claude Code, Cursor, ChatGPT, etc.).

Documentation structure:

- \`get-started/\` — concepts, quickstart, end-to-end tutorials, FAQ
- \`guides/\` — task-oriented how-to content
- \`reference/\` — workflow steps, expressions (SQL functions), connectors, CLI, glossary
- \`integrations/\` — AI coding agents, PySpark
- \`administration/\` — access management, SSO/SAML, scheduled events
- \`releases/\` — monthly release notes`,
					customSets: [
						{ label: 'Get Started', paths: ['get-started/**'], description: 'Concepts, quickstart, tutorials, and FAQ.' },
						{ label: 'Guides', paths: ['guides/**'], description: 'Task-oriented how-to content.' },
						{ label: 'Reference', paths: ['reference/**'], description: 'Workflow steps, expressions, connectors, CLI, and glossary.' },
						{ label: 'Integrations', paths: ['integrations/**'], description: 'AI coding agents and external tools.' },
						{ label: 'Administration', paths: ['administration/**'], description: 'Access management, SSO/SAML, and scheduled events.' },
					],
					exclude: ['releases/**'],
				}),
			],
		}),
	],
});
