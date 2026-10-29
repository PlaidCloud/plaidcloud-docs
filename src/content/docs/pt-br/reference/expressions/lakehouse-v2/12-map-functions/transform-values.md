---
title: TRANSFORM_VALUES (Lakehouse v2)
description: TRANSFORM_VALUES — aplica uma expressão lambda para transformar os valores de um mapa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/transform-values.md
---

Aplica uma expressão lambda para transformar os valores de um mapa.

## Sintaxe do Analyze

```python
func.transform_values(get_column(table, 'map_col'), lambda k, v: v * 10)
```

## Exemplos do Analyze

```python
func.transform_values(MAP{'a':1,'b':2}, lambda k,v: v*10)

┌─────────────────┐
│ {'a':10,'b':20} │
└─────────────────┘
```

## Sintaxe SQL

```sql
TRANSFORM_VALUES(<map_col>, lambda k, v: v * 10)
```

## Exemplos de SQL

```sql
SELECT TRANSFORM_VALUES((k, v) -> v * 10, MAP{'a':1, 'b':2});

┌─────────────────┐
│ {"a":10,"b":20} │
└─────────────────┘
```
