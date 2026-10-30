---
title: WEEKDAY (Lakehouse v2)
description: WEEKDAY — devuelve el índice del día de la semana de una fecha (0=lunes, 6=domingo).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weekday.md
---

Devuelve el índice del día de la semana de una fecha (0=lunes, 6=domingo).

## Sintaxis de Analyze

```python
func.weekday(<date>)
```

## Ejemplos de Analyze

```python
func.weekday('2024-06-15')

┌───┐
│ 5  │
└───┘
```

## Sintaxis de SQL

```sql
WEEKDAY(<date>)
```

## Ejemplos de SQL

```sql
SELECT WEEKDAY('2024-06-15');

┌───┐
│ 5  │
└───┘
```
