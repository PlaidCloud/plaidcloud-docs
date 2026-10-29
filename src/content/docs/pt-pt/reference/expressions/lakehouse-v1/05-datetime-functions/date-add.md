---
title: DATE_ADD (Lakehouse v1)
description: DATE_ADD — adiciona o intervalo de tempo ou de datas à data ou data com hora indicada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/date-add.md
---

Adiciona o intervalo de tempo ou de datas à data ou data com hora (timestamp/datetime) indicada.

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
| `<unit>`              | Tem de ser um dos seguintes valores: `YEAR`, `QUARTER`, `MONTH`, `DAY`, `HOUR`, `MINUTE` e `SECOND`              |
| `<value>`             | Número de unidades de tempo que pretende adicionar. Por exemplo, para adicionar 2 dias, será 2.                 |
| `<date_or_time_expr>` | Um valor do tipo `DATE` ou `TIMESTAMP`                                                                            |

## Tipo de retorno

A função devolve um valor do mesmo tipo que o argumento `<date_or_time_expr>`.

## Exemplos SQL

```sql
SELECT date_add(YEAR, 1, to_date('2018-01-02'));
┌───────────────────────────────────────────────────┐
│ DATE_ADD(YEAR, INTERVAL 1, to_date('2018-01-02')) │
├───────────────────────────────────────────────────┤
│ 2019-01-02                                        │
└───────────────────────────────────────────────────┘
```
