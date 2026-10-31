---
title: MAP_KEYS (Lakehouse v2)
description: MAP_KEYS — zwraca wszystkie klucze z mapy jako tablicę.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-keys.md
---

Zwraca wszystkie klucze z mapy jako tablicę.

## Składnia Analyze

```python
func.map_keys(get_column(table, 'map_col'))
```

## Przykłady Analyze

```python
func.map_keys(MAP{'a':1,'b':2})

┌───────────┐
│ ['a','b'] │
└───────────┘
```

## Składnia SQL

```sql
MAP_KEYS(<map_col>)
```

## Przykłady SQL

```sql
SELECT MAP_KEYS(MAP{'a':1, 'b':2});

┌───────────┐
│ ["a","b"] │
└───────────┘
```
