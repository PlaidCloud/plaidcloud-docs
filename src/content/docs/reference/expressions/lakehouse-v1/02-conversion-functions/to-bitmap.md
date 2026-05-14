---
title: TO_BITMAP
description: "Learn how to use the TO_BITMAP conversion function in PlaidCloud Lakehouse. Converts a value to BITMAP data type. Includes syntax and examples."
---

Converts a value to BITMAP data type.

## Analyze Syntax

```python
func.to_bitmap( <expr> )
```

## Analyze Examples

```python
func.to_bitmap('1101')

┌─────────────────────────┐
│ func.to_bitmap('1101')  │
├─────────────────────────┤
│ <bitmap binary>         │
└─────────────────────────┘
```

## SQL Syntax

```sql
TO_BITMAP( <expr> )
```

## SQL Examples

```sql
SELECT TO_BITMAP('1101');

┌───────────────────┐
│ to_bitmap('1101') │
├───────────────────┤
│ <bitmap binary>   │
└───────────────────┘
```
