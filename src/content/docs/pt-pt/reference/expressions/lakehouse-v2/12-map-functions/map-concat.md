---
title: MAP_CONCAT (Lakehouse v2)
description: MAP_CONCAT — concatena vários mapas num único mapa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-concat.md
---

Concatena vários mapas num único mapa.

## Sintaxe de Analyze

```python
func.map_concat(map1, map2)
```

## Exemplos de Analyze

```python
func.map_concat(MAP{'a':1}, MAP{'b':2})

┌───────────────┐
│ {'a':1,'b':2} │
└───────────────┘
```

## Sintaxe SQL

```sql
MAP_CONCAT(map1, map2)
```

## Exemplos SQL

```sql
SELECT MAP_CONCAT(MAP{'a':1}, MAP{'b':2});

┌───────────────┐
│ {"a":1,"b":2} │
└───────────────┘
```
