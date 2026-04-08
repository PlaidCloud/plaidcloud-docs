---
title: BASE64_DECODE_STRING
description: "Learn how to use the BASE64_DECODE_STRING cryptographic function in PlaidCloud Lakehouse. Decodes a base64-encoded string to a VARCHAR string."
---

Decodes a base64-encoded string to a VARCHAR string.

## Analyze Syntax

```python
func.base64_decode_string(<str>)
```

## Analyze Examples

```python
func.base64_decode_string('SGVsbG8=')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## SQL Syntax

```sql
BASE64_DECODE_STRING(<str>)
```

## SQL Examples

```sql
SELECT BASE64_DECODE_STRING('SGVsbG8=');

┌───────┐
│ Hello  │
└───────┘
```
