---
title: TIME_TO_SEC (Lakehouse v2)
description: TIME_TO_SEC – wandelt einen Zeitwert in Sekunden um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/time-to-sec.md
---

Wandelt einen Zeitwert in Sekunden um.

## Analyze-Syntax

```python
func.time_to_sec(<time>)
```

## Analyze-Beispiele

```python
func.time_to_sec('01:01:01')

┌──────┐
│ 3661  │
└──────┘
```

## SQL-Syntax

```sql
TIME_TO_SEC(<time>)
```

## SQL-Beispiele

```sql
SELECT TIME_TO_SEC('01:01:01');

┌──────┐
│ 3661  │
└──────┘
```
