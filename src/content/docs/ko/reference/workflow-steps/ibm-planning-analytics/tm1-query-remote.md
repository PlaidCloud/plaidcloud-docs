---
title: "TM1: 큐브 쿼리(에이전트)"
description: "클라우드에서 직접 접근할 수 없는 온프레미스 IBM TM1 / Planning Analytics 서버에서 큐브 슬라이스를 읽습니다. TM1: 큐브 쿼리와 같은 뷰/MDX/관점 쿼리이며, 설치된 PlaidLink 에이전트를 통해 전달됩니다."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote.md
---

## 설명

[TM1: 큐브 쿼리](/ko/reference/workflow-steps/ibm-planning-analytics/tm1-query/)의 온프레미스 대응 단계입니다. TM1 큐브에 대해 저장된 **뷰** 또는 **MDX** 쿼리로, 선택적 관점(POV) 슬라이스와 함께 읽어 프로젝트 테이블로 로드하는 동일한 읽기 작업이지만, 클라우드에서 직접 호출하는 대신 사용자 네트워크에 설치된 [PlaidLink 에이전트](/ko/reference/cli/plaidlink/)를 통해 전달됩니다. TM1 서버가 사용자 네트워크 내부에서만 접근할 수 있는 경우 TM1: 큐브 쿼리 대신 이 단계를 사용하십시오.

이 단계는 단계 메뉴의 **IBM TM1 / Planning Analytics** 아래에 표시됩니다.

## TM1: 큐브 쿼리와의 차이점

| | TM1: 큐브 쿼리 | TM1: 큐브 쿼리(에이전트) |
|---|---|---|
| 전송 방식 | REST를 통한 클라우드 직접 방식 | 사용자 네트워크의 PlaidLink 에이전트로 전달 |
| 구성 필드 | — | 동일하며, 필수 **에이전트**가 추가됨 |
| 큐브/뷰 검색 | 연결된 데이터베이스에서 실시간 | 사용할 수 없음 — 이름을 직접 입력 |
| 저장 전 미리 보기 | 예 | 사용할 수 없음 |

그 밖의 모든 항목, 즉 연결, 데이터베이스, 뷰/MDX 선택, 관점 슬라이스, 0/빈 셀 숨기기, 행 제한, 기간별 증분 추출 패턴은 [TM1: 큐브 쿼리](/ko/reference/workflow-steps/ibm-planning-analytics/tm1-query/) 페이지에 설명된 대로 동작합니다. 아래의 차이점만 이 단계에 해당합니다.

## 구성

### 소스 및 대상

| 필드 | 필수 | 참고 |
|---|---|---|
| 에이전트 | 예 | 이 읽기 작업을 전달할 PlaidLink 에이전트입니다. 에이전트의 빌드에 TM1 핸들러가 포함되어야 합니다(아래 [요구 사항](#요구-사항) 참조). |
| TM1 연결 | 예 | 읽는 데 사용할 [TM1 연결](/ko/guides/connections/tm1/)입니다. 연결 선택기는 선택한 에이전트로 필터링되지 않으므로 연결을 에이전트와 별도로 공유해야 합니다(아래 참조). |
| 환경 | 예 | 연결의 환경입니다. |
| 데이터베이스 | 예 | 쿼리할 TM1 데이터베이스(인스턴스)입니다. |
| 큐브 | 예 | 쿼리할 TM1 큐브입니다. 이 단계에는 실시간 검색이 없으므로 직접 입력합니다. |
| 대상 테이블 | 예 | 반환된 셀셋을 로드할 프로젝트 테이블입니다. |

### 슬라이스 및 옵션

[TM1: 큐브 쿼리](/ko/reference/workflow-steps/ibm-planning-analytics/tm1-query/#슬라이스)와 같은 필드(소스 모드(뷰 기준/MDX 기준), 뷰, MDX, 관점, 0/빈 셀 숨기기, 행 제한)이며, 모두 검색하는 방식이 아니라 직접 입력하고 미리 보기가 아니라 단계가 실행될 때 검증됩니다.

## 에이전트를 통한 검색 없음

TM1: 큐브 쿼리의 큐브, 뷰, 차원 선택기는 단계를 편집하는 동안 연결된 서버를 실시간으로 쿼리합니다. 이 단계에는 그런 실시간 검색이 없습니다. 에이전트는 양식이 브라우저에 열려 있는 동안이 아니라 실행 중에만 접근할 수 있기 때문입니다. 큐브, 뷰, MDX는 직접 입력하며, 인식되지 않는 이름은 조용히 실패하는 대신 명확한 오류와 함께 실행이 실패합니다. 같은 이유로 **미리 보기** 버튼도 없습니다. 미리 보기는 TM1에 접근해야 하는데 이는 에이전트만 할 수 있기 때문입니다.

## 요구 사항

온프레미스 TM1 서버를 읽으려면 다음이 필요합니다.

- TM1 서버에 네트워크로 접근할 수 있는 머신에 **설치된 PlaidLink 에이전트**. [PlaidLink 설치](/ko/reference/cli/plaidlink/install/)를 참조하십시오.
- **TM1 핸들러가 포함된 에이전트 빌드**. PlaidCloud는 전달하기 전에 에이전트가 알리는 기능을 확인하며, 이 기능이 생기기 전의 빌드인 에이전트는 요청을 처리할 수 없습니다. **PlaidLink는 자동으로 업데이트되지 않으므로** TM1 지원을 적용하려면 기존 에이전트를 수동으로 다시 빌드하거나 다시 설치해야 합니다. [PlaidLink 업그레이드](/ko/reference/cli/plaidlink/upgrade/)를 참조하십시오.
- **해당 에이전트와 공유된 TM1 연결**. 이미 부여된 멤버/그룹 액세스에 더해 필요하며, 연결의 `Actions > Agents` 목록에서 부여합니다. [보안 모델](/ko/guides/connections/create-connection/#보안-모델)을 참조하십시오.

## 관련 항목

- [TM1: 큐브 쿼리](/ko/reference/workflow-steps/ibm-planning-analytics/tm1-query/) — 이 단계가 따르는 클라우드 직접 방식의 대응 단계입니다.
- [TM1: 차원 읽기](/ko/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/) — TM1 계층을 PlaidCloud 차원으로 클라우드 직접 방식으로 로드합니다.
- [TM1 연결(가이드)](/ko/guides/connections/tm1/) — 연결을 만듭니다.
- [TM1 커넥터](/ko/reference/connectors/rest/tm1/) — 온프레미스 에이전트 경로를 포함한 연결 필드 참조입니다.
- [PlaidLink](/ko/reference/cli/plaidlink/) — 에이전트 설치 및 업그레이드.
- [IBM TM1 / Planning Analytics 단계](/ko/reference/workflow-steps/ibm-planning-analytics/)
