---
title: ST_Y (Lakehouse v2)
description: ST_Y — zwraca współrzędną Y (szerokość geograficzną) geometrii punktu.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-y.md
---

Zwraca współrzędną Y (szerokość geograficzną) geometrii punktu.

## Składnia Analyze

```python
func.st_y(<point>)
```

## Przykłady Analyze

```python
func.st_y(func.st_point(1.5, 2.5))

┌─────┐
│ 2.5  │
└─────┘
```

## Składnia SQL

```sql
ST_Y(<point>)
```

## Przykłady SQL

```sql
SELECT ST_Y(ST_POINT(1.5, 2.5));

┌─────┐
│ 2.5  │
└─────┘
```
