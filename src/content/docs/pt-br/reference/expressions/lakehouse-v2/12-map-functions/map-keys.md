---
title: MAP_KEYS (Lakehouse v2)
description: MAP_KEYS — retorna todas as chaves de um mapa como um array.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-keys.md
---

Retorna todas as chaves de um mapa como um array.

## Sintaxe do Analyze

```python
func.map_keys(get_column(table, 'map_col'))
```

## Exemplos do Analyze

```python
func.map_keys(MAP{'a':1,'b':2})

┌───────────┐
│ ['a','b'] │
└───────────┘
```

## Sintaxe SQL

```sql
MAP_KEYS(<map_col>)
```

## Exemplos de SQL

```sql
SELECT MAP_KEYS(MAP{'a':1, 'b':2});

┌───────────┐
│ ["a","b"] │
└───────────┘
```
