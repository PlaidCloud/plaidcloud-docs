---
title: MONTHS_DIFF (Lakehouse v2)
description: MONTHS_DIFF – gibt die Anzahl der Monate zwischen zwei Datumswerten zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/months-diff.md
---

Gibt die Anzahl der Monate zwischen zwei Datumswerten zurück.

## Analyze-Syntax

```python
func.months_diff(<end_date>, <start_date>)
```

## Analyze-Beispiele

```python
func.months_diff('2024-06-01', '2024-01-01')

┌───┐
│ 5  │
└───┘
```

## SQL-Syntax

```sql
MONTHS_DIFF(<end_date>, <start_date>)
```

## SQL-Beispiele

```sql
SELECT MONTHS_DIFF('2024-06-01', '2024-01-01');

┌───┐
│ 5  │
└───┘
```
