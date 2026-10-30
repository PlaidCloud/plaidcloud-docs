---
title: DATE_TRUNC (Lakehouse v1)
description: DATE_TRUNC — tronque une valeur de date, d'heure ou d'horodatage à la précision indiquée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/date-trunc.md
---

Tronque une valeur de date, d'heure ou d'horodatage à la précision indiquée. Par exemple, si vous tronquez `2022-07-07` à `MONTH`, le résultat est `2022-07-01` ; si vous tronquez `2022-07-07 01:01:01.123456` à `SECOND`, le résultat est `2022-07-07 01:01:01.000000`.

## Syntaxe Analyze

```python
func.date_sub(<precision>,  <date_or_time_expr>)
```

## Exemples Analyze

```python
func.date_trunc('month', func.to_date('2022-07-07'))
┌──────────────────────────────────────────────────────┐
│ func.date_trunc('month', func.to_date('2022-07-07')) │
├──────────────────────────────────────────────────────┤
│ 2022-07-01                                           │
└──────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
DATE_TRUNC(<precision>, <date_or_time_expr>)
```
## Arguments

| Arguments             | Description                                                                                        |
|-----------------------|----------------------------------------------------------------------------------------------------|
| `<precision>`          | Doit être l'une des valeurs suivantes : `YEAR`, `QUARTER`, `MONTH`, `DAY`, `HOUR`, `MINUTE` et `SECOND`  |
| `<date_or_time_expr>` | Valeur de type `DATE` ou `TIMESTAMP`                                                               |

## Type de retour

La fonction renvoie une valeur du même type que l'argument `<date_or_time_expr>`.

## Exemples SQL

```sql
select date_trunc(month, to_date('2022-07-07'));
┌──────────────────────────────────────────┐
│ date_trunc(month, to_date('2022-07-07')) │
├──────────────────────────────────────────┤
│ 2022-07-01                               │
└──────────────────────────────────────────┘
```
