---
title: MONTH (Lakehouse v2)
description: MONTH — devuelve el mes de una fecha.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/month.md
---

Devuelve el mes de una fecha.

## Sintaxis de Analyze

```python
func.month(<date>)
```

## Ejemplos de Analyze

```python
func.month('2024-06-15')

┌───┐
│ 6  │
└───┘
```

## Sintaxis de SQL

```sql
MONTH(<date>)
```

## Ejemplos de SQL

```sql
SELECT MONTH('2024-06-15');

┌───┐
│ 6  │
└───┘
```
