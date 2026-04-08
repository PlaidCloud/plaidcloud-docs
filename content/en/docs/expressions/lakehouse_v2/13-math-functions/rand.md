---
title: RAND
description: "Learn how to use the RAND math function in PlaidCloud Lakehouse. Returns a random floating-point value between 0 (inclusive) and 1 (exclusive)."
---

Returns a random floating-point value between 0 (inclusive) and 1 (exclusive).

## Analyze Syntax

```python
func.rand([<seed>])
```

## Analyze Examples

```python
func.rand()

┌───────────┐
│ 0.6347...  │
└───────────┘
```

## SQL Syntax

```sql
RAND([<seed>])
```

## SQL Examples

```sql
SELECT RAND();

┌───────────┐
│ 0.6347...  │
└───────────┘
```
