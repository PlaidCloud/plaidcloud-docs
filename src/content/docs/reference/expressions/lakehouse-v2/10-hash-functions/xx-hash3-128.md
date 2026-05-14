---
title: XX_HASH3_128
description: "Learn how to use the XX_HASH3_128 hash function in PlaidCloud Lakehouse. Returns the 128-bit xxHash3 hash of a value - see syntax, examples, and output."
---

Returns the 128-bit xxHash3 hash of a value.

## Analyze Syntax

```python
func.xx_hash3_128(<expr>[, ...])
```

## Analyze Examples

```python
func.xx_hash3_128('hello')

┌────────────┐
│ (largeint)  │
└────────────┘
```

## SQL Syntax

```sql
XX_HASH3_128(<expr>[, ...])
```

## SQL Examples

```sql
SELECT XX_HASH3_128('hello');

┌──────────────────────┐
│ (128-bit hash value)  │
└──────────────────────┘
```
