---
title: NEXT_DAY (Lakehouse v1)
description: NEXT_DAY — devuelve la fecha del próximo día de la semana especificado posterior a la fecha o marca de tiempo dada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/next-day.md
---

Devuelve la fecha del próximo día de la semana especificado posterior a la fecha o marca de tiempo dada.

## Sintaxis de Analyze

```python
func.next_day(date_expression>, <target_day>)
```

## Ejemplos de Analyze

```python
func.next_day(func.to_date('2024-11-13'), 'monday')
┌──────────────────────────────────────────────────────┐
│ func.next_day(func.to_date('2024-11-13'), 'monday')  │
├──────────────────────────────────────────────────────┤
│ 2024-11-18                                           │
└──────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
NEXT_DAY(<date_expression>, <target_day>)
```

| Parámetro           | Descripción                                                                                                                                                              |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<date_expression>` | Un valor `DATE` o `TIMESTAMP` para calcular la siguiente aparición del día especificado.                                                                                 |
| `<target_day>`      | El día de la semana objetivo del que se busca la siguiente aparición. Los valores admitidos incluyen `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday` y `sunday`. |

## Tipo de valor devuelto

Fecha.

## Ejemplos de SQL

Para encontrar el próximo lunes posterior a una fecha concreta, como 2024-11-13:

```sql
SELECT NEXT_DAY(to_date('2024-11-13'), monday) AS next_monday;

┌─────────────┐
│ next_monday │
├─────────────┤
│ 2024-11-18  │
└─────────────┘
```
