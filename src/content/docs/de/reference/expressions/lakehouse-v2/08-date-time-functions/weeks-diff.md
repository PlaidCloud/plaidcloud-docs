---
title: WEEKS_DIFF (Lakehouse v2)
description: WEEKS_DIFF – gibt die Anzahl der Wochen zwischen zwei Datumswerten zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weeks-diff.md
---

Gibt die Anzahl der Wochen zwischen zwei Datumswerten zurück.

## Analyze-Syntax

```python
func.weeks_diff(<end_date>, <start_date>)
```

## Analyze-Beispiele

```python
func.weeks_diff('2024-03-01', '2024-01-01')

┌───┐
│ 8  │
└───┘
```

## SQL-Syntax

```sql
WEEKS_DIFF(<end_date>, <start_date>)
```

## SQL-Beispiele

```sql
SELECT WEEKS_DIFF('2024-03-01', '2024-01-01');

┌───┐
│ 8  │
└───┘
```
