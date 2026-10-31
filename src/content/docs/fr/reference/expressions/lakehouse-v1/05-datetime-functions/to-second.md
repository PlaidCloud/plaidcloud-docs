---
title: TO_SECOND (Lakehouse v1)
description: TO_SECOND — convertit une date avec heure (horodatage/datetime) en nombre UInt8 contenant la seconde de la minute (0-59).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-second.md
---

Convertit une date avec heure (horodatage/datetime) en nombre UInt8 contenant la seconde de la minute (0-59).

## Syntaxe Analyze

```python
func.to_second(<expr>)
```

## Exemples Analyze

```python
func.to_second('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────┐
│ func.to_second('2023-11-12 09:38:18.165575') │
│                   UInt8                      │
├──────────────────────────────────────────────┤
│                                           18 │
└──────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_SECOND(<expr>)
```

## Arguments

| Arguments | Description |
|-----------|-------------|
| `<expr>`  | horodatage  |

## Type de retour

`TINYINT`

## Exemples SQL

```sql
SELECT
    to_second('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ to_second('2023-11-12 09:38:18.165575') │
│                  UInt8                  │
├─────────────────────────────────────────┤
│                                      18 │
└─────────────────────────────────────────┘
```
