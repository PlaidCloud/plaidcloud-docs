---
title: MAP_SIZE (Lakehouse v2)
description: MAP_SIZE — devolve o número de pares chave-valor de um mapa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-size.md
---

Devolve o número de pares chave-valor de um mapa.

## Sintaxe de Analyze

```python
func.map_size(get_column(table, 'map_col'))
```

## Exemplos de Analyze

```python
func.map_size(MAP{'a':1,'b':2,'c':3})

┌───┐
│ 3 │
└───┘
```

## Sintaxe SQL

```sql
MAP_SIZE(<map_col>)
```

## Exemplos SQL

```sql
SELECT MAP_SIZE(MAP{'a':1, 'b':2, 'c':3});

┌───┐
│ 3 │
└───┘
```
