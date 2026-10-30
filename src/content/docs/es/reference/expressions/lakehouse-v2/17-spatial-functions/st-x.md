---
title: ST_X (Lakehouse v2)
description: ST_X — Devuelve la coordenada X (longitud) de una geometría de punto.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-x.md
---

Devuelve la coordenada X (longitud) de una geometría de punto.

## Sintaxis de Analyze

```python
func.st_x(<point>)
```

## Ejemplos de Analyze

```python
func.st_x(func.st_point(1.5, 2.5))

┌─────┐
│ 1.5  │
└─────┘
```

## Sintaxis de SQL

```sql
ST_X(<point>)
```

## Ejemplos de SQL

```sql
SELECT ST_X(ST_POINT(1.5, 2.5));

┌─────┐
│ 1.5  │
└─────┘
```
