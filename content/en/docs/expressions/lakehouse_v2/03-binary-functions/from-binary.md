---
title: FROM_BINARY
description: "Learn how to use the FROM_BINARY binary function in PlaidCloud Lakehouse. Converts a binary value to a VARCHAR string based on the specified binary format."
---

Converts a binary value to a VARCHAR string based on the specified binary format.

## Analyze Syntax

```python
func.from_binary(<binary>, <format>)
```

## Analyze Examples

```python
func.from_binary(b'\x48\x65\x6c\x6c\x6f', 'utf8')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## SQL Syntax

```sql
FROM_BINARY(<binary>, <format>)
```

## SQL Examples

```sql
SELECT FROM_BINARY(X'48656C6C6F', 'utf8');

┌───────┐
│ Hello  │
└───────┘
```
