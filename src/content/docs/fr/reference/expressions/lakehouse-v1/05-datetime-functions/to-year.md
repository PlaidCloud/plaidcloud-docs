---
title: TO_YEAR (Lakehouse v1)
description: TO_YEAR convertit une date ou une date avec heure (timestamp/datetime) en nombre UInt16 contenant l'année.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-year.md
---

Convertit une date ou une date avec heure (timestamp/datetime) en nombre UInt16 contenant l'année (ap. J.-C.).

## Syntaxe Analyze

```python
func.to_year(<expr>)
```

## Exemples Analyze

```python
func.now(), func.to_year(func.now()), func.year(func.now())

┌───────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_year(func.now()) │ func.year(func.now()) │
├────────────────────────────┼──────────────────────────┼───────────────────────┤
│ 2024-03-14 23:37:03.895166 │                     2024 │                  2024 │
└───────────────────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_YEAR(<expr>)
```

## Arguments

| Arguments | Description    |
|-----------|----------------|
| `<expr>`  | date/timestamp |

## Alias

- [YEAR](../year)

## Type de retour

 `SMALLINT`

## Exemples SQL

```sql
SELECT NOW(), TO_YEAR(NOW()), YEAR(NOW());

┌───────────────────────────────────────────────────────────┐
│            now()           │ to_year(now()) │ year(now()) │
├────────────────────────────┼────────────────┼─────────────┤
│ 2024-03-14 23:37:03.895166 │           2024 │        2024 │
└───────────────────────────────────────────────────────────┘
```
