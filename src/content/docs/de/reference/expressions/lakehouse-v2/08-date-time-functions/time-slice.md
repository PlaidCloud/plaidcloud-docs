---
title: TIME_SLICE (Lakehouse v2)
description: TIME_SLICE – rundet einen Zeitpunkt auf den Anfang oder das Ende eines Zeitintervalls.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/time-slice.md
---

Rundet einen Zeitpunkt auf den Anfang oder das Ende eines Zeitintervalls.

## Analyze-Syntax

```python
func.time_slice(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## Analyze-Beispiele

```python
func.time_slice('2024-06-15 14:35:00', text('INTERVAL 15 MINUTE'))

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## SQL-Syntax

```sql
TIME_SLICE(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## SQL-Beispiele

```sql
SELECT TIME_SLICE('2024-06-15 14:35:00', INTERVAL 15 MINUTE);

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
