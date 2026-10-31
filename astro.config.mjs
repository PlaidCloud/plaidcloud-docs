// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import sitemap from '@astrojs/sitemap';
import starlightLlmsTxt from 'starlight-llms-txt';
import { fileURLToPath } from 'node:url';
import { execSync } from 'node:child_process';
import { readdirSync, statSync } from 'node:fs';
import { join, relative } from 'node:path';
import { locales } from './src/lib/locales.mjs';

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

// Matches a translated locale's URL prefix (`/de` in `/de/x/`); English is unprefixed.
const LOCALE_PREFIX = new RegExp(`^/(${Object.keys(locales).filter((l) => l !== 'root').join('|')})(?=/)`);

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
			// Workers Assets caps a file at 25 MiB; one 17.6k-URL sitemap with hreflang alternates is ~28 MB.
			entryLimit: 5000,
			// hreflang alternates between a page and its translations.
			i18n: {
				defaultLocale: 'en',
				locales: Object.fromEntries(
					Object.entries(locales).map(([key, { lang }]) => [key === 'root' ? 'en' : key, lang])
				),
			},
			// Starlight builds every locale URL, rendering English content where no
			// translation exists. Keep those fallbacks out: a locale URL is listed
			// only when its translated source file exists (urlToLastmod is keyed by
			// every docs file on disk, translations included).
			filter: (url) => !LOCALE_PREFIX.test(new URL(url).pathname) || urlToLastmod.has(url),
			serialize(item) {
				// Per-page lastmod from git history (falls back to file mtime).
				const iso = urlToLastmod.get(item.url);
				if (iso) item.lastmod = iso;
				// Priority by pathname. Every Astro URL ends in `/`, so check
				// the pathname explicitly rather than the trailing slash.
				// Locale URLs take their English page's priority.
				const pathname = new URL(item.url).pathname.replace(LOCALE_PREFIX, '');
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
			defaultLocale: 'root',
			locales,
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
					translations: { de: 'Erste Schritte', es: 'Primeros pasos', fr: 'Prise en main', 'pt-BR': 'Primeiros passos', 'pt-PT': 'Primeiros passos', pl: 'Pierwsze kroki', ja: 'はじめに', ko: '시작하기', 'zh-CN': '快速入门' },
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
							translations: { de: 'Tutorials', es: 'Tutoriales', fr: 'Tutoriels', 'pt-BR': 'Tutoriais', 'pt-PT': 'Tutoriais', pl: 'Samouczki', ja: 'チュートリアル', ko: '튜토리얼', 'zh-CN': '教程' },
							collapsed: true,
							items: [
								'get-started/tutorials',
								{
									label: 'Start Here',
									translations: { de: 'Hier beginnen', es: 'Empiece aquí', fr: 'Commencez ici', 'pt-BR': 'Comece aqui', 'pt-PT': 'Comece aqui', pl: 'Zacznij tutaj', ja: 'ここから始める', ko: '여기서 시작', 'zh-CN': '从这里开始' },
									collapsed: true,
									items: [
										'get-started/tutorials/first-15-minutes',
										'get-started/tutorials/csv-to-answer',
										'get-started/tutorials/start-from-a-project',
									],
								},
								{
									label: 'Build Your First Pipeline',
									translations: { de: 'Ihre erste Pipeline erstellen', es: 'Cree su primera canalización', fr: 'Créez votre premier pipeline', 'pt-BR': 'Crie seu primeiro pipeline', 'pt-PT': 'Crie o seu primeiro pipeline', pl: 'Tworzenie pierwszego potoku', ja: '最初のパイプラインを作成', ko: '첫 파이프라인 만들기', 'zh-CN': '构建您的第一个管道' },
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
									translations: { de: 'Sicher arbeiten', es: 'Trabaje con confianza', fr: 'Travaillez en toute confiance', 'pt-BR': 'Trabalhe com confiança', 'pt-PT': 'Trabalhe com confiança', pl: 'Praca bez obaw', ja: '安心して作業する', ko: '안심하고 작업하기', 'zh-CN': '放心工作' },
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
									translations: { de: 'Betrieb und Governance', es: 'Operación y gobernanza', fr: 'Exploitation et gouvernance', 'pt-BR': 'Operação e governança', 'pt-PT': 'Operação e governação', pl: 'Eksploatacja i nadzór', ja: '運用とガバナンス', ko: '운영 및 거버넌스', 'zh-CN': '运营与治理' },
									collapsed: true,
									items: [
										'get-started/tutorials/schedule-a-workflow',
										'get-started/tutorials/control-data-access',
									],
								},
								{
									label: 'Coming From Another Tool',
									translations: { de: 'Umstieg von einem anderen Tool', es: 'Si viene de otra herramienta', fr: 'Vous venez d’un autre outil', 'pt-BR': 'Vindo de outra ferramenta', 'pt-PT': 'Vindo de outra ferramenta', pl: 'Przejście z innego narzędzia', ja: '他のツールをお使いの方', ko: '다른 도구 사용자', 'zh-CN': '来自其他工具' },
									collapsed: true,
									items: [
										'get-started/tutorials/migrate-your-first-alteryx-workflow',
										'get-started/tutorials/excel-with-plaidxl',
									],
								},
								{
									label: 'Extend With AI',
									translations: { de: 'Mit KI erweitern', es: 'Amplíe con IA', fr: 'Étendez avec l’IA', 'pt-BR': 'Expanda com IA', 'pt-PT': 'Expanda com IA', pl: 'Rozszerzanie za pomocą AI', ja: 'AIで拡張', ko: 'AI로 확장', 'zh-CN': '使用 AI 扩展' },
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
					translations: { de: 'Grundlagen', es: 'Conceptos básicos', fr: 'Notions de base', 'pt-BR': 'Noções básicas', 'pt-PT': 'Noções básicas', pl: 'Podstawy', ja: '基本', ko: '기본 사항', 'zh-CN': '基础知识' },
					collapsed: true,
					items: [
						'guides',
						'guides/launcher',
						'guides/change-your-language',
						'guides/projects/sharing-links',
						'guides/projects/breadcrumbs-and-shareable-links',
						{
							label: 'Mobile App',
							translations: { de: 'Mobile App', es: 'Aplicación móvil', fr: 'Application mobile', 'pt-BR': 'Aplicativo móvel', 'pt-PT': 'Aplicação móvel', pl: 'Aplikacja mobilna', ja: 'モバイルアプリ', ko: '모바일 앱', 'zh-CN': '移动应用' },
							collapsed: true,
							items: [{ autogenerate: { directory: 'guides/mobile-app' } }],
						},
						{
							label: 'Email',
							translations: { de: 'E-Mail', es: 'Correo electrónico', fr: 'E-mail', 'pt-BR': 'E-mail', 'pt-PT': 'Correio eletrónico', pl: 'E-mail', ja: 'メール', ko: '이메일', 'zh-CN': '电子邮件' },
							collapsed: true,
							items: [{ autogenerate: { directory: 'guides/email' } }],
						},
						'guides/time-expense/track-time-and-expenses',
						{
							label: 'Help & Support',
							translations: { de: 'Hilfe & Support', es: 'Ayuda y soporte', fr: 'Aide et support', 'pt-BR': 'Ajuda e suporte', 'pt-PT': 'Ajuda e suporte', pl: 'Pomoc i wsparcie', ja: 'ヘルプとサポート', ko: '도움말 및 지원', 'zh-CN': '帮助与支持' },
							collapsed: true,
							items: [{ autogenerate: { directory: 'guides/support' } }],
						},
					],
				},
				{
					label: 'Connect Data',
					translations: { de: 'Daten verbinden', es: 'Conectar datos', fr: 'Connecter des données', 'pt-BR': 'Conectar dados', 'pt-PT': 'Ligar dados', pl: 'Łączenie danych', ja: 'データの接続', ko: '데이터 연결', 'zh-CN': '连接数据' },
					collapsed: true,
					items: [
						{
							label: 'Connections',
							translations: { de: 'Verbindungen', es: 'Conexiones', fr: 'Connexions', 'pt-BR': 'Conexões', 'pt-PT': 'Ligações', pl: 'Połączenia', ja: '接続', ko: '연결', 'zh-CN': '连接' },
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
									translations: { de: 'ERP & Buchhaltung', es: 'ERP y contabilidad', fr: 'ERP et comptabilité', 'pt-BR': 'ERP e contabilidade', 'pt-PT': 'ERP e contabilidade', pl: 'ERP i księgowość', ja: 'ERPと会計', ko: 'ERP 및 회계', 'zh-CN': 'ERP 与会计' },
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
									translations: { de: 'EPM & Planung', es: 'EPM y planificación', fr: 'EPM et planification', 'pt-BR': 'EPM e planejamento', 'pt-PT': 'EPM e planeamento', pl: 'EPM i planowanie', ja: 'EPMと計画', ko: 'EPM 및 계획', 'zh-CN': 'EPM 与计划' },
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
									translations: { de: 'CRM & Betrieb', es: 'CRM y operaciones', fr: 'CRM et opérations', 'pt-BR': 'CRM e operações', 'pt-PT': 'CRM e operações', pl: 'CRM i operacje', ja: 'CRMと業務', ko: 'CRM 및 운영', 'zh-CN': 'CRM 与运营' },
									collapsed: true,
									items: [
										'guides/connections/salesforce',
										'guides/connections/samsara',
									],
								},
								{
									label: 'Write-Back',
									translations: { de: 'Zurückschreiben', es: 'Escritura de retorno', fr: 'Réécriture', 'pt-BR': 'Gravação de retorno', 'pt-PT': 'Escrita de retorno', pl: 'Zapis zwrotny', ja: '書き戻し', ko: '다시 쓰기', 'zh-CN': '回写' },
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
							translations: { de: 'Dateien & Speicher', es: 'Archivos y almacenamiento', fr: 'Fichiers et stockage', 'pt-BR': 'Arquivos e armazenamento', 'pt-PT': 'Ficheiros e armazenamento', pl: 'Pliki i magazyn', ja: 'ファイルとストレージ', ko: '파일 및 스토리지', 'zh-CN': '文件与存储' },
							collapsed: true,
							items: [
								'guides/documents',
								'guides/documents/using-document',
								'guides/documents/searching-documents',
								{
									label: 'Manage Accounts & Access',
									translations: { de: 'Konten & Zugriff verwalten', es: 'Gestionar cuentas y acceso', fr: 'Gérer les comptes et l’accès', 'pt-BR': 'Gerenciar contas e acesso', 'pt-PT': 'Gerir contas e acesso', pl: 'Zarządzanie kontami i dostępem', ja: 'アカウントとアクセスの管理', ko: '계정 및 액세스 관리', 'zh-CN': '管理账户与访问权限' },
									collapsed: true,
									items: [{ autogenerate: { directory: 'guides/documents/account-management' } }],
								},
								{
									label: 'Add Cloud Object Storage',
									translations: { de: 'Cloud-Objektspeicher hinzufügen', es: 'Agregar almacenamiento de objetos en la nube', fr: 'Ajouter un stockage d’objets cloud', 'pt-BR': 'Adicionar armazenamento de objetos na nuvem', 'pt-PT': 'Adicionar armazenamento de objetos na nuvem', pl: 'Dodawanie magazynu obiektów w chmurze', ja: 'クラウドオブジェクトストレージの追加', ko: '클라우드 개체 스토리지 추가', 'zh-CN': '添加云对象存储' },
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
									translations: { de: 'Dateifreigaben & Server hinzufügen', es: 'Agregar recursos compartidos y servidores', fr: 'Ajouter des partages de fichiers et des serveurs', 'pt-BR': 'Adicionar compartilhamentos de arquivos e servidores', 'pt-PT': 'Adicionar partilhas de ficheiros e servidores', pl: 'Dodawanie udziałów plików i serwerów', ja: 'ファイル共有とサーバーの追加', ko: '파일 공유 및 서버 추가', 'zh-CN': '添加文件共享与服务器' },
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
					translations: { de: 'Daten organisieren', es: 'Organizar datos', fr: 'Organiser les données', 'pt-BR': 'Organizar dados', 'pt-PT': 'Organizar dados', pl: 'Organizowanie danych', ja: 'データの整理', ko: '데이터 구성', 'zh-CN': '组织数据' },
					collapsed: true,
					items: [
						{
							label: 'Projects',
							translations: { de: 'Projekte', es: 'Proyectos', fr: 'Projets', 'pt-BR': 'Projetos', 'pt-PT': 'Projetos', pl: 'Projekty', ja: 'プロジェクト', ko: '프로젝트', 'zh-CN': '项目' },
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
								'guides/projects/data-foundation',
							],
						},
						{
							label: 'Tables & Views',
							translations: { de: 'Tabellen & Ansichten', es: 'Tablas y vistas', fr: 'Tables et vues', 'pt-BR': 'Tabelas e visões', 'pt-PT': 'Tabelas e vistas', pl: 'Tabele i widoki', ja: 'テーブルとビュー', ko: '테이블 및 뷰', 'zh-CN': '表与视图' },
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
							translations: { de: 'Dimensionen', es: 'Dimensiones', fr: 'Dimensions', 'pt-BR': 'Dimensões', 'pt-PT': 'Dimensões', pl: 'Wymiary', ja: 'ディメンション', ko: '차원', 'zh-CN': '维度' },
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
					translations: { de: 'Transformieren & automatisieren', es: 'Transformar y automatizar', fr: 'Transformer et automatiser', 'pt-BR': 'Transformar e automatizar', 'pt-PT': 'Transformar e automatizar', pl: 'Transformacja i automatyzacja', ja: '変換と自動化', ko: '변환 및 자동화', 'zh-CN': '转换与自动化' },
					collapsed: true,
					items: [
						'guides/workflows',
						{
							label: 'Create & Edit',
							translations: { de: 'Erstellen & bearbeiten', es: 'Crear y editar', fr: 'Créer et modifier', 'pt-BR': 'Criar e editar', 'pt-PT': 'Criar e editar', pl: 'Tworzenie i edycja', ja: '作成と編集', ko: '만들기 및 편집', 'zh-CN': '创建与编辑' },
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
							translations: { de: 'Logik aufbauen', es: 'Construir la lógica', fr: 'Construire la logique', 'pt-BR': 'Construir a lógica', 'pt-PT': 'Construir a lógica', pl: 'Budowanie logiki', ja: 'ロジックの構築', ko: '로직 구성', 'zh-CN': '构建逻辑' },
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
							translations: { de: 'Ausführen & steuern', es: 'Ejecutar y controlar', fr: 'Exécuter et contrôler', 'pt-BR': 'Executar e controlar', 'pt-PT': 'Executar e controlar', pl: 'Uruchamianie i sterowanie', ja: '実行と制御', ko: '실행 및 제어', 'zh-CN': '运行与控制' },
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
							translations: { de: 'Überwachen & optimieren', es: 'Supervisar y optimizar', fr: 'Surveiller et optimiser', 'pt-BR': 'Monitorar e otimizar', 'pt-PT': 'Monitorizar e otimizar', pl: 'Monitorowanie i dostrajanie', ja: '監視とチューニング', ko: '모니터링 및 튜닝', 'zh-CN': '监控与调优' },
							collapsed: true,
							items: [
								'guides/workflows/viewing-workflow-log',
								'guides/workflows/view-workflow-report',
								'guides/workflows/view-a-dependency-audit',
								'guides/workflows/optimize-a-workflow',
								'guides/workflows/sync-dependencies',
							],
						},
						{
							label: 'Scheduling',
							translations: { de: 'Zeitplanung', es: 'Programación', fr: 'Planification', 'pt-BR': 'Agendamento', 'pt-PT': 'Agendamento', pl: 'Harmonogramy', ja: 'スケジュール設定', ko: '예약', 'zh-CN': '计划' },
							collapsed: true,
							items: [{ autogenerate: { directory: 'administration/scheduled-events' } }],
						},
					],
				},
				{
					label: 'Migrate From Other Tools',
					translations: { de: 'Von anderen Tools migrieren', es: 'Migrar desde otras herramientas', fr: 'Migrer depuis d’autres outils', 'pt-BR': 'Migrar de outras ferramentas', 'pt-PT': 'Migrar de outras ferramentas', pl: 'Migracja z innych narzędzi', ja: '他のツールからの移行', ko: '다른 도구에서 마이그레이션', 'zh-CN': '从其他工具迁移' },
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
					translations: { de: 'Umlagen', es: 'Asignaciones', fr: 'Allocations', 'pt-BR': 'Alocações', 'pt-PT': 'Alocações', pl: 'Alokacje', ja: '配賦', ko: '배부', 'zh-CN': '分摊' },
					collapsed: true,
					items: [
						'guides/allocations',
						{
							label: 'First Allocation',
							translations: { de: 'Erste Umlage', es: 'Primera asignación', fr: 'Première allocation', 'pt-BR': 'Primeira alocação', 'pt-PT': 'Primeira alocação', pl: 'Pierwsza alokacja', ja: '最初の配賦', ko: '첫 배부', 'zh-CN': '首次分摊' },
							collapsed: true,
							items: [{ autogenerate: { directory: 'guides/allocations/getting-started' } }],
						},
						{
							label: 'Setup',
							translations: { de: 'Einrichtung', es: 'Configuración', fr: 'Configuration', 'pt-BR': 'Configuração', 'pt-PT': 'Configuração', pl: 'Konfiguracja', ja: 'セットアップ', ko: '설정', 'zh-CN': '设置' },
							collapsed: true,
							items: [{ autogenerate: { directory: 'guides/allocations/setup' } }],
						},
						{
							label: 'Results & Troubleshooting',
							translations: { de: 'Ergebnisse & Fehlerbehebung', es: 'Resultados y solución de problemas', fr: 'Résultats et dépannage', 'pt-BR': 'Resultados e solução de problemas', 'pt-PT': 'Resultados e resolução de problemas', pl: 'Wyniki i rozwiązywanie problemów', ja: '結果とトラブルシューティング', ko: '결과 및 문제 해결', 'zh-CN': '结果与故障排除' },
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
					translations: { de: 'Analyse & Berichte', es: 'Análisis e informes', fr: 'Analyse et rapports', 'pt-BR': 'Análise e relatórios', 'pt-PT': 'Análise e relatórios', pl: 'Analiza i raporty', ja: '分析とレポート', ko: '분석 및 보고', 'zh-CN': '分析与报表' },
					collapsed: true,
					items: [
						{
							label: 'Dashboards',
							translations: { de: 'Dashboards', es: 'Paneles de control', fr: 'Tableaux de bord', 'pt-BR': 'Painéis', 'pt-PT': 'Painéis de controlo', pl: 'Pulpity', ja: 'ダッシュボード', ko: '대시보드', 'zh-CN': '仪表板' },
							collapsed: true,
							items: [{ autogenerate: { directory: 'guides/dashboards' } }],
						},
						'integrations/ai-coding-agents/build-dashboards',
						'integrations/ai-coding-agents/metric-definitions',
						'integrations/ai-coding-agents/analysis-paths',
					],
				},
				{
					label: 'AI Assistant (Weave)',
					translations: { de: 'KI-Assistent (Weave)', es: 'Asistente de IA (Weave)', fr: 'Assistant IA (Weave)', 'pt-BR': 'Assistente de IA (Weave)', 'pt-PT': 'Assistente de IA (Weave)', pl: 'Asystent AI (Weave)', ja: 'AIアシスタント (Weave)', ko: 'AI 어시스턴트 (Weave)', 'zh-CN': 'AI 助手 (Weave)' },
					collapsed: true,
					items: [
						'guides/ai-assistant',
						'guides/ai-assistant/weave-tab',
						{
							label: 'Review Findings',
							translations: { de: 'Befunde prüfen', es: 'Revisar hallazgos', fr: 'Examiner les constatations', 'pt-BR': 'Revisar constatações', 'pt-PT': 'Rever descobertas', pl: 'Przegląd ustaleń', ja: '検出事項の確認', ko: '결과 항목 검토', 'zh-CN': '审核发现项' },
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
							translations: { de: 'Mit Weave erstellen', es: 'Crear con Weave', fr: 'Créer avec Weave', 'pt-BR': 'Criar com Weave', 'pt-PT': 'Criar com Weave', pl: 'Tworzenie z Weave', ja: 'Weaveで作成', ko: 'Weave로 만들기', 'zh-CN': '使用 Weave 构建' },
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
							translations: { de: 'Governance für Weave', es: 'Gobernanza de Weave', fr: 'Gouvernance de Weave', 'pt-BR': 'Governança do Weave', 'pt-PT': 'Governação do Weave', pl: 'Nadzór nad Weave', ja: 'Weaveのガバナンス', ko: 'Weave 거버넌스', 'zh-CN': 'Weave 治理' },
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
					translations: { de: 'Apps erstellen', es: 'Crear aplicaciones', fr: 'Créer des applications', 'pt-BR': 'Criar aplicativos', 'pt-PT': 'Criar aplicações', pl: 'Tworzenie aplikacji', ja: 'アプリの作成', ko: '앱 만들기', 'zh-CN': '构建应用' },
					collapsed: true,
					items: [
						{
							label: 'Panel Apps',
							translations: { de: 'Panel-Apps', es: 'Aplicaciones de Panel', fr: 'Applications Panel', 'pt-BR': 'Aplicativos Panel', 'pt-PT': 'Aplicações Panel', pl: 'Aplikacje Panel', ja: 'Panelアプリ', ko: 'Panel 앱', 'zh-CN': 'Panel 应用' },
							collapsed: true,
							items: [
								'guides/panel-apps',
								{
									label: 'Use',
									translations: { de: 'Verwenden', es: 'Usar', fr: 'Utiliser', 'pt-BR': 'Usar', 'pt-PT': 'Utilizar', pl: 'Użytkowanie', ja: '使用', ko: '사용', 'zh-CN': '使用' },
									collapsed: true,
									items: [
										'guides/panel-apps/using',
										'guides/panel-apps/gallery',
									],
								},
								{
									label: 'Build',
									translations: { de: 'Erstellen', es: 'Crear', fr: 'Créer', 'pt-BR': 'Criar', 'pt-PT': 'Criar', pl: 'Tworzenie', ja: '作成', ko: '만들기', 'zh-CN': '构建' },
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
									translations: { de: 'Daten & Bereitstellung', es: 'Datos e implementación', fr: 'Données et déploiement', 'pt-BR': 'Dados e implantação', 'pt-PT': 'Dados e implementação', pl: 'Dane i wdrażanie', ja: 'データとデプロイ', ko: '데이터 및 배포', 'zh-CN': '数据与部署' },
									collapsed: true,
									items: [
										'guides/panel-apps/accessing-data',
										'guides/panel-apps/data-api',
										'guides/panel-apps/deploy-from-git',
									],
								},
							],
						},
						{
							label: 'Dash Apps',
							translations: { de: 'Dash-Apps', es: 'Aplicaciones Dash', fr: 'Applications Dash', 'pt-BR': 'Aplicativos Dash', 'pt-PT': 'Aplicações Dash', pl: 'Aplikacje Dash', ja: 'Dashアプリ', ko: 'Dash 앱', 'zh-CN': 'Dash 应用' },
							collapsed: true,
							items: [{ autogenerate: { directory: 'guides/dash-apps' } }],
						},
						{
							label: 'Custom App Sandbox',
							translations: { de: 'Sandbox für eigene Apps', es: 'Entorno de pruebas para aplicaciones personalizadas', fr: 'Bac à sable d’applications personnalisées', 'pt-BR': 'Sandbox de aplicativos personalizados', 'pt-PT': 'Sandbox de aplicações personalizadas', pl: 'Piaskownica aplikacji niestandardowych', ja: 'カスタムアプリのサンドボックス', ko: '사용자 지정 앱 샌드박스', 'zh-CN': '自定义应用沙盒' },
							collapsed: true,
							items: [{ autogenerate: { directory: 'guides/sandbox' } }],
						},
						{ label: 'PlaidCloud Git', collapsed: true, items: [{ autogenerate: { directory: 'guides/git' } }] },
						{
							label: 'Location APIs',
							translations: { de: 'Standort-APIs', es: 'API de ubicación', fr: 'API de localisation', 'pt-BR': 'APIs de localização', 'pt-PT': 'APIs de localização', pl: 'Interfejsy API lokalizacji', ja: '位置情報API', ko: '위치 API', 'zh-CN': '位置 API' },
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
					translations: { de: 'Integrationen', es: 'Integraciones', fr: 'Intégrations', 'pt-BR': 'Integrações', 'pt-PT': 'Integrações', pl: 'Integracje', ja: '連携', ko: '통합', 'zh-CN': '集成' },
					collapsed: true,
					items: [
						'integrations',
						{
							label: 'AI Agents (MCP)',
							translations: { de: 'KI-Agenten (MCP)', es: 'Agentes de IA (MCP)', fr: 'Agents IA (MCP)', 'pt-BR': 'Agentes de IA (MCP)', 'pt-PT': 'Agentes de IA (MCP)', pl: 'Agenci AI (MCP)', ja: 'AIエージェント (MCP)', ko: 'AI 에이전트 (MCP)', 'zh-CN': 'AI 代理 (MCP)' },
							collapsed: true,
							items: [
								'integrations/ai-coding-agents',
								'integrations/ai-coding-agents/getting-started',
								{
									label: 'Clients',
									translations: { de: 'Clients', es: 'Clientes', fr: 'Clients', 'pt-BR': 'Clientes', 'pt-PT': 'Clientes', pl: 'Klienci', ja: 'クライアント', ko: '클라이언트', 'zh-CN': '客户端' },
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
						{
							label: 'AI and LLM Architecture',
							translations: { de: 'KI- und LLM-Architektur', es: 'Arquitectura de IA y LLM', fr: 'Architecture IA et LLM', 'pt-BR': 'Arquitetura de IA e LLM', 'pt-PT': 'Arquitetura de IA e LLM', pl: 'Architektura AI i LLM', ja: 'AIとLLMのアーキテクチャ', ko: 'AI 및 LLM 아키텍처', 'zh-CN': 'AI 与 LLM 架构' },
							collapsed: true,
							items: [{ autogenerate: { directory: 'integrations/ai-architecture' } }],
						},
						'integrations/microsoft-365-copilot',
						{ label: 'PySpark', collapsed: true, items: [{ autogenerate: { directory: 'integrations/pyspark' } }] },
					],
				},
				{
					label: 'Administration',
					translations: { de: 'Administration', es: 'Administración', fr: 'Administration', 'pt-BR': 'Administração', 'pt-PT': 'Administração', pl: 'Administracja', ja: '管理', ko: '관리', 'zh-CN': '管理' },
					collapsed: true,
					items: [
						'administration',
						{
							label: 'Access Management',
							translations: { de: 'Zugriffsverwaltung', es: 'Gestión de acceso', fr: 'Gestion des accès', 'pt-BR': 'Gerenciamento de acesso', 'pt-PT': 'Gestão de acessos', pl: 'Zarządzanie dostępem', ja: 'アクセス管理', ko: '액세스 관리', 'zh-CN': '访问管理' },
							collapsed: true,
							items: [
								'administration/access',
								{
									label: 'Organizations & Workspaces',
									translations: { de: 'Organisationen & Workspaces', es: 'Organizaciones y espacios de trabajo', fr: 'Organisations et espaces de travail', 'pt-BR': 'Organizações e espaços de trabalho', 'pt-PT': 'Organizações e áreas de trabalho', pl: 'Organizacje i obszary robocze', ja: '組織とワークスペース', ko: '조직 및 워크스페이스', 'zh-CN': '组织与工作区' },
									collapsed: true,
									items: [{ autogenerate: { directory: 'administration/access/overview' } }],
								},
								'administration/access/member-management',
								'administration/access/member-user-identity',
								'administration/access/member-authentication',
								'administration/access/managing-security-groups-and-assignments',
								{
									label: 'Single Sign-On',
									translations: { de: 'Single Sign-On', es: 'Inicio de sesión único', fr: 'Authentification unique', 'pt-BR': 'Logon único', 'pt-PT': 'Início de sessão único', pl: 'Logowanie jednokrotne', ja: 'シングルサインオン', ko: '싱글 사인온', 'zh-CN': '单点登录' },
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
									translations: { de: 'Erweitert', es: 'Avanzado', fr: 'Avancé', 'pt-BR': 'Avançado', 'pt-PT': 'Avançado', pl: 'Zaawansowane', ja: '詳細', ko: '고급', 'zh-CN': '高级' },
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
						{
							label: 'Control Plane',
							translations: { de: 'Control Plane', es: 'Plano de control', fr: 'Plan de contrôle', 'pt-BR': 'Plano de controle', 'pt-PT': 'Plano de controlo', pl: 'Płaszczyzna sterowania', ja: 'コントロールプレーン', ko: '컨트롤 플레인', 'zh-CN': '控制平面' },
							collapsed: true,
							items: [{ autogenerate: { directory: 'administration/control-plane' } }],
						},
						'guides/projects/managing-storage',
					],
				},
				// Reference is top-level only — full tree (1,200+ entries from
				// expressions/workflow-steps) would inline into every page and
				// blow past Workers Assets size limits. Users navigate references
				// via landing pages + search (Pagefind).
				{
					label: 'Reference',
					translations: { de: 'Referenz', es: 'Referencia', fr: 'Référence', 'pt-BR': 'Referência', 'pt-PT': 'Referência', pl: 'Dokumentacja referencyjna', ja: 'リファレンス', ko: '참조', 'zh-CN': '参考' },
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
