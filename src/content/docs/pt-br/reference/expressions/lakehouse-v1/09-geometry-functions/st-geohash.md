---
title: ST_GEOHASH (Lakehouse v1)
description: ST_GEOHASH — retorna o geohash de um objeto GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geohash.md
---

Retorna o [geohash](https://en.wikipedia.org/wiki/Geohash) de um objeto GEOMETRY. Um geohash é uma string base32 curta que identifica um retângulo geodésico que contém uma localização no mundo. O argumento opcional de precisão especifica a `precision` do geohash retornado. Por exemplo, passar 5 para `precision retorna um geohash mais curto (5 caracteres) e menos preciso.

## SQL Syntax

```sql
ST_GEOHASH(<geometry> [, <precision>])
```

## Arguments

| Argumentos       | Descrição                                                                 |
|-----------------|---------------------------------------------------------------------------|
| `geometry`    | O argumento deve ser uma expressão do tipo GEOMETRY.                      |
| `[precision]` | Opcional. Especifica a precisão do geohash retornado; o padrão é 12. |

## Return Type

String.

## SQL Examples

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
