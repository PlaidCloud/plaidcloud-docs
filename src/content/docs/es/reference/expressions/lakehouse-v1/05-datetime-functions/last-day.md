---
title: LAST_DAY (Lakehouse v1)
description: LAST_DAY — devuelve el último día del intervalo especificado (semana, mes, trimestre o año).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/last-day.md
---

Devuelve el último día del intervalo especificado (semana, mes, trimestre o año) a partir de la fecha o marca de tiempo proporcionada.

## Sintaxis de Analyze

```python
func.last_day(<date_expression>, <interval>)
```

## Ejemplos de Analyze

```python
func.last_day(func.to_date('2024-11-13'), 'month')
┌──────────────────────────────────────────────────────┐
│ func.last_day(func.to_date('2024-11-13'), 'month')   │
├──────────────────────────────────────────────────────┤
│ 2024-11-30                                           │
└──────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
LAST_DAY(<date_expression>, <interval>)
```

| Parámetro           | Descripción                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------------------|
| `<date_expression>` | Un valor DATE o TIMESTAMP para calcular el último día del intervalo especificado.                             |
| `<interval>`        | El tipo de intervalo del que se busca el último día. Los valores admitidos son `week`, `month`, `quarter` y `year`. |

## Tipo de valor devuelto

Fecha.

## Ejemplos de SQL

Supongamos que desea determinar la fecha de facturación, que siempre es el último día del mes, a partir de una fecha arbitraria de una transacción (por ejemplo, 2024-11-13):

```sql
SELECT LAST_DAY(to_date('2024-11-13'), month) AS billing_date;

┌──────────────┐
│ billing_date │
├──────────────┤
│ 2024-11-30   │
└──────────────┘
```
