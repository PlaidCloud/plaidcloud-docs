---
title: FUSE_TIME_TRAVEL_SIZE (Lakehouse v1)
description: FUSE_TIME_TRAVEL_SIZE — 테이블의 이력 데이터(타임 트래블용)의 저장소 크기를 계산합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/fuse-time-travel-size.md
---

테이블의 이력 데이터(타임 트래블용)의 저장소 크기를 계산합니다.

## SQL 구문

```sql
-- Calculate historical data size for all tables in all databases
SELECT ...
FROM fuse_time_travel_size();

-- Calculate historical data size for all tables in a specified database
SELECT ...
FROM fuse_time_travel_size('<database_name>');

-- Calculate historical data size for a specified table in a specified database
SELECT ...
FROM fuse_time_travel_size('<database_name>', '<table_name>'));
```

## 출력

이 함수는 다음 열로 구성된 결과 집합을 반환합니다.

| 열 | 설명 |
|----------------------------------|-------------------------------------------------------------------------------------------------------|
| `database_name`                  | 테이블이 있는 데이터베이스의 이름입니다. |
| `table_name`                     | 테이블의 이름입니다. |
| `is_dropped`                     | 테이블이 삭제되었는지 여부를 나타냅니다(삭제된 테이블은 `true`, 그렇지 않으면 `false`). |
| `time_travel_size`               | 테이블의 이력 데이터(타임 트래블용)의 총 저장소 크기(바이트)입니다. |
| `latest_snapshot_size`           | 테이블의 최신 스냅샷의 저장소 크기(바이트)입니다. |
| `data_retention_period_in_hours` | 타임 트래블 데이터의 보존 기간(시간)입니다(`NULL`은 기본 보존 정책을 사용함을 의미합니다). |
| `error`                          | 저장소 크기를 가져오는 중 발생한 오류입니다(오류가 없으면 `NULL`). |

## SQL 예제

이 예제는 `default` 데이터베이스에 있는 모든 테이블의 이력 데이터를 계산합니다.

```sql
SELECT * FROM fuse_time_travel_size('default')

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ database_name │ table_name │ is_dropped │ time_travel_size │ latest_snapshot_size │ data_retention_period_in_hours │       error      │
├───────────────┼────────────┼────────────┼──────────────────┼──────────────────────┼────────────────────────────────┼──────────────────┤
│ default       │ books      │ true       │             2810 │                 1490 │                           NULL │ NULL             │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
