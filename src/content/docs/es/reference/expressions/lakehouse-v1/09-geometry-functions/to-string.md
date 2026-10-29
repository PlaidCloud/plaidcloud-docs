---
title: "TO_STRING (Geometría, Lakehouse v1)"
description: TO_STRING — convierte un objeto GEOMETRY en una representación de cadena.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/to-string.md
---

Convierte un objeto GEOMETRY en una representación de cadena. El formato de visualización de los datos de salida lo controla el valor de configuración `geometry_output_format`, que admite los siguientes tipos:

| Parámetro         | Descripción                                                         |
|-------------------|---------------------------------------------------------------------|
| GeoJSON (predeterminado) | El resultado GEOMETRY se muestra como un objeto JSON en formato GeoJSON. |
| WKT               | El resultado GEOMETRY se muestra como una cadena en formato WKT.          |
| WKB               | El resultado GEOMETRY se muestra como un binario en formato WKB.          |
| EWKT              | El resultado GEOMETRY se muestra como una cadena en formato EWKT.         |
| EWKB              | El resultado GEOMETRY se muestra como un binario en formato EWKB.         |

## Sintaxis de SQL

```sql
TO_STRING(<geometry>)
```

## Argumentos

| Argumentos   | Descripción                                          |
|--------------|------------------------------------------------------|
| `<geometry>` | El argumento debe ser una expresión de tipo GEOMETRY. |

## Tipo de valor devuelto

Cadena.

## Ejemplos de SQL

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
