---
title: 分摊分配
description: 配置 PlaidCloud 分摊模型，用于成本拆分、作业成本法、IT 费用回收和基于动因的分配。
sidebar:
  label: 概览
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/index.md
---

分摊使用动因数据和规则，将一组行（“源”）的数值分配到另一组行（“目标”）。PlaidCloud 支持基于规则的标记、分摊拆分、维度驱动的分摊以及递归分摊，可用于转让定价、IT 费用回收及类似的成本分配问题。

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 260" role="img" aria-label="分摊按动因数据的比例，将源成本池分配到各目标。1000 美元的源成本池经由使用量或人数等动因，按 50%、30%、20% 分配到目标 A、B 和 C。在递归模型中，目标可以回流，进入下一轮分摊。" style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="al-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="14" y="98" width="150" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="89" y="122" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">源成本池</text>
  <text x="89" y="140" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">$1,000</text>
  <path d="M164 128 L244 128" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#al-arrow)" />
  <rect x="246" y="98" width="142" height="60" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="317" y="122" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">动因 / 基准</text>
  <text x="317" y="140" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">使用量 · 人数…</text>
  <path d="M388 118 C450 100 452 62 496 62" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#al-arrow)" />
  <path d="M388 128 L496 132" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#al-arrow)" />
  <path d="M388 138 C450 156 452 202 496 202" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#al-arrow)" />
  <text x="444" y="78" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">50%</text>
  <text x="450" y="126" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">30%</text>
  <text x="444" y="188" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">20%</text>
  <rect x="498" y="40" width="168" height="44" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="582" y="66" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">目标 A — $500</text>
  <rect x="498" y="110" width="168" height="44" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="582" y="136" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">目标 B — $300</text>
  <rect x="498" y="180" width="168" height="44" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="582" y="206" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">目标 C — $200</text>
  <path d="M582 224 C582 250 90 250 89 160" stroke="var(--sl-color-gray-3)" stroke-width="1.3" fill="none" stroke-dasharray="5 4" marker-end="url(#al-arrow)" />
  <text x="330" y="248" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">递归：目标可进入下一轮分摊</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">源成本池中的数值按动因数据的比例分配到各目标。递归模型会将结果回流，进行下一轮分摊，直至数值趋于稳定。</figcaption>
</figure>
