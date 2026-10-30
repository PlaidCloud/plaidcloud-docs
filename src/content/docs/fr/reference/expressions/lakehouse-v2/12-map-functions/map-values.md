---
title: MAP_VALUES (Lakehouse v2)
description: MAP_VALUES — renvoie toutes les valeurs d'un map sous forme de tableau.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-values.md
---

Renvoie toutes les valeurs d'un map sous forme de tableau.

## Syntaxe Analyze

```python
func.map_values(get_column(table, 'map_col'))
```

## Exemples Analyze

```python
func.map_values(MAP{'a':1,'b':2})

┌───────┐
│ [1,2] │
└───────┘
```

## Syntaxe SQL

```sql
MAP_VALUES(<map_col>)
```

## Exemples SQL

```sql
SELECT MAP_VALUES(MAP{'a':1, 'b':2});

┌───────┐
│ [1,2] │
└───────┘
```
