---
title: ST_ASGEOJSON (Lakehouse v1)
description: ST_ASGEOJSON — converte um objeto GEOMETRY em uma representação GeoJSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-asgeojson.md
---

Converte um objeto GEOMETRY em uma representação [GeoJSON](https://geojson.org/).

## Sintaxe SQL

```sql
ST_ASGEOJSON(<geometry>)
```

## Argumentos

| Argumentos   | Descrição                                            |
|--------------|------------------------------------------------------|
| `<geometry>` | O argumento deve ser uma expressão do tipo GEOMETRY. |

## Tipo de retorno

Variant.

## Exemplos de SQL

```sql
SELECT
  ST_ASGEOJSON(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;LINESTRING(400000 6000000, 401000 6010000)'
    )
  ) AS pipeline_geojson;

┌─────────────────────────────────────────────────────────────────────────┐
│                             pipeline_geojson                            │
├─────────────────────────────────────────────────────────────────────────┤
│ {"coordinates":[[400000,6000000],[401000,6010000]],"type":"LineString"} │
└─────────────────────────────────────────────────────────────────────────┘
```
