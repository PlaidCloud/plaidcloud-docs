---
title: ST_SETSRID (Lakehouse v1)
description: ST_SETSRID — devolve um objeto GEOMETRY com o respetivo SRID (identificador do sistema de referência espacial) definido para o valor especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-setsrid.md
---

Devolve um objeto GEOMETRY com o respetivo [SRID (identificador do sistema de referência espacial)](https://en.wikipedia.org/wiki/Spatial_reference_system#Identifier) definido para o valor especificado. Esta função altera apenas o SRID, sem afetar as coordenadas do objeto. Se também precisar de alterar as coordenadas para corresponderem ao novo SRS (sistema de referência espacial), utilize antes [ST_TRANSFORM](../st-transform).

## Sintaxe SQL

```sql
ST_SETSRID(<geometry>, <srid>)
```

## Argumentos

| Argumentos   | Descrição                                                   |
|--------------|-------------------------------------------------------------|
| `<geometry>` | O argumento tem de ser uma expressão do tipo objeto GEOMETRY. |
| `<srid>`     | O número inteiro do SRID a definir no objeto GEOMETRY devolvido. |

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
