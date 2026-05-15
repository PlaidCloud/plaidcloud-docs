---
title: RAND() (Lakehouse v1)
description: RAND() — returns a random floating-point value v in the range 0 <= v < 1.
---

Returns a random floating-point value v in the range 0 &lt;= v &lt; 1.0. To obtain a random integer R in the range i &lt;= R &lt; j, use the expression FLOOR(i + RAND() * (j − i)).

## Analyze Syntax

```python
func.rand()
```

## Analyze Examples

```python
func.rand()

┌────────────────────┐
│    func.rand()     │
├────────────────────┤
│ 0.5191511074382174 │
└────────────────────┘
```

## SQL Syntax

```sql
RAND()
```

## SQL Examples

```sql
SELECT RAND();

┌────────────────────┐
│       rand()       │
├────────────────────┤
│ 0.5191511074382174 │
└────────────────────┘
```
