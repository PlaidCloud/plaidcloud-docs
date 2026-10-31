---
title: PlaidXL
description: PlaidXL Excel 추가 기능으로 PlaidCloud 워크스페이스에 로그인하고, 프로젝트 테이블과 차원 계층을 워크시트로 가져오며, 필요할 때 새로 고치고, PlaidXL 사용자 지정 함수로 실시간 보고서를 작성합니다.
sidebar:
  label: PlaidXL
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/index.md
---

PlaidXL은 Microsoft Excel용 PlaidCloud 추가 기능입니다. 통합 문서를 PlaidCloud 워크스페이스에 연결하여, 워크플로가 다음에 실행될 때 오래된 데이터가 되어 버리는 사본이 아니라 신뢰할 수 있는 프로젝트 테이블과 차원에서 모델과 보고서가 데이터를 읽도록 합니다.

PlaidXL은 두 가지 방식으로 사용할 수 있으며 대부분의 통합 문서에서는 둘을 함께 사용합니다.

- **작업 창** — 프로젝트를 둘러보고, 테이블이나 차원을 선택하고, 열과 필터를 지정하여 데이터를 워크시트로 가져옵니다. **Refresh All Tables**는 가져온 모든 테이블의 최신 데이터를 가져옵니다.
- **사용자 지정 함수** — `=PLAIDXL.TABLE.GET_TABLE("Sales")`, `=PLAIDXL.CELL(...)` 같은 수식으로 PlaidCloud 데이터를 셀로 바로 읽어 옵니다. 테이블과 차원을 나열하고, 계층을 배치하고, 보고서에 사용할 롤업 값을 계산하는 데 사용합니다.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 230" role="img" aria-label="Excel에는 PlaidXL 작업 창과 PlaidXL 사용자 지정 함수가 있습니다. 둘 다 사용자 본인으로 로그인한 상태에서 PlaidCloud 워크스페이스의 프로젝트에 요청을 보내며, 프로젝트는 테이블 행, 차원 계층, 롤업 값을 워크시트 셀로 반환합니다." style="width:100%;max-width:660px;height:auto;">
  <defs>
    <marker id="px-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker>
  </defs>
  <rect x="20" y="20" width="250" height="190" rx="10" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="145" y="44" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Excel 통합 문서</text>
  <rect x="40" y="62" width="210" height="52" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="145" y="84" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">PlaidXL 작업 창</text>
  <text x="145" y="102" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">탐색, 필터링, 가져오기, 새로 고침</text>
  <rect x="40" y="130" width="210" height="52" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="145" y="152" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">PLAIDXL.* 함수</text>
  <text x="145" y="170" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">테이블, 계층, 셀 값</text>
  <rect x="410" y="40" width="230" height="150" rx="10" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="525" y="66" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">PlaidCloud 워크스페이스</text>
  <rect x="430" y="80" width="190" height="94" rx="8" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="525" y="102" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">프로젝트</text>
  <text x="525" y="124" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">테이블</text>
  <text x="525" y="142" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">차원 및 계층</text>
  <path d="M252 98 L405 98" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#px-arrow)" />
  <text x="330" y="90" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">사용자 본인으로 로그인</text>
  <path d="M405 150 L254 150" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#px-arrow)" />
  <text x="330" y="168" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">행, 노드, 값</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">작업 창과 사용자 지정 함수는 모두 사용자 본인의 PlaidCloud 권한으로 선택한 프로젝트에서 데이터를 읽습니다.</figcaption>
</figure>

PlaidXL은 데이터를 읽기만 합니다. PlaidCloud에 아무것도 다시 쓰지 않으므로 가져온 시트를 편집해도 프로젝트 테이블은 변경되지 않습니다.

## 요구 사항

- Windows 또는 Mac의 Microsoft 365용 Excel 또는 Excel 2021 이상. PlaidCloud 리본 탭과 작업 창은 데스크톱 Excel에서 실행됩니다.
- 하나 이상의 워크스페이스에 속한 PlaidCloud 계정과 읽으려는 프로젝트에 대한 액세스 권한. PlaidXL에는 PlaidCloud에서 계정이 이미 볼 수 있는 프로젝트, 테이블, 차원만 표시됩니다.

## 주제

- [설치](/ko/reference/cli/plaidxl/install/) — Excel에 PlaidXL을 추가하고 작업 창 열기
- [로그인](/ko/reference/cli/plaidxl/connect/) — 워크스페이스에 연결하고, 로그아웃하고, 워크스페이스 전환하기
- [테이블 및 차원 사용](/ko/reference/cli/plaidxl/retrieve/) — 프로젝트 선택, 테이블 필터링, 시트로 가져오기 및 새로 고침
- [사용자 지정 함수](/ko/reference/cli/plaidxl/functions/) — 모든 `PLAIDXL` 함수, 인수 및 반환 값
- [사용자 지정 함수로 보고서 작성](/ko/reference/cli/plaidxl/build-a-report/) — 계층을 배치하고 롤업 값으로 채우기
- [PlaidCloud 리본](/ko/reference/cli/plaidxl/ribbon/) — 새로 고침, 드릴, 정리 명령
- [문제 해결](/ko/reference/cli/plaidxl/troubleshooting/) — 가장 흔한 문제의 해결 방법

PlaidXL을 처음 사용하십니까? [PlaidXL로 Excel에서 작업하기](/ko/get-started/tutorials/excel-with-plaidxl/) 튜토리얼에서 추가 기능 설치부터 첫 보고서까지 약 20분 만에 진행해 볼 수 있습니다.

## 관련 항목

- [프로젝트](/ko/guides/projects/) — 프로젝트에 포함된 내용과 프로젝트를 찾는 방법
- [테이블 및 뷰](/ko/guides/data/tables-views/) — PlaidXL이 가져오는 테이블
- [차원 사용](/ko/guides/dimensions/dimensions/) — PlaidXL이 배치하고 롤업하는 계층
