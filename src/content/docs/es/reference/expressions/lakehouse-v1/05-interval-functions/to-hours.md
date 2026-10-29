---
title: TO_HOURS (Lakehouse v1)
description: TO_HOURS — convierte un número determinado de horas en un tipo Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-hours.md
---

Convierte un número determinado de horas en un tipo Interval.

- Acepta como entrada enteros positivos, cero y enteros negativos.

## Sintaxis de Analyze

```python
func.to_hours(<hours>)
```

## Ejemplos de Analyze

```python
func.to_hours(2)
┌──────────────────────────────────────────────────────┐
│ func.to_hours(2)                                     │
├──────────────────────────────────────────────────────┤
│ 2:00:00                                              │
└──────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
TO_HOURS(<hours>)
```

## Tipo de retorno

Interval (con el formato `hh:mm:ss`).

## Ejemplos de SQL

```sql
SELECT TO_HOURS(2), TO_HOURS(0), TO_HOURS((- 2));

┌───────────────────────────────────────────┐
│ to_hours(2) │ to_hours(0) │ to_hours(- 2) │
├─────────────┼─────────────┼───────────────┤
│ 2:00:00     │ 00:00:00    │ -2:00:00      │
└───────────────────────────────────────────┘
```
