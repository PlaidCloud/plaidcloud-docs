---
title: TO_MINUTE (Lakehouse v1)
description: TO_MINUTE — convertit une date avec heure (horodatage/datetime) en nombre UInt8 contenant la minute de l'heure (0-59).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-minute.md
---

Convertit une date avec heure (horodatage/datetime) en nombre UInt8 contenant la minute de l'heure (0-59).


## Syntaxe Analyze

```python
func.to_minute(<expr>)
```

## Exemples Analyze

```python
func.to_minute('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_minute('2023-11-12 09:38:18.165575')       │
│                     UInt8                          │
├────────────────────────────────────────────────────┤
│                                                 38 │
└────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_MINUTE(<expr>)
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
    to_minute('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ to_minute('2023-11-12 09:38:18.165575') │
│                  UInt8                  │
├─────────────────────────────────────────┤
│                                      38 │
└─────────────────────────────────────────┘
```
