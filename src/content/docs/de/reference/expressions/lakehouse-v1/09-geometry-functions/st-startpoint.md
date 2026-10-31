---
title: ST_STARTPOINT (Lakehouse v1)
description: ST_STARTPOINT — gibt den ersten Point eines LineString zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-startpoint.md
---

Gibt den ersten Point eines LineString zurück.

## SQL-Syntax

```sql
ST_STARTPOINT(<geometry>)
```

## Argumente

| Argumente    | Beschreibung                                                                                   |
|--------------|------------------------------------------------------------------------------------------------|
| `<geometry>` | Das Argument muss ein Ausdruck vom Typ GEOMETRY sein, der einen LineString darstellt.          |

## Rückgabetyp

Geometry.

## SQL-Beispiele

```sql
SELECT
  ST_STARTPOINT(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(1 1, 2 2, 3 3, 4 4)'
    )
  ) AS pipeline_endpoint;

┌───────────────────┐
│ pipeline_endpoint │
├───────────────────┤
│ POINT(1 1)        │
└───────────────────┘
```
