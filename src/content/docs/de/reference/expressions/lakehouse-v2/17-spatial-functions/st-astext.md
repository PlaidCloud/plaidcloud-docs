---
title: ST_ASTEXT (Lakehouse v2)
description: ST_ASTEXT – wandelt eine Geometrie in ihre WKT-Darstellung (Well-Known Text) um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-astext.md
---

Wandelt eine Geometrie in ihre WKT-Darstellung (Well-Known Text) um.

## Analyze-Syntax

```python
func.st_astext(<geometry>)
```

## Analyze-Beispiele

```python
func.st_astext(func.st_point(1, 2))

┌───────────────┐
│ 'POINT (1 2)'  │
└───────────────┘
```

## SQL-Syntax

```sql
ST_ASTEXT(<geometry>)
```

## SQL-Beispiele

```sql
SELECT ST_ASTEXT(ST_POINT(1, 2));

┌─────────────┐
│ POINT (1 2)  │
└─────────────┘
```
