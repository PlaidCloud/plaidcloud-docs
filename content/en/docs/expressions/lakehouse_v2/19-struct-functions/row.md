---
title: ROW
description: "Learn how to use the ROW struct function in PlaidCloud Lakehouse. Creates a struct from a list of values - see syntax, examples, and output."
---

Creates a struct from a list of values.

## Analyze Syntax

```python
func.row(<val1>[, <val2>, ...])
```

## Analyze Examples

```python
func.row('Alice', 30)

┌────────────────────────────┐
│ {'col1':'Alice','col2':30}  │
└────────────────────────────┘
```

## SQL Syntax

```sql
ROW(<val1>[, <val2>, ...])
```

## SQL Examples

```sql
SELECT ROW('Alice', 30);

┌────────────────────────────┐
│ {"col1":"Alice","col2":30}  │
└────────────────────────────┘
```
