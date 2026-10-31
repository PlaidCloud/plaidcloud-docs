---
title: INSPECT_TABLE_PARTITION_INFO（Lakehouse v2）
description: INSPECT_TABLE_PARTITION_INFO — テーブルのパーティション情報を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-table-partition-info.md
---

テーブルのパーティション情報を返します。

## Analyze 構文

```python
func.inspect_table_partition_info(<catalog>, <db>, <table>)
```

## Analyze の例

```python
func.inspect_table_partition_info('default', 'mydb', 'my_table')

┌──────────────┐
│ (partitions)  │
└──────────────┘
```

## SQL 構文

```sql
INSPECT_TABLE_PARTITION_INFO(<catalog>, <db>, <table>)
```

## SQL の例

```sql
SELECT * FROM TABLE(INSPECT_TABLE_PARTITION_INFO('default', 'mydb', 'my_table'));

┌──────────────────┐
│ (partition info)  │
└──────────────────┘
```
