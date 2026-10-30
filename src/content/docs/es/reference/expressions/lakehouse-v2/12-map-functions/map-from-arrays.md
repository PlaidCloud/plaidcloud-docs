---
title: MAP_FROM_ARRAYS (Lakehouse v2)
description: MAP_FROM_ARRAYS — crea un mapa a partir de una matriz de claves y una matriz de valores.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-from-arrays.md
---

Crea un mapa a partir de una matriz de claves y una matriz de valores.

## Sintaxis de Analyze

```python
func.map_from_arrays(['a','b'], [1, 2])
```

## Ejemplos de Analyze

```python
func.map_from_arrays(['a', 'b', 'c'], [1, 2, 3])

┌─────────────────────┐
│ {'a':1,'b':2,'c':3} │
└─────────────────────┘
```

## Sintaxis de SQL

```sql
MAP_FROM_ARRAYS(['a','b'], [1, 2])
```

## Ejemplos de SQL

```sql
SELECT MAP_FROM_ARRAYS(['a', 'b', 'c'], [1, 2, 3]);

┌─────────────────────┐
│ {"a":1,"b":2,"c":3} │
└─────────────────────┘
```
