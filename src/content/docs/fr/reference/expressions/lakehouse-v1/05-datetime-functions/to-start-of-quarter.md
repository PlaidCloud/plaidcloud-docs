---
title: TO_START_OF_QUARTER (Lakehouse v1)
description: TO_START_OF_QUARTER arrondit à l'inférieur une date ou une date avec heure (timestamp/datetime) au premier jour du trimestre.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-quarter.md
---

Arrondit à l'inférieur une date ou une date avec heure (timestamp/datetime) au premier jour du trimestre.
Le premier jour du trimestre est le 1er janvier, le 1er avril, le 1er juillet ou le 1er octobre.
Renvoie la date.

## Syntaxe Analyze

```python
func.to_start_of_quarter(<expr>)
```

## Exemples Analyze

```python
func.to_start_of_quarter('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_quarter('2023-11-12 09:38:18.165575')         │
│                          Date                                  │
├────────────────────────────────────────────────────────────────┤
│ 2023-10-01                                                     │
└────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_START_OF_QUARTER(<expr>)
```

## Arguments

| Arguments | Description    |
|-----------|----------------|
| `<expr>`   | date/timestamp |

## Type de retour

`DATE`, renvoie la date au format « YYYY-MM-DD ».

## Exemples SQL

```sql
SELECT
  to_start_of_quarter('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────────────────┐
│ to_start_of_quarter('2023-11-12 09:38:18.165575') │
│                        Date                       │
├───────────────────────────────────────────────────┤
│ 2023-10-01                                        │
└───────────────────────────────────────────────────┘
```
