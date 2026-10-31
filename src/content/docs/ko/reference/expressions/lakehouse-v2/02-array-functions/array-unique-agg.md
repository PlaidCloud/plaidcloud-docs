---
title: ARRAY_UNIQUE_AGG (Lakehouse v2)
description: ARRAY_UNIQUE_AGG — 값을 고유 값의 배열로 집계합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-unique-agg.md
---

값을 고유 값의 배열로 집계합니다.

## Analyze 구문

```python
func.array_unique_agg(get_column(table, 'tag'))
```

## Analyze 예제

```python
func.array_unique_agg(get_column(table, 'tag'))

┌───────────────┐
│ ['a','b','c'] │
└───────────────┘
```

## SQL 구문

```sql
ARRAY_UNIQUE_AGG(<tag>)
```

## SQL 예제

```sql
SELECT ARRAY_UNIQUE_AGG(tag) FROM tags;

┌───────────────┐
│ ["a","b","c"] │
└───────────────┘
```
