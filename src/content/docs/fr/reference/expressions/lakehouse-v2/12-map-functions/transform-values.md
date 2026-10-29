---
title: TRANSFORM_VALUES (Lakehouse v2)
description: TRANSFORM_VALUES — applique une expression lambda pour transformer les valeurs d'un map.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/transform-values.md
---

Applique une expression lambda pour transformer les valeurs d'un map.

## Syntaxe Analyze

```python
func.transform_values(get_column(table, 'map_col'), lambda k, v: v * 10)
```

## Exemples Analyze

```python
func.transform_values(MAP{'a':1,'b':2}, lambda k,v: v*10)

┌─────────────────┐
│ {'a':10,'b':20} │
└─────────────────┘
```

## Syntaxe SQL

```sql
TRANSFORM_VALUES(<map_col>, lambda k, v: v * 10)
```

## Exemples SQL

```sql
SELECT TRANSFORM_VALUES((k, v) -> v * 10, MAP{'a':1, 'b':2});

┌─────────────────┐
│ {"a":10,"b":20} │
└─────────────────┘
```
