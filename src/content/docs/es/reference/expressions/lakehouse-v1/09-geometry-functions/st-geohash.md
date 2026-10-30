---
title: ST_GEOHASH (Lakehouse v1)
description: ST_GEOHASH — devuelve el geohash de un objeto GEOMETRY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geohash.md
---

Devuelve el [geohash](https://en.wikipedia.org/wiki/Geohash) de un objeto GEOMETRY. Un geohash es una cadena corta en base32 que identifica un rectángulo geodésico que contiene una ubicación en el mundo. El argumento opcional de precisión especifica la `precision` del geohash devuelto. Por ejemplo, si se pasa 5 para `precision se devuelve un geohash más corto (de 5 caracteres) y menos preciso.

## Sintaxis de SQL

```sql
ST_GEOHASH(<geometry> [, <precision>])
```

## Argumentos

| Argumentos      | Descripción                                                               |
|-----------------|---------------------------------------------------------------------------|
| `geometry`    | El argumento debe ser una expresión de tipo GEOMETRY.                      |
| `[precision]` | Opcional. Especifica la precisión del geohash devuelto; el valor predeterminado es 12. |

## Tipo de valor devuelto

Cadena.

## Ejemplos de SQL

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
