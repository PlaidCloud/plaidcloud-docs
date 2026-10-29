---
title: SECONDS_DIFF (Lakehouse v2)
description: SECONDS_DIFF – gibt die Anzahl der Sekunden zwischen zwei Datumswerten mit Uhrzeit zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/seconds-diff.md
---

Gibt die Anzahl der Sekunden zwischen zwei Datumswerten mit Uhrzeit zurück.

## Analyze-Syntax

```python
func.seconds_diff(<end>, <start>)
```

## Analyze-Beispiele

```python
func.seconds_diff('2024-01-01 00:01:30', '2024-01-01 00:00:00')

┌────┐
│ 90  │
└────┘
```

## SQL-Syntax

```sql
SECONDS_DIFF(<end>, <start>)
```

## SQL-Beispiele

```sql
SELECT SECONDS_DIFF('2024-01-01 00:01:30', '2024-01-01 00:00:00');

┌────┐
│ 90  │
└────┘
```
