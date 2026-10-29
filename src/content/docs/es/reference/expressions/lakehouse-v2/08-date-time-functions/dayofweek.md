---
title: DAYOFWEEK (Lakehouse v2)
description: DAYOFWEEK — devuelve el índice del día de la semana de una fecha (1 = domingo, 7 = sábado).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofweek.md
---

Devuelve el índice del día de la semana de una fecha (1 = domingo, 7 = sábado).

## Sintaxis de Analyze

```python
func.dayofweek(<date>)
```

## Ejemplos de Analyze

```python
func.dayofweek('2024-06-15')

┌───┐
│ 7  │
└───┘
```

## Sintaxis de SQL

```sql
DAYOFWEEK(<date>)
```

## Ejemplos de SQL

```sql
SELECT DAYOFWEEK('2024-06-15');

┌───┐
│ 7  │
└───┘
```
