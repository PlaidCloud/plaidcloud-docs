---
title: PREVIOUS_DAY (Lakehouse v2)
description: PREVIOUS_DAY – gibt das Datum des vorherigen angegebenen Wochentags vor einem bestimmten Datum zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/previous-day.md
---

Gibt das Datum des vorherigen angegebenen Wochentags vor einem bestimmten Datum zurück.

## Analyze-Syntax

```python
func.previous_day(<date>, <weekday>)
```

## Analyze-Beispiele

```python
func.previous_day('2024-06-15', 'Monday')

┌──────────────┐
│ '2024-06-10'  │
└──────────────┘
```

## SQL-Syntax

```sql
PREVIOUS_DAY(<date>, <weekday>)
```

## SQL-Beispiele

```sql
SELECT PREVIOUS_DAY('2024-06-15', 'Monday');

┌────────────┐
│ 2024-06-10  │
└────────────┘
```
