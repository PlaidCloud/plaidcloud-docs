---
title: SUM_MAP
description: SUM_MAP — sums values grouped by keys in map columns - see syntax, examples, and output.
---

Sums values grouped by keys in map columns.

## Analyze Syntax

```python
func.sum_map(get_column(table, 'key_col'), get_column(table, 'val_col'))
```

## Analyze Examples

```python
func.sum_map(get_column(table, 'keys'), get_column(table, 'values'))

┌─────────────────┐
│ {'a':10,'b':20} │
└─────────────────┘
```

## SQL Syntax

```sql
SUM_MAP(<key_col>, <val_col>)
```

## SQL Examples

```sql
SELECT SUM_MAP(keys, values) FROM metrics;

┌─────────────────┐
│ {"a":10,"b":20} │
└─────────────────┘
```
