---
title: MAP_VALUES (Lakehouse v2)
description: MAP_VALUES — 맵의 모든 값을 배열로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-values.md
---

맵의 모든 값을 배열로 반환합니다.

## Analyze 구문

```python
func.map_values(get_column(table, 'map_col'))
```

## Analyze 예제

```python
func.map_values(MAP{'a':1,'b':2})

┌───────┐
│ [1,2] │
└───────┘
```

## SQL 구문

```sql
MAP_VALUES(<map_col>)
```

## SQL 예제

```sql
SELECT MAP_VALUES(MAP{'a':1, 'b':2});

┌───────┐
│ [1,2] │
└───────┘
```
