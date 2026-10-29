---
title: Tableaux de bord
description: Créez et personnalisez des tableaux de bord PlaidCloud pour visualiser vos données avec des graphiques interactifs et des affichages de métriques dynamiques.
sidebar:
  label: Tableaux de bord
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dashboards/index.md
---

Créez des tableaux de bord interactifs sur les données de projet PlaidCloud : graphiques, métriques, colonnes calculées, filtres dynamiques et exploration intégrée des données.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 200" role="img" aria-label="Les tables et vues de projet publiées alimentent les éléments de construction du tableau de bord (graphiques, vignettes de métriques et filtres dynamiques), qui s'assemblent en un tableau de bord interactif que les membres de l'espace de travail peuvent explorer." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="db-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="16" y="74" width="140" height="56" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="86" y="98" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">données publiées</text>
  <text x="86" y="116" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">tables &amp; vues</text>
  <path d="M156 102 C196 102 206 66 244 66" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#db-arrow)" />
  <path d="M156 102 L244 102" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#db-arrow)" />
  <path d="M156 102 C196 102 206 138 244 138" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#db-arrow)" />
  <rect x="246" y="48" width="130" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="311" y="69" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">graphiques</text>
  <rect x="246" y="86" width="130" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="311" y="107" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">vignettes de métriques</text>
  <rect x="246" y="124" width="130" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="311" y="145" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">filtres dynamiques</text>
  <path d="M376 103 L436 103" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#db-arrow)" />
  <rect x="438" y="60" width="150" height="86" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="513" y="98" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Tableau de bord</text>
  <text x="513" y="116" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">interactif</text>
  <path d="M588 103 L636 103" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#db-arrow)" />
  <text x="654" y="99" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">membres</text>
  <text x="654" y="114" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">explorent</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Les tables et vues publiées alimentent des graphiques, des vignettes de métriques et des filtres dynamiques qui s'assemblent en un tableau de bord interactif que les membres peuvent explorer.</figcaption>
</figure>
