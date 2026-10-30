---
title: NEXT_DAY (Lakehouse v2)
description: NEXT_DAY – gibt das Datum des nächsten angegebenen Wochentags nach einem bestimmten Datum zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/next-day.md
---

Gibt das Datum des nächsten angegebenen Wochentags nach einem bestimmten Datum zurück.

## Analyze-Syntax

```python
func.next_day(<date>, <weekday>)
```

## Analyze-Beispiele

```python
func.next_day('2024-06-15', 'Monday')

┌──────────────┐
│ '2024-06-17'  │
└──────────────┘
```

## SQL-Syntax

```sql
NEXT_DAY(<date>, <weekday>)
```

## SQL-Beispiele

```sql
SELECT NEXT_DAY('2024-06-15', 'Monday');

┌────────────┐
│ 2024-06-17  │
└────────────┘
```
