---
title: MD5SUM (Lakehouse v2)
description: MD5SUM — returns the MD5 hash of multiple strings concatenated together.
---

Returns the MD5 hash of multiple strings concatenated together.

## Analyze Syntax

```python
func.md5sum(<str1>[, <str2>, ...])
```

## Analyze Examples

```python
func.md5sum('hello', 'world')

┌────────────────────────────────────┐
│ 'fc5e038d38a57032085441e7fe7010b0'  │
└────────────────────────────────────┘
```

## SQL Syntax

```sql
MD5SUM(<str1>[, <str2>, ...])
```

## SQL Examples

```sql
SELECT MD5SUM('hello', 'world');

┌──────────────────────────────────┐
│ fc5e038d38a57032085441e7fe7010b0  │
└──────────────────────────────────┘
```
