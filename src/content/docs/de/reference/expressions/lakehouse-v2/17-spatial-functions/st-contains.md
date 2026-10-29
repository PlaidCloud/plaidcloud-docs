---
title: ST_CONTAINS (Lakehouse v2)
description: ST_CONTAINS – prüft, ob eine Geometrie eine andere enthält. Gibt 1 zurück, wenn dies zutrifft.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-contains.md
---

Prüft, ob eine Geometrie eine andere enthält. Gibt 1 zurück, wenn dies zutrifft.

## Analyze-Syntax

```python
func.st_contains(<geometry1>, <geometry2>)
```

## Analyze-Beispiele

```python
func.st_contains(get_column(table, 'area'), func.st_point(1, 1))

┌───┐
│ 1  │
└───┘
```

## SQL-Syntax

```sql
ST_CONTAINS(<geometry1>, <geometry2>)
```

## SQL-Beispiele

```sql
SELECT ST_CONTAINS(ST_GeomFromText('POLYGON((0 0,10 0,10 10,0 10,0 0))'), ST_POINT(5, 5));

┌───┐
│ 1  │
└───┘
```
