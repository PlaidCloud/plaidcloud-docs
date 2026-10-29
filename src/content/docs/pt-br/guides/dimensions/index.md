---
title: Gerenciamento de dados - Dimensões
description: Gerencie dimensões de dados hierárquicas no PlaidCloud, incluindo atributos, hierarquias alternativas, propriedades e valores calculados.
sidebar:
  label: Visão geral
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dimensions/index.md
---

As dimensões são hierarquias que você usa para segmentar e agregar dados — centros de custo, produtos, geografia, períodos. Esta seção aborda o gerenciamento de atributos, hierarquias alternativas, propriedades e valores calculados.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 640 250" role="img" aria-label="Uma dimensão de geografia desenhada como uma árvore. A raiz Total tem dois nós filhos, Norte e Sul. Norte tem os membros folha NY e MA; Sul tem os membros folha TX e FL. Os valores das folhas são consolidados pelos pais até a raiz." style="width:100%;max-width:640px;height:auto;">
  <defs><marker id="dm-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <path d="M320 54 L175 96" stroke="var(--sl-color-gray-5)" stroke-width="1.4" fill="none" />
  <path d="M320 54 L465 96" stroke="var(--sl-color-gray-5)" stroke-width="1.4" fill="none" />
  <path d="M175 132 L90 176" stroke="var(--sl-color-gray-5)" stroke-width="1.4" fill="none" />
  <path d="M175 132 L260 176" stroke="var(--sl-color-gray-5)" stroke-width="1.4" fill="none" />
  <path d="M465 132 L380 176" stroke="var(--sl-color-gray-5)" stroke-width="1.4" fill="none" />
  <path d="M465 132 L550 176" stroke="var(--sl-color-gray-5)" stroke-width="1.4" fill="none" />
  <rect x="270" y="20" width="100" height="36" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="320" y="43" text-anchor="middle" font-size="12" font-weight="700" fill="var(--sl-color-text)">Total</text>
  <rect x="125" y="96" width="100" height="36" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="175" y="119" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Norte</text>
  <rect x="415" y="96" width="100" height="36" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="465" y="119" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Sul</text>
  <rect x="50" y="176" width="80" height="32" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="90" y="197" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">NY</text>
  <rect x="220" y="176" width="80" height="32" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="260" y="197" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">MA</text>
  <rect x="340" y="176" width="80" height="32" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="380" y="197" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">TX</text>
  <rect x="510" y="176" width="80" height="32" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="550" y="197" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">FL</text>
  <path d="M615 200 L615 40" stroke="var(--sl-color-gray-3)" stroke-width="1.3" fill="none" marker-end="url(#dm-arrow)" />
  <text x="628" y="124" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)" transform="rotate(-90 628 124)">os valores são consolidados</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Uma dimensão é uma hierarquia. Os valores das folhas são consolidados pelos nós pais até a raiz — a mesma árvore serve tanto para segmentar quanto para agregar. As hierarquias alternativas reagrupam as mesmas folhas de outra maneira.</figcaption>
</figure>
