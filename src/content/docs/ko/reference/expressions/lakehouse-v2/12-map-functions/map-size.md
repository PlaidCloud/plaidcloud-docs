---
title: MAP_SIZE (Lakehouse v2)
description: MAP_SIZE — 맵의 키-값 쌍 수를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-size.md
---

맵의 키-값 쌍 수를 반환합니다.

## Analyze 구문

```python
func.map_size(get_column(table, 'map_col'))
```

## Analyze 예제

```python
func.map_size(MAP{'a':1,'b':2,'c':3})

┌───┐
│ 3 │
└───┘
```

## SQL 구문

```sql
MAP_SIZE(<map_col>)
```

## SQL 예제

```sql
SELECT MAP_SIZE(MAP{'a':1, 'b':2, 'c':3});

┌───┐
│ 3 │
└───┘
```
