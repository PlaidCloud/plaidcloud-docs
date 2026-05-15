---
title: MURMUR_HASH3_32 (Lakehouse v2)
description: MURMUR_HASH3_32 — Returns the 32-bit MurmurHash3 hash of a value.
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
