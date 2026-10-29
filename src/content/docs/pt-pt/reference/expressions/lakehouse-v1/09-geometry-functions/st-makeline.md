---
title: ST_MAKELINE (Lakehouse v1)
description: ST_MAKELINE — constrói um objeto GEOMETRY que representa uma linha que liga os pontos dos dois objetos GEOMETRY de entrada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-makeline.md
---

Constrói um objeto GEOMETRY que representa uma linha que liga os pontos dos dois objetos GEOMETRY de entrada.

## Sintaxe SQL

```sql
ST_MAKELINE(<geometry1>, <geometry2>)
```

## Aliases

- [ST_MAKE_LINE](../st-make-line)

## Argumentos

| Argumentos    | Descrição                                                                                                   |
|---------------|-------------------------------------------------------------------------------------------------------------|
| `<geometry1>` | Um objeto GEOMETRY que contém os pontos a ligar. Este objeto tem de ser um Point, um MultiPoint ou uma LineString. |
| `<geometry2>` | Um objeto GEOMETRY que contém os pontos a ligar. Este objeto tem de ser um Point, um MultiPoint ou uma LineString. |

## Tipo de retorno

Geometry.

## Exemplos de SQL

```sql
SELECT
  ST_MAKELINE(
    ST_GEOMETRYFROMWKT(
      'POINT(-122.306100 37.554162)'
    ),
    ST_GEOMETRYFROMWKT(
      'POINT(-104.874173 56.714538)'
    )
  ) AS pipeline_line;

┌───────────────────────────────────────────────────────┐
│                     pipeline_line                     │
├───────────────────────────────────────────────────────┤
│ LINESTRING(-122.3061 37.554162,-104.874173 56.714538) │
└───────────────────────────────────────────────────────┘
```
