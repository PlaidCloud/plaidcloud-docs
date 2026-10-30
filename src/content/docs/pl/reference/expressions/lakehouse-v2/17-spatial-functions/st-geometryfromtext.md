---
title: ST_GEOMETRYFROMTEXT (Lakehouse v2)
description: ST_GEOMETRYFROMTEXT — tworzy geometrię z ciągu znaków WKT (Well-Known Text).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-geometryfromtext.md
---

Tworzy geometrię z ciągu znaków WKT (Well-Known Text).

## Składnia Analyze

```python
func.st_geometryfromtext(<wkt>)
```

## Przykłady Analyze

```python
func.st_geometryfromtext('POINT (1 2)')

┌────────────┐
│ (geometry)  │
└────────────┘
```

## Składnia SQL

```sql
ST_GEOMETRYFROMTEXT(<wkt>)
```

## Przykłady SQL

```sql
SELECT ST_ASTEXT(ST_GEOMETRYFROMTEXT('POINT (1 2)'));

┌─────────────┐
│ POINT (1 2)  │
└─────────────┘
```
