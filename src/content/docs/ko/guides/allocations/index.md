---
title: 배부 할당
description: 비용 분할, 활동 기준 원가 계산, IT 차지백, 드라이버 기반 분배를 위한 PlaidCloud 배부 모델을 구성합니다.
sidebar:
  label: 개요
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/index.md
---

배부는 드라이버 데이터와 규칙을 사용해 한 행 집합("소스")의 값을 다른 행 집합("대상")으로 나누어 줍니다. PlaidCloud는 이전 가격, IT 차지백 및 이와 유사한 비용 분배 문제를 위해 규칙 기반 태깅, Allocation Split 단계, 차원 기반 배부, 재귀 배부를 지원합니다.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 260" role="img" aria-label="배부는 드라이버 데이터에 비례하여 소스 비용 풀을 대상에 나누어 줍니다. 1,000달러의 소스 풀이 사용량이나 인원수 같은 드라이버를 거쳐 대상 A, B, C에 50%, 30%, 20%로 분할됩니다. 재귀 모델에서는 대상이 다시 입력되어 한 번 더 처리될 수 있습니다." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="al-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="14" y="98" width="150" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="89" y="122" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">소스 풀</text>
  <text x="89" y="140" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">$1,000</text>
  <path d="M164 128 L244 128" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#al-arrow)" />
  <rect x="246" y="98" width="142" height="60" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="317" y="122" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">드라이버 / 기준</text>
  <text x="317" y="140" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">사용량 · 인원수…</text>
  <path d="M388 118 C450 100 452 62 496 62" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#al-arrow)" />
  <path d="M388 128 L496 132" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#al-arrow)" />
  <path d="M388 138 C450 156 452 202 496 202" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#al-arrow)" />
  <text x="444" y="78" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">50%</text>
  <text x="450" y="126" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">30%</text>
  <text x="444" y="188" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">20%</text>
  <rect x="498" y="40" width="168" height="44" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="582" y="66" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">대상 A — $500</text>
  <rect x="498" y="110" width="168" height="44" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="582" y="136" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">대상 B — $300</text>
  <rect x="498" y="180" width="168" height="44" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="582" y="206" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">대상 C — $200</text>
  <path d="M582 224 C582 250 90 250 89 160" stroke="var(--sl-color-gray-3)" stroke-width="1.3" fill="none" stroke-dasharray="5 4" marker-end="url(#al-arrow)" />
  <text x="330" y="248" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">재귀: 대상이 다음 패스의 입력이 될 수 있음</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">소스 풀의 값은 드라이버 데이터에 비례하여 대상에 나누어집니다. 재귀 모델은 결과를 다시 입력하여 수치가 안정될 때까지 한 번 더 처리합니다.</figcaption>
</figure>
