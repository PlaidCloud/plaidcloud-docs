---
title: DATE_ADD (Lakehouse v1)
description: DATE_ADD — suma el intervalo de tiempo o de fecha a la fecha, o fecha con hora, indicada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/date-add.md
---

Suma el intervalo de tiempo o de fecha a la fecha, o fecha con hora (marca de tiempo/datetime), indicada.

## Sintaxis de Analyze

```python
func.date_add(<unit>, <value>,  <date_or_time_expr>)
```

## Ejemplos de Analyze

```python
func.date_add('YEAR', 1, func.to_date('2018-01-02'))
┌──────────────────────────────────────────────────────┐
│ func.date_add('YEAR', 1, func.to_date('2018-01-02')) │
├──────────────────────────────────────────────────────┤
│ 2019-01-02                                           │
└──────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
DATE_ADD(<unit>, <value>,  <date_or_time_expr>)
```
## Argumentos

| Argumentos            | Descripción                                                                                                       |
|-----------------------|-------------------------------------------------------------------------------------------------------------------|
| `<unit>`              | Debe ser uno de los siguientes valores: `YEAR`, `QUARTER`, `MONTH`, `DAY`, `HOUR`, `MINUTE` y `SECOND`            |
| `<value>`             | Es el número de unidades de tiempo que desea sumar. Por ejemplo, si desea sumar 2 días, será 2.                   |
| `<date_or_time_expr>` | Un valor de tipo `DATE` o `TIMESTAMP`                                                                             |

## Tipo de valor devuelto

La función devuelve un valor del mismo tipo que el argumento `<date_or_time_expr>`.

## Ejemplos de SQL

```sql
SELECT date_add(YEAR, 1, to_date('2018-01-02'));
┌───────────────────────────────────────────────────┐
│ DATE_ADD(YEAR, INTERVAL 1, to_date('2018-01-02')) │
├───────────────────────────────────────────────────┤
│ 2019-01-02                                        │
└───────────────────────────────────────────────────┘
```
