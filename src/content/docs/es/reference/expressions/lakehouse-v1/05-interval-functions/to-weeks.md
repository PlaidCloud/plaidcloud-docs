---
title: TO_WEEKS (Lakehouse v1)
description: TO_WEEKS — convierte un número determinado de semanas en un tipo Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-weeks.md
---

Convierte un número determinado de semanas en un tipo Interval.

- Acepta como entrada enteros positivos, cero y enteros negativos.

## Sintaxis de Analyze

```python
func.to_weeks(<weeks>)
```

## Ejemplos de Analyze

```python
func.to_weeks(2)
┌──────────────────────────────────────────────────────┐
│ func.to_weeks(2)                                     │
├──────────────────────────────────────────────────────┤
│ 14 days                                              │
└──────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
TO_WEEKS(<weeks>)
```

## Tipo de retorno

Interval (representado en días).

## Ejemplos de SQL

```sql
SELECT TO_WEEKS(2), TO_WEEKS(0), TO_WEEKS((- 2));

┌───────────────────────────────────────────┐
│ to_weeks(2) │ to_weeks(0) │ to_weeks(- 2) │
├─────────────┼─────────────┼───────────────┤
│ 14 days     │ 00:00:00    │ -14 days      │
└───────────────────────────────────────────┘
```
