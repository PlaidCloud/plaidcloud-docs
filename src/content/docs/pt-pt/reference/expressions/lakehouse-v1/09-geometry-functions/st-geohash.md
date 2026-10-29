---
title: ST_GEOHASH (Lakehouse v1)
description: ST_GEOHASH — devolve o geohash de um objeto GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geohash.md
---

Devolve o [geohash](https://en.wikipedia.org/wiki/Geohash) de um objeto GEOMETRY. Um geohash é uma cadeia curta em base32 que identifica um retângulo geodésico que contém uma localização no mundo. O argumento opcional de precisão especifica a `precision` do geohash devolvido. Por exemplo, ao passar 5 para `precision devolve um geohash mais curto (com 5 carateres), menos preciso.

## Sintaxe SQL

```sql
ST_GEOHASH(<geometry> [, <precision>])
```

## Argumentos

| Argumentos      | Descrição                                                                 |
|-----------------|---------------------------------------------------------------------------|
| `geometry`    | O argumento tem de ser uma expressão do tipo GEOMETRY.                      |
| `[precision]` | Opcional. Especifica a precisão do geohash devolvido; o valor predefinido é 12. |

## Tipo de retorno

String.

## Exemplos de SQL

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
