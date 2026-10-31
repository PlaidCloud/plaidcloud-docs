---
title: DATE_TRUNC (Lakehouse v1)
description: DATE_TRUNC — trunca un valor de fecha, hora o marca de tiempo a una precisión especificada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/date-trunc.md
---

Trunca un valor de fecha, hora o marca de tiempo a una precisión especificada. Por ejemplo, si trunca `2022-07-07` a `MONTH`, el resultado será `2022-07-01`; si trunca `2022-07-07 01:01:01.123456` a `SECOND`, el resultado será `2022-07-07 01:01:01.000000`.

## Sintaxis de Analyze

```python
func.date_sub(<precision>,  <date_or_time_expr>)
```

## Ejemplos de Analyze

```python
func.date_trunc('month', func.to_date('2022-07-07'))
┌──────────────────────────────────────────────────────┐
│ func.date_trunc('month', func.to_date('2022-07-07')) │
├──────────────────────────────────────────────────────┤
│ 2022-07-01                                           │
└──────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
DATE_TRUNC(<precision>, <date_or_time_expr>)
```
## Argumentos

| Argumentos            | Descripción                                                                                        |
|-----------------------|----------------------------------------------------------------------------------------------------|
| `<precision>`          | Debe ser uno de los siguientes valores: `YEAR`, `QUARTER`, `MONTH`, `DAY`, `HOUR`, `MINUTE` y `SECOND`  |
| `<date_or_time_expr>` | Un valor de tipo `DATE` o `TIMESTAMP`                                                              |

## Tipo de valor devuelto

La función devuelve un valor del mismo tipo que el argumento `<date_or_time_expr>`.

## Ejemplos de SQL

```sql
select date_trunc(month, to_date('2022-07-07'));
┌──────────────────────────────────────────┐
│ date_trunc(month, to_date('2022-07-07')) │
├──────────────────────────────────────────┤
│ 2022-07-01                               │
└──────────────────────────────────────────┘
```
