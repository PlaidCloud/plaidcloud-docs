---
title: ARRAY_UNIQUE_AGG (Lakehouse v2)
description: ARRAY_UNIQUE_AGG — 値を、重複のない値の配列に集約します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-unique-agg.md
---

値を、重複のない値の配列に集約します。

## Analyzeの構文

```python
func.array_unique_agg(get_column(table, 'tag'))
```

## Analyzeの例

```python
func.array_unique_agg(get_column(table, 'tag'))

┌───────────────┐
│ ['a','b','c'] │
└───────────────┘
```

## SQLの構文

```sql
ARRAY_UNIQUE_AGG(<tag>)
```

## SQLの例

```sql
SELECT ARRAY_UNIQUE_AGG(tag) FROM tags;

┌───────────────┐
│ ["a","b","c"] │
└───────────────┘
```
