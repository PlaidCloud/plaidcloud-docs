---
title: ST_GEOHASH (Lakehouse v1)
description: ST_GEOHASH – Gibt den Geohash für ein GEOMETRY-Objekt zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geohash.md
---

Gibt den [Geohash](https://en.wikipedia.org/wiki/Geohash) für ein GEOMETRY-Objekt zurück. Ein Geohash ist eine kurze Base32-Zeichenfolge, die ein geodätisches Rechteck identifiziert, das einen Ort auf der Welt enthält. Das optionale Präzisionsargument legt die `precision` des zurückgegebenen Geohash fest. Wenn Sie beispielsweise 5 für `precision übergeben, wird ein kürzerer Geohash (5 Zeichen lang) zurückgegeben, der weniger genau ist.

## SQL-Syntax

```sql
ST_GEOHASH(<geometry> [, <precision>])
```

## Argumente

| Argumente       | Beschreibung                                                              |
|-----------------|---------------------------------------------------------------------------|
| `geometry`    | Das Argument muss ein Ausdruck vom Typ GEOMETRY sein.                     |
| `[precision]` | Optional. Legt die Präzision des zurückgegebenen Geohash fest, Standard ist 12. |

## Rückgabetyp

Zeichenfolge (String).

## SQL-Beispiele

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
