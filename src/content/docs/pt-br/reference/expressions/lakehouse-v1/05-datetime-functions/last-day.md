---
title: LAST_DAY (Lakehouse v1)
description: LAST_DAY — retorna o último dia do intervalo especificado (semana, mês, trimestre ou ano).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/last-day.md
---

Retorna o último dia do intervalo especificado (semana, mês, trimestre ou ano) com base na data ou no timestamp fornecido.

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

| Parâmetro           | Descrição                                                                                                     |
|---------------------|---------------------------------------------------------------------------------------------------------------|
| `<date_expression>` | Um valor DATE ou TIMESTAMP para calcular o último dia do intervalo especificado.                              |
| `<interval>`        | O tipo de intervalo cujo último dia será encontrado. Os valores aceitos são `week`, `month`, `quarter` e `year`. |

## Tipo de retorno

Data.

## Exemplos de SQL

Suponha que você queira determinar a data de faturamento, que é sempre o último dia do mês, com base em uma data arbitrária de uma transação (por exemplo, 2024-11-13):

```sql
SELECT LAST_DAY(to_date('2024-11-13'), month) AS billing_date;

┌──────────────┐
│ billing_date │
├──────────────┤
│ 2024-11-30   │
└──────────────┘
```
