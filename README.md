# PlaidCloud documentation

The source for [docs.plaidcloud.com](https://docs.plaidcloud.com).

Built with [Astro](https://astro.build/) and [Starlight](https://starlight.astro.build/), deployed to Cloudflare via Workers Static Assets.

## Local development

Requires Node 22+.

```bash
npm install
npm run dev          # local dev server at http://localhost:4321
npm run build        # produce a production build in dist/
npm run preview      # serve the production build locally
```

## Repository layout

```
src/
├── assets/          PlaidCloud logo (light + dark)
├── content/
│   └── docs/        all documentation pages (markdown + MDX)
├── snippets/        reusable MDX fragments imported by docs pages
└── styles/          brand-color overrides on Starlight CSS variables
public/
├── _headers         security headers (CSP, frame-options, etc.)
├── _redirects       301 redirects from legacy Hugo URLs
├── images/          shared image assets
├── favicon.ico
└── robots.txt
astro.config.mjs     Starlight + sitemap config, sidebar definition
wrangler.jsonc       Cloudflare Workers Static Assets config
```

## Contributing

Documentation lives in `src/content/docs/`. Each `.md` or `.mdx` file is a page; folder paths become URL paths.

A typical page has front matter:

```yaml
---
title: Page Title
description: One-line summary (used in search + OG tags).
sidebar:
  label: Short Label    # optional, shown in nav
  order: 1              # optional, controls sort
---
```

For substantive contributions, see [CONTRIBUTING.md](./CONTRIBUTING.md).

## Deployment

The `astro-migration` branch is auto-built and deployed by Cloudflare Workers Builds. Pushes to this branch trigger the build pipeline (`npm ci && npm run build` → `npx wrangler deploy`).

Production cutover from the legacy Hugo site on GCS is pending DNS reconfiguration.
