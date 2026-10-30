---
title: ST_DIMENSION (Lakehouse v1)
description: ST_DIMENSION — gibt die Dimension eines Geometrieobjekts zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-dimension.md
---

Gibt die Dimension eines Geometrieobjekts zurück. Die Dimension eines GEOMETRY-Objekts ist:

| Geodaten-Objekttyp           | Dimension  |
|------------------------------|------------|
| Point / MultiPoint           | 0          |
| LineString / MultiLineString | 1          |
| Polygon / MultiPolygon       | 2          |

## SQL-Syntax

```sql
ST_DIMENSION(<geometry>)
```

## Argumente

| Argumente    | Beschreibung                                          |
|--------------|-------------------------------------------------------|
| `<geometry>` | Das Argument muss ein Ausdruck vom Typ GEOMETRY sein. |

## Rückgabetyp

UInt8.

## SQL-Beispiele

```sql
SELECT
  ST_DIMENSION(
    ST_GEOMETRYFROMWKT(
      'POINT(-122.306100 37.554162)'
    )
  ) AS pipeline_dimension;

┌────────────────────┐
│ pipeline_dimension │
├────────────────────┤
│                  0 │
└────────────────────┘

SELECT
  ST_DIMENSION(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(-124.20 42.00, -120.01 41.99)'
    )
  ) AS pipeline_dimension;

┌────────────────────┐
│ pipeline_dimension │
├────────────────────┤
│                  1 │
└────────────────────┘

SELECT
  ST_DIMENSION(
    ST_GEOMETRYFROMWKT(
      'POLYGON((-124.20 42.00, -120.01 41.99, -121.1 42.01, -124.20 42.00))'
    )
  ) AS pipeline_dimension;

┌────────────────────┐
│ pipeline_dimension │
├────────────────────┤
│                  2 │
└────────────────────┘
```
