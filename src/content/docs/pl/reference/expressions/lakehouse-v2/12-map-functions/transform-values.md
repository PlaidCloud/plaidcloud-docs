---
title: TRANSFORM_VALUES (Lakehouse v2)
description: TRANSFORM_VALUES — stosuje wyrażenie lambda do przekształcenia wartości mapy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/transform-values.md
---

Stosuje wyrażenie lambda do przekształcenia wartości mapy.

## Składnia Analyze

```python
func.transform_values(get_column(table, 'map_col'), lambda k, v: v * 10)
```

## Przykłady Analyze

```python
func.transform_values(MAP{'a':1,'b':2}, lambda k,v: v*10)

┌─────────────────┐
│ {'a':10,'b':20} │
└─────────────────┘
```

## Składnia SQL

```sql
TRANSFORM_VALUES(<map_col>, lambda k, v: v * 10)
```

## Przykłady SQL

```sql
SELECT TRANSFORM_VALUES((k, v) -> v * 10, MAP{'a':1, 'b':2});

┌─────────────────┐
│ {"a":10,"b":20} │
└─────────────────┘
```
