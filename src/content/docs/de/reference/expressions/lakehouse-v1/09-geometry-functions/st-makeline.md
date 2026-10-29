---
title: ST_MAKELINE (Lakehouse v1)
description: ST_MAKELINE — erstellt ein GEOMETRY-Objekt, das eine Linie darstellt, welche die Punkte der beiden eingegebenen GEOMETRY-Objekte verbindet.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-makeline.md
---

Erstellt ein GEOMETRY-Objekt, das eine Linie darstellt, welche die Punkte der beiden eingegebenen GEOMETRY-Objekte verbindet.

## SQL-Syntax

```sql
ST_MAKELINE(<geometry1>, <geometry2>)
```

## Aliase

- [ST_MAKE_LINE](../st-make-line)

## Argumente

| Argumente     | Beschreibung                                                                                                                   |
|---------------|--------------------------------------------------------------------------------------------------------------------------------|
| `<geometry1>` | Ein GEOMETRY-Objekt mit den zu verbindenden Punkten. Dieses Objekt muss ein Point, MultiPoint oder LineString sein.            |
| `<geometry2>` | Ein GEOMETRY-Objekt mit den zu verbindenden Punkten. Dieses Objekt muss ein Point, MultiPoint oder LineString sein.            |

## Rückgabetyp

Geometry.

## SQL-Beispiele

```sql
SELECT
  ST_MAKELINE(
    ST_GEOMETRYFROMWKT(
      'POINT(-122.306100 37.554162)'
    ),
    ST_GEOMETRYFROMWKT(
      'POINT(-104.874173 56.714538)'
    )
  ) AS pipeline_line;

┌───────────────────────────────────────────────────────┐
│                     pipeline_line                     │
├───────────────────────────────────────────────────────┤
│ LINESTRING(-122.3061 37.554162,-104.874173 56.714538) │
└───────────────────────────────────────────────────────┘
```
