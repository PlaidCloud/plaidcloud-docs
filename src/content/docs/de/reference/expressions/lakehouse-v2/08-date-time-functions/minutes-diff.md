---
title: MINUTES_DIFF (Lakehouse v2)
description: MINUTES_DIFF – gibt die Anzahl der Minuten zwischen zwei Datumswerten mit Uhrzeit zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minutes-diff.md
---

Gibt die Anzahl der Minuten zwischen zwei Datumswerten mit Uhrzeit zurück.

## Analyze-Syntax

```python
func.minutes_diff(<end>, <start>)
```

## Analyze-Beispiele

```python
func.minutes_diff('2024-01-01 11:00:00', '2024-01-01 10:00:00')

┌────┐
│ 60  │
└────┘
```

## SQL-Syntax

```sql
MINUTES_DIFF(<end>, <start>)
```

## SQL-Beispiele

```sql
SELECT MINUTES_DIFF('2024-01-01 11:00:00', '2024-01-01 10:00:00');

┌────┐
│ 60  │
└────┘
```
