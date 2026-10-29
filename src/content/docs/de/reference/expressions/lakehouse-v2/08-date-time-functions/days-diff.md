---
title: DAYS_DIFF (Lakehouse v2)
description: DAYS_DIFF – gibt die Anzahl der Tage zwischen zwei Datumswerten zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/days-diff.md
---

Gibt die Anzahl der Tage zwischen zwei Datumswerten zurück.

## Analyze-Syntax

```python
func.days_diff(<end_date>, <start_date>)
```

## Analyze-Beispiele

```python
func.days_diff('2024-03-01', '2024-01-01')

┌────┐
│ 60  │
└────┘
```

## SQL-Syntax

```sql
DAYS_DIFF(<end_date>, <start_date>)
```

## SQL-Beispiele

```sql
SELECT DAYS_DIFF('2024-03-01', '2024-01-01');

┌────┐
│ 60  │
└────┘
```
