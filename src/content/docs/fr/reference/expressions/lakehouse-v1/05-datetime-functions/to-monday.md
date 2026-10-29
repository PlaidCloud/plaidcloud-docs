---
title: TO_MONDAY (Lakehouse v1)
description: TO_MONDAY — arrondit une date ou une date avec heure (horodatage/datetime) au lundi précédent le plus proche.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-monday.md
---

Arrondit une date ou une date avec heure (horodatage/datetime) au lundi précédent le plus proche.
Renvoie la date.

## Syntaxe Analyze

```python
func.to_monday(<expr>)
```

## Exemples Analyze

```python
func.to_monday('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_monday('2023-11-12 09:38:18.165575')       │
│                      Date                          │
├────────────────────────────────────────────────────┤
│ 2023-11-06                                         │
└────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_MONDAY(<expr>)
```

## Arguments

| Arguments   | Description |
| ----------- | ----------- |
| `<expr>` | date/horodatage |

## Type de retour

`DATE`, renvoie la date au format « YYYY-MM-DD ».

## Exemples SQL

```sql
SELECT
    to_monday('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ to_monday('2023-11-12 09:38:18.165575') │
│                   Date                  │
├─────────────────────────────────────────┤
│ 2023-11-06                              │
└─────────────────────────────────────────┘
```
