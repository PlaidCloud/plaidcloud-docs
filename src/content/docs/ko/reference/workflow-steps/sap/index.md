---
title: SAP 단계
description: 재무, 마스터 데이터, 문서 작업을 위해 SAP ECC / S/4HANA RFC(Remote Function Call)를 호출하는 워크플로 단계입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/index.md
---

재무, 마스터 데이터, 문서 작업을 위해 SAP ECC / S/4HANA RFC(Remote Function Call)를 호출하는 워크플로 단계입니다.

## 단계

- [Call SAP Financial Document Attachment 단계](/ko/reference/workflow-steps/sap/call-sap-financial-document-attachment/)
- [Call SAP General Ledger Posting 단계](/ko/reference/workflow-steps/sap/call-sap-general-ledger-posting/)
- [Call SAP Master Data Table RFC 단계](/ko/reference/workflow-steps/sap/call-sap-master-data-table-rfc/)
- [Call SAP RFC 단계](/ko/reference/workflow-steps/sap/call-sap-rfc/)

## 임시 추출 단계

세 가지 단계가 SAP를 검색하고, 추출을 미리 보고 계획한 다음, 결과를 테이블에 저장합니다. 하나는 테이블을 읽고, 하나는 트랜잭션 또는 보고서를 실행하며, 하나는 저장된 SAP Query를 실행합니다. [SAP ECC / S/4HANA 임시 추출](/ko/guides/connections/sap-adhoc-extract/)을 참조하십시오.
