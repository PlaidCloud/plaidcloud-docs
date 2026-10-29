---
title: MAP_SIZE (Lakehouse v2)
description: MAP_SIZE — renvoie le nombre de paires clé-valeur d'un map.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-size.md
---

Renvoie le nombre de paires clé-valeur d'un map.

## Syntaxe Analyze

```python
func.map_size(get_column(table, 'map_col'))
```

## Exemples Analyze

```python
func.map_size(MAP{'a':1,'b':2,'c':3})

┌───┐
│ 3 │
└───┘
```

## Syntaxe SQL

```sql
MAP_SIZE(<map_col>)
```

## Exemples SQL

```sql
SELECT MAP_SIZE(MAP{'a':1, 'b':2, 'c':3});

┌───┐
│ 3 │
└───┘
```
