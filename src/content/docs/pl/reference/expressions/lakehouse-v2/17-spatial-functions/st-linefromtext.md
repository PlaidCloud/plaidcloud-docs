---
title: ST_LINEFROMTEXT (Lakehouse v2)
description: ST_LINEFROMTEXT — tworzy geometrię linii z ciągu znaków WKT.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-linefromtext.md
---

Tworzy geometrię linii z ciągu znaków WKT.

## Składnia Analyze

```python
func.st_linefromtext(<wkt>)
```

## Przykłady Analyze

```python
func.st_linefromtext('LINESTRING (0 0, 1 1, 2 2)')

┌────────────┐
│ (geometry)  │
└────────────┘
```

## Składnia SQL

```sql
ST_LINEFROMTEXT(<wkt>)
```

## Przykłady SQL

```sql
SELECT ST_ASTEXT(ST_LINEFROMTEXT('LINESTRING (0 0, 1 1, 2 2)'));

┌────────────────────────────┐
│ LINESTRING (0 0, 1 1, 2 2)  │
└────────────────────────────┘
```
