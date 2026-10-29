---
title: "CARDINALITY (Mapa, Lakehouse v2)"
description: CARDINALITY — retorna o número de pares chave-valor em um mapa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/cardinality.md
---

Retorna o número de pares chave-valor em um mapa.

## Sintaxe do Analyze

```python
func.cardinality(get_column(table, 'map_col'))
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT CARDINALITY(MAP{'a':1, 'b':2, 'c':3});

┌───┐
│ 3 │
└───┘
```
