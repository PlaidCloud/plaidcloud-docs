---
title: Export to ORC 단계
description: PlaidCloud 프로젝트 테이블을 선택한 압축 코덱을 적용한 열 기반 형식의 Apache ORC 파일로 문서 계정에 내보냅니다.
sidebar:
  order: 13.5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-to-orc.md
---

## 설명

프로젝트 테이블을 테이블마다 하나씩 [Apache ORC](https://orc.apache.org/) 파일로 문서 계정에 기록합니다. ORC는 Hive, Spark 및 대부분의 클라우드 데이터 플랫폼에서 읽는 열 기반 형식이며, 스키마가 파일에 포함됩니다. [ORC 가져오기](/ko/reference/workflow-steps/import/import-orc/) 단계와 함께 사용하십시오.

단계 양식에는 대상 파일, 접두사, 압축, 파일이 있을 때의 동작을 설정하는 **파일 매개변수** 페이지와, 내보낼 테이블을 나열하고 테이블마다 고유한 테이블 데이터 선택과 데이터 필터를 지정하는 **매개변수 기록** 페이지가 있습니다. [마이그레이션된 KNIME 워크플로](/ko/guides/workflows/migrate-knime-workflows/)는 ORC 기록기에 이 단계를 사용합니다.

## 구성

* **대상 파일**(`output_file`) — 파일을 기록할 문서 계정과 폴더입니다.
* **대상 파일 접두사**(`file_name`) — 파일 접두사입니다. 각 테이블은 `<prefix><table name>.orc`로 기록됩니다.
* **압축 옵션**(`compression`) — 파일 내부에서 사용하는 ORC 코덱으로, **Snappy**, **zlib**, **gzip**(`zlib`로 기록), **Zstandard**, **LZ4** 중에서 선택합니다. **없음**은 파일을 압축하지 않고 기록합니다.
* **매개변수 기록**(`frames`) — 내보낼 테이블입니다. 각 프레임에는 해당 테이블의 설정이 들어 있으며, 프레임 안이 아니라 단계 맨 위에 둔 테이블 수준 설정은 읽히지 않습니다.
  * `id` — 경고에 표시되는 테이블의 레이블입니다.
  * `source` — 내보낼 프로젝트 테이블입니다. 각 파일의 이름이 여기에서 정해집니다.
  * `source_columns` 및 `target_columns` — 읽는 열과 기록하는 열이며, 이름 바꾸기, 유형, 열별 집계가 포함됩니다.
  * `source_where` — 소스 행에 대한 필터입니다.
  * `aggregate` 및 `aggregation_type` — 행을 요약합니다. `aggregation_type`은 자체 설정이 없는 열에 적용되는 요약 방식입니다.
  * `having` — 요약된 행에 대한 필터입니다.
  * `distinct` — 고유한 행만 기록합니다.
  * `use_target_slicer`, `limit_target_start`, `limit_target_end` — 결과의 시작 위치부터 끝 위치까지의 행만 기록합니다.
  * `sort_columns` — AI 어시스턴트 또는 REST API로 설정하여 기록되는 행을 이 소스 열을 기준으로 정렬합니다. 첫 번째 키가 가장 우선하며, 각 키는 `{source, ascending, nulls}`입니다. 키 열을 반드시 기록해야 하는 것은 아닙니다. `nulls`의 기본값은 오름차순일 때 `first`, 내림차순일 때 `last`입니다. `aggregate` 또는 `distinct`와 함께 사용되지 않습니다.
* **파일이 있는 경우** 아래의 **이미 있는 파일**(`if_exists`) — **덮어쓰기**(`overwrite`, 기본값)는 이미 있는 파일을 대체하고, **아무것도 기록하지 않고 단계 실패**(`fail`)는 기록하려는 파일이 이미 있으면 아무것도 기록하지 않고 단계를 중단합니다.

## 관련 항목

- [내보내기 단계](/ko/reference/workflow-steps/export/)
- [ORC 가져오기](/ko/reference/workflow-steps/import/import-orc/)
- [Export to Parquet 단계](/ko/reference/workflow-steps/export/export-to-parquet/)
