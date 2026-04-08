---
title: BASE64_DECODE_BINARY
description: "Learn how to use the BASE64_DECODE_BINARY cryptographic function in PlaidCloud Lakehouse. Decodes a base64-encoded string to a binary value."
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
