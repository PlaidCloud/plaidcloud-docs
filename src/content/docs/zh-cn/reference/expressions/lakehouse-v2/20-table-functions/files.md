---
title: FILES (Lakehouse v2)
description: FILES：直接从云存储文件中读取数据。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/20-table-functions/files.md
---

直接从云存储文件中读取数据。

## Analyze 语法

```python
func.files(<path_or_properties>)
```

## Analyze 示例

```python
# FILES is a table function used in FROM clauses
# select(func.files(...))

┌─────────┐
│ (table)  │
└─────────┘
```

## SQL 语法

```sql
FILES(<path_or_properties>)
```

## SQL 示例

```sql
SELECT * FROM FILES('path' = 's3://bucket/data.parquet', 'format' = 'parquet') LIMIT 5;

┌─────────────────┐
│ (query results)  │
└─────────────────┘
```
