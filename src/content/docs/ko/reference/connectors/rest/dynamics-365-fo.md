---
title: Dynamics 365 Finance & Operations REST 커넥터
description: PlaidCloud에서 Dynamics 365 Finance & Operations 연결을 설정하여 OData/DMF 엔터티를 가져오고 분개 항목을 비동기로 전기합니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/dynamics-365-fo.md
---

## API 문서

D365 F&O의 [OData v4 엔드포인트](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/odata)와 [데이터 관리 프레임워크](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/data-management-import-export)에는 이 커넥터가 사용하는 엔드포인트와 대량 추출 경로가 문서화되어 있습니다.

## 인증 방식

이 연결은 Entra ID(Azure AD) **클라이언트 자격 증명**을 사용하여 애플리케이션으로 인증합니다. 앱 등록의 클라이언트 ID와 시크릿을 환경의 리소스 범위로 액세스 토큰으로 교환합니다. 대화형 로그인은 없습니다.

## 구성

| 필드 | 유형 | 설명 |
|---|---|---|
| 이름 | 텍스트 | 이 연결의 표시 이름입니다. |
| 환경 URL | 텍스트 | D365 F&O 환경 URL입니다(예: `https://yourorg.operations.dynamics.com`). |
| 클라이언트 ID | 텍스트 | Entra 앱 등록의 애플리케이션(클라이언트) ID입니다. |
| 클라이언트 시크릿 | 텍스트 | 앱 등록의 클라이언트 시크릿입니다. 암호화되어 저장됩니다. |
| 테넌트 ID | 텍스트 | Azure AD 테넌트 ID입니다. |
| 리소스/범위 | 텍스트 | 요청하는 OAuth2 범위이며, 일반적으로 환경 URL에 `/.default`를 붙인 값입니다. |

## 가져올 수 있는 엔터티

**Import D365 F&O Entity** 단계는 `main_accounts`, `currencies`, `customers`, `vendors`, `released_products`, `ledger_journal_headers`의 엔터티 6개를 지원합니다. 각 가져오기는 `odata` 동기 모드(일반적인 가져오기를 위한 직접 호출) 또는 `dmf` 대량 모드(대규모 추출을 위한 비동기 데이터 관리 프레임워크 내보내기 작업)로 실행되며, 날짜, 계정, 차원 범위를 포함한 엔터티별 서버 측 필터를 지원합니다. 전체 필드 참조는 [Import D365 F&O Entity 단계](/ko/reference/workflow-steps/dynamics-365-fo/import-d365fo-entity/)를 참조하십시오.

## 분개 항목 전기

**D365 F&O: Post Journal Entry** 단계는 PlaidCloud의 공유 ERP 쓰기 파이프라인을 통해 총계정원장 분개 항목을 전기합니다. D365 F&O의 비동기 사용자 지정 서비스 분개 전기 작업에 제출하고, 최종 상태가 될 때까지 폴링하며, 항목이 전기되었다고 보고하기 전에 확인합니다. 수정은 원본을 편집하는 대신 차변/대변을 맞바꾼 새 역분개 항목을 전기합니다. 필드 참조는 [D365 F&O: Post Journal Entry 단계](/ko/reference/workflow-steps/dynamics-365-fo/dynamics-365-fo-post/)를, 전체 전기 안내는 [Dynamics 365 Finance & Operations에 연결](/ko/guides/connections/dynamics-365-fo/)을 참조하십시오.

## 알려진 제한 사항

| 제한 사항 | 의미 |
|---|---|
| DMF 동기 모드는 추출 지연이 있음 | `dmf` 가져오기는 비동기 내보내기 작업을 기다리므로, 같은 크기의 `odata` 가져오기보다 훨씬 느립니다. |
| 차원 필터링은 구조에 따라 달라짐 | 계정 구조에 포함되지 않은 재무 차원은 서버 측에서 필터링할 수 없으므로, 가져온 후 워크플로에서 범위를 지정하십시오. |

## 관련 항목

- [Dynamics 365 Finance & Operations에 연결(가이드)](/ko/guides/connections/dynamics-365-fo/) — 연결을 만들고, 테스트하고, 엔터티를 가져오고, 분개를 전기하는 단계별 안내입니다.
- [Import D365 F&O Entity 단계](/ko/reference/workflow-steps/dynamics-365-fo/import-d365fo-entity/)
- [D365 F&O: Post Journal Entry 단계](/ko/reference/workflow-steps/dynamics-365-fo/dynamics-365-fo-post/)
- [ERP 전기 이력 검토](/ko/guides/connections/erp-post-history/)
