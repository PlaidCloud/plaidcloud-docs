---
title: TIME_SLOT (Lakehouse v1)
description: TIME_SLOT — arrondit l'heure à la demi-heure.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/time-slot.md
---

Arrondit l'heure à la demi-heure.

## Syntaxe Analyze

```python
func.time_slot(<expr>)
```

## Exemples Analyze

```python
func.time_slot('2023-11-12 09:38:18.165575')
┌───────────────────────────────-───-───-──────┐
│ func.time_slot('2023-11-12 09:38:18.165575') │
│                Timestamp                     │
├─────────────────────────────────-───-────────┤
│ 2023-11-12 09:30:00                          │
└─────────────────────────────────-───-────────┘
```

## Syntaxe SQL

```sql
time_slot(<expr>)
```

## Arguments

| Arguments   | Description |
| ----------- | ----------- |
| `<expr>`    | horodatage  |

## Type de retour

`TIMESTAMP`, renvoyé au format « YYYY-MM-DD hh:mm:ss.ffffff ».

## Exemples SQL

```sql
SELECT
  time_slot('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ time_slot('2023-11-12 09:38:18.165575') │
│                Timestamp                │
├─────────────────────────────────────────┤
│ 2023-11-12 09:30:00                     │
└─────────────────────────────────────────┘
```
