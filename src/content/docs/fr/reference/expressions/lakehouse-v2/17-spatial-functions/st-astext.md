---
title: ST_ASTEXT (Lakehouse v2)
description: ST_ASTEXT — convertit une géométrie en sa représentation WKT (Well-Known Text).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-astext.md
---

Convertit une géométrie en sa représentation WKT (Well-Known Text).

## Syntaxe Analyze

```python
func.st_astext(<geometry>)
```

## Exemples Analyze

```python
func.st_astext(func.st_point(1, 2))

┌───────────────┐
│ 'POINT (1 2)'  │
└───────────────┘
```

## Syntaxe SQL

```sql
ST_ASTEXT(<geometry>)
```

## Exemples SQL

```sql
SELECT ST_ASTEXT(ST_POINT(1, 2));

┌─────────────┐
│ POINT (1 2)  │
└─────────────┘
```
