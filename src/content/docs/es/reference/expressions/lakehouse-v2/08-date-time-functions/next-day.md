---
title: NEXT_DAY (Lakehouse v2)
description: NEXT_DAY — devuelve la fecha del siguiente día de la semana especificado posterior a una fecha dada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/next-day.md
---

Devuelve la fecha del siguiente día de la semana especificado posterior a una fecha dada.

## Sintaxis de Analyze

```python
func.next_day(<date>, <weekday>)
```

## Ejemplos de Analyze

```python
func.next_day('2024-06-15', 'Monday')

┌──────────────┐
│ '2024-06-17'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
NEXT_DAY(<date>, <weekday>)
```

## Ejemplos de SQL

```sql
SELECT NEXT_DAY('2024-06-15', 'Monday');

┌────────────┐
│ 2024-06-17  │
└────────────┘
```
