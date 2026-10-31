---
title: LAST_DAY (Lakehouse v1)
description: LAST_DAY — devolve o último dia do intervalo especificado (semana, mês, trimestre ou ano).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/last-day.md
---

Devolve o último dia do intervalo especificado (semana, mês, trimestre ou ano) com base na data ou no carimbo de data/hora indicado.

## Sintaxe do Analyze

```python
func.last_day(<date_expression>, <interval>)
```

## Exemplos do Analyze

```python
func.last_day(func.to_date('2024-11-13'), 'month')
┌──────────────────────────────────────────────────────┐
│ func.last_day(func.to_date('2024-11-13'), 'month')   │
├──────────────────────────────────────────────────────┤
│ 2024-11-30                                           │
└──────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
LAST_DAY(<date_expression>, <interval>)
```

| Parâmetro           | Descrição                                                                                                                  |
|---------------------|----------------------------------------------------------------------------------------------------------------------------|
| `<date_expression>` | Um valor DATE ou TIMESTAMP para calcular o último dia do intervalo especificado.                                           |
| `<interval>`        | O tipo de intervalo para o qual se pretende encontrar o último dia. Os valores aceites são `week`, `month`, `quarter` e `year`. |

## Tipo de retorno

Data.

## Exemplos SQL

Suponha que pretende determinar a data de faturação, que é sempre o último dia do mês, com base numa data arbitrária de uma transação (p. ex., 2024-11-13):

```sql
SELECT LAST_DAY(to_date('2024-11-13'), month) AS billing_date;

┌──────────────┐
│ billing_date │
├──────────────┤
│ 2024-11-30   │
└──────────────┘
```
