---
title: NEXT_DAY (Lakehouse v1)
description: NEXT_DAY — devolve a data do próximo dia da semana especificado a seguir à data ou ao carimbo de data/hora indicado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/next-day.md
---

Devolve a data do próximo dia da semana especificado a seguir à data ou ao carimbo de data/hora indicado.

## Sintaxe do Analyze

```python
func.next_day(date_expression>, <target_day>)
```

## Exemplos do Analyze

```python
func.next_day(func.to_date('2024-11-13'), 'monday')
┌──────────────────────────────────────────────────────┐
│ func.next_day(func.to_date('2024-11-13'), 'monday')  │
├──────────────────────────────────────────────────────┤
│ 2024-11-18                                           │
└──────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
NEXT_DAY(<date_expression>, <target_day>)
```

| Parâmetro           | Descrição                                                                                                                                                                       |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<date_expression>` | Um valor `DATE` ou `TIMESTAMP` para calcular a próxima ocorrência do dia especificado.                                                                                          |
| `<target_day>`      | O dia da semana de destino cuja próxima ocorrência se pretende encontrar. Os valores aceites incluem `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday` e `sunday`. |

## Tipo de retorno

Data.

## Exemplos SQL

Para encontrar a próxima segunda-feira a seguir a uma data específica, como 2024-11-13:

```sql
SELECT NEXT_DAY(to_date('2024-11-13'), monday) AS next_monday;

┌─────────────┐
│ next_monday │
├─────────────┤
│ 2024-11-18  │
└─────────────┘
```
