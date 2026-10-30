---
title: DAY (Lakehouse v2)
description: DAY — devuelve el día del mes de una fecha.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/day.md
---

Devuelve el día del mes de una fecha.

## Sintaxis de Analyze

```python
func.day(<date>)
```

## Ejemplos de Analyze

```python
func.day('2024-06-15')

┌────┐
│ 15  │
└────┘
```

## Sintaxis de SQL

```sql
DAY(<date>)
```

## Ejemplos de SQL

```sql
SELECT DAY('2024-06-15');

┌────┐
│ 15  │
└────┘
```
