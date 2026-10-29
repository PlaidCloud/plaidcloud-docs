// Starlight locales (`root` = English, unprefixed URLs). Shared by
// astro.config.mjs (Starlight + sitemap i18n) and og-image.ts (which maps a
// translated page id back to its English source).
export const locales = {
	root: { label: 'English', lang: 'en' },
	de: { label: 'Deutsch', lang: 'de' },
	es: { label: 'Español', lang: 'es' },
	fr: { label: 'Français', lang: 'fr' },
	'pt-br': { label: 'Português (Brasil)', lang: 'pt-BR' },
	'pt-pt': { label: 'Português (Portugal)', lang: 'pt-PT' },
	pl: { label: 'Polski', lang: 'pl' },
	ja: { label: '日本語', lang: 'ja' },
	ko: { label: '한국어', lang: 'ko' },
	'zh-cn': { label: '简体中文', lang: 'zh-CN' },
};
