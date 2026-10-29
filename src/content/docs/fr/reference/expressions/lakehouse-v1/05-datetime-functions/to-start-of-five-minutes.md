---
title: TO_START_OF_FIVE_MINUTES (Lakehouse v1)
description: TO_START_OF_FIVE_MINUTES — arrondit une date avec heure (horodatage/datetime) au début de l'intervalle de cinq minutes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-five-minutes.md
---

Arrondit une date avec heure (horodatage/datetime) au début de l'intervalle de cinq minutes.

## Syntaxe Analyze

```python
func.to_start_of_five_minutes(<expr>)
```

## Exemples Analyze

```python
func.to_start_of_five_minutes('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_five_minutes('2023-11-12 09:38:18.165575')    │
│                          Timestamp                             │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-12 09:35:00                                            │
└────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_START_OF_FIVE_MINUTES(<expr>)
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
  to_start_of_five_minutes('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────┐
│ to_start_of_five_minutes('2023-11-12 09:38:18.165575') │
│                        Timestamp                       │
├────────────────────────────────────────────────────────┤
│ 2023-11-12 09:35:00                                    │
└────────────────────────────────────────────────────────┘
```
