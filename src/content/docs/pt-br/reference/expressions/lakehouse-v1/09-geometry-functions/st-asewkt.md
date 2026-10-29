---
title: ST_ASEWKT (Lakehouse v1)
description: ST_ASEWKT — converte um objeto GEOMETRY para o formato EWKT (extended well-known-text).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-asewkt.md
---

Converte um objeto GEOMETRY para uma representação no formato [EWKT (extended well-known-text)](https://postgis.net/docs/ST_GeomFromEWKT.html).

## Sintaxe SQL

```sql
ST_ASEWKT(<geometry>)
```

## Argumentos

| Argumentos   | Descrição                                            |
|--------------|------------------------------------------------------|
| `<geometry>` | O argumento deve ser uma expressão do tipo GEOMETRY. |

## Tipo de retorno

String.

## Exemplos de SQL

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
