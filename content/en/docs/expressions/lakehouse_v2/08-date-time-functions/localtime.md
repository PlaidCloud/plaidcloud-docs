---
title: LOCALTIME
description: "Learn how to use the LOCALTIME date/time function in PlaidCloud Lakehouse. Returns the current date and time. Alias for `NOW` - with syntax and examples."
---

Returns the current date and time. Alias for `NOW`.

## Analyze Syntax

```python
func.localtime()
```

## Analyze Examples

```python
func.localtime()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## SQL Syntax

```sql
LOCALTIME()
```

## SQL Examples

```sql
SELECT LOCALTIME();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
