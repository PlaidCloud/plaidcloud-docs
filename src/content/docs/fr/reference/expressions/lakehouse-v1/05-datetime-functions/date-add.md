---
title: DATE_ADD (Lakehouse v1)
description: DATE_ADD — ajoute l'intervalle de temps ou de date à la date ou à la date avec heure fournie.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/date-add.md
---

Ajoute l'intervalle de temps ou de date à la date ou à la date avec heure (horodatage/datetime) fournie.

## Syntaxe Analyze

```python
func.date_add(<unit>, <value>,  <date_or_time_expr>)
```

## Exemples Analyze

```python
func.date_add('YEAR', 1, func.to_date('2018-01-02'))
┌──────────────────────────────────────────────────────┐
│ func.date_add('YEAR', 1, func.to_date('2018-01-02')) │
├──────────────────────────────────────────────────────┤
│ 2019-01-02                                           │
└──────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
DATE_ADD(<unit>, <value>,  <date_or_time_expr>)
```
## Arguments

| Arguments             | Description                                                                                                       |
|-----------------------|-------------------------------------------------------------------------------------------------------------------|
| `<unit>`              | Doit être l'une des valeurs suivantes : `YEAR`, `QUARTER`, `MONTH`, `DAY`, `HOUR`, `MINUTE` et `SECOND`          |
| `<value>`             | Nombre d'unités de temps à ajouter. Par exemple, pour ajouter 2 jours, cette valeur est 2.                        |
| `<date_or_time_expr>` | Valeur de type `DATE` ou `TIMESTAMP`                                                                              |

## Type de retour

La fonction renvoie une valeur du même type que l'argument `<date_or_time_expr>`.

## Exemples SQL

```sql
SELECT date_add(YEAR, 1, to_date('2018-01-02'));
┌───────────────────────────────────────────────────┐
│ DATE_ADD(YEAR, INTERVAL 1, to_date('2018-01-02')) │
├───────────────────────────────────────────────────┤
│ 2019-01-02                                        │
└───────────────────────────────────────────────────┘
```
