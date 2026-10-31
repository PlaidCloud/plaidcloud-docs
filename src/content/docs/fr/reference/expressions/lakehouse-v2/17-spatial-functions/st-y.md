---
title: ST_Y (Lakehouse v2)
description: ST_Y — renvoie la coordonnée Y (latitude) d'une géométrie de type point.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-y.md
---

Renvoie la coordonnée Y (latitude) d'une géométrie de type point.

## Syntaxe Analyze

```python
func.st_y(<point>)
```

## Exemples Analyze

```python
func.st_y(func.st_point(1.5, 2.5))

┌─────┐
│ 2.5  │
└─────┘
```

## Syntaxe SQL

```sql
ST_Y(<point>)
```

## Exemples SQL

```sql
SELECT ST_Y(ST_POINT(1.5, 2.5));

┌─────┐
│ 2.5  │
└─────┘
```
