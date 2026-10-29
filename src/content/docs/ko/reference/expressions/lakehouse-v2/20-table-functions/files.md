---
title: FILES (Lakehouse v2)
description: FILES — 클라우드 스토리지 파일에서 데이터를 직접 읽습니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/20-table-functions/files.md
---

클라우드 스토리지 파일에서 데이터를 직접 읽습니다.

## Analyze 구문

```python
func.files(<path_or_properties>)
```

## Analyze 예제

```python
# FILES is a table function used in FROM clauses
# select(func.files(...))

┌─────────┐
│ (table)  │
└─────────┘
```

## SQL 구문

```sql
FILES(<path_or_properties>)
```

## SQL 예제

```sql
SELECT * FROM FILES('path' = 's3://bucket/data.parquet', 'format' = 'parquet') LIMIT 5;

┌─────────────────┐
│ (query results)  │
└─────────────────┘
```
