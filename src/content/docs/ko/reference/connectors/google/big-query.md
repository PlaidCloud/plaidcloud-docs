---
title: Google BigQuery 커넥터
description: PlaidCloud에서 Google BigQuery 연결을 구성하여 분석 쿼리를 실행하고 대규모 데이터를 워크플로에 통합합니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/google/big-query.md
---

## 연결 문서
[Google BigQuery 문서](https://docs.cloud.google.com/bigquery/docs)

## 구성

이 필드는 연결을 만들거나 편집할 때 나타납니다. 필수 여부는 사용하도록 설정한 인증 옵션에 따라 달라집니다.

### 식별 정보

| 필드 | 유형 | 설명 |
|---|---|---|
| 이름 | 텍스트 | 이 연결의 표시 이름입니다. |
| 별칭 | 텍스트(여러 줄) | 연결에 대한 선택적 별칭 또는 메모입니다. |
| 활성 여부 | 토글 | 연결의 사용 여부입니다. 삭제하지 않고 일시 중지하려면 비활성화합니다. |
| DB 읽기 전용 | 토글 | 연결을 읽기 전용 작업으로 제한합니다. |
| 액세스 유형 | 선택 | 이 연결의 읽기 전용, 쓰기 전용 또는 읽기/쓰기 액세스 수준입니다. |

### BigQuery 연결

| 필드 | 필수 | 설명 |
|---|---|---|
| 프로젝트 | 예 | 데이터 세트를 보유한 Google Cloud 프로젝트입니다. |
| 데이터 세트 | 예 | 읽고 쓸 BigQuery 데이터 세트입니다. |
| 테이블 | 예 | 데이터 세트에 있는 테이블입니다. |

### 인증 자격 증명

| 필드 | 필수 | 설명 |
|---|---|---|
| 서비스 계정 키(JSON) | 예 | 데이터 세트를 읽을 수 있는 Google 서비스 계정의 JSON 키 파일 전체를 붙여넣습니다. 데이터 세트에 쓰려는 경우에만 쓰기 권한을 부여합니다. 키는 쓰기 전용이므로, 편집할 때 비워 두면 저장된 키가 유지됩니다. |

이 연결은 사용자가 제공한 서비스 계정 키로만 인증합니다. [SQL 가져오기](/ko/reference/workflow-steps/import/import-sql/) 단계는 이 연결을 통해 BigQuery를 읽고, [Export External Database Tables](/ko/reference/workflow-steps/export/export-external-tables/) 단계는 BigQuery 로드 작업으로 여기에 씁니다.
