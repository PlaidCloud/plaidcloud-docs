---
title: TO_START_OF_WEEK (Lakehouse v1)
description: TO_START_OF_WEEK renvoie le premier jour de la semaine pour une date ou une date avec heure.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-week.md
---

Renvoie le premier jour de la semaine pour une date ou une date avec heure (timestamp/datetime).
Le premier jour de la semaine peut être le dimanche ou le lundi, selon l'argument `mode`.

## Syntaxe Analyze

```python
func.to_start_of_week(<expr>)
```

## Exemples Analyze

```python
func.to_start_of_week('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_week('2023-11-12 09:38:18.165575')            │
│                          Date                                  │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-12                                                     │
└────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_START_OF_WEEK(<expr> [, mode])
```

## Arguments

| Arguments | Description                                                                                         |
|-----------|-----------------------------------------------------------------------------------------------------|
| `<expr>`  | date/timestamp                                                                                      |
| `[mode]`  | Facultatif. S'il vaut 0, le résultat est le dimanche ; sinon, le résultat est le lundi. La valeur par défaut est 0 |

## Type de retour

`DATE`, renvoie la date au format « YYYY-MM-DD ».

## Exemples SQL

```sql
SELECT
  to_start_of_week('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────┐
│ to_start_of_week('2023-11-12 09:38:18.165575') │
│                      Date                      │
├────────────────────────────────────────────────┤
│ 2023-11-12                                     │
└────────────────────────────────────────────────┘
```
