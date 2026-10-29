---
title: "CARDINALITY (Map, Lakehouse v2)"
description: CARDINALITY — renvoie le nombre de paires clé-valeur d'un map.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/cardinality.md
---

Renvoie le nombre de paires clé-valeur d'un map.

## Syntaxe Analyze

```python
func.cardinality(get_column(table, 'map_col'))
```

## Exemples Analyze

```python
func.cardinality(MAP{'a':1,'b':2,'c':3})

┌───┐
│ 3 │
└───┘
```

## Syntaxe SQL

```sql
CARDINALITY(<map_col>)
```

## Exemples SQL

```sql
SELECT CARDINALITY(MAP{'a':1, 'b':2, 'c':3});

┌───┐
│ 3 │
└───┘
```
