---
title: ST_POINT (Lakehouse v2)
description: ST_POINT — tworzy geometrię punktu na podstawie wartości długości i szerokości geograficznej.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-point.md
---

Tworzy geometrię punktu na podstawie wartości długości i szerokości geograficznej.

## Składnia Analyze

```python
func.st_point(<lng>, <lat>)
```

## Przykłady Analyze

```python
func.st_point(-73.9857, 40.7484)

┌────────────┐
│ (geometry)  │
└────────────┘
```

## Składnia SQL

```sql
ST_POINT(<lng>, <lat>)
```

## Przykłady SQL

```sql
SELECT ST_ASTEXT(ST_POINT(-73.9857, 40.7484));

┌──────────────────────────┐
│ POINT (-73.9857 40.7484)  │
└──────────────────────────┘
```
