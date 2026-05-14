---
title: PERCENTILE_HASH
description: "Learn how to use the PERCENTILE_HASH percentile function in PlaidCloud Lakehouse. Computes a percentile state from a numeric value - with syntax and examples."
---

Computes a percentile state from a numeric value.

## Analyze Syntax

```python
func.percentile_hash(<value>)
```

## Analyze Examples

```python
func.percentile_hash(42.5)

┌─────────┐
│ (state)  │
└─────────┘
```

## SQL Syntax

```sql
PERCENTILE_HASH(<value>)
```

## SQL Examples

```sql
SELECT PERCENTILE_HASH(42.5);

┌────────────────────┐
│ (percentile state)  │
└────────────────────┘
```
