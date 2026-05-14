---
title: TO_BOOLEAN
description: "Learn how to use the TO_BOOLEAN conversion function in PlaidCloud Lakehouse. Converts a value to BOOLEAN data type. Includes syntax and examples."
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
