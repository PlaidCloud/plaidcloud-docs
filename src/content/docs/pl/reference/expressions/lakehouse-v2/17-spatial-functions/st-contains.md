---
title: ST_CONTAINS (Lakehouse v2)
description: ST_CONTAINS — sprawdza, czy jedna geometria zawiera drugą. Zwraca 1, jeśli tak.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-contains.md
---

Sprawdza, czy jedna geometria zawiera drugą. Zwraca 1, jeśli tak.

## Składnia Analyze

```python
func.st_contains(<geometry1>, <geometry2>)
```

## Przykłady Analyze

```python
func.st_contains(get_column(table, 'area'), func.st_point(1, 1))

┌───┐
│ 1  │
└───┘
```

## Składnia SQL

```sql
ST_CONTAINS(<geometry1>, <geometry2>)
```

## Przykłady SQL

```sql
SELECT ST_CONTAINS(ST_GeomFromText('POLYGON((0 0,10 0,10 10,0 10,0 0))'), ST_POINT(5, 5));

┌───┐
│ 1  │
└───┘
```
