---
title: MAP_VALUES (Lakehouse v2)
description: MAP_VALUES — devolve todos os valores de um mapa como uma matriz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-values.md
---

Devolve todos os valores de um mapa como uma matriz.

## Sintaxe de Analyze

```python
func.map_values(get_column(table, 'map_col'))
```

## Exemplos de Analyze

```python
func.map_values(MAP{'a':1,'b':2})

┌───────┐
│ [1,2] │
└───────┘
```

## Sintaxe SQL

```sql
MAP_VALUES(<map_col>)
```

## Exemplos SQL

```sql
SELECT MAP_VALUES(MAP{'a':1, 'b':2});

┌───────┐
│ [1,2] │
└───────┘
```
