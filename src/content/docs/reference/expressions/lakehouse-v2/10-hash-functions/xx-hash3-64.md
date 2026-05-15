---
title: XX_HASH3_64
description: XX_HASH3_64 — returns the 64-bit xxHash3 hash of a value - see syntax, examples, and output.
---

Returns the 64-bit xxHash3 hash of a value.

## Analyze Syntax

```python
func.xx_hash3_64(<expr>[, ...])
```

## Analyze Examples

```python
func.xx_hash3_64('hello')

┌──────────┐
│ (bigint)  │
└──────────┘
```

## SQL Syntax

```sql
XX_HASH3_64(<expr>[, ...])
```

## SQL Examples

```sql
SELECT XX_HASH3_64('hello');

┌──────────────────────┐
│ -7685981735718036227  │
└──────────────────────┘
```
