---
title: WEEK (Lakehouse v2)
description: WEEK — devuelve el número de semana del año de una fecha.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/week.md
---

Devuelve el número de semana del año de una fecha.

## Sintaxis de Analyze

```python
func.week(<date>[, <mode>])
```

## Ejemplos de Analyze

```python
func.week('2024-06-15')

┌────┐
│ 24  │
└────┘
```

## Sintaxis de SQL

```sql
WEEK(<date>[, <mode>])
```

## Ejemplos de SQL

```sql
SELECT WEEK('2024-06-15');

┌────┐
│ 24  │
└────┘
```
