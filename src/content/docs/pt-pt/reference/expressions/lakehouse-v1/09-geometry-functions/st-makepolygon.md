---
title: ST_MAKEPOLYGON (Lakehouse v1)
description: ST_MAKEPOLYGON — constrói um objeto GEOMETRY que representa um Polygon sem buracos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-makepolygon.md
---

Constrói um objeto GEOMETRY que representa um Polygon sem buracos. A função utiliza a LineString especificada como anel exterior.

## Sintaxe SQL

```sql
ST_MAKEPOLYGON(<geometry>)
```

## Aliases

- [ST_POLYGON](../st-polygon)

## Argumentos

| Argumentos   | Descrição                                            |
|--------------|------------------------------------------------------|
| `<geometry>` | O argumento tem de ser uma expressão do tipo GEOMETRY. |

## Tipo de retorno

Geometry.

## Exemplos de SQL

```sql
SELECT
  ST_MAKEPOLYGON(
    ST_GEOMETRYFROMWKT(
      'LINESTRING(0.0 0.0, 1.0 0.0, 1.0 2.0, 0.0 2.0, 0.0 0.0)'
    )
  ) AS pipeline_polygon;

┌────────────────────────────────┐
│        pipeline_polygon        │
├────────────────────────────────┤
│ POLYGON((0 0,1 0,1 2,0 2,0 0)) │
└────────────────────────────────┘
```
