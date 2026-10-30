---
title: DATE_ADD (Lakehouse v1)
description: DATE_ADD — adiciona o intervalo de tempo ou de data à data ou à data com hora fornecida.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/date-add.md
---

Adiciona o intervalo de tempo ou de data à data ou à data com hora (timestamp/datetime) fornecida.

## Sintaxe do Analyze

```python
func.date_add(<unit>, <value>,  <date_or_time_expr>)
```

## Exemplos do Analyze

```python
func.date_add('YEAR', 1, func.to_date('2018-01-02'))
┌──────────────────────────────────────────────────────┐
│ func.date_add('YEAR', 1, func.to_date('2018-01-02')) │
├──────────────────────────────────────────────────────┤
│ 2019-01-02                                           │
└──────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
DATE_ADD(<unit>, <value>,  <date_or_time_expr>)
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
SELECT date_add(YEAR, 1, to_date('2018-01-02'));
┌───────────────────────────────────────────────────┐
│ DATE_ADD(YEAR, INTERVAL 1, to_date('2018-01-02')) │
├───────────────────────────────────────────────────┤
│ 2019-01-02                                        │
└───────────────────────────────────────────────────┘
```
