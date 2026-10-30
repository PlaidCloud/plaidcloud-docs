---
title: POINT_IN_POLYGON (Lakehouse v1)
description: POINT_IN_POLYGON — berechnet, ob ein angegebener Punkt innerhalb des Polygons liegt, das durch die Verbindung mehrerer Punkte entsteht.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/point-in-polygon.md
---

Berechnet, ob ein angegebener Punkt innerhalb des Polygons liegt, das durch die Verbindung mehrerer Punkte entsteht. Ein Polygon ist eine geschlossene Form, die durch Koordinatenpaare in der Reihenfolge ihres Auftretens verbunden wird. Eine geänderte Reihenfolge der Koordinatenpaare kann zu einer anderen Form führen.

## Analyze-Syntax

```python
func.point_in_polygon((x,y), [(a,b), (c,d), (e,f) ... ])
```

## Analyze-Beispiele

```python
func.point_in_polygon((3., 3.), [(6, 0), (8, 4), (5, 8), (0, 2)])

┌─────────────────────────────────────────────────────────────────┐
│ func.point_in_polygon((3, 3), [(6, 0), (8, 4), (5, 8), (0, 2)]) │
├─────────────────────────────────────────────────────────────────┤
│                                                               1 │
└─────────────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
POINT_IN_POLYGON((x,y), [(a,b), (c,d), (e,f) ... ])
```

## SQL-Beispiele

```sql
SELECT POINT_IN_POLYGON((3., 3.), [(6, 0), (8, 4), (5, 8), (0, 2)]);

┌────────────────────────────────────────────────────────────┐
│ point_in_polygon((3, 3), [(6, 0), (8, 4), (5, 8), (0, 2)]) │
├────────────────────────────────────────────────────────────┤
│                                                          1 │
└────────────────────────────────────────────────────────────┘
```
