---
title: LAST_DAY (Lakehouse v2)
description: LAST_DAY – gibt den letzten Tag des Monats für ein angegebenes Datum zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/last-day.md
---

Gibt den letzten Tag des Monats für ein angegebenes Datum zurück.

## Analyze-Syntax

```python
func.last_day(<date>[, <unit>])
```

## Analyze-Beispiele

```python
func.last_day('2024-02-15')

┌──────────────┐
│ '2024-02-29'  │
└──────────────┘
```

## SQL-Syntax

```sql
LAST_DAY(<date>[, <unit>])
```

## SQL-Beispiele

```sql
SELECT LAST_DAY('2024-02-15');

┌────────────┐
│ 2024-02-29  │
└────────────┘
```
