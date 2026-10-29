---
title: 대시보드
description: PlaidCloud 대시보드를 만들고 사용자 지정하여 대화형 차트, 그래프, 동적 지표 표시로 데이터를 시각화합니다.
sidebar:
  label: 대시보드
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dashboards/index.md
---

PlaidCloud 프로젝트 데이터를 기반으로 대화형 대시보드를 빌드합니다. 차트, 지표, 계산된 열, 동적 필터, 임베디드 데이터 탐색을 사용할 수 있습니다.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 200" role="img" aria-label="게시된 프로젝트 테이블과 뷰가 차트, 지표 타일, 동적 필터라는 대시보드 구성 요소에 데이터를 공급하고, 이 구성 요소들이 워크스페이스 멤버가 탐색할 하나의 대화형 대시보드로 조립됩니다." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="db-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="16" y="74" width="140" height="56" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="86" y="98" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">게시된 데이터</text>
  <text x="86" y="116" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">테이블 &amp; 뷰</text>
  <path d="M156 102 C196 102 206 66 244 66" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#db-arrow)" />
  <path d="M156 102 L244 102" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#db-arrow)" />
  <path d="M156 102 C196 102 206 138 244 138" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#db-arrow)" />
  <rect x="246" y="48" width="130" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="311" y="69" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">차트</text>
  <rect x="246" y="86" width="130" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="311" y="107" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">지표 타일</text>
  <rect x="246" y="124" width="130" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="311" y="145" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">동적 필터</text>
  <path d="M376 103 L436 103" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#db-arrow)" />
  <rect x="438" y="60" width="150" height="86" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="513" y="98" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">대시보드</text>
  <text x="513" y="116" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">대화형</text>
  <path d="M588 103 L636 103" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#db-arrow)" />
  <text x="654" y="99" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">멤버</text>
  <text x="654" y="114" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">탐색</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">게시된 테이블과 뷰가 차트, 지표 타일, 동적 필터에 데이터를 공급하며, 이들이 멤버가 탐색할 하나의 대화형 대시보드로 조립됩니다.</figcaption>
</figure>
