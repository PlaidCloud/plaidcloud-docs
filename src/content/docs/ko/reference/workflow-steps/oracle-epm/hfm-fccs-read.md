---
title: "HFM/FCCS: 데이터 읽기(임시)"
description: 단계 양식에서 관점을 구성하여 Oracle FCCS의 데이터 슬라이스를 셀프 서비스로 가져옵니다. 반환된 그리드는 자동으로 테이블로 저장되고, 반복 가져오기는 캐시되며, 엔터티 열은 행 수준 보안을 적용할 수 있고, 선택적인 대상 범위 지정으로 예약된 반복 로드로 전환할 수 있습니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/oracle-epm/hfm-fccs-read.md
---

## 설명

쿼리를 작성하는 대신 **관점(POV)** 으로 [HFM/FCCS 연결](/ko/guides/connections/hfm-fccs/)을 통해 Oracle **FCCS**(Financial Consolidation and Close, EPM Cloud)에서 임시 데이터 슬라이스를 읽습니다. 재무 담당자가 애플리케이션을 선택하고 FCCS 차원으로 POV를 구성한 뒤 단계를 실행하면, 반환된 그리드가 프로젝트 테이블로 자동 저장됩니다(읽기 시 스키마 적용 방식이며 테이블은 그리드의 열로 생성됨). 실시간 쿼리처럼 느껴지지만 내부적으로는 단계가 FCCS에 내보내기 작업을 제출하고, 완료될 때까지 **폴링**한 다음 결과를 가져와 저장합니다. 따라서 오래 걸리는 슬라이스도 대기를 막지 않으며 HFM 팀에 요청 티켓을 보낼 필요가 없습니다.

이 단계는 단계 메뉴의 **Oracle EPM (HFM/FCCS)** 아래에 표시됩니다.

:::note[엔터티 차원의 범위를 지정하십시오]
**엔터티** 선택을 한정된 범위로 유지하십시오. 범위가 지정되지 않은 추출은 내보내기 작업이 실행되는 동안 FCCS 애플리케이션을 오랫동안 잠글 수 있습니다.
:::

## 구성

### 소스 및 대상

| 필드 | 필수 | 참고 |
|---|---|---|
| HFM/FCCS 연결 | 예 | 읽기에 사용할 [HFM/FCCS 연결](/ko/guides/connections/hfm-fccs/)입니다. |
| 환경 | 예 | 연결의 환경입니다. |
| 애플리케이션 | 예 | 읽어 올 FCCS 애플리케이션입니다. 설정된 경우 연결의 기본 애플리케이션이 기본값입니다. 애플리케이션을 선택하면 POV의 라이브 멤버 검색이 실행됩니다. |
| 대상 테이블 | 예 | 반환된 그리드가 저장되는 프로젝트 테이블입니다. |

### 관점

FCCS 차원으로 슬라이스를 구성합니다. 지원되는 파드에서는 연결과 애플리케이션을 선택하면 라이브 메타데이터 검색에서 멤버 목록이 자동으로 채워지며, 이전 파드에서는 멤버 이름을 직접 입력합니다.

| 차원 | 필수 | 참고 |
|---|---|---|
| 시나리오 | 예 | |
| 연도 | 예 | |
| 기간 | 예 | |
| 엔터티 | 범위 한정 | 한정된 슬라이스를 지정해야 합니다. 양식은 빈 선택, "all", 또는 500개 멤버를 초과하는 선택을 거부합니다. 내보내기가 애플리케이션을 잠그지 않도록 범위를 한정하십시오. |
| 계정 | 아니요 | |
| Custom1–Custom4 | 아니요 | 애플리케이션의 사용자 지정 차원입니다. |
| ICP | 아니요 | 회사 간 거래(Intercompany)입니다. |
| 뷰 | 아니요 | |
| 값 | 아니요 | |

설정하지 않은 선택 차원은 해당 축에 필터를 적용하지 않습니다(FCCS의 기본 멤버가 사용됩니다).

### 대상 범위 지정

기본적으로 꺼져 있으며, 실행할 때마다 임시 슬라이스가 대상 테이블을 덮어쓰면서 저장됩니다.

| 필드 | 참고 |
|---|---|
| 대상 범위 지정(예약된 반복 로드) | 선택하면 대상이 **영구** 테이블이 됩니다. 단계는 덮어쓰는 대신 키셋 업서트로 병합하며, 이후 그리드에 새 열이 있으면 스키마가 추가 방식으로 확장됩니다(새 열은 경고를 발생시키지만 실패하지 않음). 이 단계를 예약된 워크플로에 배치하면 데이터를 지우지 않고 누적하는 반복 로드가 됩니다. |
| 키 열 | 대상 범위 지정을 켠 경우에만 사용할 수 있습니다. 병합 키를 구성하는 쉼표로 구분된 열입니다(예: `Entity, Account`). **비워 두면** 저장된 그리드에 있는 POV 차원 열을 병합 키로 사용합니다. |

## 작동 방식

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 720 130" role="img" aria-label="단계가 FCCS에 내보내기 작업을 제출하고, 완료될 때까지 폴링하고, 그리드를 가져와 테이블로 저장합니다. 반복되는 관점은 대신 캐시된 테이블에서 제공됩니다." style="width:100%;max-width:720px;height:auto;">
<defs><marker id="hf-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
<rect x="10" y="46" width="96" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="58" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">작업 제출</text>
<rect x="150" y="46" width="96" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="198" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">폴링</text>
<rect x="290" y="46" width="96" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="338" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">그리드 가져오기</text>
<rect x="430" y="46" width="120" height="40" rx="7" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" /><text x="490" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">테이블 저장</text>
<path d="M106 66 L150 66" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#hf-arrow)" />
<path d="M246 66 L290 66" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#hf-arrow)" />
<path d="M386 66 L430 66" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#hf-arrow)" />
<text x="198" y="34" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">실행 중에는…</text>
<rect x="590" y="46" width="120" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="650" y="64" text-anchor="middle" font-size="10" fill="var(--sl-color-text)">반복 POV</text><text x="650" y="78" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">캐시에서 제공</text>
<path d="M550 82 C570 100 630 100 650 88" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" stroke-dasharray="4 3" marker-end="url(#hf-arrow)" />
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">실행은 내보내기 작업을 제출하고, 폴링하고, 그리드를 가져와 테이블로 저장합니다. 같은 관점을 다시 요청하면 이미 저장된 사본에서 제공됩니다.</figcaption>
</figure>

작업이 실행되는 동안 단계에는 폴링 상태가 표시됩니다. 저장이 완료되면 테이블이 그리드의 열로 생성되므로 미리 스키마를 정의할 필요가 없습니다.

## 캐싱

같은 POV를 다시 요청하면 FCCS에 내보내기를 다시 제출하는 대신 **이미 저장된 테이블에서 즉시 제공**됩니다. 실행은 애플리케이션, 대상 테이블, 관점, **기준 시점** 태그(기본값 `latest`)를 키로 식별되며, 이미 저장된 슬라이스로 확인되는 반복 실행은 테이블을 다시 쓰지 않고 그대로 두었다고 보고합니다. 같은 POV를 새로 추출하도록 강제하려면 기준 시점 태그를 변경하십시오.

## 행 수준 보안

저장된 그리드의 엔터티 축은 정확히 **`Entity`** 라는 이름의 열로 정규화되므로 테이블은 **행 수준 보안을 적용할 수 있는 상태**입니다. 관리자가 [행 액세스](/ko/administration/access/managing-security-groups-and-assignments/)로 이를 관리하여 셀프 서비스 사용자가 권한이 있는 엔터티만 볼 수 있도록 할 수 있습니다.

이는 **자동이 아니라 관리자의 통제 하에 관리됩니다**. 추출은 연결의 서비스 계정으로 실행되므로 PlaidCloud는 단계가 자체 보안을 선언하도록 허용하지 않습니다. 관리자는 표준 행 액세스 워크플로를 따릅니다.

1. 보고용으로 저장된 테이블을 **게시**합니다.
2. `Entity` 열을 관리 속성으로 **선언**합니다(기본 거부).
3. 첫 번째 관리되는 쓰기를 **승인**합니다.
4. 권한이 적용되도록 **조정**합니다.

관리자가 이 작업을 수행하기 전까지는 테이블에 필터가 적용되지 않습니다. [보안 그룹 및 할당 관리](/ko/administration/access/managing-security-groups-and-assignments/)를 참조하십시오.

## 기능 제한

| 제한 사항 | 의미 |
|---|---|
| 읽기 전용 | FCCS에서 슬라이스를 추출합니다. 연결 데이터를 쓰거나, 연결 작업을 실행하거나, 다시 전기하지 않습니다. |
| 한정된 엔터티 필수 | 양식은 빈 선택, "all", 또는 500개 멤버를 초과하는 엔터티 선택을 거부하며, 단일 집계 멤버도 서버 측에서 확장될 수 있으므로 슬라이스의 범위를 한정하십시오. |
| 이전 파드에서는 수동 멤버 입력 | 파드가 메타데이터 엔드포인트를 제공하지 않으면 멤버 목록이 자동으로 채워지지 않으므로 멤버 이름을 직접 입력하십시오. |
| 행 수준 보안은 관리자가 관리 | `Entity` 열은 RLS를 적용할 수 있는 상태이지만, 테이블에 필터가 적용되려면 관리자가 게시, 선언, 첫 쓰기 승인, 조정을 수행해야 합니다. |

## 관련 항목

- [HFM / FCCS에서 추출(가이드)](/ko/guides/connections/hfm-fccs/) — 전체 안내입니다.
- [HFM / FCCS 커넥터](/ko/reference/connectors/rest/hfm-fccs/) — 연결 필드 참조입니다.
- [Oracle EPM (HFM / FCCS) 단계](/ko/reference/workflow-steps/oracle-epm/)
- [보안 그룹 및 할당 관리](/ko/administration/access/managing-security-groups-and-assignments/)
