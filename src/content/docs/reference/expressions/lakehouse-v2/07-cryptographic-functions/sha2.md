---
title: SHA2 (Lakehouse v2)
description: SHA2 — returns the SHA-2 hash of a string for a specified bit length (224, 256, 384, or 512).
---

Returns the SHA-2 hash of a string for a specified bit length (224, 256, 384, or 512).

## Analyze Syntax

```python
func.sha2(<str>, <bit_length>)
```

## Analyze Examples

```python
func.sha2('hello', 256)

┌───────────────┐
│ '2cf24dba...'  │
└───────────────┘
```

## SQL Syntax

```sql
SHA2(<str>, <bit_length>)
```

## SQL Examples

```sql
SELECT SHA2('hello', 256);

┌──────────────────────────────────────────────────────────────────┐
│ 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824  │
└──────────────────────────────────────────────────────────────────┘
```
