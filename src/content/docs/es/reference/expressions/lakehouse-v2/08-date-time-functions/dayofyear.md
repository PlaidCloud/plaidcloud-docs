---
title: DAYOFYEAR (Lakehouse v2)
description: DAYOFYEAR — devuelve el día del año de una fecha.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofyear.md
---

Devuelve el día del año de una fecha.

## Sintaxis de Analyze

```python
func.dayofyear(<date>)
```

## Ejemplos de Analyze

```python
func.dayofyear('2024-06-15')

┌─────┐
│ 167  │
└─────┘
```

## Sintaxis de SQL

```sql
DAYOFYEAR(<date>)
```

## Ejemplos de SQL

```sql
SELECT DAYOFYEAR('2024-06-15');

┌─────┐
│ 167  │
└─────┘
```
