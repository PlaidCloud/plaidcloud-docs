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

// The production build (Cloudflare Workers Builds) checks out a shallow clone,
// so `git log` would report the single HEAD commit for every file and every
// page would share one lastmod (the build time) — defeating freshness signals
// in both the sitemap and the JSON-LD `dateModified`. Unshallow once so the
// per-file dates below are real. No-op locally (already a full clone).
try {
	const shallow = execSync('git rev-parse --is-shallow-repository', {
		encoding: 'utf8',
		stdio: ['ignore', 'pipe', 'ignore'],
	}).trim();
	if (shallow === 'true') {
		// timeout so a hung fetch can't stall the CI build — on timeout
		// execSync throws and we fall through to the mtime fallback.
		execSync('git fetch --unshallow', { stdio: 'ignore', timeout: 60_000 });
	}
} catch {
	// no git / no network / timed out — lastmod falls back to file mtime
}

// One `git log` pass over the docs tree, newest commit first, keeping the first
// date seen per file. A `git log` per file spawned one process per page, which
// grows linearly with the corpus.
const fileToLastmod = new Map();
try {
	const log = execSync(`git -C "${DOCS_ROOT}" -c core.quotePath=off log --relative --format=%x00%aI --name-only -- .`, {
		encoding: 'utf8',
		stdio: ['ignore', 'pipe', 'ignore'],
		maxBuffer: 1024 * 1024 * 1024,
	});
	for (const commit of log.split('\0').slice(1)) {
		const [iso, ...files] = commit.trim().split('\n');
		for (const f of files) if (f && !fileToLastmod.has(f)) fileToLastmod.set(f, iso);
	}
} catch {
	// no git — every page falls back to file mtime below
}

const urlToLastmod = new Map();
for (const f of walkDocs(DOCS_ROOT)) {
	const iso = fileToLastmod.get(relative(DOCS_ROOT, f)) ?? statSync(f).mtime.toISOString();
	urlToLastmod.set(fileToUrl(f), iso);
}

export default defineConfig({
	site: 'https://docs.plaidcloud.com',
	vite: {
		resolve: {
			alias: {
				'@snippets': fileURLToPath(new URL('./src/snippets', import.meta.url)),
				'@components': fileURLToPath(new URL('./src/components', import.meta.url)),
			},
		},
		// @resvg/resvg-js is a native addon — keep Vite from trying to bundle it
		// when the open-graph endpoint runs during the build.
		ssr: { external: ['@resvg/resvg-js'] },
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
			// Sidebar = journey sections. Pages are slug entries (titles/labels come
			// from frontmatter, per locale); autogenerate only where a folder is
			// exactly one group. A new guide must be added here by hand.
			sidebar: [
				{
					label: 'Get Started',
					items: [
						'get-started',
						'get-started/sign-up',
						'get-started/quickstart',
						'get-started/platform-architecture',
						'get-started/concepts',
						'get-started/supported-browsers',
						'get-started/faq',
						{
							label: 'Tutorials',
							collapsed: true,
							items: [
								'get-started/tutorials',
								{
									label: 'Start Here',
									collapsed: true,
									items: [
										'get-started/tutorials/first-15-minutes',
										'get-started/tutorials/csv-to-answer',
										'get-started/tutorials/start-from-a-project',
									],
								},
								{
									label: 'Build Your First Pipeline',
									collapsed: true,
									items: [
										'get-started/tutorials/connect-a-data-source',
										'get-started/tutorials/analyze-netsuite-financials',
										'get-started/tutorials/analyze-sage-intacct-financials',
										'get-started/tutorials/load-and-transform-data',
										'get-started/tutorials/transform-with-sql',
										'get-started/tutorials/design-a-dimension',
										'get-started/tutorials/build-an-allocation',
										'get-started/tutorials/build-a-dashboard',
									],
								},
								{
									label: 'Work With Confidence',
									collapsed: true,
									items: [
										'get-started/tutorials/snapshots-and-time-travel',
										'get-started/tutorials/debug-a-workflow',
										'get-started/tutorials/reuse-variables-macros-udfs',
										'get-started/tutorials/collaborate-versions-and-sharing',
									],
								},
								{
									label: 'Operate and Govern',
									collapsed: true,
									items: [
										'get-started/tutorials/schedule-a-workflow',
										'get-started/tutorials/control-data-access',
									],
								},
								{
									label: 'Coming From Another Tool',
									collapsed: true,
									items: [
										'get-started/tutorials/migrate-your-first-alteryx-workflow',
										'get-started/tutorials/excel-with-plaidxl',
									],
								},
								{
									label: 'Extend With AI',
									collapsed: true,
									items: [
										'get-started/tutorials/fix-a-workflow-with-ai',
										'get-started/tutorials/mcp-with-ai-agent',
										'get-started/tutorials/panel-ai-agent',
									],
								},
							],
						},
					],
				},
				{
					label: 'Basics',
					collapsed: true,
					items: [
						'guides',
						'guides/launcher',
						'guides/change-your-language',
						'guides/projects/sharing-links',
						'guides/projects/breadcrumbs-and-shareable-links',
						{ label: 'Mobile App', collapsed: true, items: [{ autogenerate: { directory: 'guides/mobile-app' } }] },
						{ label: 'Email', collapsed: true, items: [{ autogenerate: { directory: 'guides/email' } }] },
						'guides/time-expense/track-time-and-expenses',
						{ label: 'Help & Support', collapsed: true, items: [{ autogenerate: { directory: 'guides/support' } }] },
					],
				},
				{
					label: 'Connect Data',
					collapsed: true,
					items: [
						{
							label: 'Connections',
							collapsed: true,
							items: [
								'guides/connections',
								'guides/connections/create-connection',
								'guides/connections/clone-connection',
								'guides/connections/external-lakehouse',
								'guides/connections/singer-sources',
								'guides/connections/plaidcloud-git',
								{
									label: 'ERP & Accounting',
									collapsed: true,
									items: [
										'guides/connections/acumatica',
										'guides/connections/business-central',
										'guides/connections/dynamics-365-fo',
										'guides/connections/oracle-fusion',
										'guides/connections/quickbooks',
										'guides/connections/sage-intacct',
										'guides/connections/s4hana-cloud',
										'guides/connections/sap-adhoc-extract',
										'guides/connections/workday-financials',
										'guides/connections/xero',
									],
								},
								{
									label: 'NetSuite',
									collapsed: true,
									items: [
										'guides/connections/netsuite',
										'guides/connections/import-netsuite-financials',
										'guides/connections/netsuite-access-for-data-foundation',
										'guides/connections/netsuite-financial-queries',
										'guides/connections/post-netsuite-journal-entries',
									],
								},
								{
									label: 'EPM & Planning',
									collapsed: true,
									items: [
										'guides/connections/anaplan',
										'guides/connections/essbase',
										'guides/connections/hfm-fccs',
										'guides/connections/tm1',
									],
								},
								{
									label: 'CRM & Operations',
									collapsed: true,
									items: [
										'guides/connections/salesforce',
										'guides/connections/samsara',
									],
								},
								{
									label: 'Write-Back',
									collapsed: true,
									items: [
										'guides/connections/posting-register',
										'guides/connections/erp-post-history',
									],
								},
							],
						},
						{
							label: 'Files & Storage',
							collapsed: true,
							items: [
								'guides/documents',
								'guides/documents/using-document',
								'guides/documents/searching-documents',
								{ label: 'Manage Accounts & Access', collapsed: true, items: [{ autogenerate: { directory: 'guides/documents/account-management' } }] },
								{
									label: 'Add Cloud Object Storage',
									collapsed: true,
									items: [
										'guides/documents/adding-accounts',
										'guides/documents/adding-accounts/add-aws-s3-account',
										'guides/documents/adding-accounts/add-google-cloud-storage-account',
										'guides/documents/adding-accounts/add-managed-bucket-account',
										'guides/documents/adding-accounts/add-wasabi-hot-storage-account',
										'guides/documents/adding-accounts/add-azure-blob-storage-account',
										'guides/documents/adding-accounts/add-azure-data-lake-gen2-account',
										'guides/documents/adding-accounts/add-minio-account',
										'guides/documents/adding-accounts/add-backblaze-b2-account',
										'guides/documents/adding-accounts/add-cloudflare-r2-account',
										'guides/documents/adding-accounts/add-digitalocean-spaces-account',
										'guides/documents/adding-accounts/add-linode-object-storage-account',
									],
								},
								{
									label: 'Add File Shares & Servers',
									collapsed: true,
									items: [
										'guides/documents/adding-accounts/add-google-drive-account',
										'guides/documents/adding-accounts/add-onedrive-account',
										'guides/documents/adding-accounts/add-ftp-account',
										'guides/documents/adding-accounts/add-sftp-account',
										'guides/documents/adding-accounts/add-webdav-account',
									],
								},
							],
						},
					],
				},
				{
					label: 'Organize Data',
					collapsed: true,
					items: [
						{
							label: 'Projects',
							collapsed: true,
							items: [
								'guides/projects',
								'guides/projects/viewing-projects',
								'guides/projects/managing-projects',
								'guides/projects/archive-a-project',
								'guides/projects/viewing-the-project-log',
								'guides/projects/compare-and-merge-projects',
								'guides/projects/export-to-portable-format',
								'guides/projects/organizing-with-labels',
								'guides/projects/data-foundation-enterprise-profitability',
							],
						},
						{
							label: 'Tables & Views',
							collapsed: true,
							items: [
								'guides/data',
								'guides/data/tables-views',
								'guides/data/table-explorer',
								'guides/projects/managing-tables-and-views',
								'guides/projects/managing-data-editors',
								'guides/data/publish',
								'guides/data/table-snapshots',
								'guides/data/selecting-latest-record-in-large-history-table',
								'guides/data/currency-data-type',
								'guides/data/vector-data-type',
								'guides/data/migrate-project-lakehouse',
							],
						},
						{
							label: 'Dimensions',
							collapsed: true,
							items: [
								{ autogenerate: { directory: 'guides/dimensions' } },
								'guides/projects/managing-hierarchies',
							],
						},
					],
				},
				{
					label: 'Transform & Automate',
					collapsed: true,
					items: [
						'guides/workflows',
						{
							label: 'Create & Edit',
							collapsed: true,
							items: [
								'guides/workflows/where-are-workflows',
								'guides/workflows/workflow-explorer',
								'guides/workflows/create-workflow',
								'guides/workflows/duplicate-a-workflow',
								'guides/workflows/advanced-workflows',
								'guides/workflows/copy-paste-steps',
								'guides/workflows/change-the-order-of-steps-in-a-workflow',
								'guides/workflows/step-numbers',
								'guides/workflows/prettify-code-in-editors',
								'guides/workflows/column-propagation',
								'guides/workflows/preview-step-data',
							],
						},
						{
							label: 'Build Logic',
							collapsed: true,
							items: [
								'guides/workflows/manage-workflow-variables',
								'guides/workflows/step-conditions',
								'guides/workflows/create-a-macro',
								'guides/workflows/multi-table-join-step',
								'guides/workflows/llm-step',
								'guides/workflows/rest-request-step',
								'guides/workflows/notify-email-templates',
								'guides/workflows/geospatial-analytics',
							],
						},
						{
							label: 'Run & Control',
							collapsed: true,
							items: [
								'guides/workflows/run-a-workflow',
								'guides/workflows/running-one-step-in-a-workflow',
								'guides/workflows/running-a-range-of-steps-in-a-workflow',
								'guides/workflows/skip-steps-in-a-workflow',
								'guides/workflows/continue-on-error',
								'guides/workflows/managing-step-errors',
								'guides/workflows/controlling-parallel-execution',
								'guides/workflows/text-alerts',
							],
						},
						{
							label: 'Monitor & Tune',
							collapsed: true,
							items: [
								'guides/workflows/viewing-workflow-log',
								'guides/workflows/view-workflow-report',
								'guides/workflows/view-a-dependency-audit',
								'guides/workflows/optimize-a-workflow',
								'guides/workflows/sync-dependencies',
							],
						},
						{ label: 'Scheduling', collapsed: true, items: [{ autogenerate: { directory: 'administration/scheduled-events' } }] },
					],
				},
				{
					label: 'Migrate From Other Tools',
					collapsed: true,
					items: [
						{
							label: 'Alteryx',
							collapsed: true,
							items: [
								'guides/workflows/alteryx-migration-readiness-checklist',
								'guides/workflows/package-alteryx-dependencies',
								'guides/workflows/convert-yxdb-files-for-import',
								'guides/workflows/migrate-alteryx-workflows',
								'guides/workflows/troubleshoot-alteryx-imports',
								'guides/workflows/validate-converted-alteryx-workflows',
								'guides/workflows/validate-alteryx-reports-and-artifacts',
								'guides/workflows/use-converted-alteryx-apps',
								'guides/workflows/migrate-spatial-alteryx-workflows',
								'guides/workflows/orchestrate-alteryx-migrations-with-mcp',
							],
						},
						'guides/workflows/migrate-knime-workflows',
						'guides/workflows/migrate-prophecy-projects',
						'guides/workflows/migrate-savant-analyses',
					],
				},
				{
					label: 'Allocate',
					collapsed: true,
					items: [
						'guides/allocations',
						{ label: 'First Allocation', collapsed: true, items: [{ autogenerate: { directory: 'guides/allocations/getting-started' } }] },
						{ label: 'Setup', collapsed: true, items: [{ autogenerate: { directory: 'guides/allocations/setup' } }] },
						{
							label: 'Results & Troubleshooting',
							collapsed: true,
							items: [
								{ autogenerate: { directory: 'guides/allocations/results' } },
								'integrations/ai-coding-agents/tracing-allocations',
							],
						},
					],
				},
				{
					label: 'Analyze & Report',
					collapsed: true,
					items: [
						{ label: 'Dashboards', collapsed: true, items: [{ autogenerate: { directory: 'guides/dashboards' } }] },
						'integrations/ai-coding-agents/metric-definitions',
						'integrations/ai-coding-agents/analysis-paths',
					],
				},
				{
					label: 'AI Assistant (Weave)',
					collapsed: true,
					items: [
						'guides/ai-assistant',
						'guides/ai-assistant/weave-tab',
						{
							label: 'Review Findings',
							collapsed: true,
							items: [
								'guides/ai-assistant/weave-findings',
								'guides/ai-assistant/weave-metric-insights',
								'guides/ai-assistant/weave-readiness',
								'guides/ai-assistant/weave-reconciliation',
								'guides/ai-assistant/weave-monthly-summary',
							],
						},
						{
							label: 'Build With Weave',
							collapsed: true,
							items: [
								'guides/ai-assistant/fixing-workflow-errors',
								'guides/ai-assistant/generate-sql-extract',
								'guides/ai-assistant/impact-preview',
								'guides/ai-assistant/check-while-you-edit',
								'guides/ai-assistant/weave-documentation',
							],
						},
						{
							label: 'Govern Weave',
							collapsed: true,
							items: [
								'guides/ai-assistant/weave-activity',
								'guides/ai-assistant/weave-ai-features',
							],
						},
					],
				},
				{
					label: 'Build Apps',
					collapsed: true,
					items: [
						{
							label: 'Panel Apps',
							collapsed: true,
							items: [
								'guides/panel-apps',
								{
									label: 'Use',
									collapsed: true,
									items: [
										'guides/panel-apps/using',
										'guides/panel-apps/gallery',
									],
								},
								{
									label: 'Build',
									collapsed: true,
									items: [
										'guides/panel-apps/creating',
										'guides/panel-apps/studio',
										'guides/panel-apps/app-kit',
										'guides/panel-apps/build-with-weave',
										'guides/panel-apps/branding',
										'guides/panel-apps/alerts-and-digests',
									],
								},
								{
									label: 'Data & Deploy',
									collapsed: true,
									items: [
										'guides/panel-apps/accessing-data',
										'guides/panel-apps/data-api',
										'guides/panel-apps/deploy-from-git',
									],
								},
							],
						},
						{ label: 'Dash Apps', collapsed: true, items: [{ autogenerate: { directory: 'guides/dash-apps' } }] },
						{ label: 'Custom App Sandbox', collapsed: true, items: [{ autogenerate: { directory: 'guides/sandbox' } }] },
						{ label: 'PlaidCloud Git', collapsed: true, items: [{ autogenerate: { directory: 'guides/git' } }] },
						{
							label: 'Location APIs',
							collapsed: true,
							items: [
								'guides/data/geocoding-api',
								'guides/data/drive-time-routing-api',
							],
						},
					],
				},
				{
					label: 'Integrations',
					collapsed: true,
					items: [
						'integrations',
						{
							label: 'AI Agents (MCP)',
							collapsed: true,
							items: [
								'integrations/ai-coding-agents',
								'integrations/ai-coding-agents/getting-started',
								{
									label: 'Clients',
									collapsed: true,
									items: [
										'integrations/ai-coding-agents/claude-code',
										'integrations/ai-coding-agents/claude-desktop',
										'integrations/ai-coding-agents/chatgpt',
										'integrations/ai-coding-agents/copilot',
										'integrations/ai-coding-agents/cursor',
										'integrations/ai-coding-agents/gemini',
										'integrations/ai-coding-agents/grok',
									],
								},
								'integrations/ai-coding-agents/honest-answers',
								'integrations/ai-coding-agents/troubleshooting',
							],
						},
						{ label: 'AI and LLM Architecture', collapsed: true, items: [{ autogenerate: { directory: 'integrations/ai-architecture' } }] },
						'integrations/microsoft-365-copilot',
						{ label: 'PySpark', collapsed: true, items: [{ autogenerate: { directory: 'integrations/pyspark' } }] },
					],
				},
				{
					label: 'Administration',
					collapsed: true,
					items: [
						'administration',
						{
							label: 'Access Management',
							collapsed: true,
							items: [
								'administration/access',
								{ label: 'Organizations & Workspaces', collapsed: true, items: [{ autogenerate: { directory: 'administration/access/overview' } }] },
								'administration/access/member-management',
								'administration/access/member-user-identity',
								'administration/access/member-authentication',
								'administration/access/managing-security-groups-and-assignments',
								{
									label: 'Single Sign-On',
									collapsed: true,
									items: [
										'administration/access/advanced/managing-single-sign-on-for-organization',
										'administration/access/advanced/entra-saml-setup',
										'administration/access/advanced/okta-saml-setup',
										'administration/access/advanced/google-saml-setup',
										'administration/access/advanced/aws-saml-setup',
										'administration/access/advanced/auth0-saml-setup',
									],
								},
								{
									label: 'Advanced',
									collapsed: true,
									items: [
										'administration/access/advanced',
										'administration/access/advanced/manage-organization-administrators',
										'administration/access/advanced/setting-member-expiration-period',
									],
								},
								'administration/access/usage-reports',
							],
						},
						{ label: 'Control Plane', collapsed: true, items: [{ autogenerate: { directory: 'administration/control-plane' } }] },
						'guides/projects/managing-storage',
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
						'reference',
						'reference/connectors',
						'reference/workflow-steps',
						'reference/expressions',
						'reference/cli',
						'reference/glossary',
					],
				},
				'releases',
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
- **MCP server**: every workspace exposes \`/mcp\` for AI coding agents (Claude Code, Cursor, ChatGPT, etc.).

Documentation structure:

- \`get-started/\` — concepts, quickstart, end-to-end tutorials, FAQ
- \`guides/\` — task-oriented how-to content
- \`reference/\` — workflow steps, expressions (SQL functions), connectors, CLI, glossary
- \`integrations/\` — AI and LLM architecture, Microsoft 365 Copilot, AI coding agents, PySpark
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
