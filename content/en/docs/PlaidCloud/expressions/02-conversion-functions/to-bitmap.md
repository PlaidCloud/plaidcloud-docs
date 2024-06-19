---
title: TO_BITMAP
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