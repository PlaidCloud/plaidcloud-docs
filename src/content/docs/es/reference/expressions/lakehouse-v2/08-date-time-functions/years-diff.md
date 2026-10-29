---
title: YEARS_DIFF (Lakehouse v2)
description: YEARS_DIFF — devuelve el número de años entre dos fechas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/years-diff.md
---

Devuelve el número de años entre dos fechas.

## Sintaxis de Analyze

```python
func.years_diff(<end_date>, <start_date>)
```

## Ejemplos de Analyze

```python
func.years_diff('2029-01-01', '2024-01-01')

┌───┐
│ 5  │
└───┘
```

## Sintaxis de SQL

```sql
YEARS_DIFF(<end_date>, <start_date>)
```

## Ejemplos de SQL

```sql
SELECT YEARS_DIFF('2029-01-01', '2024-01-01');

┌───┐
│ 5  │
└───┘
```
