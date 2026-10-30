---
title: ST_POINT (Lakehouse v2)
description: ST_POINT — Crea una geometría de punto a partir de valores de longitud y latitud.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-point.md
---

Crea una geometría de punto a partir de valores de longitud y latitud.

## Sintaxis de Analyze

```python
func.st_point(<lng>, <lat>)
```

## Ejemplos de Analyze

```python
func.st_point(-73.9857, 40.7484)

┌────────────┐
│ (geometry)  │
└────────────┘
```

## Sintaxis de SQL

```sql
ST_POINT(<lng>, <lat>)
```

## Ejemplos de SQL

```sql
SELECT ST_ASTEXT(ST_POINT(-73.9857, 40.7484));

┌──────────────────────────┐
│ POINT (-73.9857 40.7484)  │
└──────────────────────────┘
```
