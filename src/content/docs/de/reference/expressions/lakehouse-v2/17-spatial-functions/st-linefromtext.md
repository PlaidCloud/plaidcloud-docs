---
title: ST_LINEFROMTEXT (Lakehouse v2)
description: ST_LINEFROMTEXT – erstellt eine Liniengeometrie aus einer WKT-Zeichenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-linefromtext.md
---

Erstellt eine Liniengeometrie aus einer WKT-Zeichenfolge.

## Analyze-Syntax

```python
func.st_linefromtext(<wkt>)
```

## Analyze-Beispiele

```python
func.st_linefromtext('LINESTRING (0 0, 1 1, 2 2)')

┌────────────┐
│ (geometry)  │
└────────────┘
```

## SQL-Syntax

```sql
ST_LINEFROMTEXT(<wkt>)
```

## SQL-Beispiele

```sql
SELECT ST_ASTEXT(ST_LINEFROMTEXT('LINESTRING (0 0, 1 1, 2 2)'));

┌────────────────────────────┐
│ LINESTRING (0 0, 1 1, 2 2)  │
└────────────────────────────┘
```
