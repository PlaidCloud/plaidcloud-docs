---
title: ST_ASEWKB (Lakehouse v1)
description: ST_ASEWKB — konwertuje obiekt GEOMETRY na format EWKB (rozszerzony well-known binary).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-asewkb.md
---

Konwertuje obiekt GEOMETRY na reprezentację w formacie [EWKB (rozszerzony well-known binary)](https://postgis.net/docs/ST_GeomFromEWKB.html).

## Składnia SQL

```sql
ST_ASEWKB(<geometry>)
```

## Argumenty

| Argumenty    | Opis                                                 |
|--------------|------------------------------------------------------|
| `<geometry>` | Argument musi być wyrażeniem typu GEOMETRY. |

## Typ zwracany

Binary.

## Przykłady SQL

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
