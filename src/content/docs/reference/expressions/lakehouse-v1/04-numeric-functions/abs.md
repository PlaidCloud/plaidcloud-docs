---
title: ABS
description: "Learn how to use the ABS numeric function in PlaidCloud Lakehouse. Returns the absolute value of x. Includes detailed syntax, examples, and usage reference."
---

Returns the absolute value of `x`.

## Analyze Syntax

```python
func.abs( <x> )
```

## Analyze Examples

```python
func.abs((- 5))

┌─────────────────┐
│ func.abs((- 5)) │
├─────────────────┤
│               5 │
└─────────────────┘
```

## SQL Syntax

```sql
ABS( <x> )
```

## SQL Examples

```sql
SELECT ABS(-5);

┌────────────┐
│ abs((- 5)) │
├────────────┤
│          5 │
└────────────┘
```
