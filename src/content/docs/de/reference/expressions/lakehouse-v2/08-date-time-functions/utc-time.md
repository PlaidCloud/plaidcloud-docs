---
title: UTC_TIME (Lakehouse v2)
description: UTC_TIME – gibt die aktuelle UTC-Uhrzeit zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/utc-time.md
---

Gibt die aktuelle UTC-Uhrzeit zurück.

## Analyze-Syntax

```python
func.utc_time()
```

## Analyze-Beispiele

```python
func.utc_time()

┌────────────┐
│ '18:30:00'  │
└────────────┘
```

## SQL-Syntax

```sql
UTC_TIME()
```

## SQL-Beispiele

```sql
SELECT UTC_TIME();

┌──────────┐
│ 18:30:00  │
└──────────┘
```
