---
title: DATE_TRUNC (Lakehouse v1)
description: DATE_TRUNC — trunca um valor de data, hora ou carimbo de data/hora para uma precisão especificada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/date-trunc.md
---

Trunca um valor de data, hora ou carimbo de data/hora para uma precisão especificada. Por exemplo, se truncar `2022-07-07` para `MONTH`, o resultado será `2022-07-01`; se truncar `2022-07-07 01:01:01.123456` para `SECOND`, o resultado será `2022-07-07 01:01:01.000000`.

## Sintaxe do Analyze

```python
func.date_sub(<precision>,  <date_or_time_expr>)
```

## Exemplos do Analyze

```python
func.date_trunc('month', func.to_date('2022-07-07'))
┌──────────────────────────────────────────────────────┐
│ func.date_trunc('month', func.to_date('2022-07-07')) │
├──────────────────────────────────────────────────────┤
│ 2022-07-01                                           │
└──────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
DATE_TRUNC(<precision>, <date_or_time_expr>)
```
## Argumentos

| Argumentos            | Descrição                                                                                           |
|-----------------------|-----------------------------------------------------------------------------------------------------|
| `<precision>`          | Tem de ser um dos seguintes valores: `YEAR`, `QUARTER`, `MONTH`, `DAY`, `HOUR`, `MINUTE` e `SECOND` |
| `<date_or_time_expr>` | Um valor do tipo `DATE` ou `TIMESTAMP`                                                              |

## Tipo de retorno

A função devolve um valor do mesmo tipo que o argumento `<date_or_time_expr>`.

## Exemplos SQL

```sql
select date_trunc(month, to_date('2022-07-07'));
┌──────────────────────────────────────────┐
│ date_trunc(month, to_date('2022-07-07')) │
├──────────────────────────────────────────┤
│ 2022-07-01                               │
└──────────────────────────────────────────┘
```
