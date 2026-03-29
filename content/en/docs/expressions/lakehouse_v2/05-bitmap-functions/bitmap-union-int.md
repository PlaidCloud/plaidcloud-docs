---
title: BITMAP_UNION_INT
---

Returns the count of distinct integer values (aggregate).

## Analyze Syntax

```python
func.bitmap_union_int(get_column(table, 'id'))
```

## Analyze Examples

```python
func.bitmap_union_int(get_column(table, 'user_id'))

┌─────┐
│ 500 │
└─────┘
```

## SQL Syntax

```sql
BITMAP_UNION_INT(<id>)
```

## SQL Examples

```sql
SELECT BITMAP_UNION_INT(user_id) FROM visits;

┌─────┐
│ 500 │
└─────┘
```
