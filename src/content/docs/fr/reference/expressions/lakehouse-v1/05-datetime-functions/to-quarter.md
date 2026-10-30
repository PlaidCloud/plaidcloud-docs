---
title: TO_QUARTER (Lakehouse v1)
description: TO_QUARTER — extrait le trimestre (1, 2, 3 ou 4) d'une date ou d'un horodatage donné.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-quarter.md
---

Extrait le trimestre (1, 2, 3 ou 4) d'une date ou d'un horodatage donné.

## Syntaxe Analyze

```python
func.to_quarter(<expr>)
```

## Exemples Analyze

```python
func.now(), func.to_quarter(func.now()), func.quarter(func.now())

┌─────────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_quarter(func.now()) │ func.quarter(func.now()) │
├────────────────────────────┼─────────────────────────────┼──────────────────────────┤
│ 2024-03-14 23:32:52.743133 │                           3 │                        3 │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_QUARTER( <date_or_time_expr> )
```

## Alias

- [QUARTER](../quarter)

## Type de retour

Entier.

## Exemples SQL

```sql
SELECT NOW(), TO_QUARTER(NOW()), QUARTER(NOW());

┌─────────────────────────────────────────────────────────────────┐
│            now()           │ to_quarter(now()) │ quarter(now()) │
├────────────────────────────┼───────────────────┼────────────────┤
│ 2024-03-14 23:32:52.743133 │                 1 │              1 │
└─────────────────────────────────────────────────────────────────┘
```
