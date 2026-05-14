---
title: SEC_TO_TIME
description: "Learn how to use the SEC_TO_TIME date/time function in PlaidCloud Lakehouse. Converts seconds to a time value - see syntax, examples, and output."
---

Converts seconds to a time value.

## Analyze Syntax

```python
func.sec_to_time(<seconds>)
```

## Analyze Examples

```python
func.sec_to_time(3661)

┌────────────┐
│ '01:01:01'  │
└────────────┘
```

## SQL Syntax

```sql
SEC_TO_TIME(<seconds>)
```

## SQL Examples

```sql
SELECT SEC_TO_TIME(3661);

┌──────────┐
│ 01:01:01  │
└──────────┘
```
