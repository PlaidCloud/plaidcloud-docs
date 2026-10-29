---
title: ST_SETSRID (Lakehouse v1)
description: ST_SETSRID — retorna um objeto GEOMETRY com o SRID (identificador do sistema de referência espacial) definido.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-setsrid.md
---

Retorna um objeto GEOMETRY com o [SRID (identificador do sistema de referência espacial)](https://en.wikipedia.org/wiki/Spatial_reference_system#Identifier) definido com o valor especificado. Esta função altera apenas o SRID, sem afetar as coordenadas do objeto. Se você também precisar alterar as coordenadas para corresponder ao novo SRS (sistema de referência espacial), use [ST_TRANSFORM](../st-transform).

## Sintaxe SQL

```sql
ST_SETSRID(<geometry>, <srid>)
```

## Argumentos

| Argumentos   | Descrição                                                    |
|--------------|--------------------------------------------------------------|
| `<geometry>` | O argumento deve ser uma expressão do tipo objeto GEOMETRY.  |
| `<srid>`     | O inteiro SRID a definir no objeto GEOMETRY retornado.       |

## Tipo de retorno

Geometry.

## Exemplos de SQL

```sql
SET GEOMETRY_OUTPUT_FORMAT = 'EWKT'

SELECT ST_SETSRID(TO_GEOMETRY('POINT(13 51)'), 4326) AS geometry

┌────────────────────────┐
│        geometry        │
├────────────────────────┤
│ SRID=4326;POINT(13 51) │
└────────────────────────┘

```
