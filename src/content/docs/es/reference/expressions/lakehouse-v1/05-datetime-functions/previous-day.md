---
title: PREVIOUS_DAY (Lakehouse v1)
description: PREVIOUS_DAY — devuelve la fecha del día de la semana especificado más reciente anterior a la fecha dada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/previous-day.md
---

Devuelve la fecha del día de la semana especificado más reciente anterior a la fecha o marca de tiempo dada.

## Sintaxis de Analyze

```python
func.next_day(date_expression>, <target_day>)
```

## Ejemplos de Analyze

```python
func.next_day(func.to_date('2024-11-13'), 'friday')
┌──────────────────────────────────────────────────────┐
│ func.next_day(func.to_date('2024-11-13'), 'friday')  │
├──────────────────────────────────────────────────────┤
│ 2024-11-08                                           │
└──────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
PREVIOUS_DAY(<date_expression>, <target_day>)
```

| Parámetro           | Descripción                                                                                                                                                              |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<date_expression>` | Un valor `DATE` o `TIMESTAMP` para calcular la aparición anterior del día especificado.                                                                                  |
| `<target_day>`      | El día de la semana objetivo del que se busca la aparición anterior. Los valores admitidos incluyen `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday` y `sunday`. |

## Tipo de valor devuelto

Fecha.

## Ejemplos de SQL

Si necesita encontrar el viernes anterior a una fecha dada, como 2024-11-13:

```sql
SELECT PREVIOUS_DAY(to_date('2024-11-13'), friday) AS last_friday;

┌─────────────┐
│ last_friday │
├─────────────┤
│ 2024-11-08  │
└─────────────┘
```
