---
title: WEEKOFYEAR (Lakehouse v2)
description: WEEKOFYEAR — devuelve la semana del año de una fecha. Alias de `WEEK`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weekofyear.md
---

Devuelve la semana del año de una fecha. Alias de `WEEK`.

## Sintaxis de Analyze

```python
func.weekofyear(<date>)
```

## Ejemplos de Analyze

```python
func.weekofyear('2024-06-15')

┌────┐
│ 24  │
└────┘
```

## Sintaxis de SQL

```sql
WEEKOFYEAR(<date>)
```

## Ejemplos de SQL

```sql
SELECT WEEKOFYEAR('2024-06-15');

┌────┐
│ 24  │
└────┘
```
