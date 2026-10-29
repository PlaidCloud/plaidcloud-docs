---
title: MAP_FILTER (Lakehouse v2)
description: MAP_FILTER — filtra os pares chave-valor de um mapa através de uma expressão lambda.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-filter.md
---

Filtra os pares chave-valor de um mapa através de uma expressão lambda.

## Sintaxe de Analyze

```python
func.map_filter(get_column(table, 'map_col'), lambda k, v: v > 1)
```

## Exemplos de Analyze

```python
func.map_filter(MAP{'a':1,'b':2,'c':3}, lambda k,v: v>1)

┌───────────────┐
│ {'b':2,'c':3} │
└───────────────┘
```

## Sintaxe SQL

```sql
MAP_FILTER(<map_col>, lambda k, v: v > 1)
```

## Exemplos SQL

```sql
SELECT MAP_FILTER((k, v) -> v > 1, MAP{'a':1, 'b':2, 'c':3});

┌───────────────┐
│ {"b":2,"c":3} │
└───────────────┘
```
