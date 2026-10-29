---
title: TIME_SLICE (Lakehouse v2)
description: TIME_SLICE — ramène une heure donnée au début ou à la fin d'un intervalle de temps.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/time-slice.md
---

Ramène une heure donnée au début ou à la fin d'un intervalle de temps.

## Syntaxe Analyze

```python
func.time_slice(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## Exemples Analyze

```python
func.time_slice('2024-06-15 14:35:00', text('INTERVAL 15 MINUTE'))

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## Syntaxe SQL

```sql
TIME_SLICE(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## Exemples SQL

```sql
SELECT TIME_SLICE('2024-06-15 14:35:00', INTERVAL 15 MINUTE);

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
