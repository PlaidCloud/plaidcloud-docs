---
title: ST_MAKEPOLYGON (Lakehouse v1)
description: ST_MAKEPOLYGON — erstellt ein GEOMETRY-Objekt, das ein Polygon ohne Löcher darstellt.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-makepolygon.md
---

Erstellt ein GEOMETRY-Objekt, das ein Polygon ohne Löcher darstellt. Die Funktion verwendet den angegebenen LineString als äußere Schleife.

## SQL-Syntax

```sql
ST_MAKEPOLYGON(<geometry>)
```

## Aliase

- [ST_POLYGON](../st-polygon)

## Argumente

| Argumente    | Beschreibung                                          |
|--------------|-------------------------------------------------------|
| `<geometry>` | Das Argument muss ein Ausdruck vom Typ GEOMETRY sein. |

## Rückgabetyp

Geometry.

## SQL-Beispiele

```sql
SELECT
  ST_MAKEPOLYGON(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(0.0 0.0, 1.0 0.0, 1.0 2.0, 0.0 2.0, 0.0 0.0)'
    )
  ) AS pipeline_polygon;

┌────────────────────────────────┐
│        pipeline_polygon        │
├────────────────────────────────┤
│ POLYGON((0 0,1 0,1 2,0 2,0 0)) │
└────────────────────────────────┘
```
