---
title: ST_GEOMPOINTFROMGEOHASH (Lakehouse v1)
description: ST_GEOMPOINTFROMGEOHASH — retorna um objeto GEOMETRY para o ponto que representa o centro de um geohash.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-geompointfromgeohash.md
---

Retorna um objeto GEOMETRY para o ponto que representa o centro de um [geohash](https://en.wikipedia.org/wiki/Geohash).

## Sintaxe SQL

```sql
ST_GEOMPOINTFROMGEOHASH(<geohash>)
```

## Argumentos

| Argumentos  | Descrição                        |
|-------------|----------------------------------|
| `<geohash>` | O argumento deve ser um geohash. |

## Tipo de retorno

Geometry.

## Exemplos de SQL

```sql
SELECT
  ST_GEOMPOINTFROMGEOHASH(
    's02equ0'
  ) AS pipeline_geometry;

┌──────────────────────────────────────────────┐
│               pipeline_geometry              │
│                   Geometry                   │
├──────────────────────────────────────────────┤
│ POINT(1.0004425048828125 2.0001983642578125) │
└──────────────────────────────────────────────┘
```
