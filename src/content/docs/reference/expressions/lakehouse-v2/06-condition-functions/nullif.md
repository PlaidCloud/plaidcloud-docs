---
title: NULLIF (Lakehouse v2)
description: NULLIF — returns NULL if two expressions are equal, otherwise returns the first expression.
---

Returns NULL if two expressions are equal, otherwise returns the first expression.

## Analyze Syntax

```python
func.nullif(get_column(table, 'value'), 0)
```

## Analyze Examples

```python
func.nullif(get_column(table, 'divisor'), 0)
```

## SQL Syntax

```sql
NULLIF(<value>, 0)
```

## SQL Examples

```sql
SELECT 100 / NULLIF(divisor, 0) AS safe_division FROM calculations;

┌───────────────┐
│ safe_division │
├───────────────┤
│         50.00 │
│          NULL │
│         25.00 │
└───────────────┘
```
