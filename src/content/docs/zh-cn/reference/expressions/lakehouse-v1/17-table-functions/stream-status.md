---
title: STREAM_STATUS (Lakehouse v1)
description: STREAM_STATUS：返回流中是否有可供消费的变更数据捕获记录（true/false）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/stream-status.md
---

提供指定流的状态信息，返回单列结果（`has_data`），其值为 `true` 或 `false`： 

- `true`：表示该流**可能包含**变更数据捕获记录。
- `false`：表示该流当前不包含任何变更数据捕获记录。

:::note
结果（`has_data`）为 `true` 并**不**保证一定存在变更数据捕获记录。其他操作（例如执行表压缩操作）也可能导致 `true` 值，即使实际上没有变更数据捕获记录。
:::

:::note
在任务中使用 `STREAM_STATUS` 时，引用流必须包含数据库名称（例如 `STREAM_STATUS('mydb.stream_name')`）。
:::

## SQL 语法

```sql
SELECT * FROM STREAM_STATUS('<database_name>.<stream_name>');
-- OR
SELECT * FROM STREAM_STATUS('<stream_name>');  -- Uses current database
```

## SQL 示例

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
