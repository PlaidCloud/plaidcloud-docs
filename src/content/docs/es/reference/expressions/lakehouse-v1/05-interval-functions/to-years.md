---
title: TO_YEARS (Lakehouse v1)
description: TO_YEARS — convierte un número determinado de años en un tipo Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-years.md
---

Convierte un número determinado de años en un tipo Interval.

- Acepta como entrada enteros positivos, cero y enteros negativos.

## Sintaxis de Analyze

```python
func.to_years(<years>)
```

## Ejemplos de Analyze

```python
func.to_years(2)
┌──────────────────────────────────────────────────────┐
│ func.to_years(2)                                     │
├──────────────────────────────────────────────────────┤
│ 2 years                                              │
└──────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
TO_YEARS(<years>)
```

## Tipo de retorno

Interval (representado en años).

## Ejemplos de SQL

```sql
SELECT TO_YEARS(2), TO_YEARS(0), TO_YEARS((- 2));

┌───────────────────────────────────────────┐
│ to_years(2) │ to_years(0) │ to_years(- 2) │
├─────────────┼─────────────┼───────────────┤
│ 2 years     │ 00:00:00    │ -2 years      │
└───────────────────────────────────────────┘
```
