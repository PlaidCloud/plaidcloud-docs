---
title: DATE_SUB (Lakehouse v1)
description: DATE_SUB — subtrai o intervalo de tempo ou de data da data ou da data com hora (timestamp/datetime) fornecida.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/date-sub.md
---

Subtrai o intervalo de tempo ou de data da data ou da data com hora (timestamp/datetime) fornecida.

## Sintaxe do Analyze

```python
func.date_sub(<unit>, <value>,  <date_or_time_expr>)
```

## Exemplos do Analyze

```python
func.date_sub('YEAR', 1, func.to_date('2018-01-02'))
┌──────────────────────────────────────────────────────┐
│ func.date_sub('YEAR', 1, func.to_date('2018-01-02')) │
├──────────────────────────────────────────────────────┤
│ 2017-01-02                                           │
└──────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
DATE_SUB(<unit>, <value>,  <date_or_time_expr>)
```
## Argumentos

| Argumentos            | Descrição                                                                                                         |
|-----------------------|-------------------------------------------------------------------------------------------------------------------|
| `<unit>`              | Deve ser um dos seguintes valores: `YEAR`, `QUARTER`, `MONTH`, `DAY`, `HOUR`, `MINUTE` e `SECOND`                 |
| `<value>`             | É o número de unidades de tempo que você deseja adicionar. Por exemplo, para adicionar 2 dias, o valor será 2.    |
| `<date_or_time_expr>` | Um valor do tipo `DATE` ou `TIMESTAMP`                                                                            |

## Tipo de retorno

A função retorna um valor do mesmo tipo do argumento `<date_or_time_expr>`.

## Exemplos de SQL

```sql
SELECT date_sub(YEAR, 1, to_date('2018-01-02'));
┌───────────────────────────────────────────────────┐
│ DATE_SUB(YEAR, INTERVAL 1, to_date('2018-01-02')) │
├───────────────────────────────────────────────────┤
│ 2017-01-02                                        │
└───────────────────────────────────────────────────┘
```
