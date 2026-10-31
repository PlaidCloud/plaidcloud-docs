---
title: MAP_CONCAT (Lakehouse v2)
description: MAP_CONCAT — concatena vários mapas em um único mapa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-concat.md
---

Concatena vários mapas em um único mapa.

## Sintaxe do Analyze

```python
func.map_concat(map1, map2)
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT MAP_CONCAT(MAP{'a':1}, MAP{'b':2});

┌───────────────┐
│ {"a":1,"b":2} │
└───────────────┘
```
