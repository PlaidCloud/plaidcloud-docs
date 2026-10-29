---
title: TM1 커넥터
description: REST API를 통해 PlaidCloud를 IBM TM1 / Planning Analytics 서버에 연결합니다. 기본 Basic 인증 또는 CAM 네임스페이스 인증을 사용하며, 클라우드에서 직접 연결하거나 클라우드가 직접 접근할 수 없는 서버는 온프레미스 PlaidLink 에이전트를 통해 연결합니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/tm1.md
---

게시된 OData v4 REST API를 통해 PlaidCloud를 IBM **TM1 / Planning Analytics** 서버에 연결합니다. JVM 브리지나 PAOlap 드라이버는 필요하지 않습니다. [TM1: 큐브 쿼리](/ko/reference/workflow-steps/ibm-planning-analytics/tm1-query/)로 큐브 데이터를, [TM1: 차원 읽기](/ko/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/)로 TM1 차원 계층을 읽을 수 있으며, 두 단계 모두 클라우드에서 직접 연결합니다. 사내 네트워크 안에서만 접근할 수 있는 TM1 서버의 경우 [TM1: 큐브 쿼리(에이전트)](/ko/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/)가 설치된 PlaidLink 에이전트를 통해 동일한 읽기를 수행합니다.

연결 선택기에는 이 연결 유형이 **IBM Planning Analytics (TM1)** 로 표시됩니다.

## 인증 방식

TM1의 REST 로그인 방식에 맞춰 두 가지 인증 모드를 제공합니다.

- **Native** — TM1 사용자 이름과 비밀번호를 사용하는 HTTP Basic 인증입니다.
- **CAM** — 네임스페이스 범위의 IBM Cognos Access Manager 싱글 사인온입니다. 요청에는 사용자 이름, 비밀번호, 네임스페이스를 함께 사용해 만든 `Authorization: CAMNamespace` 헤더가 포함되며, 일반 Basic 인증과는 다릅니다.

PlanningAnalytics-as-a-Service(PAaaS) 베어러 토큰 로그인은 아직 지원하지 않으며, 위의 두 REST 로그인 방식만 지원합니다.

## 구성

| 필드 | 필수 | 설명 |
|---|---|---|
| Name | 예 | 이 연결의 표시 이름입니다. |
| Host | 예 | TM1 REST API 호스트입니다. 예: `https://tm1-prod.example.com:8010` 또는 PAaaS URL. |
| 기본 데이터베이스 | 아니요 | TM1: 큐브 쿼리 단계의 Database 필드를 미리 채워 주는 편의 값입니다. 각 단계에서 재정의할 수 있습니다. |
| 인증 모드 | 예 | `Native`(TM1 사용자/비밀번호) 또는 `CAM`(Cognos Access Manager SSO)입니다. 기본값은 Native입니다. |
| Username | 예 | 인증에 사용할 TM1 계정입니다. |
| Password | 예 | 암호화되어 저장됩니다. |
| CAM 네임스페이스 | CAM 사용 시에만 | 인증할 Cognos Access Manager 네임스페이스입니다. Native 모드에서는 사용되지 않습니다. |
| SSL 인증서 확인 | 아니요 | 기본적으로 켜져 있습니다. 테스트 서버에서 알려진 자체 서명 인증서를 사용할 때만 끄십시오. |
| Timeout (seconds) | 아니요 | 기본값은 30입니다. |

## 연결 테스트

**연결 테스트**는 서버의 `Configuration` 싱글턴(`GET {host}/api/v1/Configuration`)을 호출합니다. 이 호출은 TM1이 제공하는 인증된 호출 중 가장 가볍고 데이터베이스나 큐브 컨텍스트가 필요하지 않습니다. 테스트에 성공하면 서버의 **`ProductVersion`** 이 보고되며, 호스트에 접근할 수 있고 자격 증명이 인증된다는 것을 모두 확인할 수 있습니다.

## 읽기 전용

이 커넥터는 읽기 전용입니다. TM1에서 큐브 데이터와 차원 계층을 읽어 오기만 하며, TM1에 쓰기, 전기 또는 TI 프로세스 실행을 하지 않습니다.

## 연결로 할 수 있는 작업

- **저장된 뷰 또는 MDX로 큐브 데이터 읽기.** [TM1: 큐브 쿼리](/ko/reference/workflow-steps/ibm-planning-analytics/tm1-query/) 단계는 이름이 지정된 큐브 뷰 또는 원시 MDX 쿼리를 실행하고, 선택적으로 POV(관점) 슬라이스를 적용한 다음 결과를 테이블로 저장합니다.
- **TM1 계층을 PlaidCloud 차원으로 로드.** [TM1: 차원 읽기](/ko/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/) 단계는 차원의 요소, 부모/자식 관계, 속성을 읽어 PlaidCloud 차원을 만듭니다.
- **기간별 슬라이스로 증분 추출.** TM1에는 기본 제공 변경 추적 기능이 없으므로 새 데이터만 필요한 워크플로는 기간 또는 버전으로 쿼리 범위를 좁힙니다. 패턴은 단계 레퍼런스를 참조하십시오.
- **큐브, 뷰, 차원을 클라우드에서 직접 실시간 검색.** 단계 양식의 Cube, View, Dimension 선택기는 연결된 서버를 직접 쿼리하므로 이름을 무작정 입력하지 않고 실제 이름을 선택할 수 있습니다.
- **온프레미스 에이전트를 통해 클라우드가 접근할 수 없는 TM1 서버 읽기.** 아래의 [방화벽 뒤의 TM1 읽기](#방화벽-뒤의-tm1-읽기)를 참조하십시오.

## 방화벽 뒤의 TM1 읽기

사내 네트워크 안에서만 접근할 수 있는 TM1 서버, 즉 공개 엔드포인트도 허용 목록에 등록된 IP도 없고 PlaidCloud로의 VPN도 없는 서버는 클라우드 직접 연결 대신 설치된 **PlaidLink 에이전트**를 통해 접근합니다. [TM1: 큐브 쿼리(에이전트)](/ko/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) 워크플로 단계는 TM1: 큐브 쿼리와 동일한 뷰/MDX/POV 쿼리를 실행하되, 이를 에이전트로 전달합니다. 에이전트는 사내 네트워크에서 TM1에 접속해 결과를 반환합니다.

이 경로에는 다음이 필요합니다.

- **설치된 PlaidLink 에이전트**: TM1 서버에 네트워크로 접근할 수 있는 머신에 설치되어 있어야 합니다. [PlaidLink 설치](/ko/reference/cli/plaidlink/install/)를 참조하십시오.
- **TM1 핸들러가 포함된 에이전트 빌드**: PlaidCloud는 쿼리를 보내기 전에 에이전트가 알리는 기능을 확인하므로, 이전 에이전트 빌드는 다시 빌드하고 재설치하기 전에는 TM1 요청을 처리할 수 없습니다. PlaidLink는 자동 업데이트되지 않습니다. [PlaidLink 업그레이드](/ko/reference/cli/plaidlink/upgrade/)를 참조하십시오.
- **해당 에이전트와 공유된 이 TM1 연결**: 연결에 이미 부여된 멤버/그룹 접근 권한과 별개로, 연결의 `Actions > Agents` 목록에서 공유해야 합니다. [보안 모델](/ko/guides/connections/create-connection/#보안-모델)을 참조하십시오.

TM1: 큐브 쿼리(에이전트)는 실시간 검색을 지원하지 않습니다. 에이전트는 실행 중에만 접근할 수 있고 단계 양식이 열려 있는 동안에는 접근할 수 없으므로, 큐브, 뷰, MDX는 직접 입력하며 단계를 실행할 때 검증됩니다. TM1: 차원 읽기는 클라우드 직접 연결만 지원하며 아직 온프레미스 경로가 없습니다.

## 알려진 제한 사항

| 제한 사항 | 의미 |
|---|---|
| 읽기 전용 | 쓰기 반영이나 TI 프로세스 실행이 없습니다. |
| 온프레미스 접근은 쿼리 전용 | 온프레미스 PlaidLink 에이전트 경로는 큐브 읽기(TM1: 큐브 쿼리(에이전트))만 지원합니다. TM1: 차원 읽기는 아직 온프레미스 경로가 없으며, PlaidCloud가 직접 접근할 수 있는 네트워크 경로가 필요합니다. |
| 차원 읽기는 단일 계층, 단일 부모만 지원 | 요소가 둘 이상의 부모 아래에 있는 TM1 계층은 PlaidCloud 차원으로 로드할 수 없으며, 통합 가중치의 크기(0.5, 2.0)는 표현할 수 없고 부호만 표현됩니다. [TM1: 차원 읽기](/ko/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/#이-단계에서-표현할-수-없는-항목)를 참조하십시오. |
| PAaaS 베어러 인증 미지원 | Native(Basic) 및 CAM 인증만 지원됩니다. |

## 관련 문서

- [TM1에 연결(가이드)](/ko/guides/connections/tm1/) — 연결을 만들고 쿼리를 작성합니다.
- [TM1: 큐브 쿼리](/ko/reference/workflow-steps/ibm-planning-analytics/tm1-query/) — 클라우드 직접 연결 방식의 큐브 읽기.
- [TM1: 큐브 쿼리(에이전트)](/ko/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) — 온프레미스 에이전트를 통한 큐브 읽기.
- [TM1: 차원 읽기](/ko/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/) — TM1 계층을 PlaidCloud 차원으로 로드합니다.
- [연결 생성 및 관리](/ko/guides/connections/create-connection/)
