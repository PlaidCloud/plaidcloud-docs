---
title: Atribuições de alocação
description: Configure modelos de alocação do PlaidCloud para divisão de custos, custeio baseado em atividades, rateio de custos de TI e distribuição baseada em direcionadores.
sidebar:
  label: Visão geral
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/index.md
---

As alocações distribuem valores de um conjunto de linhas ("origem") para outro ("destino") usando dados de direcionadores e regras. O PlaidCloud oferece suporte a marcação baseada em regras, divisão de alocação, alocação orientada por dimensão e alocações recursivas para preço de transferência, rateio de custos de TI e problemas semelhantes de distribuição de custos.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 260" role="img" aria-label="Uma alocação distribui um conjunto de custos de origem entre destinos em proporção aos dados dos direcionadores. Um conjunto de origem de 1000 dólares passa por direcionadores como uso ou número de funcionários e é dividido em 50, 30 e 20 por cento entre os destinos A, B e C. Em um modelo recursivo, um destino pode retornar para outra passagem." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="al-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="14" y="98" width="150" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="89" y="122" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">conjunto de origem</text>
  <text x="89" y="140" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">$1,000</text>
  <path d="M164 128 L244 128" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#al-arrow)" />
  <rect x="246" y="98" width="142" height="60" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="317" y="122" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">direcionadores / base</text>
  <text x="317" y="140" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">uso · funcionários…</text>
  <path d="M388 118 C450 100 452 62 496 62" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#al-arrow)" />
  <path d="M388 128 L496 132" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#al-arrow)" />
  <path d="M388 138 C450 156 452 202 496 202" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#al-arrow)" />
  <text x="444" y="78" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">50%</text>
  <text x="450" y="126" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">30%</text>
  <text x="444" y="188" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">20%</text>
  <rect x="498" y="40" width="168" height="44" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="582" y="66" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Destino A — $500</text>
  <rect x="498" y="110" width="168" height="44" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="582" y="136" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Destino B — $300</text>
  <rect x="498" y="180" width="168" height="44" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="582" y="206" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Destino C — $200</text>
  <path d="M582 224 C582 250 90 250 89 160" stroke="var(--sl-color-gray-3)" stroke-width="1.3" fill="none" stroke-dasharray="5 4" marker-end="url(#al-arrow)" />
  <text x="330" y="248" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">recursivo: um destino pode alimentar a próxima passagem</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Os valores de um conjunto de origem são divididos entre os destinos em proporção aos dados dos direcionadores. Os modelos recursivos devolvem os resultados para outra passagem até que os números se estabilizem.</figcaption>
</figure>
