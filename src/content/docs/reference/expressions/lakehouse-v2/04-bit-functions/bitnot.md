---
title: BITNOT
description: "Learn how to use the BITNOT bit function in PlaidCloud Lakehouse. Returns the bitwise NOT of a numeric value - see syntax, examples, and output."
---

Returns the bitwise NOT of a numeric value.

## Analyze Syntax

```python
func.bitnot(<x>)
```

## Analyze Examples

```python
func.bitnot(0)

┌──────┐
│ '-1'  │
└──────┘
```

## SQL Syntax

```sql
BITNOT(<x>)
```

## SQL Examples

```sql
SELECT BITNOT(0);

┌────┐
│ -1  │
└────┘
```
