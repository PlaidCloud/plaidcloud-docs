---
title: LAST_DAY (Lakehouse v2)
description: LAST_DAY — devuelve el último día del mes de una fecha determinada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/last-day.md
---

Devuelve el último día del mes de una fecha determinada.

## Sintaxis de Analyze

```python
func.last_day(<date>[, <unit>])
```

## Ejemplos de Analyze

```python
func.last_day('2024-02-15')

┌──────────────┐
│ '2024-02-29'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
LAST_DAY(<date>[, <unit>])
```

## Ejemplos de SQL

```sql
SELECT LAST_DAY('2024-02-15');

┌────────────┐
│ 2024-02-29  │
└────────────┘
```
