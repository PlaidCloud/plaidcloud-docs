---
title: SEC_TO_TIME
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
