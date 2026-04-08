---
title: UNIX_TIMESTAMP
description: "Learn how to use the UNIX_TIMESTAMP date/time function in PlaidCloud Lakehouse. Converts a datetime to a Unix timestamp - see syntax, examples, and output."
---

Converts a datetime to a Unix timestamp.

## Analyze Syntax

```python
func.unix_timestamp([<datetime>])
```

## Analyze Examples

```python
func.unix_timestamp('2024-01-01 00:00:00')

┌────────────┐
│ 1704067200  │
└────────────┘
```

## SQL Syntax

```sql
UNIX_TIMESTAMP([<datetime>])
```

## SQL Examples

```sql
SELECT UNIX_TIMESTAMP('2024-01-01 00:00:00');

┌────────────┐
│ 1704067200  │
└────────────┘
```
