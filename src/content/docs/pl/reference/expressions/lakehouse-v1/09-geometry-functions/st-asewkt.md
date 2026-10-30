---
title: ST_ASEWKT (Lakehouse v1)
description: ST_ASEWKT — konwertuje obiekt GEOMETRY na format EWKT (rozszerzony well-known text).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-asewkt.md
---

Konwertuje obiekt GEOMETRY na reprezentację w formacie [EWKT (rozszerzony well-known text)](https://postgis.net/docs/ST_GeomFromEWKT.html).

## Składnia SQL

```sql
ST_ASEWKT(<geometry>)
```

## Argumenty

| Argumenty    | Opis                                                 |
|--------------|------------------------------------------------------|
| `<geometry>` | Argument musi być wyrażeniem typu GEOMETRY. |

## Typ zwracany

String.

## Przykłady SQL

```sql
SELECT
  ST_ASEWKT(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;LINESTRING(400000 6000000, 401000 6010000)'
    )
  ) AS pipeline_ewkt;

┌─────────────────────────────────────────────────────┐
│                    pipeline_ewkt                    │
├─────────────────────────────────────────────────────┤
│ SRID=4326;LINESTRING(400000 6000000,401000 6010000) │
└─────────────────────────────────────────────────────┘

SELECT
  ST_ASEWKT(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;POINT(-122.35 37.55)'
    )
  ) AS pipeline_ewkt;

┌────────────────────────────────┐
│          pipeline_ewkt         │
├────────────────────────────────┤
│ SRID=4326;POINT(-122.35 37.55) │
└────────────────────────────────┘
```
