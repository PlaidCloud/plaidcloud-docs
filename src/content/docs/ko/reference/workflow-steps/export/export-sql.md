---
title: Export to SQL 단계
description: PlaidCloud 워크플로 단계에서 외부 SQL 데이터베이스로 데이터를 내보내 결과를 다운스트림 데이터베이스 시스템에 로드합니다.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-sql.md
---

## 설명



PlaidCloud 프로젝트 테이블을 CREATE TABLE 및 INSERT 문이 담긴 SQL 파일로 문서 계정에 기록합니다. CSV나 Parquet 대신 SQL 스크립트를 수집하는 시스템에 데이터를 전달해야 할 때 유용합니다.

원격 데이터베이스에 직접 로드하려면 해당 데이터베이스의 내보내기 단계 또는 [Agent Remote Import](/ko/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database/)를 대신 사용하십시오. 이러한 방법은 더 빠르며 중간 파일이 필요하지 않습니다.

## 미리 보기

**소스** 탭의 **미리 보기**는 단계를 실행하지 않고 소스 테이블의 최대 100개 행을 표시합니다. 테이블에 행이 더 많으면 미리 보기에 처음 행만 표시된다고 안내합니다. 소스 테이블이 아직 없으면 미리 볼 항목이 없다고 안내합니다. 잠긴 프로젝트에서는 미리 보기를 사용할 수 없습니다.

## 추가 설정

**행 순서**의 **행 정렬 기준**(`sort_columns`)은 기록되는 행을 이러한 소스 열 기준으로 정렬하며, 첫 번째 키부터 순서대로 적용됩니다. 각 키에는 **열**, **오름차순**, **NULL 값** 설정이 있습니다. 키 열은 기록되지 않아도 됩니다. **NULL 값**의 기본값은 오름차순일 때 처음, 내림차순일 때 마지막입니다. **요약** 또는 **고유**와 함께 사용되지 않습니다.

## 예제


아직 예제가 없습니다...
