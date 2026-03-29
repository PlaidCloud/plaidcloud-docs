---
title: HEX_DECODE_STRING
---

Decodes a hexadecimal string to a VARCHAR string.

## Analyze Syntax

```python
func.hex_decode_string(<hex_str>)
```

## Analyze Examples

```python
func.hex_decode_string('48656C6C6F')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## SQL Syntax

```sql
HEX_DECODE_STRING(<hex_str>)
```

## SQL Examples

```sql
SELECT HEX_DECODE_STRING('48656C6C6F');

┌───────┐
│ Hello  │
└───────┘
```
