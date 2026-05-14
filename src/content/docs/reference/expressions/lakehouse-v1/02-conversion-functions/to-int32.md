---
title: TO_INT32
description: "Learn how to use the TO_INT32 conversion function in PlaidCloud Lakehouse. Converts a value to INT32 data type. Includes syntax and examples."
---

Converts a value to INT32 data type.

## Analyze Syntax

```python
func.to_int32( <expr> )
```

## Analyze Examples

```python
func.to_int32('123')

┌──────────────────────┐
│ func.to_int32('123') │
├──────────────────────┤
│                  123 │
└──────────────────────┘
```

## SQL Syntax

```sql
TO_INT32( <expr> )
```

## SQL Examples

```sql
SELECT TO_INT32('123');

┌─────────────────┐
│ to_int32('123') │
├─────────────────┤
│             123 │
└─────────────────┘
```
