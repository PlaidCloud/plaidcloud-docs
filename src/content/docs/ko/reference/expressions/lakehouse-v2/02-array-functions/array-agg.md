---
title: ARRAY_AGG (Lakehouse v2)
description: ARRAY_AGG — 값을 배열로 집계합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-agg.md
---

값을 배열로 집계합니다.

## Analyze 구문

```python
func.array_agg(get_column(table, 'name'))
```

## Analyze 예제

```python
func.array_agg(get_column(table, 'name'))
```

## SQL 구문

```sql
ARRAY_AGG(<name>)
```

## SQL 예제

```sql
SELECT ARRAY_AGG(name) FROM employees;

┌─────────────────────────────┐
│ array_agg(name)             │
├─────────────────────────────┤
│ ["Alice","Bob","Charlie"]   │
└─────────────────────────────┘
```
