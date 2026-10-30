---
title: MAP_FROM_ARRAYS (Lakehouse v2)
description: MAP_FROM_ARRAYS — cria um mapa a partir de uma matriz de chaves e de uma matriz de valores.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-from-arrays.md
---

Cria um mapa a partir de uma matriz de chaves e de uma matriz de valores.

## Sintaxe de Analyze

```python
func.map_from_arrays(['a','b'], [1, 2])
```

## Exemplos de Analyze

```python
func.map_from_arrays(['a', 'b', 'c'], [1, 2, 3])

┌─────────────────────┐
│ {'a':1,'b':2,'c':3} │
└─────────────────────┘
```

## Sintaxe SQL

```sql
MAP_FROM_ARRAYS(['a','b'], [1, 2])
```

## Exemplos SQL

```sql
SELECT MAP_FROM_ARRAYS(['a', 'b', 'c'], [1, 2, 3]);

┌─────────────────────┐
│ {"a":1,"b":2,"c":3} │
└─────────────────────┘
```
