---
title: Workday Financials 커넥터
description: PlaidCloud에서 Integration System User로 Workday Financials 연결을 설정하여 RaaS 보고서로 데이터를 가져오고 SOAP로 분개 전표를 전기합니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/workday-financials.md
---

## API 문서

Workday의 [SOAP 웹 서비스](https://community.workday.com/sites/default/files/file-hosting/productionapi/)와 [Report-as-a-Service(RaaS)](https://doc.workday.com/)는 이 커넥터가 사용하는 인터페이스를 설명합니다.

## 인증 방식

이 연결은 **Integration System User(ISU)** 로 인증합니다. ISU는 시스템 간 통합을 위해 만들어진 Workday 사용자 유형이며, 이 커넥터에 필요한 접근 권한(읽기용 보고서 접근, 전기용 Submit Accounting Journal 비즈니스 프로세스)만 부여하는 Integration System 보안 그룹으로 보호됩니다. 요청에는 ISU의 사용자 이름과 비밀번호가 포함되며, 대화형 로그인은 없습니다.

## 구성

| 필드 | 유형 | 설명 |
|---|---|---|
| Name | 텍스트 | 이 연결의 표시 이름입니다. |
| Tenant Host | 텍스트 | Workday 호스트입니다. 예: `wd5-impl.workday.com`. |
| Tenant Name | 텍스트 | Workday 테넌트 이름입니다. |
| ISU Username | 텍스트 | Integration System User의 사용자 이름입니다. |
| ISU Password | 텍스트 | Integration System User의 비밀번호입니다. 암호화되어 저장됩니다. |

## 데이터 가져오기

Workday Financials에는 미리 정의된 고정 엔터티 집합이 없습니다. 대신 **Import Workday Entity** 단계가 Workday에서 직접 만들고 웹 서비스 접근 권한과 함께 게시한 **Report-as-a-Service(RaaS) 보고서**를 호출하며, 보고서 URL은 사용자가 지정합니다. 이 단계는 `company`, `ledger`, `period`, `accounting_date`(범위), `ledger_account`(범위), `cost_center`에 대한 필터를 지원하며 각 필터는 보고서 매개변수로 전달됩니다. 따라서 보고서에 일치하는 프롬프트가 정의되어 있어야만 필터가 동작합니다. 전체 필드 레퍼런스는 [Import Workday Entity](/ko/reference/workflow-steps/workday-financials/import-workday-entity/) 단계를 참조하십시오.

## 분개 전표 전기

**Workday Financials: Post Journal Entry** 단계는 PlaidCloud의 공유 ERP 쓰기 파이프라인을 통해 회계 분개를 전기합니다. Workday의 `Submit_Accounting_Journal` SOAP 작업을 사용하며, 전기 완료를 보고하기 전에 분개의 비즈니스 프로세스 상태를 최종 상태가 될 때까지 폴링합니다. 정정은 원본을 수정하는 대신 차변/대변을 바꾼 새로운 역분개를 전기합니다. 필드 레퍼런스는 [Workday Financials: Post Journal Entry](/ko/reference/workflow-steps/workday-financials/workday-post/)를, 전체 전기 안내는 [Workday Financials에 연결](/ko/guides/connections/workday-financials/)을 참조하십시오.

## 알려진 제한 사항

| 제한 사항 | 의미 |
|---|---|
| 가져오기 형태는 RaaS 보고서에 따라 달라짐 | PlaidCloud에는 Workday Financials용 사전 정의된 엔터티가 없으며, 보고서의 필드, 프롬프트, 접근 제어는 모두 Workday에 있습니다. Workday에서 보고서를 변경하면 PlaidCloud 쪽 변경 없이도 가져오기 형태가 바뀔 수 있습니다. |
| 비즈니스 프로세스 승인으로 인한 지연 | Submit Accounting Journal 비즈니스 프로세스의 승인 단계를 거치는 분개는 Workday에서 승인될 때까지 `pending` 상태로 유지되며, 최종 상태 폴링은 승인을 기다립니다. |
## 관련 문서

- [Workday Financials에 연결(가이드)](/ko/guides/connections/workday-financials/) — 연결 생성, 테스트, 보고서 가져오기, 분개 전기까지 단계별로 안내합니다.
- [Import Workday Entity](/ko/reference/workflow-steps/workday-financials/import-workday-entity/)
- [Workday Financials: Post Journal Entry](/ko/reference/workflow-steps/workday-financials/workday-post/)
- [ERP 전기 이력 검토](/ko/guides/connections/erp-post-history/)
- [Workday REST 커넥터](/ko/reference/connectors/rest/workday/) — HR/급여 REST 데이터를 위한 별도의 범용 Workday 커넥터입니다.
