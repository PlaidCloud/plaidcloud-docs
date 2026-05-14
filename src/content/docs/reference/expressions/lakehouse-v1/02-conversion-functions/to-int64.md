---
title: TO_INT64
description: "Learn how to use the TO_INT64 conversion function in PlaidCloud Lakehouse. Converts a value to INT64 data type. Includes syntax and examples."
---

Converts a value to INT64 data type.

## Analyze Syntax

```python
func.to_int64( <expr> )
```

## Analyze Examples

```python
func.to_int64('123')

┌──────────────────────┐
│ func.to_int64('123') │
├──────────────────────┤
│                  123 │
└──────────────────────┘
```

## SQL Syntax

```sql
TO_INT64( <expr> )
```

## SQL Examples

```sql
SELECT TO_INT64('123');

┌─────────────────┐
│ to_int64('123') │
├─────────────────┤
│             123 │
└─────────────────┘
```
