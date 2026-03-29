---
title: MD5SUM_NUMERIC
---

Returns the MD5 hash of multiple strings as a 128-bit numeric value.

## Analyze Syntax

```python
func.md5sum_numeric(<str1>[, <str2>, ...])
```

## Analyze Examples

```python
func.md5sum_numeric('hello')

┌────────────┐
│ (largeint)  │
└────────────┘
```

## SQL Syntax

```sql
MD5SUM_NUMERIC(<str1>[, <str2>, ...])
```

## SQL Examples

```sql
SELECT MD5SUM_NUMERIC('hello');

┌─────────────────────────────────────────┐
│ 268224579284945131320661290344218476706  │
└─────────────────────────────────────────┘
```
