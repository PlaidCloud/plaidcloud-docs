---
title: ST_X (Lakehouse v2)
description: ST_X — renvoie la coordonnée X (longitude) d'une géométrie de type point.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-x.md
---

Renvoie la coordonnée X (longitude) d'une géométrie de type point.

## Syntaxe Analyze

```python
func.st_x(<point>)
```

## Exemples Analyze

```python
func.st_x(func.st_point(1.5, 2.5))

┌─────┐
│ 1.5  │
└─────┘
```

## Syntaxe SQL

```sql
ST_X(<point>)
```

## Exemples SQL

```sql
SELECT ST_X(ST_POINT(1.5, 2.5));

┌─────┐
│ 1.5  │
└─────┘
```
