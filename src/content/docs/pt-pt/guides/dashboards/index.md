---
title: Painéis de controlo
description: Crie e personalize painéis de controlo do PlaidCloud para visualizar dados com gráficos interativos, diagramas e apresentações dinâmicas de indicadores.
sidebar:
  label: Painéis de controlo
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dashboards/index.md
---

Crie painéis de controlo interativos sobre os dados de projetos do PlaidCloud — gráficos, indicadores, colunas calculadas, filtros dinâmicos e exploração de dados incorporada.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 200" role="img" aria-label="As tabelas e vistas publicadas de um projeto alimentam os blocos de construção do painel de controlo — gráficos, mosaicos de indicadores e filtros dinâmicos — que se juntam num painel de controlo interativo para os membros da área de trabalho explorarem." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="db-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="16" y="74" width="140" height="56" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="86" y="98" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">dados publicados</text>
  <text x="86" y="116" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">tabelas &amp; vistas</text>
  <path d="M156 102 C196 102 206 66 244 66" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#db-arrow)" />
  <path d="M156 102 L244 102" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#db-arrow)" />
  <path d="M156 102 C196 102 206 138 244 138" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#db-arrow)" />
  <rect x="246" y="48" width="130" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="311" y="69" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">gráficos</text>
  <rect x="246" y="86" width="130" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="311" y="107" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">mosaicos de indicadores</text>
  <rect x="246" y="124" width="130" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="311" y="145" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">filtros dinâmicos</text>
  <path d="M376 103 L436 103" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#db-arrow)" />
  <rect x="438" y="60" width="150" height="86" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="513" y="98" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Painel de controlo</text>
  <text x="513" y="116" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">interativo</text>
  <path d="M588 103 L636 103" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#db-arrow)" />
  <text x="654" y="99" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">membros</text>
  <text x="654" y="114" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">exploram</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">As tabelas e vistas publicadas alimentam gráficos, mosaicos de indicadores e filtros dinâmicos que se juntam num painel de controlo interativo para os membros explorarem.</figcaption>
</figure>
