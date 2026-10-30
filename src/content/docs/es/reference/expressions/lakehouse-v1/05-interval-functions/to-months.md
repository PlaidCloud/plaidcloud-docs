---
title: TO_MONTHS (Lakehouse v1)
description: TO_MONTHS — convierte un número determinado de meses en un tipo Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-months.md
---

Convierte un número determinado de meses en un tipo Interval.

- Acepta como entrada enteros positivos, cero y enteros negativos.

## Sintaxis de Analyze

```python
func.to_months(<months>)
```

## Ejemplos de Analyze

```python
func.to_months(2)
┌──────────────────────────────────────────────────────┐
│ func.to_months(2)                                    │
├──────────────────────────────────────────────────────┤
│ 2 months                                             │
└──────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
TO_MONTHS(<months>)
```

## Tipo de retorno

Interval (representado en meses).

## Ejemplos de SQL

```sql
SELECT TO_MONTHS(2), TO_MONTHS(0), TO_MONTHS((- 2));

┌──────────────────────────────────────────────┐
│ to_months(2) │ to_months(0) │ to_months(- 2) │
├──────────────┼──────────────┼────────────────┤
│ 2 months     │ 00:00:00     │ -2 months      │
└──────────────────────────────────────────────┘
```
