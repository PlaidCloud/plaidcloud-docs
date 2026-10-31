---
title: ST_ASEWKB (Lakehouse v1)
description: ST_ASEWKB — wandelt ein GEOMETRY-Objekt in das Format EWKB (Extended Well-Known Binary) um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-asewkb.md
---

Wandelt ein GEOMETRY-Objekt in eine Darstellung im Format [EWKB (Extended Well-Known Binary)](https://postgis.net/docs/ST_GeomFromEWKB.html) um.

## SQL-Syntax

```sql
ST_ASEWKB(<geometry>)
```

## Argumente

| Argumente    | Beschreibung                                                |
|--------------|-------------------------------------------------------------|
| `<geometry>` | Das Argument muss ein Ausdruck vom Typ GEOMETRY sein.       |

## Rückgabetyp

Binary.

## SQL-Beispiele

```sql
SELECT
  ST_ASEWKB(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;LINESTRING(400000 6000000, 401000 6010000)'
    )
  ) AS pipeline_ewkb;

┌────────────────────────────────────────────────────────────────────────────────────────────┐
│                                        pipeline_ewkb                                       │
├────────────────────────────────────────────────────────────────────────────────────────────┤
│ 0102000020E61000000200000000000000006A18410000000060E3564100000000A07918410000000024ED5641 │
└────────────────────────────────────────────────────────────────────────────────────────────┘

SELECT
  ST_ASEWKB(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;POINT(-122.35 37.55)'
    )
  ) AS pipeline_ewkb;

┌────────────────────────────────────────────────────┐
│                    pipeline_ewkb                   │
├────────────────────────────────────────────────────┤
│ 0101000020E61000006666666666965EC06666666666C64240 │
└────────────────────────────────────────────────────┘
```
