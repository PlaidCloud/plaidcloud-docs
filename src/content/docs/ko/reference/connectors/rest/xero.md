---
title: Xero REST 커넥터
description: 원클릭 OAuth 승인으로 PlaidCloud에서 Xero 연결을 설정하고, Accounting API 엔터티를 가져오며, 수동 분개, 송장, 청구서, 결제, 대변 전표를 전기합니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/xero.md
---

## API 문서

Xero의 [Accounting API 레퍼런스](https://developer.xero.com/documentation/api/accounting/overview)에 이 커넥터가 사용하는 엔터티, `where=` 필터, 생성 페이로드가 설명되어 있습니다.

## 인증 방식

이 연결은 Xero의 **OAuth 2.0** 승인으로 인증합니다. PlaidCloud가 OAuth 앱을 직접 등록하므로 클라이언트 ID나 클라이언트 시크릿을 얻거나 입력할 필요가 없습니다. **Xero에 연결**을 클릭하고 Xero에 로그인한 다음 승인하면 됩니다. PlaidCloud는 발급된 토큰을 연결에 저장하고 자동으로 갱신하며, 갱신 토큰이 교체될 때마다 저장하므로 오랫동안 사용하지 않은 연결도 계속 동작합니다.

하나의 승인은 승인한 모든 Xero 조직에 적용됩니다. 연결은 그중 정확히 하나를 대상으로 합니다. **조직** 선택기에는 승인으로 반환된 조직이 나열되며, 모든 요청에는 해당 조직의 테넌트 ID가 포함됩니다. 두 번째 조직에서 읽거나 전기하려면 Xero 연결을 하나 더 만들고 그 연결에서 해당 조직을 선택하십시오.

Xero의 Demo Company는 연결 설정이 아니라 조직의 속성입니다. 데모 조직도 다른 조직과 마찬가지로 **조직** 목록에 나타나므로, 샌드박스 연결이란 데모 조직을 가리키는 연결을 말합니다.

## 구성

| 필드 | 유형 | 설명 |
|---|---|---|
| Name | 텍스트 | 이 연결의 표시 이름입니다. |
| Xero에 연결 | 버튼 | Xero 로그인 및 동의 흐름을 시작합니다. |
| 연결 상태 | 상태 | 승인이 완료될 때까지는 `Not connected`로 표시되고, 완료된 후에는 승인이 포함하는 조직의 수를 보고합니다. |
| 조직 | 선택 | 이 연결이 읽고 전기할 Xero 조직입니다. 승인 결과로 채워집니다. |

## 속도 제한

Xero는 조직마다 분당 60회, 일일 5,000회 호출로 제한하고 동시 호출은 최대 5건으로 제한합니다. PlaidCloud는 분당 제한과 동시성 제한을 연결별로 관리하므로 한 조직이 제한되어도 다른 연결의 호출이 멈추지 않으며, 제한 응답에 대해서는 Xero의 `Retry-After`를 따릅니다. 일일 한도는 직접 관리해야 하므로, 여러 건을 한꺼번에 실행하기보다 대량 가져오기를 일정에 맞춰 분산하십시오.

## 가져올 수 있는 엔터티

**Xero: 엔터티 가져오기** 단계는 Accounting API 엔터티 11개를 지원합니다. `accounts`, `contacts`, `invoices`, `credit_notes`, `payments`, `manual_journals`, `bank_transactions`, `items`, `tracking_categories`, `tax_rates`, `currencies`입니다. 각 가져오기에는 선택적으로 상태 제한, 날짜 범위, 수정 시점 기준 시작 시각을 지정할 수 있습니다. 전체 필드 레퍼런스는 [Xero: 엔터티 가져오기](/ko/reference/workflow-steps/xero/import-xero-entity/)를 참조하십시오.

## 문서 전기

**Xero: 문서 전기** 단계는 헤더 테이블과 라인 테이블로부터 수동 분개, 송장, 청구서, 결제, 대변 전표를 PlaidCloud의 공유 ERP 쓰기 파이프라인을 통해 전기합니다. 필드 레퍼런스는 [Xero: 문서 전기](/ko/reference/workflow-steps/xero/xero-post/)를, 전체 전기 안내는 [Xero에 연결](/ko/guides/connections/xero/)을 참조하십시오.

## 알려진 제한 사항

| 제한 사항 | 의미 |
|---|---|
| 수동 분개와 결제는 결과가 불분명할 때 조회할 수 없음 | 송장, 청구서, 대변 전표에는 PlaidCloud가 부여하고 다시 조회할 수 있는 문서 번호가 있습니다. 수동 분개의 설명과 결제의 참조는 조회할 수 없으므로, 둘 중 하나의 쓰기 결과가 불확실하면 추측하지 않고 격리하여 Xero에서 직접 확인하도록 남겨 둡니다. |
| 되돌리기는 수동 분개와 송장만 지원 | 수동 분개는 차변/대변을 바꾼 분개로, 송장은 이를 상쇄하는 대변 전표로 되돌립니다. 청구서, 결제, 대변 전표에는 문서화된 취소 페이로드가 없으므로 PlaidCloud는 임의로 만들지 않고 되돌리기를 거부합니다. |
| 필터는 고정 필드이며 쿼리 언어가 아님 | Xero의 쿼리 API는 엔터티별로 상태 제한과 날짜 범위만 제공하고 자유로운 필터 언어를 제공하지 않으므로, 가져오기 단계는 필드/연산자/값 테이블 대신 이러한 필드를 제공합니다. |
| 연결당 조직 하나 | 모든 요청에는 테넌트 ID 하나가 포함됩니다. 두 번째 조직에는 두 번째 연결이 필요합니다. |

## 관련 문서

- [Xero에 연결(가이드)](/ko/guides/connections/xero/) — 연결 생성, 테스트, 엔터티 가져오기, 문서 전기까지 단계별로 안내합니다.
- [Xero: 엔터티 가져오기](/ko/reference/workflow-steps/xero/import-xero-entity/)
- [Xero: 문서 전기](/ko/reference/workflow-steps/xero/xero-post/)
- [ERP 전기 이력 검토](/ko/guides/connections/erp-post-history/)
