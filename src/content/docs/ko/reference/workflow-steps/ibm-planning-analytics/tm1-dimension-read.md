---
title: "TM1: 차원 읽기"
description: IBM TM1 / Planning Analytics 계층(요소, 부모/자식 에지, 요소 속성)을 REST를 통해 클라우드 직접 방식으로 읽어 PlaidCloud 차원으로 로드합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read.md
---

## 설명

[TM1 연결](/ko/guides/connections/tm1/)을 통해 IBM **TM1 / Planning Analytics** 차원에서 계층 하나를 읽어 PlaidCloud 차원으로 로드합니다. TM1 계층의 요소, 부모/자식 에지, 요소 속성은 먼저 테이블에 부모/자식 행으로 스테이징되고, PlaidCloud 차원은 이 스테이징 테이블에서 만들어집니다. PlaidCloud 자체의 Dimension Load 단계가 수행하는 것과 같은 로드이므로, TM1 계층은 직접 만든 계층이나 외부에서 가져온 다른 계층과 똑같이 로드됩니다.

이 단계는 단계 메뉴의 **IBM TM1 / Planning Analytics** 아래에 표시됩니다.

단계는 REST API를 통해 TM1에 **클라우드에서 직접** 연결하며, 온프레미스 에이전트는 관여하지 않습니다. 온프레미스 방식은 [TM1: 큐브 쿼리(에이전트)](/ko/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/)를 참조하십시오.

## 구성

### TM1 소스

| 필드 | 필수 | 참고 |
|---|---|---|
| TM1 연결 | 예 | 읽는 데 사용할 [TM1 연결](/ko/guides/connections/tm1/)입니다. |
| 환경 | 예 | 연결의 환경입니다. |
| 데이터베이스 | 예 | 읽을 TM1 데이터베이스(인스턴스)입니다. 연결에 기본 데이터베이스가 설정되어 있으면 이것이 기본값입니다. |
| TM1 차원 | 예 | 읽을 TM1 차원입니다. 연결된 데이터베이스에서 실시간으로 검색하거나 직접 입력합니다. |
| TM1 계층 | 아니요 | 차원 안의 계층입니다. 차원을 선택하면 실시간으로 검색하거나 직접 입력합니다. 비워 두면 차원의 고유(암시적) 계층을 읽으며, TM1은 이 계층에 차원과 같은 이름을 붙입니다. |
| 스테이징 테이블 | 예 | PlaidCloud 차원을 만들기 전에 원시 부모/자식/속성 행을 담는 테이블입니다. |

차원과 계층을 선택하면 양식에 어떤 TM1 요소 속성이 PlaidCloud **별칭**으로, 어떤 속성이 **속성**으로 로드되는지 표시됩니다. 이는 TM1 자체의 속성 유형(`Alias` 대 `Numeric`/`String`)에 따라 결정됩니다. 모든 요소의 TM1 유형(Numeric, String 또는 Consolidated)도 `tm1_element_type`이라는 이름의 속성으로 로드됩니다.

### 대상 PlaidCloud 차원

| 필드 | 필수 | 참고 |
|---|---|---|
| 차원을 동적으로 지정 | 둘 중 하나 | 대상 차원 이름이며, 실행 시 확인되는 `{variable}` 토큰을 포함할 수 있습니다. 기본으로 선택되어 있습니다. |
| 특정 차원 사용 | 둘 중 하나 | 대신 트리에서 이미 있는 PlaidCloud 차원을 선택합니다. |
| 대체 계층 | 아니요 | 로드할 PlaidCloud 대체 계층 키입니다. 비워 두면 기본 계층에 로드합니다. |

대체 계층으로 로드할 때는 무엇이든 기록하기 전에 검증합니다. PlaidCloud 대체 계층은 차원의 기본 계층에 이미 있는 노드의 부모를 바꿀 수 없으며, TM1 대체 계층은 정의상 TM1 자체의 기본 계층과 요소를 공유하므로 이 옵션에서는 이것이 예외적인 경우가 아니라 일반적인 형태입니다. 구문 분석한 행 중 부모가 대상 차원의 기본 계층에 이미 있는 행이 하나라도 있으면, 단계는 스테이징 테이블을 건드리기 전에 충돌하는 부모를 알려 주며 즉시 실패합니다.

## 이 단계에서 표현할 수 없는 항목

| 제한 사항 | 의미 |
|---|---|
| 부모가 여러 개인 요소는 거부됨 | PlaidCloud 차원 노드는 계층마다 부모가 정확히 하나입니다. 같은 계층에서 두 합산 아래에 있는 TM1 요소는 로드할 수 없으며, 단계는 첫 번째 합산에서 요소를 조용히 제외하는 대신 문제가 되는 모든 요소와 그 부모를 나열한 명명된 오류와 함께 실패합니다. 대체 롤업을 별도의 PlaidCloud 차원으로 읽거나 TM1에서 중복된 부모 관계를 먼저 해결하십시오. |
| 합산 가중치는 부호만 반영됨 | PlaidCloud 에지는 계수가 아니라 합산 플래그(`+`, `-`, `~`)를 가집니다. TM1 가중치 `0`은 `~`가 되고(멤버가 부모로 롤업되지 않음), 음수 가중치는 `-`가, 양수 가중치는 `+`가 되며, 가중치가 없으면(TM1 자체의 기본값) `+`로 처리됩니다. **0.5, 2.0 같은 소수 또는 배수 가중치는 표현할 수 없습니다**. 일반 `+`로 로드되며 배수는 사라집니다. 이는 조용히 넘어가지 않고 집계되어 알려집니다. 실행의 단계 경고에는 영향을 받은 에지 수가 보고되고 `parent -> child (weight)` 형식(예: `Total Revenue -> Product A (0.5)`)으로 나열되며, 10개까지만 표시하고 그 이상은 "(외 N개)"로 표시합니다. 루트 에지(부모 없음)는 비워 두지 않고 `(root)`로 표시합니다. 숫자가 아닌 가중치가 있으면 추측하지 않고 즉시 거부합니다. |
| 에이전트를 통한 검색 없음 | 이 단계는 클라우드 직접 방식 전용입니다. 클라우드에서 접근할 수 없는 TM1 서버를 읽으려면 [TM1: 큐브 쿼리(에이전트)](/ko/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/)를 참조하십시오. |

## 관련 항목

- [TM1 연결(가이드)](/ko/guides/connections/tm1/) — 연결을 만듭니다.
- [TM1 커넥터](/ko/reference/connectors/rest/tm1/) — 온프레미스 에이전트 경로를 포함한 연결 필드 참조입니다.
- [TM1: 큐브 쿼리](/ko/reference/workflow-steps/ibm-planning-analytics/tm1-query/) — 큐브 데이터를 클라우드 직접 방식으로 읽습니다.
- [TM1: 큐브 쿼리(에이전트)](/ko/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) — 온프레미스 PlaidLink 에이전트를 통해 큐브 데이터를 읽습니다.
- [Dimension Load 단계](/ko/reference/workflow-steps/dimensions/dimension-load/) — 이 단계가 기반으로 하는 것과 같은 차원 로드 메커니즘입니다.
- [IBM TM1 / Planning Analytics 단계](/ko/reference/workflow-steps/ibm-planning-analytics/)
