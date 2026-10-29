---
title: ST_CONTAINS (Lakehouse v2)
description: ST_CONTAINS — vérifie si une géométrie en contient une autre. Renvoie 1 si c'est le cas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-contains.md
---

Vérifie si une géométrie en contient une autre. Renvoie 1 si c'est le cas.

## Syntaxe Analyze

```python
func.st_contains(<geometry1>, <geometry2>)
```

## Exemples Analyze

```python
func.st_contains(get_column(table, 'area'), func.st_point(1, 1))

┌───┐
│ 1  │
└───┘
```

## Syntaxe SQL

```sql
ST_CONTAINS(<geometry1>, <geometry2>)
```

## Exemples SQL

```sql
SELECT ST_CONTAINS(ST_GeomFromText('POLYGON((0 0,10 0,10 10,0 10,0 0))'), ST_POINT(5, 5));

┌───┐
│ 1  │
└───┘
```
