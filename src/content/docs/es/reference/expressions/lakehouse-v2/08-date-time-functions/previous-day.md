---
title: PREVIOUS_DAY (Lakehouse v2)
description: PREVIOUS_DAY — devuelve la fecha del día de la semana especificado anterior a una fecha dada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/previous-day.md
---

Devuelve la fecha del día de la semana especificado anterior a una fecha dada.

## Sintaxis de Analyze

```python
func.previous_day(<date>, <weekday>)
```

## Ejemplos de Analyze

```python
func.previous_day('2024-06-15', 'Monday')

┌──────────────┐
│ '2024-06-10'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
PREVIOUS_DAY(<date>, <weekday>)
```

## Ejemplos de SQL

```sql
SELECT PREVIOUS_DAY('2024-06-15', 'Monday');

┌────────────┐
│ 2024-06-10  │
└────────────┘
```
