---
title: ST_CIRCLE (Lakehouse v2)
description: ST_CIRCLE — crea una geometría de círculo a partir de la longitud y la latitud del centro y un radio en metros.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-circle.md
---

Crea una geometría de círculo a partir de la longitud y la latitud del centro y un radio en metros.

## Sintaxis de Analyze

```python
func.st_circle(<lng>, <lat>, <radius>)
```

## Ejemplos de Analyze

```python
func.st_circle(0, 0, 100)

┌────────────┐
│ (geometry)  │
└────────────┘
```

## Sintaxis de SQL

```sql
ST_CIRCLE(<lng>, <lat>, <radius>)
```

## Ejemplos de SQL

```sql
SELECT ST_ASTEXT(ST_CIRCLE(0, 0, 100));

┌─────────────────────┐
│ CIRCLE((0, 0), 100)  │
└─────────────────────┘
```
