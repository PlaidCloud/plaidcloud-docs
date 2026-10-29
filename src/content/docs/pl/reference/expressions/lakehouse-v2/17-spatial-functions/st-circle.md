---
title: ST_CIRCLE (Lakehouse v2)
description: ST_CIRCLE — tworzy geometrię koła na podstawie długości i szerokości geograficznej środka oraz promienia w metrach.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-circle.md
---

Tworzy geometrię koła na podstawie długości i szerokości geograficznej środka oraz promienia w metrach.

## Składnia Analyze

```python
func.st_circle(<lng>, <lat>, <radius>)
```

## Przykłady Analyze

```python
func.st_circle(0, 0, 100)

┌────────────┐
│ (geometry)  │
└────────────┘
```

## Składnia SQL

```sql
ST_CIRCLE(<lng>, <lat>, <radius>)
```

## Przykłady SQL

```sql
SELECT ST_ASTEXT(ST_CIRCLE(0, 0, 100));

┌─────────────────────┐
│ CIRCLE((0, 0), 100)  │
└─────────────────────┘
```
