---
title: 데이터 및 서비스 커넥터
description: 데이터베이스, ERP, REST API, 클라우드 스토리지, Git 리포지토리 등 외부 데이터 소스 및 서비스에 PlaidCloud를 연결합니다.
sidebar:
  label: 커넥터
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/index.md
---

PlaidCloud는 목적별로 만들어진 커넥터를 통해 외부 데이터 소스 및 서비스에 연결합니다. 각 커넥터는 하나의 제공자 계열에 대한 인증, 프로토콜, 데이터 형태의 세부 사항을 처리합니다.

## 범주

### 데이터베이스 및 데이터 레이크

관계형 데이터베이스, 클라우드 웨어하우스, 쿼리 엔진, 레이크하우스 형식입니다.

- [데이터베이스](/ko/reference/connectors/databases/) — PostgreSQL, MySQL, SQL Server, Oracle, Snowflake, Redshift, BigQuery, Databricks, MongoDB, Kafka 등 15개 이상
- [오픈 테이블](/ko/reference/connectors/open-tables/) — Apache Iceberg, Delta Lake, Hudi, Hive 오픈 테이블 형식

### 클라우드 및 SaaS 서비스

- [REST](/ko/reference/connectors/rest/) — Salesforce, NetSuite, Workday, QuickBooks, Stripe, Dynamics 등
- [ERP 시스템](/ko/reference/connectors/erp/) — SAP ECC / S/4HANA, Oracle EBS/Fusion, Infor, JD Edwards
- [클라우드 서비스](/ko/reference/connectors/cloud-services/) — 서드파티 데이터 서비스
- [Google](/ko/reference/connectors/google/) — BigQuery, Google 스프레드시트
- [협업](/ko/reference/connectors/collaboration/) — Slack, Microsoft Teams, Tableau
- [Singer 소스](/ko/reference/connectors/singer-sources/) — Stripe, GitHub, HubSpot, 데이터베이스 등 130개 이상의 Singer 탭 소스

### 개발 및 소스 제어

- [Git 제공자](/ko/reference/connectors/git/) — PlaidCloud Git(관리형 내장 서비스), GitHub, GitLab, Bitbucket, Azure Repos, CodeCommit

## 관련 항목

- [연결 가이드](/ko/guides/connections/) — 연결을 만들고 관리하는 작업 중심 안내
- [워크플로 단계 참조](/ko/reference/workflow-steps/) — 연결을 구성한 후 수행할 수 있는 작업
