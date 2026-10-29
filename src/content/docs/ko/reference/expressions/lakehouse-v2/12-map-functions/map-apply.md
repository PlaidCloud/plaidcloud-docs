---
title: MAP_APPLY (Lakehouse v2)
description: MAP_APPLY — 맵의 각 키-값 쌍에 람다 식을 적용합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-apply.md
---

맵의 각 키-값 쌍에 람다 식을 적용합니다.

## Analyze 구문

```python
func.map_apply(get_column(table, 'map_col'), lambda k, v: (k, v*2))
```

## Analyze 예제

```python
func.map_apply(MAP{'a':1,'b':2}, lambda k,v: (k, v*2))

┌───────────────┐
│ {'a':2,'b':4} │
└───────────────┘
```

## SQL 구문

```sql
MAP_APPLY(<map_col>, lambda k, v: (k, v*2))
```

## SQL 예제

```sql
SELECT MAP_APPLY((k, v) -> (k, v * 2), MAP{'a':1, 'b':2});

┌───────────────┐
│ {"a":2,"b":4} │
└───────────────┘
```
