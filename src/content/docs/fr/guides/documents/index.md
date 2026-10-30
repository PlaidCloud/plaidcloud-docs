---
title: Gestion des fichiers
description: Gérez les comptes de stockage de fichiers dans PlaidCloud pour importer et exporter des données aux formats CSV, Excel, Parquet et autres.
sidebar:
  label: Vue d'ensemble
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/index.md
---

PlaidCloud Documents : stockez, organisez, recherchez et partagez des fichiers aux côtés de vos données et de vos workflows. Les documents peuvent provenir de n'importe quel compte de stockage connecté et être référencés dans les workflows.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 200" role="img" aria-label="Des comptes de stockage connectés, tels que S3, Google Cloud Storage et OneDrive, alimentent PlaidCloud Documents, où les fichiers sont stockés, organisés, recherchés et partagés. Les étapes de workflow référencent ensuite ces fichiers pour importer et exporter des données." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="dc-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="76" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-gray-3)">comptes de stockage</text>
  <rect x="16" y="40" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="60" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">S3</text>
  <rect x="16" y="82" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="102" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Cloud Storage</text>
  <rect x="16" y="124" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="144" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">OneDrive</text>
  <path d="M136 55 C186 55 206 92 246 96" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <path d="M136 97 L246 100" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <path d="M136 139 C186 139 206 108 246 104" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <rect x="248" y="70" width="180" height="64" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="338" y="96" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Documents</text>
  <text x="338" y="115" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">stocker · organiser · rechercher · partager</text>
  <path d="M428 102 L510 102" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#dc-arrow)" />
  <rect x="512" y="76" width="152" height="52" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="588" y="100" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">étapes de workflow</text>
  <text x="588" y="118" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">importer · exporter des fichiers</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Les fichiers arrivent dans Documents depuis n'importe quel compte de stockage connecté, où vous les stockez, les organisez, les recherchez et les partagez, puis vous les référencez depuis des étapes de workflow pour importer et exporter des données.</figcaption>
</figure>
