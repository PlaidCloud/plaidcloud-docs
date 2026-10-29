---
title: POINT_IN_POLYGON (Lakehouse v1)
description: POINT_IN_POLYGON — détermine si un point donné se trouve à l'intérieur du polygone formé en reliant plusieurs points.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/point-in-polygon.md
---

Détermine si un point donné se trouve à l'intérieur du polygone formé en reliant plusieurs points. Un polygone est une forme fermée dont les paires de coordonnées sont reliées dans l'ordre où elles apparaissent. Modifier l'ordre des paires de coordonnées peut produire une forme différente.

## Syntaxe Analyze

```python
func.point_in_polygon((x,y), [(a,b), (c,d), (e,f) ... ])
```

## Exemples Analyze

```python
func.point_in_polygon((3., 3.), [(6, 0), (8, 4), (5, 8), (0, 2)])

┌─────────────────────────────────────────────────────────────────┐
│ func.point_in_polygon((3, 3), [(6, 0), (8, 4), (5, 8), (0, 2)]) │
├─────────────────────────────────────────────────────────────────┤
│                                                               1 │
└─────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
POINT_IN_POLYGON((x,y), [(a,b), (c,d), (e,f) ... ])
```

## Exemples SQL

```sql
SELECT POINT_IN_POLYGON((3., 3.), [(6, 0), (8, 4), (5, 8), (0, 2)]);

┌────────────────────────────────────────────────────────────┐
│ point_in_polygon((3, 3), [(6, 0), (8, 4), (5, 8), (0, 2)]) │
├────────────────────────────────────────────────────────────┤
│                                                          1 │
└────────────────────────────────────────────────────────────┘
```
