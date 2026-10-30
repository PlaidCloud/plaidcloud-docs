---
title: HOURS_DIFF (Lakehouse v2)
description: HOURS_DIFF – gibt die Anzahl der Stunden zwischen zwei Datums-/Zeitwerten zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/hours-diff.md
---

Gibt die Anzahl der Stunden zwischen zwei Datums-/Zeitwerten zurück.

## Analyze-Syntax

```python
func.hours_diff(<end>, <start>)
```

## Analyze-Beispiele

```python
func.hours_diff('2024-01-02 10:00:00', '2024-01-01 10:00:00')

┌────┐
│ 24  │
└────┘
```

## SQL-Syntax

```sql
HOURS_DIFF(<end>, <start>)
```

## SQL-Beispiele

```sql
SELECT HOURS_DIFF('2024-01-02 10:00:00', '2024-01-01 10:00:00');

┌────┐
│ 24  │
└────┘
```
