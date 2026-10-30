---
title: MAP_KEYS (Lakehouse v2)
description: MAP_KEYS — 맵의 모든 키를 배열로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-keys.md
---

맵의 모든 키를 배열로 반환합니다.

## Analyze 구문

```python
func.map_keys(get_column(table, 'map_col'))
```

## Analyze 예제

```python
func.map_keys(MAP{'a':1,'b':2})

┌───────────┐
│ ['a','b'] │
└───────────┘
```

## SQL 구문

```sql
MAP_KEYS(<map_col>)
```

## SQL 예제

```sql
SELECT MAP_KEYS(MAP{'a':1, 'b':2});

┌───────────┐
│ ["a","b"] │
└───────────┘
```
