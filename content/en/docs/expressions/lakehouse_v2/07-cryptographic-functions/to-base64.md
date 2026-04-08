---
title: TO_BASE64
description: "Learn how to use the TO_BASE64 cryptographic function in PlaidCloud Lakehouse. Encodes a string to a base64-encoded string - with syntax and examples."
---

Encodes a string to a base64-encoded string.

## Analyze Syntax

```python
func.to_base64(<str>)
```

## Analyze Examples

```python
func.to_base64('Hello')

┌────────────┐
│ 'SGVsbG8='  │
└────────────┘
```

## SQL Syntax

```sql
TO_BASE64(<str>)
```

## SQL Examples

```sql
SELECT TO_BASE64('Hello');

┌──────────┐
│ SGVsbG8=  │
└──────────┘
```
