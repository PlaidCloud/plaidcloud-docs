---
title: DAYNAME (Lakehouse v2)
description: DAYNAME — devuelve el nombre del día de la semana de una fecha.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayname.md
---

Devuelve el nombre del día de la semana de una fecha.

## Sintaxis de Analyze

```python
func.dayname(<date>)
```

## Ejemplos de Analyze

```python
func.dayname('2024-06-15')

┌────────────┐
│ 'Saturday'  │
└────────────┘
```

## Sintaxis de SQL

```sql
DAYNAME(<date>)
```

## Ejemplos de SQL

```sql
SELECT DAYNAME('2024-06-15');

┌──────────┐
│ Saturday  │
└──────────┘
```
