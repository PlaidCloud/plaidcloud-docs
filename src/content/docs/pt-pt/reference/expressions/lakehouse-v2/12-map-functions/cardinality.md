---
title: "CARDINALITY (Mapa, Lakehouse v2)"
description: CARDINALITY — devolve o número de pares chave-valor de um mapa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/cardinality.md
---

Devolve o número de pares chave-valor de um mapa.

## Sintaxe de Analyze

```python
func.cardinality(get_column(table, 'map_col'))
```

## Exemplos de Analyze

```python
func.cardinality(MAP{'a':1,'b':2,'c':3})

┌───┐
│ 3 │
└───┘
```

## Sintaxe SQL

```sql
CARDINALITY(<map_col>)
```

## Exemplos SQL

```sql
SELECT CARDINALITY(MAP{'a':1, 'b':2, 'c':3});

┌───┐
│ 3 │
└───┘
```
