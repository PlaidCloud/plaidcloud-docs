---
title: MURMUR_HASH3_32
description: "Learn how to use the MURMUR_HASH3_32 hash function in PlaidCloud Lakehouse. Returns the 32-bit MurmurHash3 hash of a value - with syntax and examples."
---

Returns the 32-bit MurmurHash3 hash of a value.

## Analyze Syntax

```python
func.murmur_hash3_32(<expr>[, ...])
```

## Analyze Examples

```python
func.murmur_hash3_32('hello')

┌───────────┐
│ 613153351  │
└───────────┘
```

## SQL Syntax

```sql
MURMUR_HASH3_32(<expr>[, ...])
```

## SQL Examples

```sql
SELECT MURMUR_HASH3_32('hello');

┌───────────┐
│ 613153351  │
└───────────┘
```
