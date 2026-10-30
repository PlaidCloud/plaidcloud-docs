---
title: TO_YYYYMMDD (Lakehouse v1)
description: TO_YYYYMMDD convertit une date ou une date avec heure (timestamp/datetime) en nombre UInt32.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-yyyymmdd.md
---

Convertit une date ou une date avec heure (timestamp/datetime) en nombre UInt32 contenant l'année, le mois et le jour (YYYY * 10000 + MM * 100 + DD).

## Syntaxe Analyze

```python
func.to_yyyymmdd(<expr>)
```

## Exemples Analyze

```python
func.to_yyyymmdd('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────┐
│ func.to_yyyymmdd('2023-11-12 09:38:18.165575') │
│                   UInt32                       │
├────────────────────────────────────────────────┤
│                                       20231112 │
└────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_YYYYMMDD(<expr>)
```

## Arguments

| Arguments | Description   |
|-----------|---------------|
| `<expr>`  | date/datetime |

## Type de retour

`INT`, renvoyé au format `YYYYMMDD`.

## Exemples SQL

```sql
SELECT
  to_yyyymmdd('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────────┐
│ to_yyyymmdd('2023-11-12 09:38:18.165575') │
│                   UInt32                  │
├───────────────────────────────────────────┤
│                                  20231112 │
└───────────────────────────────────────────┘
```
