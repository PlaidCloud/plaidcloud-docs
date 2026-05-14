---
title: TO_BINARY
description: "Learn how to use the TO_BINARY binary function in PlaidCloud Lakehouse. Converts a VARCHAR string to a binary value based on the specified binary format."
---

Converts a VARCHAR string to a binary value based on the specified binary format.

## Analyze Syntax

```python
func.to_binary(<str>, <format>)
```

## Analyze Examples

```python
func.to_binary('Hello', 'utf8')

┌──────────┐
│ b'Hello'  │
└──────────┘
```

## SQL Syntax

```sql
TO_BINARY(<str>, <format>)
```

## SQL Examples

```sql
SELECT TO_BINARY('Hello', 'utf8');

┌────────────┐
│ 48656C6C6F  │
└────────────┘
```
