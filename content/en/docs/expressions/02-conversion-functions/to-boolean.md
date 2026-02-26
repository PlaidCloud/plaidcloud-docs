---
title: TO_BOOLEAN
---

Converts a value to BOOLEAN data type.

## Analyze Syntax

```python
func.to_boolean( <expr> )
```

## Analyze Examples

```python
func.to_boolean('true')

┌──────────────────────────┐
│ func.to_boolean('true')  │
├──────────────────────────┤
│ true                     │
└──────────────────────────┘
```

## SQL Syntax

```sql
TO_BOOLEAN( <expr> )
```

## SQL Examples

```sql
SELECT TO_BOOLEAN('true');

┌────────────────────┐
│ to_boolean('true') │
├────────────────────┤
│ true               │
└────────────────────┘
```