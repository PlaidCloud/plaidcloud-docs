---
title: MILLISECONDS_DIFF (Lakehouse v2)
description: MILLISECONDS_DIFF – gibt die Anzahl der Millisekunden zwischen zwei Datumswerten mit Uhrzeit zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/milliseconds-diff.md
---

Gibt die Anzahl der Millisekunden zwischen zwei Datumswerten mit Uhrzeit zurück.

## Analyze-Syntax

```python
func.milliseconds_diff(<end>, <start>)
```

## Analyze-Beispiele

```python
func.milliseconds_diff('2024-01-01 00:00:01', '2024-01-01 00:00:00')

┌──────┐
│ 1000  │
└──────┘
```

## SQL-Syntax

```sql
MILLISECONDS_DIFF(<end>, <start>)
```

## SQL-Beispiele

```sql
SELECT MILLISECONDS_DIFF('2024-01-01 00:00:01', '2024-01-01 00:00:00');

┌──────┐
│ 1000  │
└──────┘
```
