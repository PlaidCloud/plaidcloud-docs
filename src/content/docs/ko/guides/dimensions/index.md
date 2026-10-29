---
title: 데이터 관리 - 차원
description: 특성, 대체 계층, 속성, 계산된 값을 포함하여 PlaidCloud에서 계층형 데이터 차원을 관리합니다.
sidebar:
  label: 개요
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dimensions/index.md
---

차원은 데이터를 분할하고 집계하는 데 사용하는 계층으로, 비용 센터, 제품, 지역, 기간 등이 해당합니다. 이 섹션에서는 특성, 대체 계층, 속성, 계산된 값을 관리하는 방법을 다룹니다.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 640 250" role="img" aria-label="트리로 그린 지역 차원입니다. 루트인 합계에는 북부와 남부라는 두 개의 하위 노드가 있습니다. 북부에는 리프 멤버 NY와 MA가, 남부에는 리프 멤버 TX와 FL이 있습니다. 리프 값은 상위 노드를 거쳐 루트까지 롤업됩니다." style="width:100%;max-width:640px;height:auto;">
  <defs><marker id="dm-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <path d="M320 54 L175 96" stroke="var(--sl-color-gray-5)" stroke-width="1.4" fill="none" />
  <path d="M320 54 L465 96" stroke="var(--sl-color-gray-5)" stroke-width="1.4" fill="none" />
  <path d="M175 132 L90 176" stroke="var(--sl-color-gray-5)" stroke-width="1.4" fill="none" />
  <path d="M175 132 L260 176" stroke="var(--sl-color-gray-5)" stroke-width="1.4" fill="none" />
  <path d="M465 132 L380 176" stroke="var(--sl-color-gray-5)" stroke-width="1.4" fill="none" />
  <path d="M465 132 L550 176" stroke="var(--sl-color-gray-5)" stroke-width="1.4" fill="none" />
  <rect x="270" y="20" width="100" height="36" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="320" y="43" text-anchor="middle" font-size="12" font-weight="700" fill="var(--sl-color-text)">합계</text>
  <rect x="125" y="96" width="100" height="36" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="175" y="119" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">북부</text>
  <rect x="415" y="96" width="100" height="36" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="465" y="119" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">남부</text>
  <rect x="50" y="176" width="80" height="32" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="90" y="197" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">NY</text>
  <rect x="220" y="176" width="80" height="32" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="260" y="197" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">MA</text>
  <rect x="340" y="176" width="80" height="32" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="380" y="197" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">TX</text>
  <rect x="510" y="176" width="80" height="32" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="550" y="197" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">FL</text>
  <path d="M615 200 L615 40" stroke="var(--sl-color-gray-3)" stroke-width="1.3" fill="none" marker-end="url(#dm-arrow)" />
  <text x="628" y="124" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)" transform="rotate(-90 628 124)">값 롤업</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">차원은 계층입니다. 리프 값은 상위 노드를 거쳐 루트까지 롤업되며, 같은 트리가 분할과 집계를 모두 처리합니다. 대체 계층은 같은 리프를 다른 방식으로 다시 그룹화합니다.</figcaption>
</figure>
