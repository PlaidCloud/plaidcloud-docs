---
title: 仪表板
description: 创建并自定义 PlaidCloud 仪表板，通过交互式图表、图形和动态指标展示来可视化数据。
sidebar:
  label: 仪表板
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dashboards/index.md
---

基于 PlaidCloud 项目数据构建交互式仪表板，包括图表、指标、计算列、动态筛选器和嵌入式数据探索。

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 200" role="img" aria-label="已发布的项目表和视图为仪表板的构建块（图表、指标磁贴和动态筛选器）提供数据，这些构建块组合成一个交互式仪表板，供工作区成员探索。" style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="db-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="16" y="74" width="140" height="56" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="86" y="98" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">已发布数据</text>
  <text x="86" y="116" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">表与视图</text>
  <path d="M156 102 C196 102 206 66 244 66" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#db-arrow)" />
  <path d="M156 102 L244 102" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#db-arrow)" />
  <path d="M156 102 C196 102 206 138 244 138" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#db-arrow)" />
  <rect x="246" y="48" width="130" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="311" y="69" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">图表</text>
  <rect x="246" y="86" width="130" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="311" y="107" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">指标磁贴</text>
  <rect x="246" y="124" width="130" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="311" y="145" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">动态筛选器</text>
  <path d="M376 103 L436 103" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#db-arrow)" />
  <rect x="438" y="60" width="150" height="86" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="513" y="98" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">仪表板</text>
  <text x="513" y="116" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">交互式</text>
  <path d="M588 103 L636 103" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#db-arrow)" />
  <text x="654" y="99" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">成员</text>
  <text x="654" y="114" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">探索</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">已发布的表和视图为图表、指标磁贴和动态筛选器提供数据，它们组合成一个交互式仪表板，供成员探索。</figcaption>
</figure>
