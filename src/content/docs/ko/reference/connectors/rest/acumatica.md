---
title: Acumatica REST 커넥터
description: PlaidCloud에서 Acumatica 계약 기반 REST API 연결을 설정하여 마스터 및 트랜잭션 데이터를 가져오고 분개 트랜잭션, 송장, 청구서, 결제를 전기합니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/acumatica.md
---

## API 문서

Acumatica의 [계약 기반 REST API](https://help.acumatica.com/Help?ScreenId=ShowWiki&pageid=e0dea52d-0339-4f34-a6c0-9615ce6a25c2)에는 이 커넥터가 사용하는 엔드포인트와 쿼리 옵션이 문서화되어 있습니다.

## 인증 방식

이 연결은 **세션 기반**입니다. PlaidCloud는 제한된 작업 단위마다 한 번 로그인(사용자 이름, 비밀번호, 회사, 선택적 브랜치와 함께 `POST <instance>/entity/auth/login`)하고, 그 단위의 모든 호출에서 결과로 받은 세션 쿠키를 재사용하며, 작업이 끝나면 로그아웃합니다. 이는 베어러 토큰 또는 OAuth 흐름이 아닙니다. 세션은 Acumatica 라이선스의 동시 세션 한도에 포함되며, 체험판 및 하위 티어 인스턴스는 이 한도가 2까지 낮을 수 있으므로 하나의 연결에서 많은 Acumatica 단계를 병렬로 실행하지 마십시오.

## 구성

| 필드 | 유형 | 설명 |
|---|---|---|
| 이름 | 텍스트 | 이 연결의 표시 이름입니다. |
| 인스턴스 기본 URL | 텍스트 | Acumatica 인스턴스 URL입니다(예: `https://yourcompany.acumatica.com`). |
| 엔드포인트 이름 | 텍스트 | 계약 엔드포인트 이름입니다. 사용자 지정 엔드포인트를 게시하지 않았다면 `Default`입니다. |
| 엔드포인트 버전 | 텍스트 | 선택 사항이며 예는 `25.200.001`입니다. 비워 두면 엔드포인트의 최신 게시 버전을 사용합니다. |
| 회사/테넌트 | 텍스트 | 이 연결이 로그인하는 정확한 Acumatica 회사 ID입니다. |
| 브랜치 | 텍스트 | 선택 사항입니다. 비워 두면 로그인 사용자의 기본 브랜치를 사용합니다. |
| 사용자 이름 | 텍스트 | PlaidCloud API 사용자의 로그인 이름입니다. |
| 비밀번호 | 텍스트 | PlaidCloud API 사용자의 비밀번호입니다. 암호화되어 저장됩니다. |

## 가져올 수 있는 엔터티

**Import Acumatica Entity** 단계는 계약 기반 엔터티 18개를 지원합니다.

**마스터 및 참조 데이터** — `account`, `subaccount`, `ledger`, `financial_period`, `branch`, `currency`, `currency_rate`, `customer`, `vendor`, `stock_item`, `warehouse`, `employee`, `tax_category`, `project`

**트랜잭션 데이터** — `sales_invoice`, `bill`, `sales_order`, `shipment`

각 가져오기는 `Active Only` 토글, `Updated After` 기준 시점, 엔터티별 서버 측 필터를 지원합니다. 전체 필드 참조는 [Import Acumatica Entity 단계](/ko/reference/workflow-steps/acumatica/import-acumatica-entity/)를 참조하십시오.

## 문서 전기

**Acumatica Post** 단계는 PlaidCloud의 공유 ERP 쓰기 파이프라인을 통해 **JournalTransaction**, **SalesInvoice**, **Bill**, **Payment** 문서를 전기합니다. 보류 상태로 생성하고, 릴리스(비동기 작업)한 다음, 문서가 전기되었다고 보고하기 전에 릴리스를 확인합니다. 필드 참조는 [Acumatica: Post Documents 단계](/ko/reference/workflow-steps/acumatica/acumatica-post/)를, 전체 전기 안내는 [Acumatica에 연결](/ko/guides/connections/acumatica/)을 참조하십시오.

## 알려진 제한 사항

| 제한 사항 | 의미 |
|---|---|
| GI에 의존하는 읽기는 지원하지 않음 | 시산표, 총계정원장 트랜잭션 상세, 재고 현황, 예산, 회사 간 데이터는 위의 계약 기반 엔터티 18개가 아니라 Acumatica 일반 조회(Generic Inquiry, GI) 뒤에 있습니다. Acumatica에서 GI를 만들고 [범용 REST 연결](/ko/reference/connectors/rest/generic-rest/)로 가져오십시오. |
| 쓰기에 기본 멱등성 키 없음 | Acumatica의 PUT 기반 쓰기 API에는 멱등성 필드가 없으며, 이중 전기를 막는 유일한 장치는 PlaidCloud 자체의 원장 선점입니다. |
| 되돌리기는 수동 | 문서 유형 중 문서화된 무효화/되돌리기 작업이 있는 유형은 없습니다. 전기된 문서는 PlaidCloud에서 되돌릴 수 없으므로 Acumatica에서 직접 수정하십시오. |
| 결제 상관 필드 없음 | Acumatica에는 결과가 모호한 경우 결제를 PlaidCloud의 요청과 연결해 주는 문서화된 필드가 없으며, 상태가 불확실한 결제는 수동 해결을 위해 격리됩니다. |
| 라인 항목 필터링은 서버 측이 아님 | `$filter` 방식의 필터는 엔터티 및 헤더 필드에만 적용되며 문서의 라인 항목 차원(예: 라인 수준 비용 센터)에는 적용되지 않습니다. 가져온 후 워크플로에서 라인의 범위를 지정하십시오. |

## 관련 항목

- [Acumatica에 연결(가이드)](/ko/guides/connections/acumatica/) — 연결을 만들고, 테스트하고, 엔터티를 가져오고, 배치를 전기하는 단계별 안내입니다.
- [Import Acumatica Entity 단계](/ko/reference/workflow-steps/acumatica/import-acumatica-entity/)
- [Acumatica: Post Documents 단계](/ko/reference/workflow-steps/acumatica/acumatica-post/)
- [ERP 전기 이력 검토](/ko/guides/connections/erp-post-history/)
