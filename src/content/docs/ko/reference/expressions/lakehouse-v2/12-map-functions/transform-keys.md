---
title: TRANSFORM_KEYS (Lakehouse v2)
description: TRANSFORM_KEYS — 람다 식을 적용하여 맵의 키를 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/transform-keys.md
---

람다 식을 적용하여 맵의 키를 변환합니다.

## Analyze 구문

```python
func.transform_keys(get_column(table, 'map_col'), lambda k, v: upper(k))
```

## Analyze 예제

```python
func.transform_keys(MAP{'a':1,'b':2}, lambda k,v: upper(k))

┌───────────────┐
│ {'A':1,'B':2} │
└───────────────┘
```

## SQL 구문

```sql
TRANSFORM_KEYS(<map_col>, lambda k, v: upper(k))
```

## SQL 예제

```sql
SELECT TRANSFORM_KEYS((k, v) -> UPPER(k), MAP{'a':1, 'b':2});

┌───────────────┐
│ {"A":1,"B":2} │
└───────────────┘
```
