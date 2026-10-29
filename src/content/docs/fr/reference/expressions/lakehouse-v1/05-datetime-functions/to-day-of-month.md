---
title: TO_DAY_OF_MONTH (Lakehouse v1)
description: TO_DAY_OF_MONTH — convertit une date ou une date avec heure (horodatage/datetime) en nombre UInt8.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-day-of-month.md
---

Convertit une date ou une date avec heure (horodatage/datetime) en nombre UInt8 contenant le numéro du jour du mois (1-31).

## Syntaxe Analyze

```python
func.to_day_of_month(<expr>)
```

## Exemples Analyze

```python
func.now(), func.to_day_of_month(func.now()), func.day(func.now())

┌──────────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_day_of_month(func.now()) │ func.day(func.now()) │
├────────────────────────────┼──────────────────────────────────┼──────────────────────┤
│ 2024-03-14 23:35:41.947962 │                               14 │                   14 │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_DAY_OF_MONTH(<expr>)
```

## Arguments

| Arguments | Description      |
|-----------|------------------|
| `<expr>`  | date/horodatage  |

## Alias

- [DAY](../day)

## Type de retour

`TINYINT`

## Exemples SQL

```sql
SELECT NOW(), TO_DAY_OF_MONTH(NOW()), DAY(NOW());

┌──────────────────────────────────────────────────────────────────┐
│            now()           │ to_day_of_month(now()) │ day(now()) │
├────────────────────────────┼────────────────────────┼────────────┤
│ 2024-03-14 23:35:41.947962 │                     14 │         14 │
└──────────────────────────────────────────────────────────────────┘
```
