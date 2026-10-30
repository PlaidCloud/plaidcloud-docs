---
title: ST_MAKEGEOMPOINT (Lakehouse v1)
description: ST_MAKEGEOMPOINT — erstellt ein GEOMETRY-Objekt, das einen Point mit dem angegebenen Längen- und Breitengrad darstellt.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-makegeompoint.md
---

Erstellt ein GEOMETRY-Objekt, das einen Point mit dem angegebenen Längen- und Breitengrad darstellt.

## SQL-Syntax

```sql
ST_MAKEGEOMPOINT(<longitude>, <latitude>)
```

## Aliase

- [ST_GEOM_POINT](../st-geom-point)

## Argumente

| Argumente     | Beschreibung                                     |
|---------------|--------------------------------------------------|
| `<longitude>` | Ein Double-Wert, der den Längengrad darstellt.   |
| `<latitude>`  | Ein Double-Wert, der den Breitengrad darstellt.  |

## Rückgabetyp

Geometry.

## SQL-Beispiele

```sql
SELECT
  ST_MAKEGEOMPOINT(
    7.0, 8.0
  ) AS pipeline_point;

┌────────────────┐
│ pipeline_point │
├────────────────┤
│ POINT(7 8)     │
└────────────────┘

SELECT
  ST_MAKEGEOMPOINT(
    -122.3061, 37.554162
  ) AS pipeline_point;

┌────────────────────────────┐
│       pipeline_point       │
├────────────────────────────┤
│ POINT(-122.3061 37.554162) │
└────────────────────────────┘
```
