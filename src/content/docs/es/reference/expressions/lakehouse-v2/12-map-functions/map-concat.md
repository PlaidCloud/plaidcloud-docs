---
title: MAP_CONCAT (Lakehouse v2)
description: MAP_CONCAT — concatena varios mapas en un solo mapa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-concat.md
---

Concatena varios mapas en un solo mapa.

## Sintaxis de Analyze

```python
func.map_concat(map1, map2)
```

## Ejemplos de Analyze

```python
func.map_concat(MAP{'a':1}, MAP{'b':2})

┌───────────────┐
│ {'a':1,'b':2} │
└───────────────┘
```

## Sintaxis de SQL

```sql
MAP_CONCAT(map1, map2)
```

## Ejemplos de SQL

```sql
SELECT MAP_CONCAT(MAP{'a':1}, MAP{'b':2});

┌───────────────┐
│ {"a":1,"b":2} │
└───────────────┘
```
