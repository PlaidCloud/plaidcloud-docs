---
title: ST_X (Lakehouse v2)
description: ST_X — zwraca współrzędną X (długość geograficzną) geometrii punktu.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-x.md
---

Zwraca współrzędną X (długość geograficzną) geometrii punktu.

## Składnia Analyze

```python
func.st_x(<point>)
```

## Przykłady Analyze

```python
func.st_x(func.st_point(1.5, 2.5))

┌─────┐
│ 1.5  │
└─────┘
```

## Składnia SQL

```sql
ST_X(<point>)
```

## Przykłady SQL

```sql
SELECT ST_X(ST_POINT(1.5, 2.5));

┌─────┐
│ 1.5  │
└─────┘
```
