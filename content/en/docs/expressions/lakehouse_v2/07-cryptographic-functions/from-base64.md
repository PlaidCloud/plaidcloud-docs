---
title: FROM_BASE64
description: "Learn how to use the FROM_BASE64 cryptographic function in PlaidCloud Lakehouse. Decodes a base64-encoded string. Alias for `BASE64_DECODE_STRING`."
---

Decodes a base64-encoded string. Alias for `BASE64_DECODE_STRING`.

## Analyze Syntax

```python
func.from_base64(<str>)
```

## Analyze Examples

```python
func.from_base64('SGVsbG8=')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## SQL Syntax

```sql
FROM_BASE64(<str>)
```

## SQL Examples

```sql
SELECT FROM_BASE64('SGVsbG8=');

┌───────┐
│ Hello  │
└───────┘
```
