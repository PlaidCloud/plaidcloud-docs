---
title: MD5
description: "Learn how to use the MD5 cryptographic function in PlaidCloud Lakehouse. Returns the MD5 hash of a string as a 32-character hexadecimal string."
---

Returns the MD5 hash of a string as a 32-character hexadecimal string.

## Analyze Syntax

```python
func.md5(<str>)
```

## Analyze Examples

```python
func.md5('hello')

┌────────────────────────────────────┐
│ '5d41402abc4b2a76b9719d911017c592'  │
└────────────────────────────────────┘
```

## SQL Syntax

```sql
MD5(<str>)
```

## SQL Examples

```sql
SELECT MD5('hello');

┌──────────────────────────────────┐
│ 5d41402abc4b2a76b9719d911017c592  │
└──────────────────────────────────┘
```
