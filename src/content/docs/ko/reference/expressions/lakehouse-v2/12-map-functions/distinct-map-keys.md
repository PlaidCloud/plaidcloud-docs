---
title: DISTINCT_MAP_KEYS (Lakehouse v2)
description: DISTINCT_MAP_KEYS — 맵에서 고유한 키를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/distinct-map-keys.md
---

맵에서 고유한 키를 반환합니다.

## Analyze 구문

```python
func.distinct_map_keys(get_column(table, 'map_col'))
```

## Analyze 예제

```python
func.distinct_map_keys(get_column(table, 'tags'))

┌───────────────┐
│ ['a','b','c'] │
└───────────────┘
```

## SQL 구문

```sql
DISTINCT_MAP_KEYS(<map_col>)
```

## SQL 예제

```sql
SELECT DISTINCT_MAP_KEYS(MAP{'a':1, 'b':2, 'c':3});

┌───────────────┐
│ ["a","b","c"] │
└───────────────┘
```
