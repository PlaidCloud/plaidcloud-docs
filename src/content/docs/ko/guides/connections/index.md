---
title: 연결
description: 워크플로가 외부 데이터베이스, 클라우드 스토리지, ERP, REST API에 접근할 수 있게 하는 저장된 구성인 PlaidCloud 연결을 설정하고 관리합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/connections/index.md
---

**연결**은 PlaidCloud가 데이터베이스, 클라우드 스토리지 계정, ERP, REST API와 같은 외부 시스템에 접근할 수 있게 하는 저장된 구성입니다. 해당 시스템에서 읽거나 쓰는 워크플로 단계가 연결을 참조하므로, 자격 증명과 엔드포인트 세부 정보를 한곳에서 관리합니다.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 210" role="img" aria-label="여러 워크플로 단계가 하나의 저장된 연결을 참조하며, 이 연결은 자격 증명과 엔드포인트를 한곳에 보관하고 데이터베이스, 클라우드 스토리지, ERP 또는 REST API와 같은 외부 시스템에 접근합니다." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="cn-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="76" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-gray-3)">워크플로 단계</text>
  <rect x="16" y="40" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="61" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">가져오기 단계</text>
  <rect x="16" y="88" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="109" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">내보내기 단계</text>
  <rect x="16" y="136" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="157" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">조회 단계</text>
  <path d="M136 57 C190 57 210 96 248 100" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <path d="M136 105 L248 108" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <path d="M136 153 C190 153 210 118 248 114" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <rect x="250" y="76" width="180" height="66" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="340" y="104" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">연결</text>
  <text x="340" y="122" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">자격 증명 + 엔드포인트, 한 번만</text>
  <path d="M430 109 L512 109" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#cn-arrow)" />
  <rect x="514" y="80" width="150" height="58" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="589" y="104" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">외부 시스템</text>
  <text x="589" y="122" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">DB · 스토리지 · ERP · REST</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">연결을 한 번 구성하면 외부 시스템을 읽거나 쓰는 모든 단계가 이를 가리키므로, 자격 증명과 엔드포인트 세부 정보가 단계마다 중복되지 않습니다.</figcaption>
</figure>

## 가이드

- [연결 만들기 및 관리](/ko/guides/connections/create-connection/) — 연결을 만들고, 편집하고, 테스트하고, 액세스를 제어하며, 환경별로 구성합니다.
- [자체 웨어하우스 사용](/ko/guides/connections/external-lakehouse/) — 자체 Snowflake 또는 Databricks 웨어하우스를 직접 연결하고, 자신의 ID로 로그인하고, 여러 웨어하우스를 관리하며, 실행별 비용을 확인합니다.
- [PlaidCloud Git 연결](/ko/guides/connections/plaidcloud-git/) — 서버 URL이나 자격 증명 없이 워크스페이스의 자체 관리형 Git 서버에 연결하고, 여기에서 Panel 앱 빌드를 자동화합니다.
- [연결 복제](/ko/guides/connections/clone-connection/) — 새 환경이나 테넌트를 위해 기존 연결을 복제합니다.
- [Data Foundation: Common Finance Model](/ko/guides/projects/data-foundation/) — Common Finance Model은 여러 ERP 시스템과 인스턴스의 ERP 데이터를 하나의 계정과목표, 하나의 엔터티 집합, 하나의 보고 통화를 가진 단일 모델로 통합하며, 보고서, 지표, AI 어시스턴트가 이를 모두 읽습니다.
- [Singer 소스](/ko/guides/connections/singer-sources/) — Singer 탭으로 Stripe, GitHub, Slack, BigQuery 같은 소스에 연결한 다음 해당 데이터를 프로젝트 테이블로 가져옵니다.
- [NetSuite에 연결](/ko/guides/connections/netsuite/) — NetSuite 연결을 설정하고 SuiteQL로 재무 및 운영 데이터를 가져옵니다.
- [Data Foundation용 NetSuite 액세스](/ko/guides/connections/netsuite-access-for-data-foundation/) — Data Foundation이 NetSuite를 직접 읽을 수 있도록 NetSuite 관리자가 설정하는 항목과 회신할 내용입니다.
- [NetSuite 재무 데이터 가져오기](/ko/guides/connections/import-netsuite-financials/) — SuiteQL을 작성하지 않고 기본 제공 NetSuite 가져오기 단계로 잔액, 총계정원장 상세, 마스터 데이터를 가져옵니다.
- [NetSuite 분개 전표 전기](/ko/guides/connections/post-netsuite-journal-entries/) — 헤더 및 라인 테이블을 매핑하고, 미리 보고, 분개 항목을 NetSuite에 전기합니다.
- [Acumatica에 연결](/ko/guides/connections/acumatica/) — Acumatica 연결을 설정하고, 엔터티를 가져오고, 분개 거래, 송장, 청구서, 결제를 전기합니다.
- [Business Central에 연결](/ko/guides/connections/business-central/) — Azure AD로 Business Central 연결을 설정하고, OData 엔터티를 가져오고, 일반 분개 라인을 전기합니다.
- [Dynamics 365 Finance & Operations에 연결](/ko/guides/connections/dynamics-365-fo/) — Azure AD로 D365 F&O 연결을 설정하고, OData/DMF 엔터티를 가져오고, 분개 항목을 전기합니다.
- [Oracle Fusion에 연결](/ko/guides/connections/oracle-fusion/) — Oracle Fusion 연결을 설정하고, 총계정원장 잔액과 분개 배치를 가져오고, FBDI를 통해 분개를 전기합니다.
- [Workday Financials에 연결](/ko/guides/connections/workday-financials/) — 통합 시스템 사용자로 Workday Financials 연결을 설정하고, RaaS 보고서를 가져오고, 분개 항목을 전기합니다.
- [SAP S/4HANA Cloud에 연결](/ko/guides/connections/s4hana-cloud/) — OAuth2로 S/4HANA Cloud 직접 연결을 설정하고, 시산표와 분개 항목 라인을 가져오고, SOAP를 통해 분개 항목을 전기합니다.
- [SAP ECC / S/4HANA 임시 추출](/ko/guides/connections/sap-adhoc-extract/) — 테이블, 트랜잭션 코드 또는 저장된 SAP 쿼리로 SAP을 검색하고, 추출을 미리 보고 계획한 다음, PlaidLink 에이전트를 통해 테이블에 저장합니다.
- [Sage Intacct에 연결](/ko/guides/connections/sage-intacct/) — Sage Intacct 연결을 설정하고 재무 및 회계 데이터를 가져옵니다.
- [Xero에 연결](/ko/guides/connections/xero/) — 한 번의 클릭으로 Xero 조직을 승인하고, Accounting API 엔터티를 가져오고, 수동 분개, 송장, 청구서, 결제, 대변 전표를 전기합니다.
- [Salesforce에 연결](/ko/guides/connections/salesforce/) — Salesforce External Client App과 Run As 사용자를 설정한 다음 CRM 개체를 프로젝트 테이블로 추출합니다.
- [HFM / FCCS에서 추출(임시)](/ko/guides/connections/hfm-fccs/) — Oracle FCCS에 연결하고 관점 선택기로 데이터 슬라이스를 직접 가져옵니다. HFM 팀에 요청 티켓을 보낼 필요가 없습니다.
- [TM1에 연결](/ko/guides/connections/tm1/) — IBM TM1 / Planning Analytics 서버에 연결하고 뷰 또는 MDX로 기간별로 나눈 큐브 데이터를 읽습니다.
- [Anaplan에 연결](/ko/guides/connections/anaplan/) — Anaplan에 연결하여 저장된 뷰를 읽거나, 기존 내보내기 작업을 실행하거나, 목록을 PlaidCloud 차원으로 로드합니다. 읽기 전용입니다.
- [QuickBooks에 연결](/ko/guides/connections/quickbooks/) — QuickBooks Online의 사전 요구 사항과 현재 제한 사항입니다.
- [전기 등록부 검토](/ko/guides/connections/posting-register/) — 재무 및 회계 담당자가 볼 수 있는 모든 프로젝트와 연결의 ERP 전기 내역을 검토하는 테넌트 수준 콘솔입니다.

## 관련 문서

- [커넥터 참조](/ko/reference/connectors/) — 지원되는 시스템의 전체 카탈로그와 각 시스템에 필요한 필드입니다.
