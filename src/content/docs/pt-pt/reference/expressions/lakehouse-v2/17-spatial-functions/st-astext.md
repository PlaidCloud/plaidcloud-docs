---
title: ST_ASTEXT (Lakehouse v2)
description: ST_ASTEXT — converte uma geometria na sua representação WKT (Well-Known Text).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-astext.md
---

Converte uma geometria na sua representação WKT (Well-Known Text).

## Sintaxe de Analyze

```python
func.st_astext(<geometry>)
```

## Exemplos de Analyze

```python
func.st_astext(func.st_point(1, 2))

┌───────────────┐
│ 'POINT (1 2)'  │
└───────────────┘
```

## Sintaxe SQL

```sql
ST_ASTEXT(<geometry>)
```

## Exemplos SQL

```sql
SELECT ST_ASTEXT(ST_POINT(1, 2));

┌─────────────┐
│ POINT (1 2)  │
└─────────────┘
```
