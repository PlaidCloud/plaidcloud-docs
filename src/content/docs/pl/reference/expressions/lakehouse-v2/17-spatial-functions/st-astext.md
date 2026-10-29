---
title: ST_ASTEXT (Lakehouse v2)
description: ST_ASTEXT — konwertuje geometrię na jej reprezentację WKT (Well-Known Text).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-astext.md
---

Konwertuje geometrię na jej reprezentację WKT (Well-Known Text).

## Składnia Analyze

```python
func.st_astext(<geometry>)
```

## Przykłady Analyze

```python
func.st_astext(func.st_point(1, 2))

┌───────────────┐
│ 'POINT (1 2)'  │
└───────────────┘
```

## Składnia SQL

```sql
ST_ASTEXT(<geometry>)
```

## Przykłady SQL

```sql
SELECT ST_ASTEXT(ST_POINT(1, 2));

┌─────────────┐
│ POINT (1 2)  │
└─────────────┘
```
