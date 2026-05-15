---
title: XX_HASH3_128 (Lakehouse v2)
description: XX_HASH3_128 — returns the 128-bit xxHash3 hash of a value.
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
