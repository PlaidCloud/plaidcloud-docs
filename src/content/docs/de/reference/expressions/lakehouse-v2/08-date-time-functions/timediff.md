---
title: TIMEDIFF (Lakehouse v2)
description: TIMEDIFF – gibt die Differenz zwischen zwei Zeitwerten zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timediff.md
---

Gibt die Differenz zwischen zwei Zeitwerten zurück.

## Analyze-Syntax

```python
func.timediff(<time1>, <time2>)
```

## Analyze-Beispiele

```python
func.timediff('15:30:00', '10:00:00')

┌────────────┐
│ '05:30:00'  │
└────────────┘
```

## SQL-Syntax

```sql
TIMEDIFF(<time1>, <time2>)
```

## SQL-Beispiele

```sql
SELECT TIMEDIFF('15:30:00', '10:00:00');

┌──────────┐
│ 05:30:00  │
└──────────┘
```
