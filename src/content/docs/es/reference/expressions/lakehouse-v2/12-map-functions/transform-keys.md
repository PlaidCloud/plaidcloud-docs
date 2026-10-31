---
title: TRANSFORM_KEYS (Lakehouse v2)
description: TRANSFORM_KEYS — aplica una expresión lambda para transformar las claves de un mapa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/transform-keys.md
---

Aplica una expresión lambda para transformar las claves de un mapa.

## Sintaxis de Analyze

```python
func.transform_keys(get_column(table, 'map_col'), lambda k, v: upper(k))
```

## Ejemplos de Analyze

```python
func.transform_keys(MAP{'a':1,'b':2}, lambda k,v: upper(k))

┌───────────────┐
│ {'A':1,'B':2} │
└───────────────┘
```

## Sintaxis de SQL

```sql
TRANSFORM_KEYS(<map_col>, lambda k, v: upper(k))
```

## Ejemplos de SQL

```sql
SELECT TRANSFORM_KEYS((k, v) -> UPPER(k), MAP{'a':1, 'b':2});

┌───────────────┐
│ {"A":1,"B":2} │
└───────────────┘
```
