---
title: BASE64_DECODE_BINARY
---

Decodes a base64-encoded string to a binary value.

## Analyze Syntax

```python
func.base64_decode_binary(<str>)
```

## Analyze Examples

```python
func.base64_decode_binary('SGVsbG8=')

┌──────────┐
│ b'Hello'  │
└──────────┘
```

## SQL Syntax

```sql
BASE64_DECODE_BINARY(<str>)
```

## SQL Examples

```sql
SELECT BASE64_DECODE_BINARY('SGVsbG8=');

┌───────┐
│ Hello  │
└───────┘
```
