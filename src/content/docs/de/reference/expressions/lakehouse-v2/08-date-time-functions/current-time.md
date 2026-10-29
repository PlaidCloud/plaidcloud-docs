---
title: CURRENT_TIME (Lakehouse v2)
description: CURRENT_TIME – gibt die aktuelle Uhrzeit zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/current-time.md
---

Gibt die aktuelle Uhrzeit zurück.

## Analyze-Syntax

```python
func.current_time()
```

## Analyze-Beispiele

```python
func.current_time()

┌────────────┐
│ '14:30:00'  │
└────────────┘
```

## SQL-Syntax

```sql
CURRENT_TIME()
```

## SQL-Beispiele

```sql
SELECT CURRENT_TIME();

┌──────────┐
│ 14:30:00  │
└──────────┘
```
