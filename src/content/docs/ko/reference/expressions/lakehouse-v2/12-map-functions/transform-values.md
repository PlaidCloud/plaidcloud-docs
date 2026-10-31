---
title: TRANSFORM_VALUES (Lakehouse v2)
description: TRANSFORM_VALUES — 람다 식을 적용하여 맵의 값을 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/transform-values.md
---

람다 식을 적용하여 맵의 값을 변환합니다.

## Analyze 구문

```python
func.transform_values(get_column(table, 'map_col'), lambda k, v: v * 10)
```

## Analyze 예제

```python
func.transform_values(MAP{'a':1,'b':2}, lambda k,v: v*10)

┌─────────────────┐
│ {'a':10,'b':20} │
└─────────────────┘
```

## SQL 구문

```sql
TRANSFORM_VALUES(<map_col>, lambda k, v: v * 10)
```

## SQL 예제

```sql
SELECT TRANSFORM_VALUES((k, v) -> v * 10, MAP{'a':1, 'b':2});

┌─────────────────┐
│ {"a":10,"b":20} │
└─────────────────┘
```
