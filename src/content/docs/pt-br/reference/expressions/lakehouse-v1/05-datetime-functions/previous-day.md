---
title: PREVIOUS_DAY (Lakehouse v1)
description: PREVIOUS_DAY — retorna a data do dia da semana especificado mais recente antes da data fornecida.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/previous-day.md
---

Retorna a data do dia da semana especificado mais recente antes da data ou do timestamp fornecido.

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

| Parâmetro           | Descrição                                                                                                                                                                |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<date_expression>` | Um valor `DATE` ou `TIMESTAMP` para calcular a ocorrência anterior do dia especificado.                                                                                  |
| `<target_day>`      | O dia da semana de destino cuja ocorrência anterior será encontrada. Os valores aceitos incluem `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday` e `sunday`. |

## Tipo de retorno

Data.

## Exemplos de SQL

Para encontrar a sexta-feira anterior a uma data específica, como 2024-11-13:

```sql
SELECT PREVIOUS_DAY(to_date('2024-11-13'), friday) AS last_friday;

┌─────────────┐
│ last_friday │
├─────────────┤
│ 2024-11-08  │
└─────────────┘
```
