---
title: ST_GEOHASH (Lakehouse v1)
description: ST_GEOHASH — zwraca geohash dla obiektu GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geohash.md
---

Zwraca [geohash](https://en.wikipedia.org/wiki/Geohash) dla obiektu GEOMETRY. Geohash to krótki ciąg base32 identyfikujący prostokąt geodezyjny zawierający lokalizację na świecie. Opcjonalny argument precision określa dokładność (`precision`) zwracanego geohasha. Na przykład przekazanie wartości 5 jako `precision zwraca krótszy geohash (o długości 5 znaków), który jest mniej dokładny.

## Składnia SQL

```sql
ST_GEOHASH(<geometry> [, <precision>])
```

## Argumenty

| Argumenty       | Opis                                                                      |
|-----------------|---------------------------------------------------------------------------|
| `geometry`    | Argument musi być wyrażeniem typu GEOMETRY.                               |
| `[precision]` | Opcjonalny. Określa dokładność zwracanego geohasha, domyślnie 12. |

## Typ zwracany

String.

## Przykłady SQL

```sql
SELECT
  ST_GEOHASH(
    ST_GEOMETRYFROMWKT(
      'POINT(-122.306100 37.554162)'
    )
  ) AS pipeline_geohash;

┌──────────────────┐
│ pipeline_geohash │
├──────────────────┤
│ 9q9j8ue2v71y     │
└──────────────────┘

SELECT
  ST_GEOHASH(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;POINT(-122.35 37.55)'
    ),
    5
  ) AS pipeline_geohash;

┌──────────────────┐
│ pipeline_geohash │
├──────────────────┤
│ 9q8vx            │
└──────────────────┘
```
