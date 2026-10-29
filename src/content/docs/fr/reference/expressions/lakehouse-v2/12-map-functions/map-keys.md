---
title: MAP_KEYS (Lakehouse v2)
description: MAP_KEYS — renvoie toutes les clés d'un map sous forme de tableau.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-keys.md
---

Renvoie toutes les clés d'un map sous forme de tableau.

## Syntaxe Analyze

```python
func.map_keys(get_column(table, 'map_col'))
```

## Exemples Analyze

```python
func.map_keys(MAP{'a':1,'b':2})

┌───────────┐
│ ['a','b'] │
└───────────┘
```

## Syntaxe SQL

```sql
MAP_KEYS(<map_col>)
```

## Exemples SQL

```sql
SELECT MAP_KEYS(MAP{'a':1, 'b':2});

┌───────────┐
│ ["a","b"] │
└───────────┘
```
