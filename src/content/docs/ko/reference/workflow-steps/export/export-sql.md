---
title: Export to SQL 단계
description: PlaidCloud 워크플로 단계에서 외부 SQL 데이터베이스로 데이터를 내보내 결과를 하위 데이터베이스 시스템에 로드합니다.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-sql.md
---

## 설명



PlaidCloud 프로젝트 테이블을 CREATE TABLE 및 INSERT 문이 포함된 SQL 파일로 문서 계정에 기록합니다. CSV나 Parquet가 아니라 SQL 스크립트를 수집하는 시스템에 데이터를 넘겨야 할 때 유용합니다.

원격 데이터베이스에 직접 로드하려면 해당 데이터베이스 내보내기 단계나 [Agent Remote Import 단계](/ko/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database/)를 대신 사용하십시오. 이들은 더 빠르고 중간 파일이 필요하지 않습니다.

## 추가 설정

**행 순서**의 **행 정렬 기준**(`sort_columns`)은 기록되는 행을 이 소스 열로 정렬하며 첫 번째 키부터 적용하고, 각 키마다 **열**, **오름차순**, **NULL 값** 설정이 있습니다. 키 열을 반드시 기록할 필요는 없습니다. **NULL 값**의 기본값은 오름차순에서는 먼저, 내림차순에서는 나중입니다. **요약** 또는 **고유**와 함께 사용하지 않습니다.

## 예제


아직 예제가 없습니다...
