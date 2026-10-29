---
title: TO_START_OF_MINUTE (Lakehouse v1)
description: TO_START_OF_MINUTE — arrondit une date avec heure (horodatage/datetime) au début de la minute.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-minute.md
---

Arrondit une date avec heure (horodatage/datetime) au début de la minute.

## Syntaxe Analyze

```python
func.to_start_of_minute(<expr>)
```

## Exemples Analyze

```python
func.to_start_of_minute('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_minute('2023-11-12 09:38:18.165575')          │
│                          Timestamp                             │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-12 09:38:00                                            │
└────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_START_OF_MINUTE( <expr> )
```

## Arguments

| Arguments | Description |
|-----------|-------------|
| `<expr>`  | horodatage  |

## Type de retour

`TIMESTAMP`, renvoie la date au format « YYYY-MM-DD hh:mm:ss.ffffff ».

## Exemples SQL

```sql
SELECT
  to_start_of_minute('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────────┐
│ to_start_of_minute('2023-11-12 09:38:18.165575') │
│                     Timestamp                    │
├──────────────────────────────────────────────────┤
│ 2023-11-12 09:38:00                              │
└──────────────────────────────────────────────────┘
```
