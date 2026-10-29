---
title: "TO_STRING (Geometria, Lakehouse v1)"
description: TO_STRING — converte um objeto GEOMETRY em uma representação String.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/to-string.md
---

Converte um objeto GEOMETRY em uma representação String. O formato de exibição dos dados de saída é controlado pela configuração `geometry_output_format`, que contém os seguintes tipos:

| Parâmetro         | Descrição                                                              |
|-------------------|------------------------------------------------------------------------|
| GeoJSON (padrão)  | O resultado GEOMETRY é renderizado como um objeto JSON no formato GeoJSON. |
| WKT               | O resultado GEOMETRY é renderizado como uma String no formato WKT.     |
| WKB               | O resultado GEOMETRY é renderizado como um Binary no formato WKB.      |
| EWKT              | O resultado GEOMETRY é renderizado como uma String no formato EWKT.    |
| EWKB              | O resultado GEOMETRY é renderizado como um Binary no formato EWKB.     |

## Sintaxe SQL

```sql
TO_STRING(<geometry>)
```

## Argumentos

| Argumentos   | Descrição                                            |
|--------------|------------------------------------------------------|
| `<geometry>` | O argumento deve ser uma expressão do tipo GEOMETRY. |

## Tipo de retorno

String.

## Exemplos de SQL

```sql
SET geometry_output_format='GeoJSON';

SELECT
  TO_GEOMETRY(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;LINESTRING(400000 6000000, 401000 6010000)'
    )
  ) AS pipeline_geometry;

┌────────────────────────────────────────────────────────────────────────────┐
│                              pipeline_geometry                             │
├────────────────────────────────────────────────────────────────────────────┤
│ {"type": "LineString", "coordinates": [[400000,6000000],[401000,6010000]]} │
└────────────────────────────────────────────────────────────────────────────┘

SET geometry_output_format='WKT';

SELECT
  TO_GEOMETRY(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;LINESTRING(400000 6000000, 401000 6010000)'
    )
  ) AS pipeline_geometry;

┌───────────────────────────────────────────┐
│             pipeline_geometry             │
├───────────────────────────────────────────┤
│ LINESTRING(400000 6000000,401000 6010000) │
└───────────────────────────────────────────┘

SET geometry_output_format='EWKT';

SELECT
  TO_GEOMETRY(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;LINESTRING(400000 6000000, 401000 6010000)'
    )
  ) AS pipeline_geometry;

┌─────────────────────────────────────────────────────┐
│                  pipeline_geometry                  │
├─────────────────────────────────────────────────────┤
│ SRID=4326;LINESTRING(400000 6000000,401000 6010000) │
└─────────────────────────────────────────────────────┘

SET geometry_output_format='WKB';

SELECT
  TO_GEOMETRY(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;LINESTRING(400000 6000000, 401000 6010000)'
    )
  ) AS pipeline_geometry;

┌────────────────────────────────────────────────────────────────────────────────────┐
│                                  pipeline_geometry                                 │
├────────────────────────────────────────────────────────────────────────────────────┤
│ 01020000000200000000000000006A18410000000060E3564100000000A07918410000000024ED5641 │
└────────────────────────────────────────────────────────────────────────────────────┘

SET geometry_output_format='EWKB';

SELECT
  TO_GEOMETRY(
    ST_GEOMETRYFROMWKT(
      'SRID=4326;LINESTRING(400000 6000000, 401000 6010000)'
    )
  ) AS pipeline_geometry;

┌────────────────────────────────────────────────────────────────────────────────────────────┐
│                                      pipeline_geometry                                     │
├────────────────────────────────────────────────────────────────────────────────────────────┤
│ 0102000020E61000000200000000000000006A18410000000060E3564100000000A07918410000000024ED5641 │
└────────────────────────────────────────────────────────────────────────────────────────────┘
```
