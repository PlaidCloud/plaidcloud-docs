---
title: TRANSFORM_VALUES (Lakehouse v2)
description: TRANSFORM_VALUES — aplica una expresión lambda para transformar los valores de un mapa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/transform-values.md
---

Aplica una expresión lambda para transformar los valores de un mapa.

## Sintaxis de Analyze

```python
func.transform_values(get_column(table, 'map_col'), lambda k, v: v * 10)
```

## Ejemplos de Analyze

```python
func.transform_values(MAP{'a':1,'b':2}, lambda k,v: v*10)

┌─────────────────┐
│ {'a':10,'b':20} │
└─────────────────┘
```

## Sintaxis de SQL

```sql
TRANSFORM_VALUES(<map_col>, lambda k, v: v * 10)
```

## Ejemplos de SQL

```sql
SELECT TRANSFORM_VALUES((k, v) -> v * 10, MAP{'a':1, 'b':2});

┌─────────────────┐
│ {"a":10,"b":20} │
└─────────────────┘
```
