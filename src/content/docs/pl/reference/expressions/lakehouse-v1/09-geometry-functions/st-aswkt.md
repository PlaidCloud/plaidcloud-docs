---
title: ST_ASWKT (Lakehouse v1)
description: ST_ASWKT — konwertuje obiekt GEOMETRY na reprezentację w formacie WKT (well-known text).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-aswkt.md
---

Konwertuje obiekt GEOMETRY na reprezentację w formacie [WKT (well-known text)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry).

## Składnia SQL

```sql
ST_ASWKT(<geometry>)
```

## Aliasy

- [ST_ASTEXT](../st-astext)

## Argumenty

| Argumenty    | Opis                                                 |
|--------------|------------------------------------------------------|
| `<geometry>` | Argument musi być wyrażeniem typu GEOMETRY. |

## Typ zwracany

String.

## Przykłady SQL

```sql
SELECT
  ST_ASWKT(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;LINESTRING(400000 6000000, 401000 6010000)'
    )
  ) AS pipeline_wkt;

┌───────────────────────────────────────────┐
│                pipeline_wkt               │
├───────────────────────────────────────────┤
│ LINESTRING(400000 6000000,401000 6010000) │
└───────────────────────────────────────────┘

SELECT
  ST_ASTEXT(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;POINT(-122.35 37.55)'
    )
  ) AS pipeline_wkt;

┌──────────────────────┐
│     pipeline_wkt     │
├──────────────────────┤
│ POINT(-122.35 37.55) │
└──────────────────────┘
```
