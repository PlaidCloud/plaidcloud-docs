---
title: ST_TRANSFORM (Lakehouse v1)
description: ST_TRANSFORM — converte um objeto GEOMETRY de um sistema de referência espacial (SRS) para outro.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-transform.md
---

Converte um objeto GEOMETRY de um [sistema de referência espacial (SRS)](https://en.wikipedia.org/wiki/Spatial_reference_system) para outro. Se só precisar de alterar o SRID sem alterar as coordenadas (por exemplo, se o SRID estava incorreto), utilize antes [ST_SETSRID](../st-setsrid).

## Sintaxe SQL

```sql
ST_TRANSFORM(<geometry> [, <from_srid>], <to_srid>)
```

## Argumentos

| Argumentos    | Descrição                                                                                                                                                 |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<geometry>`  | O argumento tem de ser uma expressão do tipo objeto GEOMETRY.                                                                                             |
| `<from_srid>` | SRID opcional que identifica o SRS atual do objeto GEOMETRY de entrada; se este argumento for omitido, utiliza o SRID especificado no objeto GEOMETRY de entrada. |
| `<to_srid>`   | O SRID que identifica o SRS a utilizar; transforma o objeto GEOMETRY de entrada num novo objeto que utiliza este SRS.                                     |

## Tipo de retorno

Geometry.

## Exemplos de SQL

```sql
SET GEOMETRY_OUTPUT_FORMAT = 'EWKT'

SELECT ST_TRANSFORM(ST_GEOMFROMWKT('POINT(389866.35 5819003.03)', 32633), 3857) AS transformed_geom

┌───────────────────────────────────────────────┐
│                transformed_geom               │
├───────────────────────────────────────────────┤
│ SRID=3857;POINT(1489140.093766 6892872.19868) │
└───────────────────────────────────────────────┘

SELECT ST_TRANSFORM(ST_GEOMFROMWKT('POINT(4.500212 52.161170)'), 4326, 28992) AS transformed_geom

┌──────────────────────────────────────────────┐
│               transformed_geom               │
├──────────────────────────────────────────────┤
│ SRID=28992;POINT(94308.670475 464038.168827) │
└──────────────────────────────────────────────┘

```
