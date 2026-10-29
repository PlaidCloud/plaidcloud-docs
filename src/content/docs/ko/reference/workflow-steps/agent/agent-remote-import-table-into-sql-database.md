---
title: Agent Remote Import Table into SQL Database 단계
description: 방화벽 뒤에서 데이터를 안전하게 로드할 수 있도록 PlaidLink 에이전트를 통해 PlaidCloud 테이블 데이터를 원격 SQL 데이터베이스로 가져옵니다.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database.md
---

## 설명



PlaidLink 에이전트를 통해서만 접근할 수 있는 데이터베이스로 PlaidCloud 프로젝트 테이블을 푸시합니다. 에이전트가 PlaidCloud에서 데이터를 받아 로컬에서 로드를 수행하므로, 온프레미스 운영 데이터베이스를 PlaidCloud 분석과 동기화된 상태로 유지하는 데 유용합니다.

일반적인 사용 방식: PlaidCloud가 새로 고친 예측 또는 배부 결과를 생성하면 에이전트가 이를 온프레미스 ERP, 데이터 마트 또는 운영 보고 데이터베이스에 로드합니다.


## 데이터가 에이전트에 도달하는 방식

버전 1.2.33 이상의 PlaidLink 에이전트는 테이블의 행을 하나의 Parquet 파일로 받습니다. 숫자, 날짜, 타임스탬프, 참/거짓 값은 각자의 유형으로 도착합니다. 시간, 간격, JSON 열 같은 다른 열은 텍스트로 도착합니다. 빈 텍스트 값은 이전과 같이 빈 값(NULL)으로 도착합니다.

이전 에이전트는 이전과 같이 압축된 탭 구분 파일로 행을 받습니다. Parquet을 받으려면 [에이전트를 업그레이드](/ko/reference/cli/plaidlink/upgrade/)하십시오.

## 예제

아직 예제가 없습니다...
