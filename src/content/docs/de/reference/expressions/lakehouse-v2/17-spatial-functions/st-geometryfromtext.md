---
title: ST_GEOMETRYFROMTEXT (Lakehouse v2)
description: ST_GEOMETRYFROMTEXT – erstellt eine Geometrie aus einer WKT-Zeichenfolge (Well-Known Text).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-geometryfromtext.md
---

Erstellt eine Geometrie aus einer WKT-Zeichenfolge (Well-Known Text).

## Analyze-Syntax

```python
func.st_geometryfromtext(<wkt>)
```

## Analyze-Beispiele

```python
func.st_geometryfromtext('POINT (1 2)')

┌────────────┐
│ (geometry)  │
└────────────┘
```

## SQL-Syntax

```sql
ST_GEOMETRYFROMTEXT(<wkt>)
```

## SQL-Beispiele

```sql
SELECT ST_ASTEXT(ST_GEOMETRYFROMTEXT('POINT (1 2)'));

┌─────────────┐
│ POINT (1 2)  │
└─────────────┘
```
