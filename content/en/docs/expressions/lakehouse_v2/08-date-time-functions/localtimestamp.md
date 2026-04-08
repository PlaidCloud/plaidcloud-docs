---
title: LOCALTIMESTAMP
description: "Learn how to use the LOCALTIMESTAMP date/time function in PlaidCloud Lakehouse. Returns the current date and time. Alias for `NOW` - with syntax and examples."
---

Returns the current date and time. Alias for `NOW`.

## Analyze Syntax

```python
func.localtimestamp()
```

## Analyze Examples

```python
func.localtimestamp()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## SQL Syntax

```sql
LOCALTIMESTAMP()
```

## SQL Examples

```sql
SELECT LOCALTIMESTAMP();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
