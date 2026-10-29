---
title: Business Central REST 커넥터
description: PlaidCloud에서 Azure AD 클라이언트 자격 증명으로 Microsoft Dynamics 365 Business Central 연결을 설정하여 OData 엔터티를 가져오고 일반 분개장 라인을 전기합니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/business-central.md
---

## API 문서

Business Central의 [표준 OData v2.0 API](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/)에는 이 커넥터가 사용하는 엔터티와 `$filter`/`$orderby` 옵션이 문서화되어 있습니다.

## 인증 방식

이 연결은 Entra ID(Azure AD) **클라이언트 자격 증명(S2S)** 을 사용하여 애플리케이션으로 인증합니다. 앱 등록의 클라이언트 ID와 시크릿을 `https://login.microsoftonline.com/<tenant id>/oauth2/v2.0/token`에서 액세스 토큰으로 교환하며, 범위는 `https://api.businesscentral.dynamics.com/.default`입니다. 대화형 로그인은 없습니다. 앱 등록에는 Business Central에 대한 API 권한(`API.ReadWrite.All` 또는 관리자가 발급하는 더 좁은 범위)이 부여되어야 합니다.

모든 요청은 하나의 **환경**(예: `Production` 또는 샌드박스 환경)과 그 안의 하나의 **회사**로 범위가 지정되며, 둘 다 요청마다 선택하는 것이 아니라 연결에 설정됩니다.

## 구성

| 필드 | 유형 | 설명 |
|---|---|---|
| 이름 | 텍스트 | 이 연결의 표시 이름입니다. |
| 클라이언트 ID | 텍스트 | Entra 앱 등록의 애플리케이션(클라이언트) ID입니다. |
| 클라이언트 시크릿 | 텍스트 | 앱 등록의 클라이언트 시크릿입니다. 암호화되어 저장됩니다. |
| 테넌트 ID | 텍스트 | Azure AD 테넌트 ID입니다. |
| 환경 | 텍스트 | Business Central 환경 이름입니다(예: `Production`). |
| 회사 | 텍스트 | 이 연결이 읽고 전기하는 대상인 Business Central 회사 ID입니다. |

## 가져올 수 있는 엔터티

**Import Business Central Entity** 단계는 `accounts`, `generalLedgerEntries`, `customers`, `vendors`, `items`, `journals`의 엔터티 6개를 지원합니다. 각 가져오기는 엔터티별 서버 측 필터를 지원합니다. 전체 필드 참조는 [Import Business Central Entity 단계](/ko/reference/workflow-steps/business-central/import-business-central-entity/)를 참조하십시오.

`generalLedgerEntries`는 읽기 전용이며 전기된 항목만 포함합니다. 아직 전기되지 않은 분개장 배치에 남아 있는 라인은 포함되지 않으므로, 시산표나 총계정원장 상세를 가져올 때 사용하는 엔터티입니다.

## 일반 분개장 라인 전기

**Business Central Post** 단계는 **기존** 분개장 배치 안에 라인을 만들고 PlaidCloud의 공유 ERP 쓰기 파이프라인을 통해 해당 배치를 전기합니다. 전기하기 전에 배치에 이 요청의 라인만 들어 있는지 확인하고, 분개장 배치 자체가 아니라 `generalLedgerEntries`를 기준으로 전기를 확인합니다. 필드 참조는 [Business Central: Post General Journal Lines 단계](/ko/reference/workflow-steps/business-central/business-central-post/)를, 전체 전기 안내는 [Business Central에 연결](/ko/guides/connections/business-central/)을 참조하십시오.

## 알려진 제한 사항

| 제한 사항 | 의미 |
|---|---|
| 쓰기 문서 유형은 하나뿐 | 일반 분개장 라인 전기만 지원합니다. 초안 문서 흐름(판매/구매 송장, 초안 → 전기됨)은 지원하지 않습니다. 해당 흐름의 전기 작업이 Microsoft의 공개 문서에 명확히 정의되어 있지 않기 때문입니다. |
| 기존 배치에만 전기 | 이 커넥터는 Business Central에서 분개장 배치를 만들지 않으므로, 먼저 그곳에서 만들어야 합니다. |
| 같은 배치에 대한 동시 전기 | 멱등성 보호는 분개장 배치가 아니라 문서 번호 기준으로 적용되므로, 서로 다른 문서 번호가 같은 배치에 동시에 전기될 때 순차 처리가 보장되지 않습니다. |

## 관련 항목

- [Business Central에 연결(가이드)](/ko/guides/connections/business-central/) — 연결을 만들고, 테스트하고, 엔터티를 가져오고, 분개를 전기하는 단계별 안내입니다.
- [Import Business Central Entity 단계](/ko/reference/workflow-steps/business-central/import-business-central-entity/)
- [Business Central: Post General Journal Lines 단계](/ko/reference/workflow-steps/business-central/business-central-post/)
- [ERP 전기 이력 검토](/ko/guides/connections/erp-post-history/)
