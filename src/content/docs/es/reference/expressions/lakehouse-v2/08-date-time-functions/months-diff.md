---
title: MONTHS_DIFF (Lakehouse v2)
description: MONTHS_DIFF — devuelve el número de meses entre dos fechas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/months-diff.md
---

Devuelve el número de meses entre dos fechas.

## Sintaxis de Analyze

```python
func.months_diff(<end_date>, <start_date>)
```

## Ejemplos de Analyze

```python
func.months_diff('2024-06-01', '2024-01-01')

┌───┐
│ 5  │
└───┘
```

## Sintaxis de SQL

```sql
MONTHS_DIFF(<end_date>, <start_date>)
```

## Ejemplos de SQL

```sql
SELECT MONTHS_DIFF('2024-06-01', '2024-01-01');

┌───┐
│ 5  │
└───┘
```
