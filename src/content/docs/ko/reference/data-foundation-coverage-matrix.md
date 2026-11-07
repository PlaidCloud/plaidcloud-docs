---
title: Data Foundation 지원 범위 매트릭스
description: Data Foundation이 연결하는 각 시스템이 어떤 Common Finance Model 데이터 세트를 직접 제공하는지, 어떤 데이터 세트를 파일로 추가해야 하는지 보여 줍니다.
sidebar:
  label: Data Foundation 지원 범위
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/data-foundation-coverage-matrix.md
---

Data Foundation은 연결한 모든 ERP 시스템과 인스턴스를 직접 읽어 하나의 Common Finance Model에 통합합니다. 시스템에 없는 데이터는 파일로 채울 수 있으므로 아래의 모든 데이터 세트는 파일로도 제공할 수 있습니다.

## 범례

| 표시 | 의미 |
| --- | --- |
| **전체** | Data Foundation이 시스템에서 데이터 세트를 직접 읽습니다. |
| **전체¹** | 시스템에 데이터가 있으면 직접 읽습니다. 데이터가 없는 시스템이나 데이터에 접근할 수 없는 연결이 있어도 로드는 중단되지 않습니다. |
| **파일** | 시스템이 이 데이터 세트를 제공하지 않습니다. 파일로 추가하십시오. |

## SAP, Oracle, Dynamics 365

| 데이터 세트 | SAP S/4HANA | SAP ECC | SAP S/4HANA Cloud | Oracle E-Business Suite | Oracle Fusion | Dynamics 365 Finance and Operations |
| --- | --- | --- | --- | --- | --- | --- |
| 엔터티 | 전체 | 전체 | 전체 | 전체 | 전체 | 전체 |
| 회계 달력 | 전체 | 전체 | 전체 | 전체 | 전체 | 전체 |
| 계정과목표 | 전체 | 전체 | 전체 | 전체 | 전체 | 전체 |
| 부서 | 전체 | 전체 | 전체 | 전체 | 전체 | 전체 |
| 이익 센터 | 전체¹ | 전체¹ | 파일 | 파일 | 파일 | 파일 |
| 제품 | 전체 | 전체 | 전체 | 전체¹ | 전체¹ | 전체 |
| 고객 | 전체 | 전체 | 전체 | 전체¹ | 전체¹ | 전체 |
| 총계정원장 | 전체 | 전체 | 전체 | 전체 | 전체 | 전체 |
| 시산표 | 전체 | 전체 | 전체 | 전체 | 전체 | 전체 |
| 판매 라인 | 전체¹ | 전체¹ | 전체¹ | 전체¹ | 전체¹ | 전체¹ |
| 파이프라인 | 파일 | 파일 | 파일 | 파일 | 파일 | 파일 |
| 재고 잔액 | 전체¹ | 전체¹ | 전체¹ | 파일 | 파일 | 전체¹ |
| 예산 | 전체¹ | 전체¹ | 전체¹ | 파일 | 파일 | 전체¹ |
| 배부 동인 | 전체¹ | 전체¹ | 파일 | 파일 | 파일 | 파일 |
| 환율 | 전체 | 전체 | 전체 | 전체 | 전체 | 전체 |
| 세그먼트 값 | 파일 | 파일 | 파일 | 파일 | 파일 | 파일 |
| 평가 기준별 CO-PA | 파일 | 파일 | 파일 | 파일 | 파일 | 파일 |

## 중견 기업 및 클라우드 재무 시스템

| 데이터 세트 | Business Central | Sage Intacct | QuickBooks Online | Xero | Workday | NetSuite |
| --- | --- | --- | --- | --- | --- | --- |
| 엔터티 | 전체 | 전체 | 전체 | 전체 | 전체 | 전체 |
| 회계 달력 | 전체 | 전체 | 전체 | 전체 | 전체 | 전체 |
| 계정과목표 | 전체 | 전체 | 전체 | 전체 | 전체 | 전체 |
| 부서 | 전체 | 전체 | 전체¹ | 전체 | 전체 | 전체 |
| 이익 센터 | 파일 | 파일 | 파일 | 파일 | 파일 | 파일 |
| 제품 | 전체 | 전체 | 전체¹ | 전체 | 전체¹ | 전체 |
| 고객 | 전체 | 전체 | 전체¹ | 전체 | 전체¹ | 전체 |
| 총계정원장 | 전체 | 전체 | 전체 | 전체 | 전체 | 전체 |
| 시산표 | 전체 | 전체 | 전체 | 전체 | 전체 | 전체 |
| 판매 라인 | 전체¹ | 전체¹ | 전체¹ | 전체¹ | 전체¹ | 전체 |
| 파이프라인 | 파일 | 파일 | 파일 | 파일 | 파일 | 파일 |
| 재고 잔액 | 파일 | 파일 | 전체¹ | 파일 | 파일 | 전체¹ |
| 예산 | 전체¹ | 전체¹ | 전체¹ | 전체¹ | 파일 | 전체¹ |
| 배부 동인 | 전체¹ | 전체¹ | 파일 | 파일 | 전체¹ | 전체 |
| 환율 | 전체 | 전체 | 전체¹ | 파일 | 전체 | 전체¹ |
| 세그먼트 값 | 파일 | 파일 | 파일 | 파일 | 전체¹ | 전체 |
| 평가 기준별 CO-PA | 파일 | 파일 | 파일 | 파일 | 파일 | 파일 |

## CRM, 통합, 계획 소스

| 데이터 세트 | Salesforce | OneStream | Anaplan |
| --- | --- | --- | --- |
| 엔터티 | 파일 | 파일 | 파일 |
| 회계 달력 | 파일 | 파일 | 파일 |
| 계정과목표 | 파일 | 파일 | 파일 |
| 부서 | 파일 | 파일 | 파일 |
| 이익 센터 | 파일 | 파일 | 파일 |
| 제품 | 전체¹ | 파일 | 파일 |
| 고객 | 전체¹ | 파일 | 파일 |
| 총계정원장 | 파일 | 파일 | 파일 |
| 시산표 | 파일 | 파일 | 파일 |
| 판매 라인 | 파일 | 파일 | 파일 |
| 파이프라인 | 전체¹ | 파일 | 파일 |
| 재고 잔액 | 파일 | 파일 | 파일 |
| 예산 | 파일 | 전체 | 전체 |
| 배부 동인 | 파일 | 파일 | 파일 |
| 환율 | 파일 | 파일 | 파일 |
| 세그먼트 값 | 파일 | 파일 | 파일 |
| 평가 기준별 CO-PA | 파일 | 파일 | 파일 |

## 시스템별 참고 사항

- **Salesforce**는 CRM 소스입니다. 고객, 제품, 영업 파이프라인을 제공하며 원장은 제공하지 않습니다.
- **OneStream**은 결과 소스입니다. 예산 데이터 세트만 제공하며, 통합 결과를 가져와 Data Foundation이 그룹 손익계산서를 이에 대해 대사할 수 있게 합니다.
- **Anaplan**은 계획 소스입니다. Budget, Forecast 또는 Consolidated 계획에서 예산 데이터 세트만 제공합니다.
- **SAP S/4HANA와 SAP ECC**는 동일한 마스터 데이터를 읽습니다. ECC는 재무 회계 및 관리 회계 라인 항목에서 원장을 읽고, 총계정원장 합계 테이블에서 합계를 읽습니다. 이익 센터는 시스템에 있을 때 읽습니다. 판매 라인은 CO-PA가 아니라 청구 문서입니다.
- **평가 기준별 CO-PA**는 어떤 시스템에서도 직접 읽지 않습니다. 파일로 추가하십시오.
- **Workday**에는 직접적인 분개 또는 잔액 서비스가 없습니다. Data Foundation이 만들어야 할 보고서를 안내하고 그 보고서를 읽습니다. 세그먼트 값(워크태그), 고객, 제품, 판매 라인, 헤드카운트 동인은 선택 보고서에서 가져옵니다. 예산은 파일로 유지됩니다.
- **Xero**는 환율을 제공하지 않습니다. 엔터티가 둘 이상의 통화를 사용하는 경우 파일로 추가하십시오.
- **QuickBooks Online**은 회사 파일에 있는 경우 부서, 고객, 제품, 환율, 예산, 재고, 판매 라인을 읽습니다.
- **NetSuite**는 사용자 지정 세그먼트를 세그먼트 값으로 읽습니다. 환율과 재고는 계정에서 제공하는 경우에 읽으며, 예산은 계정이 NetSuite Budgets를 사용하고 역할이 이를 읽을 수 있는 경우에 읽습니다.

## 관련 항목

- [Data Foundation](/ko/guides/projects/data-foundation/)
- [Data Foundation 시작하기](/ko/guides/projects/data-foundation-getting-started/)
- [ERP 외부 데이터용 파일 추가](/ko/guides/projects/data-foundation/#erp-외부-데이터용-파일-추가)
- 연결 접근 가이드:
  - [NetSuite](/ko/guides/connections/netsuite-access-for-data-foundation/)
  - [Salesforce](/ko/guides/connections/salesforce-access-for-data-foundation/)
  - [SAP S/4HANA](/ko/guides/connections/sap-s4hana-access-for-data-foundation/)
  - [SAP ECC](/ko/guides/connections/sap-ecc-access-for-data-foundation/)
  - [SAP S/4HANA Cloud](/ko/guides/connections/s4hana-cloud-access-for-data-foundation/)
  - [Oracle E-Business Suite](/ko/guides/connections/oracle-ebs-access-for-data-foundation/)
  - [Oracle Fusion](/ko/guides/connections/oracle-fusion-access-for-data-foundation/)
  - [Dynamics 365 Finance and Operations](/ko/guides/connections/dynamics-365-fo-access-for-data-foundation/)
  - [Business Central](/ko/guides/connections/business-central-access-for-data-foundation/)
  - [Sage Intacct](/ko/guides/connections/sage-intacct-access-for-data-foundation/)
  - [QuickBooks Online](/ko/guides/connections/quickbooks-access-for-data-foundation/)
  - [Xero](/ko/guides/connections/xero-access-for-data-foundation/)
  - [Workday](/ko/guides/connections/workday-access-for-data-foundation/)
  - [OneStream](/ko/guides/connections/onestream-for-data-foundation/)
  - [Anaplan](/ko/guides/connections/anaplan/#data-foundation의-소스로서의-anaplan)
