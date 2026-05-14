---
title: HEX_DECODE_BINARY
description: "Learn how to use the HEX_DECODE_BINARY string function in PlaidCloud Lakehouse. Decodes a hexadecimal string to a binary value - with syntax and examples."
---

Decodes a hexadecimal string to a binary value.

## Analyze Syntax

```python
func.hex_decode_binary(<hex_str>)
```

## Analyze Examples

```python
func.hex_decode_binary('48656C6C6F')

┌──────────┐
│ b'Hello'  │
└──────────┘
```

## SQL Syntax

```sql
HEX_DECODE_BINARY(<hex_str>)
```

## SQL Examples

```sql
SELECT HEX_DECODE_BINARY('48656C6C6F');

┌───────┐
│ Hello  │
└───────┘
```
