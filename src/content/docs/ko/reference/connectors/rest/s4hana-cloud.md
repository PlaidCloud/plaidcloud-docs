---
title: SAP S/4HANA Cloud REST 커넥터
description: PlaidCloud에서 SAP S/4HANA Cloud Public Edition 연결을 설정하여 OData로 시산표와 분개 항목 데이터를 가져오고 SOAP로 분개 항목을 전기합니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/s4hana-cloud.md
---

## API 문서

SAP API Business Hub의 SAP S/4HANA Cloud [시산표 API(`API_OPLACCTGDOCITEMCUBE_SRV`)](https://api.sap.com/)와 [분개 항목 - 기본 API(`API_JOURNALENTRYITEMBASIC_SRV`)](https://api.sap.com/)에는 이 커넥터가 사용하는 OData 엔드포인트가 문서화되어 있으며, 통신 약정(Communication Arrangement)을 통해 노출되는 SOAP 분개 항목 대량 생성 서비스도 함께 다룹니다.

## 인증 방식

이 연결은 **OAuth2 클라이언트 자격 증명**을 사용하여 애플리케이션으로 인증합니다. 통신 약정의 클라이언트 ID와 시크릿을 테넌트의 OAuth2 토큰 엔드포인트에서 액세스 토큰으로 교환합니다. 대화형 로그인은 없습니다.

## 구성

| 필드 | 유형 | 설명 |
|---|---|---|
| 이름 | 텍스트 | 이 연결의 표시 이름입니다. |
| 호스트 | 텍스트 | S/4HANA Cloud 테넌트 호스트입니다(예: `https://yourorg.s4hana.ondemand.com`). |
| 토큰 URL | 텍스트 | 통신 약정의 OAuth2 토큰 엔드포인트입니다. |
| 클라이언트 ID | 텍스트 | 통신 약정의 OAuth2 클라이언트 ID입니다. |
| 클라이언트 시크릿 | 텍스트 | 통신 약정의 OAuth2 클라이언트 시크릿입니다. 암호화되어 저장됩니다. |

## 가져올 수 있는 엔터티

**Import S/4HANA Entity** 단계는 두 가지 엔터티를 지원합니다. `trial_balance`(`API_OPLACCTGDOCITEMCUBE_SRV`를 통한 기간 말 총계정원장 계정 잔액 집계)와 `journal_entry_items`(`API_JOURNALENTRYITEMBASIC_SRV`를 통한 전기된 분개 항목 라인)입니다. 둘 다 `CompanyCode`, `GLAccount`, `CostCenter`, `ProfitCenter`, `FiscalYear`, `FiscalPeriod`, `Ledger`에 대한 서버 측 필터를 지원하며, `PostingDate`, `FiscalYear`, `FiscalPeriod`는 `ge`/`le` 범위 경계를 허용합니다. 전체 필드 참조는 [Import S/4HANA Entity 단계](/ko/reference/workflow-steps/s4hana-cloud/import-s4hana-entity/)를 참조하십시오.

## 분개 항목 전기

**S/4HANA: Post Journal Entry** 단계는 PlaidCloud의 공유 ERP 쓰기 파이프라인을 통해 총계정원장 분개 항목을 전기합니다. S/4HANA Cloud의 `JournalEntryBulkCreateRequest_In` SOAP 서비스로 제출하고, `JournalEntryBulkCreateConfirmation_Out` 확인을 폴링하며, 항목이 전기되었다고 보고하기 전에 확인합니다. 수정은 원본을 편집하는 대신 차변/대변을 맞바꾼 새 역분개 항목을 전기합니다. 필드 참조는 [S/4HANA: Post Journal Entry 단계](/ko/reference/workflow-steps/s4hana-cloud/s4hana-post/)를, 전체 전기 안내는 [SAP S/4HANA Cloud에 연결](/ko/guides/connections/s4hana-cloud/)을 참조하십시오.

## 알려진 제한 사항

| 제한 사항 | 의미 |
|---|---|
| 확인 지연 | SOAP 대량 생성 서비스는 요청을 비동기로 처리하므로, 같은 크기의 동기 OData 쓰기보다 훨씬 느립니다. |
| 필터링 가능한 필드는 통신 시나리오에 따라 달라짐 | 통신 시나리오에서 노출하지 않는 비용 객체나 차원은 서버 측에서 필터링할 수 없으므로, 가져온 후 워크플로에서 범위를 지정하십시오. |

## 관련 항목

- [SAP S/4HANA Cloud에 연결(가이드)](/ko/guides/connections/s4hana-cloud/) — 연결을 만들고, 테스트하고, 엔터티를 가져오고, 분개를 전기하는 단계별 안내입니다.
- [Import S/4HANA Entity 단계](/ko/reference/workflow-steps/s4hana-cloud/import-s4hana-entity/)
- [S/4HANA: Post Journal Entry 단계](/ko/reference/workflow-steps/s4hana-cloud/s4hana-post/)
- [ERP 전기 이력 검토](/ko/guides/connections/erp-post-history/)
- [SAP ECC / S/4HANA 커넥터](/ko/reference/connectors/erp/sap-s4/) — 온프레미스 또는 프라이빗 클라우드 S/4HANA를 위한 별도의 RFC/에이전트 기반 커넥터입니다.
