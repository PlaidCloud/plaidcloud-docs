---
title: UNNEST_BITMAP
---

Expands a bitmap into a set of rows.

## Analyze Syntax

```python
func.unnest_bitmap(<bitmap>)
```

## Analyze Examples

```python
func.unnest_bitmap(get_column(table, 'bm'))
```

## SQL Syntax

```sql
UNNEST_BITMAP(<bitmap>)
```

## SQL Examples

```sql
SELECT * FROM TABLE(UNNEST_BITMAP(BITMAP_FROM_STRING('1,2,3')));

┌───────┐
│ value │
├───────┤
│     1 │
│     2 │
│     3 │
└───────┘
```
