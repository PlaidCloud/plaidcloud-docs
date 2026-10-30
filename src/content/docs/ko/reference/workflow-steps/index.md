---
title: 워크플로 단계
description: PlaidCloud의 모든 워크플로 단계 유형입니다. 가져오기, 내보내기, 변환, 배부, 차원, 문서, 알림 등을 다룹니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/index.md
---

워크플로 단계는 PlaidCloud 자동화의 구성 요소입니다. 각 단계는 하나의 작업(CSV 가져오기, 두 테이블 조인, 알림 전송 등)을 수행하며, 단계를 조합하여 순차적으로, 병렬로, 조건에 따라, 또는 반복해서 실행되는 워크플로를 구성합니다.

## 범주

### 데이터 이동

- [가져오기](/ko/reference/workflow-steps/import/) — CSV, Excel, Parquet, JSON, ORC, Delta Lake, SQL, BigQuery, MongoDB, Kafka, SPSS, Singer 소스 등에서 데이터를 가져옵니다
- [내보내기](/ko/reference/workflow-steps/export/) — CSV, XML, SQL, Excel, Google 스프레드시트, Parquet, ORC, MongoDB, Kafka, 테이블 아카이브 등으로 데이터를 내보냅니다

### 테이블 변환

- [테이블](/ko/reference/workflow-steps/tables/) — 조인, 유니온, 필터, 조회, 피벗, 멜트, 대상 지정 업데이트, 소스 테이블에서 행 액세스 권한 부여, 특정 시점으로 복원
- [공통 작업](/ko/reference/workflow-steps/common/) — 공유되는 데이터 매핑 및 필터링 패턴

### 지리 공간

- [지리 공간](/ko/reference/workflow-steps/spatial/) — 공간 파일 가져오기 및 내보내기, 버퍼, 매치, 측정, 다시 투영, 지오메트리 생성. Alteryx 공간 도구를 모두 지원합니다

### 모델링

- [배부](/ko/reference/workflow-steps/allocation/) — 동인 기반 분배, 분할 배부, 규칙 기반 태깅
- [차원](/ko/reference/workflow-steps/dimensions/) — 계층 로드, 정렬, 지우기, 내보내기, 관리
- [최적화](/ko/reference/workflow-steps/optimization/) — 선형 및 혼합 정수 솔버 단계
- [머신러닝](/ko/reference/workflow-steps/machine-learning/) — XGBoost와 KNIME 학습기를 포함한 모델을 학습시키고, 이를 사용해 테이블을 채점합니다

### 문서 및 파일

- [문서](/ko/reference/workflow-steps/document/) — 파일 작업, 디렉터리 목록, 암호화, PDF 조작, 이미지 처리, 인코딩 변환, Excel 셀 업데이트
- [텍스트 및 문서](/ko/reference/workflow-steps/text-documents/) — PDF 텍스트 추출, 이미지 OCR, Blob 읽기 및 쓰기, 감성 분석, 토픽 모델링, 워드 클라우드

### 커뮤니케이션

- [알림](/ko/reference/workflow-steps/notifications/) — 이메일, Slack, Teams, SMS, 웹훅, Twitter, 로그
- [보고서](/ko/reference/workflow-steps/reports/) — RML 템플릿으로 단일 또는 일괄 PDF 보고서를 렌더링합니다

### 워크플로 제어

- [워크플로 제어](/ko/reference/workflow-steps/workflow-control/) — 변수, 루프, 하위 워크플로, 매크로, 오류 처리, 행 수 검증
- [일반](/ko/reference/workflow-steps/general/) — LLM 단계, Pass, 대기, User Defined Transform, Run Remote Python, Alteryx 실행기
- [패키지 매크로](/ko/reference/workflow-steps/macros/) — Alteryx 패키지 매크로에 해당하는 단계: Create Samples, DateTime Now, Heat Map, Pie Wedge Trade Area

### 엔터프라이즈 통합

- [에이전트](/ko/reference/workflow-steps/agent/) — 온프레미스 리소스를 위한 PlaidLink 에이전트 작업
- [NetSuite](/ko/reference/workflow-steps/netsuite/) — 잔액, 총계정원장 상세, 마스터 데이터 또는 직접 작성한 [SuiteQL 쿼리](/ko/reference/workflow-steps/netsuite/import-suiteql-query/)를 가져오고, NetSuite에 분개 전표를 전기합니다
- [Acumatica](/ko/reference/workflow-steps/acumatica/) — 마스터 및 트랜잭션 엔터티를 가져오고, 분개 트랜잭션, 청구서, 매입 청구서, 결제를 전기합니다
- [Business Central](/ko/reference/workflow-steps/business-central/) — OData 엔터티를 가져오고, 일반 분개 라인을 전기합니다
- [Xero](/ko/reference/workflow-steps/xero/) — Accounting API 엔터티를 가져오고, 수동 분개, 청구서, 매입 청구서, 결제, 대변 전표를 전기합니다
- [Dynamics 365 F&O](/ko/reference/workflow-steps/dynamics-365-fo/) — OData/DMF 엔터티를 가져오고, 분개 전표를 전기합니다
- [Oracle Fusion](/ko/reference/workflow-steps/oracle-fusion/) — 총계정원장 잔액과 분개 배치를 가져오고, FBDI를 통해 분개 전표를 전기합니다
- [Oracle EPM (HFM / FCCS)](/ko/reference/workflow-steps/oracle-epm/) — 관점 선택기로 Oracle FCCS에서 임시 데이터 슬라이스를 직접 가져오며, 선택적으로 일정에 따른 반복 로드를 설정할 수 있습니다
- [Oracle Essbase](/ko/reference/workflow-steps/essbase/) — 큐브에 대해 실시간 MDX 쿼리를 실행하거나 차원 아웃라인을 PlaidCloud 차원으로 로드합니다. 클라우드 직접 연결 방식입니다
- [IBM TM1 / Planning Analytics](/ko/reference/workflow-steps/ibm-planning-analytics/) — 저장된 뷰 또는 MDX로 큐브를 읽거나 차원 계층을 읽습니다. 클라우드 직접 연결 또는 온프레미스 에이전트를 통해 사용합니다
- [Anaplan](/ko/reference/workflow-steps/anaplan/) — 저장된 뷰를 읽거나, 기존 내보내기 작업을 실행하거나, 하나 이상의 목록을 PlaidCloud 차원으로 로드합니다. 클라우드 직접 연결 방식이며 읽기 전용입니다
- [Workday Financials](/ko/reference/workflow-steps/workday-financials/) — RaaS 보고서를 가져오고, 회계 분개를 전기합니다
- [Salesforce](/ko/reference/workflow-steps/salesforce/) — 조직에서 읽은 개체 및 필드 목록을 사용해 Bulk API 2.0으로 표준 또는 사용자 지정 CRM 개체를 프로젝트 테이블로 추출합니다
- [Sage Intacct](/ko/reference/workflow-steps/sage-intacct/) — 잔액, 매입 청구서, 임시 쿼리, 총계정원장/차원 개체를 가져오고, 분개 전표를 전기합니다
- [SAP S/4HANA Cloud](/ko/reference/workflow-steps/s4hana-cloud/) — OData를 통해 시산표와 분개 전표 항목을 가져오고, SOAP를 통해 분개 전표를 전기합니다
- [SAP](/ko/reference/workflow-steps/sap/) — SAP ECC / S/4HANA RFC 호출
- [SAP-PCM](/ko/reference/workflow-steps/sap-pcm/) — SAP Profitability and Cost Management 모델 제어
