---
title: ST_ASWKT (Lakehouse v1)
description: ST_ASWKT — converte um objeto GEOMETRY numa representação no formato WKT (well-known-text).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-aswkt.md
---

Converte um objeto GEOMETRY numa representação no formato [WKT (well-known-text)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry).

## Sintaxe SQL

```sql
ST_ASWKT(<geometry>)
```

## Aliases

- [ST_ASTEXT](../st-astext)

## Argumentos

| Argumentos   | Descrição                                            |
|--------------|------------------------------------------------------|
| `<geometry>` | O argumento tem de ser uma expressão do tipo GEOMETRY. |

## Tipo de retorno

String.

## Exemplos de SQL

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
