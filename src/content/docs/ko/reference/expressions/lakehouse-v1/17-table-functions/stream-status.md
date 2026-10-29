---
title: STREAM_STATUS (Lakehouse v1)
description: STREAM_STATUS — 스트림에 소비할 변경 데이터 캡처 레코드가 있는지 여부(true/false)를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/stream-status.md
---

지정한 스트림의 상태에 대한 정보를 제공하며, `true` 또는 `false` 값을 가질 수 있는 단일 열 결과(`has_data`)를 반환합니다. 

- `true`: 스트림에 변경 데이터 캡처 레코드가 **있을 수 있음**을 나타냅니다.
- `false`: 스트림에 현재 변경 데이터 캡처 레코드가 없음을 나타냅니다.

:::note
결과(`has_data`)가 `true`라고 해서 변경 데이터 캡처 레코드가 반드시 존재한다는 것을 **보장하지는** 않습니다. 테이블 컴팩트 작업과 같은 다른 작업으로 인해 실제 변경 데이터 캡처 레코드가 없는데도 `true` 값이 나올 수 있습니다.
:::

:::note
작업에서 `STREAM_STATUS`를 사용할 때는 스트림을 참조할 때 데이터베이스 이름을 포함해야 합니다(예: `STREAM_STATUS('mydb.stream_name')`).
:::

## SQL 구문

```sql
SELECT * FROM STREAM_STATUS('<database_name>.<stream_name>');
-- OR
SELECT * FROM STREAM_STATUS('<stream_name>');  -- Uses current database
```

## SQL 예제

```sql
-- Create a table 't' with a column 'c'
CREATE TABLE t (c int);

-- Create a stream 's' on the table 't'
CREATE STREAM s ON TABLE t;

-- Check the initial status of the stream 's'
SELECT * FROM STREAM_STATUS('s');

-- The result should be 'false' indicating no change data capture records initially
┌──────────┐
│ has_data │
├──────────┤
│ false    │
└──────────┘

-- Insert a value into the table 't'
INSERT INTO t VALUES (1);

-- Check the updated status of the stream 's' after the insertion
SELECT * FROM STREAM_STATUS('s');

-- The result should now be 'true' indicating the presence of change data capture records
┌──────────┐
│ has_data │
├──────────┤
│ true     │
└──────────┘

-- Example with database name specified
SELECT * FROM STREAM_STATUS('mydb.s');
```
