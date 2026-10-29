---
title: FILES（Lakehouse v2）
description: FILES — クラウドストレージ上のファイルからデータを直接読み取ります。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/20-table-functions/files.md
---

クラウドストレージ上のファイルからデータを直接読み取ります。

## Analyze 構文

```python
func.files(<path_or_properties>)
```

## Analyze の例

```python
# FILES is a table function used in FROM clauses
# select(func.files(...))

┌─────────┐
│ (table)  │
└─────────┘
```

## SQL 構文

```sql
FILES(<path_or_properties>)
```

## SQL の例

```sql
SELECT * FROM FILES('path' = 's3://bucket/data.parquet', 'format' = 'parquet') LIMIT 5;

┌─────────────────┐
│ (query results)  │
└─────────────────┘
```
