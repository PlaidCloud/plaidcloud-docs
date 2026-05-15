---
title: XX_HASH3_64 (Lakehouse v2)
description: XX_HASH3_64 — returns the 64-bit xxHash3 hash of a value.
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
