---
title: HOURS_SUB (Lakehouse v2)
description: HOURS_SUB – subtrahiert eine angegebene Anzahl von Stunden von einem Datums-/Zeitwert.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/hours-sub.md
---

Subtrahiert eine angegebene Anzahl von Stunden von einem Datums-/Zeitwert.

## Analyze-Syntax

```python
func.hours_sub(<datetime>, <n>)
```

## Analyze-Beispiele

```python
func.hours_sub('2024-01-01 15:00:00', 5)

┌───────────────────────┐
│ '2024-01-01 10:00:00'  │
└───────────────────────┘
```

## SQL-Syntax

```sql
HOURS_SUB(<datetime>, <n>)
```

## SQL-Beispiele

```sql
SELECT HOURS_SUB('2024-01-01 15:00:00', 5);

┌─────────────────────┐
│ 2024-01-01 10:00:00  │
└─────────────────────┘
```
