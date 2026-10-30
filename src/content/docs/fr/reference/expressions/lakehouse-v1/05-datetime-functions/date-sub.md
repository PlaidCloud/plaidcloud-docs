---
title: DATE_SUB (Lakehouse v1)
description: DATE_SUB — soustrait l'intervalle de temps ou de date de la date ou de la date avec heure (horodatage/datetime) fournie.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/date-sub.md
---

Soustrait l'intervalle de temps ou de date de la date ou de la date avec heure (horodatage/datetime) fournie.

## Syntaxe Analyze

```python
func.date_sub(<unit>, <value>,  <date_or_time_expr>)
```

## Exemples Analyze

```python
func.date_sub('YEAR', 1, func.to_date('2018-01-02'))
┌──────────────────────────────────────────────────────┐
│ func.date_sub('YEAR', 1, func.to_date('2018-01-02')) │
├──────────────────────────────────────────────────────┤
│ 2017-01-02                                           │
└──────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
DATE_SUB(<unit>, <value>,  <date_or_time_expr>)
```
## Arguments

| Arguments             | Description                                                                                                       |
|-----------------------|-------------------------------------------------------------------------------------------------------------------|
| `<unit>`              | Doit être l'une des valeurs suivantes : `YEAR`, `QUARTER`, `MONTH`, `DAY`, `HOUR`, `MINUTE` et `SECOND`          |
| `<value>`             | Nombre d'unités de temps à soustraire. Par exemple, pour soustraire 2 jours, cette valeur est 2.                  |
| `<date_or_time_expr>` | Valeur de type `DATE` ou `TIMESTAMP`                                                                              |

## Type de retour

La fonction renvoie une valeur du même type que l'argument `<date_or_time_expr>`.

## Exemples SQL

```sql
SELECT date_sub(YEAR, 1, to_date('2018-01-02'));
┌───────────────────────────────────────────────────┐
│ DATE_SUB(YEAR, INTERVAL 1, to_date('2018-01-02')) │
├───────────────────────────────────────────────────┤
│ 2017-01-02                                        │
└───────────────────────────────────────────────────┘
```
