---
title: "[ NOT ] IN"
description: "Learn how to use the [ NOT ] IN conditional function in PlaidCloud Lakehouse. Checks whether a value is (or is not) in an explicit list. Includes syntax and..."
---

Checks whether a value is (or is not) in an explicit list.

## Analyze Syntax

```python
table.columns.in_((<value1>, <value2> ...))
```

## Analyze Examples

```python
table.columns.in_((<value1>, <value2> ...))

┌──────────────────────────┐
│ table.column.in_((2, 3)) │
├──────────────────────────┤
│ true                     │
└──────────────────────────┘
```

## SQL Syntax

```sql
<value> [ NOT ] IN (<value1>, <value2> ...)
```

## SQL Examples

```sql
SELECT 1 NOT IN (2, 3);

┌────────────────┐
│ 1 not in(2, 3) │
├────────────────┤
│ true           │
└────────────────┘
```
