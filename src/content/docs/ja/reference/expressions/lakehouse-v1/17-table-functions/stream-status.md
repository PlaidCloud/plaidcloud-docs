---
title: STREAM_STATUS（Lakehouse v1）
description: STREAM_STATUS — ストリームに処理対象の変更データキャプチャレコードがあるかどうか（true/false）を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/stream-status.md
---

指定したストリームのステータスに関する情報を提供し、`true` または `false` のいずれかの値を取る単一列の結果（`has_data`）を返します。 

- `true`: ストリームに変更データキャプチャレコードが**含まれている可能性がある**ことを示します。
- `false`: ストリームに現在、変更データキャプチャレコードが含まれていないことを示します。

:::note
結果（`has_data`）が `true` であっても、変更データキャプチャレコードが確実に存在するとは**限りません**。テーブルのコンパクト操作など、ほかの操作によっても、実際の変更データキャプチャレコードがない場合に `true` になることがあります。
:::

:::note
タスクで `STREAM_STATUS` を使用する場合は、ストリームを参照する際にデータベース名を含める必要があります（例: `STREAM_STATUS('mydb.stream_name')`）。
:::

## SQLの構文

```sql
SELECT * FROM STREAM_STATUS('<database_name>.<stream_name>');
-- OR
SELECT * FROM STREAM_STATUS('<stream_name>');  -- Uses current database
```

## SQLの例

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
