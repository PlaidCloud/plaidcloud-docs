---
title: TRANSFORM_KEYS (Lakehouse v2)
description: TRANSFORM_KEYS — stosuje wyrażenie lambda do przekształcenia kluczy mapy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/transform-keys.md
---

Stosuje wyrażenie lambda do przekształcenia kluczy mapy.

## Składnia Analyze

```python
func.transform_keys(get_column(table, 'map_col'), lambda k, v: upper(k))
```

## Przykłady Analyze

```python
func.transform_keys(MAP{'a':1,'b':2}, lambda k,v: upper(k))

┌───────────────┐
│ {'A':1,'B':2} │
└───────────────┘
```

## Składnia SQL

```sql
TRANSFORM_KEYS(<map_col>, lambda k, v: upper(k))
```

## Przykłady SQL

```sql
SELECT TRANSFORM_KEYS((k, v) -> UPPER(k), MAP{'a':1, 'b':2});

┌───────────────┐
│ {"A":1,"B":2} │
└───────────────┘
```
