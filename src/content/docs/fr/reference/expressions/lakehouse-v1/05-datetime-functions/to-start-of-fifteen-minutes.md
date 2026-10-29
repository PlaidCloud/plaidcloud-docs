---
title: TO_START_OF_FIFTEEN_MINUTES (Lakehouse v1)
description: TO_START_OF_FIFTEEN_MINUTES — arrondit la date avec heure (horodatage/datetime) au début de l'intervalle de quinze minutes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-fifteen-minutes.md
---

Arrondit la date avec heure (horodatage/datetime) au début de l'intervalle de quinze minutes.

## Syntaxe Analyze

```python
func.to_start_of_fifteen_minutes(<expr>)
```

## Exemples Analyze

```python
func.to_start_of_fifteen_minutes('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_fifteen_minutes('2023-11-12 09:38:18.165575') │
│                          Timestamp                             │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-12 09:30:00                                            │
└────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_START_OF_FIFTEEN_MINUTES(<expr>)
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
  to_start_of_fifteen_minutes('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────────────────────────┐
│ to_start_of_fifteen_minutes('2023-11-12 09:38:18.165575') │
│                         Timestamp                         │
├───────────────────────────────────────────────────────────┤
│ 2023-11-12 09:30:00                                       │
└───────────────────────────────────────────────────────────┘
```
