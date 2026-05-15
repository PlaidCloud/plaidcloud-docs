---
title: BAR (Lakehouse v2)
description: "Use the BAR utility function in PlaidCloud Lakehouse. Returns a visual bar string representation of a value within a range. Useful for text-based."
---

Returns a visual bar string representation of a value within a range. Useful for text-based visualizations.

## Analyze Syntax

```python
func.bar(<value>, <min>, <max>, <width>)
```

## Analyze Examples

```python
func.bar(50, 0, 100, 20)

┌──────────────────────┐
│ ██████████           │
└──────────────────────┘
```

## SQL Syntax

```sql
BAR(<value>, <min>, <max>, <width>)
```

## SQL Examples

```sql
SELECT score, BAR(score, 0, 100, 20) AS bar FROM students;

┌───────┬──────────────────────┐
│ score │ bar                  │
├───────┼──────────────────────┤
│    25 │ █████                │
│    50 │ ██████████           │
│    75 │ ███████████████      │
│   100 │ ████████████████████ │
└───────┴──────────────────────┘
```
