---
title: DPOW
description: "Learn how to use the DPOW math function in PlaidCloud Lakehouse. Alias for `POW`. See [POW](pow) - see syntax, examples, and output."
---

Alias for `POW`. See [POW](pow).

## Analyze Syntax

```python
func.dpow(2, 10)
```

## Analyze Examples

```python
func.dpow(2, 10)

┌────────┐
│ 1024.0 │
└────────┘
```

## SQL Syntax

```sql
DPOW(<x>)
```

## SQL Examples

```sql
SELECT DPOW(2, 10);

┌────────┐
│ 1024.0 │
└────────┘
```
