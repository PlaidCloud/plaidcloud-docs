---
title: PREVIOUS_DAY (Lakehouse v1)
description: PREVIOUS_DAY — devolve a data do dia da semana especificado mais recente anterior à data indicada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/previous-day.md
---

Devolve a data do dia da semana especificado mais recente anterior à data ou ao carimbo de data/hora indicado.

## Sintaxe do Analyze

```python
func.next_day(date_expression>, <target_day>)
```

## Exemplos do Analyze

```python
func.next_day(func.to_date('2024-11-13'), 'friday')
┌──────────────────────────────────────────────────────┐
│ func.next_day(func.to_date('2024-11-13'), 'friday')  │
├──────────────────────────────────────────────────────┤
│ 2024-11-08                                           │
└──────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
PREVIOUS_DAY(<date_expression>, <target_day>)
```

| Parâmetro           | Descrição                                                                                                                                                                       |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<date_expression>` | Um valor `DATE` ou `TIMESTAMP` para calcular a ocorrência anterior do dia especificado.                                                                                         |
| `<target_day>`      | O dia da semana de destino cuja ocorrência anterior se pretende encontrar. Os valores aceites incluem `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday` e `sunday`. |

## Tipo de retorno

Data.

## Exemplos SQL

Se precisar de encontrar a sexta-feira anterior a uma determinada data, como 2024-11-13:

```sql
SELECT PREVIOUS_DAY(to_date('2024-11-13'), friday) AS last_friday;

┌─────────────┐
│ last_friday │
├─────────────┤
│ 2024-11-08  │
└─────────────┘
```
