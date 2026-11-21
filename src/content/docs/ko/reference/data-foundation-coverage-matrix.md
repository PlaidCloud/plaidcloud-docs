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
| **전체¹** | 시스템에 데이터가 있으면 직접 읽습니다. 데이터가 없는 시스템이 있어도 로드는 중단되지 않습니다. 데이터에 접근할 수 없는 연결은 해당 데이터 세트를 비워 두거나 해당 데이터 세트만 실패시키며, 나머지는 로드됩니다. |
| **파일** | 시스템이 이 데이터 세트를 제공하지 않습니다. 파일로 추가하십시오. |

## SAP, Oracle, Dynamics 365

| 데이터 세트 | SAP S/4HANA | SAP ECC | SAP S/4HANA Cloud | Oracle E-Business Suite | Oracle Fusion | Dynamics 365 Finance and Operations |
| --- | --- | --- | --- | --- | --- | --- |
| 엔터티 | 전체 | 전체 | 전체 | 전체 | 전체 | 전체 |
| 회계 달력 | 전체 | 전체 | 전체 | 전체 | 전체 | 전체 |
| 계정과목표 | 전체 | 전체 | 전체 | 전체 | 전체 | 전체 |
| 부서 | 전체 | 전체 | 전체 | 전체 | 전체 | 전체 |
| 이익 센터 | 전체¹ | 전체¹ | 전체¹ | 전체¹ | 파일 | 전체¹ |
| 사이트 | 전체¹ | 전체¹ | 전체¹ | 전체¹ | 전체¹ | 전체¹ |
| 프로젝트 | 파일 | 파일 | 파일 | 파일 | 파일 | 파일 |
| 영업 담당자 | 파일 | 파일 | 파일 | 파일 | 파일 | 파일 |
| 제품 | 전체 | 전체 | 전체 | 전체¹ | 전체¹ | 전체 |
| 고객 | 전체 | 전체 | 전체 | 전체¹ | 전체¹ | 전체 |
| 공급업체 | 전체¹ | 전체¹ | 전체¹ | 전체¹ | 전체¹ | 전체¹ |
| 총계정원장 | 전체 | 전체 | 전체 | 전체 | 전체 | 전체 |
| 시산표 | 전체 | 전체 | 전체 | 전체 | 전체 | 전체 |
| 월말 잔액 | 파일 | 전체¹ | 파일 | 전체¹ | 전체¹ | 파일 |
| 은행 잔액 | 파일 | 전체¹ | 파일 | 전체¹ | 전체¹ | 전체¹ |
| 판매 라인 | 전체¹ | 전체¹ | 전체¹ | 전체¹ | 전체¹ | 전체¹ |
| 파이프라인 | 파일 | 파일 | 파일 | 파일 | 파일 | 파일 |
| 공급업체 청구서 라인 | 전체¹ | 전체¹ | 전체¹ | 전체¹ | 전체¹ | 전체¹ |
| 구매 주문 | 전체¹ | 전체¹ | 파일 | 전체¹ | 전체¹ | 파일 |
| 미결 항목 | 전체¹ | 전체¹ | 전체¹ | 전체¹ | 전체¹ | 전체¹ |
| 결제 | 전체¹ | 전체¹ | 전체¹ | 전체¹ | 전체¹ | 전체¹ |
| 재고 잔액 | 전체¹ | 전체¹ | 전체¹ | 전체¹ | 전체¹ | 전체¹ |
| 표준 원가 | 전체¹ | 전체¹ | 파일 | 전체¹ | 전체¹ | 파일 |
| 고정 자산 | 전체¹ | 전체¹ | 파일 | 전체¹ | 전체¹ | 파일 |
| 자산 변동 | 전체¹ | 전체¹ | 파일 | 전체¹ | 전체¹ | 파일 |
| 예산 | 전체¹ | 전체¹ | 전체¹ | 전체¹ | 전체¹ | 전체¹ |
| 배부 동인 | 전체¹ | 전체¹ | 파일 | 파일 | 파일 | 파일 |
| 환율 | 전체 | 전체 | 전체 | 전체 | 전체 | 전체 |
| 세그먼트 값 | 파일 | 파일 | 파일 | 파일 | 파일 | 파일 |
| 평가 기준별 CO-PA | 전체¹ | 전체¹ | 파일 | 파일 | 파일 | 파일 |

## 중견 기업 및 클라우드 재무 시스템

| 데이터 세트 | Business Central | Sage 100 | Sage Intacct | QuickBooks Online | Xero | Workday | NetSuite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 엔터티 | 전체 | 전체 | 전체 | 전체 | 전체 | 전체 | 전체 |
| 회계 달력 | 전체 | 전체 | 전체 | 전체 | 전체 | 전체 | 전체 |
| 계정과목표 | 전체 | 전체 | 전체 | 전체 | 전체 | 전체 | 전체 |
| 부서 | 전체 | 전체¹ | 전체 | 파일 | 전체¹ | 전체 | 전체 |
| 이익 센터 | 전체¹ | 파일 | 전체¹ | 전체¹ | 전체¹ | 파일 | 전체¹ |
| 사이트 | 전체¹ | 파일 | 전체¹ | 전체¹ | 전체¹ | 파일 | 전체¹ |
| 프로젝트 | 파일 | 파일 | 전체¹ | 파일 | 파일 | 파일 | 파일 |
| 영업 담당자 | 파일 | 파일 | 파일 | 파일 | 파일 | 파일 | 전체¹ |
| 제품 | 전체 | 파일 | 전체 | 전체¹ | 전체¹ | 전체¹ | 전체 |
| 고객 | 전체 | 파일 | 전체 | 전체¹ | 전체¹ | 전체¹ | 전체 |
| 공급업체 | 전체¹ | 파일 | 전체¹ | 전체¹ | 전체¹ | 전체¹ | 전체¹ |
| 총계정원장 | 전체 | 전체 | 전체 | 전체 | 전체 | 전체 | 전체 |
| 시산표 | 전체 | 전체 | 전체 | 전체 | 전체 | 전체 | 전체 |
| 월말 잔액 | 전체¹ | 파일 | 전체¹ | 전체¹ | 전체¹ | 전체¹ | 파일 |
| 은행 잔액 | 전체¹ | 파일 | 전체¹ | 전체¹ | 전체¹ | 전체¹ | 전체¹ |
| 판매 라인 | 전체¹ | 파일 | 전체¹ | 전체¹ | 전체¹ | 전체¹ | 전체 |
| 파이프라인 | 파일 | 파일 | 파일 | 파일 | 파일 | 파일 | 파일 |
| 공급업체 청구서 라인 | 전체¹ | 파일 | 전체¹ | 전체¹ | 전체¹ | 전체¹ | 전체¹ |
| 미결 항목 | 전체¹ | 파일 | 전체¹ | 전체¹ | 전체¹ | 전체¹ | 전체¹ |
| 결제 | 전체¹ | 파일 | 전체¹ | 전체¹ | 전체¹ | 전체¹ | 전체¹ |
| 구매 주문 | 파일 | 파일 | 파일 | 파일 | 파일 | 파일 | 파일 |
| 재고 잔액 | 전체¹ | 파일 | 파일 | 전체¹ | 파일 | 파일 | 전체¹ |
| 표준 원가 | 파일 | 파일 | 파일 | 파일 | 파일 | 파일 | 파일 |
| 고정 자산 | 파일 | 파일 | 파일 | 파일 | 파일 | 파일 | 파일 |
| 자산 변동 | 파일 | 파일 | 파일 | 파일 | 파일 | 파일 | 파일 |
| 예산 | 전체¹ | 파일 | 전체¹ | 전체¹ | 전체¹ | 전체¹ | 전체¹ |
| 배부 동인 | 전체¹ | 파일 | 전체¹ | 파일 | 파일 | 전체¹ | 전체 |
| 환율 | 전체 | 파일 | 전체 | 전체¹ | 파일 | 전체 | 전체¹ |
| 세그먼트 값 | 파일 | 파일 | 파일 | 파일 | 파일 | 전체¹ | 전체¹ |
| 평가 기준별 CO-PA | 파일 | 파일 | 파일 | 파일 | 파일 | 파일 | 파일 |

## CRM, 통합, 계획 소스

| 데이터 세트 | Salesforce | OneStream | Anaplan |
| --- | --- | --- | --- |
| 엔터티 | 파일 | 파일 | 파일 |
| 회계 달력 | 전체¹ | 파일 | 파일 |
| 계정과목표 | 파일 | 파일 | 파일 |
| 부서 | 파일 | 파일 | 파일 |
| 이익 센터 | 파일 | 파일 | 파일 |
| 프로젝트 | 전체¹ | 파일 | 파일 |
| 영업 담당자 | 전체¹ | 파일 | 파일 |
| 제품 | 전체¹ | 파일 | 파일 |
| 고객 | 전체¹ | 파일 | 파일 |
| 총계정원장 | 파일 | 파일 | 파일 |
| 시산표 | 파일 | 파일 | 파일 |
| 판매 라인 | 파일 | 파일 | 파일 |
| 파이프라인 | 전체¹ | 파일 | 파일 |
| 판매 주문 | 전체¹ | 파일 | 파일 |
| 재고 잔액 | 파일 | 파일 | 파일 |
| 예산 | 파일 | 전체 | 전체 |
| 배부 동인 | 파일 | 전체¹ | 전체¹ |
| 환율 | 파일 | 파일 | 파일 |
| 세그먼트 값 | 파일 | 파일 | 파일 |
| 평가 기준별 CO-PA | 파일 | 파일 | 파일 |

## 시스템별 참고 사항

- **판매 주문, 계약, 이연 수익, 재고 변동**은 Salesforce 주문을 제외하고 어떤 시스템에서도 읽지 않습니다. 파일로 추가하십시오.
- **Salesforce**는 CRM 소스입니다. 고객, 제품, 영업 파이프라인, 영업 담당자(사용자), 프로젝트로서의 캠페인, 회계 월과 주문을 제공하며 원장은 제공하지 않습니다. 주문을 읽으려면 Salesforce에서 Orders가 사용 설정되어 있어야 합니다. Salesforce가 주문 읽기를 거부하면 주문 월만 실패하며, 해당 월은 마지막으로 로드된 내용을 유지합니다.
- **OneStream**은 결과 소스입니다. 예산 데이터 세트를 제공하며, 통합 결과를 가져와 Data Foundation이 그룹 손익계산서를 이에 대해 대사할 수 있게 하고, Budget 또는 Forecast 시나리오를 계획으로 제공합니다. 선택적인 두 번째 어댑터는 계획 인원수와 수량을 배부 동인으로 제공합니다.
- **Anaplan**은 계획 소스입니다. Budget, Forecast 또는 Consolidated 계획에서 예산 데이터 세트를 제공하며, 선택적인 두 번째 내보내기에서 배부 동인을 제공합니다.
- **SAP S/4HANA와 SAP ECC**는 동일한 마스터 데이터, 공급업체, 공급업체 청구서, 구매 주문, 미결 항목, 결제, 고정 자산 대장, 표준 원가를 읽습니다. ECC는 재무 회계 및 관리 회계 라인 항목에서 원장을 읽고, 총계정원장 합계 테이블에서 합계와 월말 잔액을 읽습니다. 이익 센터와 플랜트(사이트)는 시스템에 있을 때 읽습니다. 판매 라인은 청구 문서입니다. 평가 기준별 CO-PA는 지정한 경영 단위(operating concern)의 라인 항목 테이블에서 읽으며, 지정하지 않으면 파일로 추가하십시오.
- **Oracle E-Business Suite**는 각각에 대해 지정한 계정과목표 세그먼트에서 사이트와 이익 센터를 읽습니다.
- **Oracle Fusion**은 각 선택 데이터 세트를 해당 BI Publisher 보고서에서 읽습니다. 고객, 제품, 사이트 또는 공급업체 보고서를 배포하지 않으면 해당 데이터 세트는 경고와 함께 비어 있게 됩니다. 그 밖의 보고서의 데이터 세트는 실패하고 마지막으로 로드된 내용을 유지합니다. 나머지는 모두 로드됩니다.
- **Workday**에는 직접적인 분개 또는 잔액 서비스가 없습니다. Data Foundation이 만들어야 할 보고서를 안내하고 그 보고서를 읽습니다. 세그먼트 값(워크태그), 고객, 제품, 공급업체, 판매 라인, 보조 원장, 은행 잔액, 예산, 동인은 선택 보고서에서 가져오며, 월말 잔액은 기초 잔액 보고서의 기말 잔액에서 가져옵니다.
- **Sage 100**은 PlaidLink 에이전트를 통해 읽으며, 연결 하나당 회사 하나를 읽습니다. 장부를 하나의 통화로 관리하므로 환율을 제공하지 않으며, Data Foundation은 제품, 고객, 판매 라인을 읽지 않습니다. 부서는 계정 마스크에 부서 세그먼트가 있을 때 계정의 부서 세그먼트에서 읽습니다.
- **Xero**는 환율을 제공하지 않습니다. 엔터티가 둘 이상의 통화를 사용하는 경우 파일로 추가하십시오. 부서, 사이트, 이익 센터는 이름이 정확히 Department, Site, Profit centre인 추적 범주의 옵션입니다. Xero는 추적 범주를 두 개까지 허용하므로 조직에는 세 가지 중 최대 두 가지만 있습니다.
- **QuickBooks Online**에는 부서가 없습니다. 위치는 사이트로, 클래스는 이익 센터로 읽습니다. 고객, 제품, 공급업체, 환율, 예산, 재고, 판매, 구매는 회사에 있는 경우에 읽으며, 재고는 회사가 보유 수량을 추적하는 경우에만 읽습니다.
- **NetSuite**는 사용자 지정 세그먼트를 세그먼트 값으로, 클래스를 이익 센터로, 위치를 사이트로 읽습니다. 환율과 재고는 계정에서 제공하는 경우에 읽으며, 예산은 계정이 NetSuite Budgets를 사용하고 역할이 이를 읽을 수 있는 경우에 읽습니다.

## 월말 잔액

Data Foundation은 각 시스템이 매월 말에 직접 보고하는 기말 잔액([수치를 신뢰할 수 있습니까?](/ko/guides/projects/data-foundation-proof/) 참조)을 다음에서 읽습니다.

| 시스템 | 월말 잔액을 읽는 위치 |
| --- | --- |
| SAP ECC | 총계정원장 합계 테이블(`FAGLFLEXT`, 클래식 총계정원장에서는 `GLT0`) |
| Oracle E-Business Suite | `GL_BALANCES`(모든 기간이 있어야 함) |
| Oracle Fusion | 모든 기간을 다루는 PlaidCloudBalances 보고서 |
| Business Central | 매월 말의 시산표 |
| Sage Intacct | 계정 잔액(각 월의 기말 잔액) |
| QuickBooks Online | 매월 말의 Trial Balance 보고서 |
| Xero | 매월 말의 Trial Balance 보고서 |
| Workday | Beginning Balances 보고서의 기말 잔액 |

SAP S/4HANA, SAP S/4HANA Cloud, Dynamics 365 Finance and Operations, NetSuite, Sage 100은 Data Foundation이 읽는 별도의 잔액을 보고하지 않습니다. 이러한 시스템도 평소처럼 로드되고 작동합니다. Business Central이 월말 시산표 제공을 거부하면 해당 월의 잔액은 실패하고 마지막으로 로드된 내용을 유지합니다.

## 분개 상세

금액 외에도 각 총계정원장 라인에는 시스템에 있는 경우 분개 유형, 문서 날짜, 입력한 사람과 입력 시각, 승인자, 역분개 대상 분개, 세금이 담깁니다. 회계 달력에는 각 기간의 상태가 담깁니다.

| 시스템 | 분개 유형 | 문서 날짜 | 입력자 및 입력 시각 | 승인자 | 역분개 | 세금 | 기간 상태 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SAP S/4HANA | 예 | 예 | 예 | 아니요 | 아니요 | 코드 | 예 |
| SAP ECC | 예 | 예 | 예 | 아니요 | 예 | 코드 및 금액 | 예 |
| SAP S/4HANA Cloud | 예 | 예 | 예 | 아니요 | 예 | 아니요 | 아니요 |
| Oracle E-Business Suite | 예 | 예 | 예 | 예 | 예 | 아니요 | 예 |
| Oracle Fusion | 예 | 예 | 예 | 예 | 예 | 아니요 | 예 |
| Dynamics 365 Finance and Operations | 예 | 예 | 예 | 아니요 | 아니요 | 아니요 | 예 |
| Business Central | 예 | 예 | 예 | 아니요 | 예 | 아니요 | 예 |
| Sage 100 | 아니요 | 아니요 | 아니요 | 아니요 | 아니요 | 아니요 | 기간이 끝나면 마감됨 |
| Sage Intacct | 예 | 예 | 예 | 예 | 예 | 아니요 | 예 |
| QuickBooks Online | 예 | 예 | 예 | 아니요 | 아니요 | 아니요 | 장부 마감일 |
| Xero | 예 | 예 | 입력 시각만 | 아니요 | 아니요 | 아니요 | 잠금 날짜 |
| Workday | 예 | 예 | 예 | 예 | 예 | 코드 및 금액 | 예 |
| NetSuite | 예 | 예 | 예 | 아니요 | 아니요 | 아니요 | 예 |

SAP S/4HANA Cloud는 분개를 입력한 사람과 역분개 대상을 Journal Entry 서비스에서, Sage Intacct는 분개 배치에서 읽으며, Oracle E-Business Suite는 승인자를 `GL_JE_BATCHES`에서 읽습니다. 이를 읽을 수 없는 연결에서는 해당 열이 비어 있습니다.

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
  - [Sage 100](/ko/guides/connections/sage-100/)
  - [Sage Intacct](/ko/guides/connections/sage-intacct-access-for-data-foundation/)
  - [QuickBooks Online](/ko/guides/connections/quickbooks-access-for-data-foundation/)
  - [Xero](/ko/guides/connections/xero-access-for-data-foundation/)
  - [Workday](/ko/guides/connections/workday-access-for-data-foundation/)
  - [OneStream](/ko/guides/connections/onestream-for-data-foundation/)
  - [Anaplan](/ko/guides/connections/anaplan/#data-foundation의-소스로서의-anaplan)
