---
title: MAP_FILTER (Lakehouse v2)
description: MAP_FILTER — 람다 식을 사용하여 맵의 키-값 쌍을 필터링합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-filter.md
---

람다 식을 사용하여 맵의 키-값 쌍을 필터링합니다.

## Analyze 구문

```python
func.map_filter(get_column(table, 'map_col'), lambda k, v: v > 1)
```

## Analyze 예제

```python
func.map_filter(MAP{'a':1,'b':2,'c':3}, lambda k,v: v>1)

┌───────────────┐
│ {'b':2,'c':3} │
└───────────────┘
```

## SQL 구문

```sql
MAP_FILTER(<map_col>, lambda k, v: v > 1)
```

## SQL 예제

```sql
SELECT MAP_FILTER((k, v) -> v > 1, MAP{'a':1, 'b':2, 'c':3});

┌───────────────┐
│ {"b":2,"c":3} │
└───────────────┘
```
