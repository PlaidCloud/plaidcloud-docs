---
title: FROM_UNIXTIME
description: "Learn how to use the FROM_UNIXTIME date/time function in PlaidCloud Lakehouse. Converts a Unix timestamp to a datetime string - with syntax and examples."
---

Converts a Unix timestamp to a datetime string.

## Analyze Syntax

```python
func.from_unixtime(<timestamp>[, <format>])
```

## Analyze Examples

```python
func.from_unixtime(1704067200)

┌───────────────────────┐
│ '2024-01-01 00:00:00'  │
└───────────────────────┘
```

## SQL Syntax

```sql
FROM_UNIXTIME(<timestamp>[, <format>])
```

## SQL Examples

```sql
SELECT FROM_UNIXTIME(1704067200);

┌─────────────────────┐
│ 2024-01-01 00:00:00  │
└─────────────────────┘
```
