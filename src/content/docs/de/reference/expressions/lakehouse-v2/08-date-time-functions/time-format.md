---
title: TIME_FORMAT (Lakehouse v2)
description: TIME_FORMAT – formatiert einen Zeitwert gemäß einer Formatzeichenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/time-format.md
---

Formatiert einen Zeitwert gemäß einer Formatzeichenfolge.

## Analyze-Syntax

```python
func.time_format(<time>, <format>)
```

## Analyze-Beispiele

```python
func.time_format('14:30:00', '%H hours %i minutes')

┌───────────────────────┐
│ '14 hours 30 minutes'  │
└───────────────────────┘
```

## SQL-Syntax

```sql
TIME_FORMAT(<time>, <format>)
```

## SQL-Beispiele

```sql
SELECT TIME_FORMAT('14:30:00', '%H hours %i minutes');

┌─────────────────────┐
│ 14 hours 30 minutes  │
└─────────────────────┘
```
