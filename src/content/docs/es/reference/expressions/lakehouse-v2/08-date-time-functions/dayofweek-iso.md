---
title: DAYOFWEEK_ISO (Lakehouse v2)
description: DAYOFWEEK_ISO — devuelve el índice ISO del día de la semana de una fecha (1 = lunes, 7 = domingo).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofweek-iso.md
---

Devuelve el índice ISO del día de la semana de una fecha (1 = lunes, 7 = domingo).

## Sintaxis de Analyze

```python
func.dayofweek_iso(<date>)
```

## Ejemplos de Analyze

```python
func.dayofweek_iso('2024-06-15')

┌───┐
│ 6  │
└───┘
```

## Sintaxis de SQL

```sql
DAYOFWEEK_ISO(<date>)
```

## Ejemplos de SQL

```sql
SELECT DAYOFWEEK_ISO('2024-06-15');

┌───┐
│ 6  │
└───┘
```
