---
title: MAP_SIZE (Lakehouse v2)
description: MAP_SIZE — retorna o número de pares chave-valor em um mapa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-size.md
---

Retorna o número de pares chave-valor em um mapa.

## Sintaxe do Analyze

```python
func.map_size(get_column(table, 'map_col'))
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT MAP_SIZE(MAP{'a':1, 'b':2, 'c':3});

┌───┐
│ 3 │
└───┘
```
