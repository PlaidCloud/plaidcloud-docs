---
title: ST_MAKEPOLYGON (Lakehouse v1)
description: ST_MAKEPOLYGON — constrói um objeto GEOMETRY que representa um Polygon sem furos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-makepolygon.md
---

Constrói um objeto GEOMETRY que representa um Polygon sem furos. A função usa a LineString especificada como o laço externo.

## Sintaxe SQL

```sql
ST_MAKEPOLYGON(<geometry>)
```

## Aliases

- [ST_POLYGON](../st-polygon)

## Argumentos

| Argumentos   | Descrição                                            |
|--------------|------------------------------------------------------|
| `<geometry>` | O argumento deve ser uma expressão do tipo GEOMETRY. |

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
