---
title: "CARDINALITY (맵, Lakehouse v2)"
description: CARDINALITY — 맵의 키-값 쌍 수를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/cardinality.md
---

맵의 키-값 쌍 수를 반환합니다.

## Analyze 구문

```python
func.cardinality(get_column(table, 'map_col'))
```

## Analyze 예제

```python
func.cardinality(MAP{'a':1,'b':2,'c':3})

┌───┐
│ 3 │
└───┘
```

## SQL 구문

```sql
CARDINALITY(<map_col>)
```

## SQL 예제

```sql
SELECT CARDINALITY(MAP{'a':1, 'b':2, 'c':3});

┌───┐
│ 3 │
└───┘
```
