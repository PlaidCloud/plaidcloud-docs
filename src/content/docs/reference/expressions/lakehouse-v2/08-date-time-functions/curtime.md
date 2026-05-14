---
title: CURTIME
description: "Learn how to use the CURTIME date/time function in PlaidCloud Lakehouse. Returns the current time. Alias for `CURRENT_TIME` - with syntax and examples."
---

Returns the current time. Alias for `CURRENT_TIME`.

## Analyze Syntax

```python
func.curtime()
```

## Analyze Examples

```python
func.curtime()

┌────────────┐
│ '14:30:00'  │
└────────────┘
```

## SQL Syntax

```sql
CURTIME()
```

## SQL Examples

```sql
SELECT CURTIME();

┌──────────┐
│ 14:30:00  │
└──────────┘
```
