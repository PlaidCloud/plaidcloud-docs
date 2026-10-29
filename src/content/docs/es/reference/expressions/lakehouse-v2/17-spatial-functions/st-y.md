---
title: ST_Y (Lakehouse v2)
description: ST_Y — Devuelve la coordenada Y (latitud) de una geometría de punto.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-y.md
---

Devuelve la coordenada Y (latitud) de una geometría de punto.

## Sintaxis de Analyze

```python
func.st_y(<point>)
```

## Ejemplos de Analyze

```python
func.st_y(func.st_point(1.5, 2.5))

┌─────┐
│ 2.5  │
└─────┘
```

## Sintaxis de SQL

```sql
ST_Y(<point>)
```

## Ejemplos de SQL

```sql
SELECT ST_Y(ST_POINT(1.5, 2.5));

┌─────┐
│ 2.5  │
└─────┘
```
