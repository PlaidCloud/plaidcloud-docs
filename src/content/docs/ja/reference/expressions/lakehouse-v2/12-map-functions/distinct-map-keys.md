---
title: DISTINCT_MAP_KEYS (Lakehouse v2)
description: DISTINCT_MAP_KEYS — マップから重複を除いたキーを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/distinct-map-keys.md
---

マップから重複を除いたキーを返します。

## Analyzeの構文

```python
func.distinct_map_keys(get_column(table, 'map_col'))
```

## Analyzeの例

```python
func.distinct_map_keys(get_column(table, 'tags'))

┌───────────────┐
│ ['a','b','c'] │
└───────────────┘
```

## SQLの構文

```sql
DISTINCT_MAP_KEYS(<map_col>)
```

## SQLの例

```sql
SELECT DISTINCT_MAP_KEYS(MAP{'a':1, 'b':2, 'c':3});

┌───────────────┐
│ ["a","b","c"] │
└───────────────┘
```
