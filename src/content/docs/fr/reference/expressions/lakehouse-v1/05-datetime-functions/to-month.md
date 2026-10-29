---
title: TO_MONTH (Lakehouse v1)
description: TO_MONTH — convertit une date ou une date avec heure (horodatage/datetime) en nombre UInt8 contenant.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-month.md
---

Convertit une date ou une date avec heure (horodatage/datetime) en nombre UInt8 contenant le numéro du mois (1-12).

## Syntaxe Analyze

```python
func.to_month(<expr>)
```

## Exemples Analyze

```python
func.now(), func.to_month(func.now()), func.month(func.now())

┌─────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_month(func.now()) │ func.month(func.now()) │
├────────────────────────────┼───────────────────────────┼────────────────────────┤
│ 2024-03-14 23:34:02.161291 │                         3 │                      3 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_MONTH(<expr>)
```

## Arguments

| Arguments | Description     |
|-----------|-----------------|
| `<expr>`  | date/horodatage |

## Alias

- [MONTH](../month)

## Type de retour

 `TINYINT`

## Exemples SQL

```sql
SELECT NOW(), TO_MONTH(NOW()), MONTH(NOW());

┌─────────────────────────────────────────────────────────────┐
│            now()           │ to_month(now()) │ month(now()) │
├────────────────────────────┼─────────────────┼──────────────┤
│ 2024-03-14 23:34:02.161291 │               3 │            3 │
└─────────────────────────────────────────────────────────────┘
```
