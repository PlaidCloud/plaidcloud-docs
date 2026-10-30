---
title: TO_DAYS (Lakehouse v1)
description: TO_DAYS — convierte un número determinado de días en un tipo Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-days.md
---

Convierte un número determinado de días en un tipo Interval.

- Acepta como entrada enteros positivos, cero y enteros negativos.

## Sintaxis de Analyze

```python
func.to_days(<days>)
```

## Ejemplos de Analyze

```python
func.to_days(2)
┌──────────────────────────────────────────────────────┐
│ func.to_days(2)                                      │
├──────────────────────────────────────────────────────┤
│ 200 days                                             │
└──────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
TO_DAYS(<days>)
```

## Tipo de retorno

Interval (representado en días).

## Ejemplos de SQL

```sql
SELECT TO_DAYS(2), TO_DAYS(0), TO_DAYS(-2);

┌────────────────────────────────────────┐
│ to_days(2) │ to_days(0) │ to_days(- 2) │
├────────────┼────────────┼──────────────┤
│ 2 days     │ 00:00:00   │ -2 days      │
└────────────────────────────────────────┘
```
