---
title: MAP_APPLY (Lakehouse v2)
description: MAP_APPLY — aplica una expresión lambda a cada par clave-valor de un mapa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-apply.md
---

Aplica una expresión lambda a cada par clave-valor de un mapa.

## Sintaxis de Analyze

```python
func.map_apply(get_column(table, 'map_col'), lambda k, v: (k, v*2))
```

## Ejemplos de Analyze

```python
func.map_apply(MAP{'a':1,'b':2}, lambda k,v: (k, v*2))

┌───────────────┐
│ {'a':2,'b':4} │
└───────────────┘
```

## Sintaxis de SQL

```sql
MAP_APPLY(<map_col>, lambda k, v: (k, v*2))
```

## Ejemplos de SQL

```sql
SELECT MAP_APPLY((k, v) -> (k, v * 2), MAP{'a':1, 'b':2});

┌───────────────┐
│ {"a":2,"b":4} │
└───────────────┘
```
