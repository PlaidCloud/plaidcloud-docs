---
title: TO_YYYYMMDDHHMMSS (Lakehouse v1)
description: TO_YYYYMMDDHHMMSS convertit une date ou une date avec heure (timestamp/datetime) en nombre UInt64.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-yyyymmddhhmmss.md
---

Convertit une date ou une date avec heure (timestamp/datetime) en nombre UInt64 contenant l'année, le mois, le jour, l'heure, les minutes et les secondes (YYYY * 10000000000 + MM * 100000000 + DD * 1000000 + hh * 10000 + mm * 100 + ss).

## Syntaxe Analyze

```python
func.to_yyyymmddhhmmss(<expr>)
```

## Exemples Analyze

```python
func.to_yyyymmddhhmmss('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────────────┐
│ func.to_yyyymmddhhmmss('2023-11-12 09:38:18.165575') │
│                   UInt64                             │
├──────────────────────────────────────────────────────┤
│                                       20231112092818 │
└──────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_YYYYMMDDHHMMSS(<expr>)
```

## Arguments

| Arguments | Description    |
|-----------|----------------|
| `<expr>`  | date/timestamp |

## Type de retour

`BIGINT`, renvoyé au format `YYYYMMDDhhmmss`.

## Exemples SQL

```sql
SELECT
  to_yyyymmddhhmmss('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────────────┐
│ to_yyyymmddhhmmss('2023-11-12 09:38:18.165575') │
│                      UInt64                     │
├─────────────────────────────────────────────────┤
│                                  20231112092818 │
└─────────────────────────────────────────────────┘
```
