---
title: "Essbase: 차원 읽기"
description: Oracle Essbase 차원 아웃라인을 클라우드 직접 방식으로 PlaidCloud 차원의 기본 계층으로 읽어 오며, 공유, 레이블 전용, Dynamic Calc, 속성 멤버와 아웃라인이 표현할 수 없는 모든 항목은 이름을 밝히고 거부합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/essbase/essbase-dimension-read.md
---

## 설명

[Oracle Essbase 연결](/ko/guides/connections/essbase/)을 통해 Oracle **Essbase** 큐브에서 차원 아웃라인 하나를 읽어 PlaidCloud 차원의 **기본 계층**으로 로드합니다.

이 단계는 단계 메뉴의 **Oracle Essbase** 아래에 표시됩니다.

이 단계는 REST API를 통해 Essbase에 **클라우드 직접** 방식으로 접근합니다. 이 단계에는 온프레미스 에이전트 경로가 없으며 원격 변형도 없습니다.

## 구성

### Essbase 소스

| 필드 | 필수 | 참고 |
|---|---|---|
| 연결 | 예 | 읽을 때 사용할 [Oracle Essbase 연결](/ko/guides/connections/essbase/)입니다. |
| 애플리케이션 | 예 | 읽어 올 Essbase 애플리케이션입니다. 선택기에는 연결의 서비스 계정이 볼 수 있는 애플리케이션이 나열되며, 연결에 기본 애플리케이션이 설정되어 있으면 미리 선택됩니다. |
| 큐브(데이터베이스) | 예 | 선택한 애플리케이션 안에서 아웃라인을 읽어 올 큐브입니다. |
| 차원 | 예 | 아웃라인을 읽어 올 Essbase 차원입니다. |

### 대상 PlaidCloud 차원

| 필드 | 필수 | 참고 |
|---|---|---|
| 대상 차원 | 예 | 아웃라인을 로드할 PlaidCloud 차원입니다. |

## 이 단계에서 표현할 수 없는 항목

| 제한 사항 | 의미 |
|---|---|
| 공유 멤버 | 공유 멤버는 두 번째 부모 아래에서 다른 멤버의 데이터를 다시 사용합니다. PlaidCloud 차원 노드의 부모는 정확히 하나이므로, 공유 멤버는 중복으로 로드되거나 조용히 누락되는 대신 이름을 밝히고 거부됩니다. 기본 롤업을 별도의 PlaidCloud 차원으로 읽어 오십시오. 공유 멤버의 두 번째 부모는 여기서 표현할 수 없습니다. |
| 레이블 전용 멤버 | 레이블 전용 멤버는 탐색을 위해 존재하며 자체 데이터를 보유하지 않습니다. 하위 단계에서 비어 있을 것으로 기대하지 않는 일반 멤버로 로드되는 대신 이름을 밝히고 거부됩니다. |
| Dynamic Calc 멤버 | Dynamic Calc 멤버의 값은 Essbase가 즉석에서 계산하며 저장되지 않습니다. 이 단계는 계산된 데이터가 아니라 아웃라인 구조를 읽으므로, Dynamic Calc 멤버는 저장된 멤버처럼 로드되는 대신 이름을 밝히고 거부됩니다. |
| 속성 차원 | 속성 차원은 기본 차원의 멤버를 분류하며, 그 자체로 팩트의 계층이 아닙니다. 속성 차원을 읽는 것은 즉시 거부되므로 대신 기본 차원을 읽으십시오. |
| 표현할 수 없는 통합 연산자 | PlaidCloud 에지에는 통합 플래그(`+`, `-` 또는 `~`)가 있습니다. Essbase의 `+`와 `-` 연산자는 그대로 매핑됩니다. `*`, `/`, `%`는 단순한 롤업 부호로 표현할 수 없으므로, 이를 사용하는 멤버는 잘못된 부호로 로드되는 대신 이름을 밝히고 거부됩니다. |
| 멤버 상한을 초과하는 아웃라인 | 전체 아웃라인 멤버가 **5,000개**를 초과하는 차원 아웃라인은 일부만 로드되지 않고 거부되며, 오류에 확인된 개수와 상한이 모두 표시됩니다. 계층의 더 얕은 수준이나 더 작은 하위 트리를 읽어 한도 이하로 줄이십시오. |

## 관련 항목

- [Oracle Essbase에 연결(가이드)](/ko/guides/connections/essbase/) — 연결을 만듭니다.
- [Oracle Essbase 커넥터](/ko/reference/connectors/erp/oracle-essbase/) — 연결 필드 참조입니다.
- [Essbase: 큐브 쿼리](/ko/reference/workflow-steps/essbase/essbase-query/) — 큐브에 대해 실시간 MDX 쿼리를 클라우드 직접 방식으로 실행합니다.
- [Oracle Essbase 단계](/ko/reference/workflow-steps/essbase/)
