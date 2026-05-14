---
title: TO_VARIANT
description: "Learn how to use the TO_VARIANT conversion function in PlaidCloud Lakehouse. Converts a value to VARIANT data type. Includes syntax and examples."
---

Converts a value to VARIANT data type.

## Analyze Syntax

```python
func.to_variant( <expr> )
```

## Analyze Examples

```python
func.to_variant(to_bitmap('100,200,300'))

┌───────────────────────────────────────────┐
│ func.to_variant(to_bitmap('100,200,300')) │
├───────────────────────────────────────────┤
│ [100,200,300]                             │
└───────────────────────────────────────────┘
```

## SQL Syntax

```sql
TO_VARIANT( <expr> )
```

## SQL Examples

```sql
SELECT TO_VARIANT(TO_BITMAP('100,200,300'));

┌──────────────────────────────────────┐
│ to_variant(to_bitmap('100,200,300')) │
├──────────────────────────────────────┤
│ [100,200,300]                        │
└──────────────────────────────────────┘
```
