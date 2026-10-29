---
title: CONVERT_TZ (Lakehouse v2)
description: CONVERT_TZ – rechnet einen Datums-/Zeitwert von einer Zeitzone in eine andere um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/convert-tz.md
---

Rechnet einen Datums-/Zeitwert von einer Zeitzone in eine andere um.

## Analyze-Syntax

```python
func.convert_tz(<datetime>, <from_tz>, <to_tz>)
```

## Analyze-Beispiele

```python
func.convert_tz('2024-01-01 12:00:00', 'UTC', 'America/New_York')

┌───────────────────────┐
│ '2024-01-01 07:00:00'  │
└───────────────────────┘
```

## SQL-Syntax

```sql
CONVERT_TZ(<datetime>, <from_tz>, <to_tz>)
```

## SQL-Beispiele

```sql
SELECT CONVERT_TZ('2024-01-01 12:00:00', 'UTC', 'America/New_York');

┌─────────────────────┐
│ 2024-01-01 07:00:00  │
└─────────────────────┘
```
