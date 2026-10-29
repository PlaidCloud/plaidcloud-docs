---
title: MINUTES_SUB (Lakehouse v2)
description: MINUTES_SUB – subtrahiert eine angegebene Anzahl von Minuten von einem Datum mit Uhrzeit.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minutes-sub.md
---

Subtrahiert eine angegebene Anzahl von Minuten von einem Datum mit Uhrzeit.

## Analyze-Syntax

```python
func.minutes_sub(<datetime>, <n>)
```

## Analyze-Beispiele

```python
func.minutes_sub('2024-01-01 10:45:00', 45)

┌───────────────────────┐
│ '2024-01-01 10:00:00'  │
└───────────────────────┘
```

## SQL-Syntax

```sql
MINUTES_SUB(<datetime>, <n>)
```

## SQL-Beispiele

```sql
SELECT MINUTES_SUB('2024-01-01 10:45:00', 45);

┌─────────────────────┐
│ 2024-01-01 10:00:00  │
└─────────────────────┘
```
