---
title: DAYS_DIFF (Lakehouse v2)
description: DAYS_DIFF — devuelve el número de días entre dos fechas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/days-diff.md
---

Devuelve el número de días entre dos fechas.

## Sintaxis de Analyze

```python
func.days_diff(<end_date>, <start_date>)
```

## Ejemplos de Analyze

```python
func.days_diff('2024-03-01', '2024-01-01')

┌────┐
│ 60  │
└────┘
```

## Sintaxis de SQL

```sql
DAYS_DIFF(<end_date>, <start_date>)
```

## Ejemplos de SQL

```sql
SELECT DAYS_DIFF('2024-03-01', '2024-01-01');

┌────┐
│ 60  │
└────┘
```
