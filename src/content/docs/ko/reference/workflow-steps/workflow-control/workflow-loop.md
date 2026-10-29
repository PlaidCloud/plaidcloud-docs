---
title: Workflow Loop 단계
description: PlaidCloud 워크플로 단계에서 루프를 만들어 값 집합을 순회하며 컬렉션의 각 항목마다 단계를 반복합니다.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/workflow-loop.md
---

## 설명

데이터 세트의 행마다 대상 워크플로를 한 번씩 실행하며, 각 반복 전에 해당 행의 열 값을 프로젝트 변수로 설정합니다. 입력을 바꿔 가며 여러 번 실행해야 하는 매개변수화된 프로세스가 있을 때 사용합니다. 예를 들어 "이 테이블에 있는 모든 사업부에 대해 월 마감 실행" 또는 "나열된 모든 분기에 대해 이 보고서 로드"와 같은 경우입니다.

각 루프 반복에서는 변수가 수동으로 설정된 것처럼 보이므로, 호출된 워크플로는 표준 `\{variable_name}` 구문을 사용해 식, 필터, 파일 경로, 테이블 이름에서 변수를 참조할 수 있습니다. 루프는 기본적으로 순차 실행되며, 반복이 병렬로 실행되지 않습니다.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 690 170" role="img" aria-label="Q1, Q2, Q3 행이 있는 데이터 세트에 대한 Workflow Loop입니다. 각 행의 열 값이 프로젝트 변수가 된 다음 대상 워크플로가 실행되며, 행마다 한 번씩 병렬이 아닌 순차로 진행됩니다." style="width:100%;max-width:690px;height:auto;">
  <defs><marker id="wl-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="14" y="50" width="120" height="74" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="74" y="44" text-anchor="middle" font-size="12" font-weight="700" fill="var(--sl-color-text)">데이터 세트</text>
  <text x="74" y="76" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Q1</text>
  <text x="74" y="96" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Q2</text>
  <text x="74" y="116" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Q3</text>
  <path d="M134 87 L178 87" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#wl-arrow)" />
  <rect x="180" y="63" width="140" height="48" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="250" y="83" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">quarter = Q1</text>
  <text x="250" y="99" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">1회차</text>
  <path d="M320 87 L360 87" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#wl-arrow)" />
  <rect x="362" y="63" width="140" height="48" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="432" y="83" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">quarter = Q2</text>
  <text x="432" y="99" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">2회차</text>
  <path d="M502 87 L542 87" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#wl-arrow)" />
  <rect x="544" y="63" width="138" height="48" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="613" y="83" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">quarter = Q3</text>
  <text x="613" y="99" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">3회차</text>
  <text x="408" y="142" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">순차 실행 — 병렬이 아니라 한 번에 한 회차씩</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">각 행의 열이 프로젝트 변수가 된 다음 대상 워크플로가 실행되며, 행마다 한 번씩 순차로 진행됩니다. 격리된 병렬 팬아웃이 필요하면 대신 <a href="/ko/guides/workflows/create-a-macro/">매크로</a>를 사용하십시오.</figcaption>
</figure>



## 중지할 워크플로


먼저 **프로젝트** 드롭다운 메뉴에서 각 루프마다 실행할 워크플로가 들어 있는 프로젝트를 선택합니다.



다음으로 **워크플로** 드롭다운 메뉴에서 실행할 워크플로를 선택합니다.

## 반복이 실패하는 경우

기본적으로 루프는 워크플로가 실패한 첫 번째 반복에서 중지되고 단계도 실패합니다. **오류 처리**에서 **실패한 반복 이후에도 계속**을 선택하면 한 반복이 실패하더라도 모든 반복을 실행합니다. 각 실패는 각 반복의 결과와 함께 **반복 실행 상태**에 보관되며, 단계는 실패한 반복의 개수를 알려 주는 경고와 함께 종료됩니다. 선택을 해제하면 루프는 첫 번째 실패에서 중지됩니다.

## 예시

예시는 곧 추가될 예정입니다
