---
title: ST_ASTEXT (Lakehouse v2)
description: ST_ASTEXT — convierte una geometría en su representación WKT (Well-Known Text).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-astext.md
---

Convierte una geometría en su representación WKT (Well-Known Text).

## Sintaxis de Analyze

```python
func.st_astext(<geometry>)
```

## Ejemplos de Analyze

```python
func.st_astext(func.st_point(1, 2))

┌───────────────┐
│ 'POINT (1 2)'  │
└───────────────┘
```

## Sintaxis de SQL

```sql
ST_ASTEXT(<geometry>)
```

## Ejemplos de SQL

```sql
SELECT ST_ASTEXT(ST_POINT(1, 2));

┌─────────────┐
│ POINT (1 2)  │
└─────────────┘
```
