---
title: STRLEFT
---

Returns the leftmost N characters of a string. Alias for `LEFT`.

## Analyze Syntax

```python
func.strleft(<str>, <len>)
```

## Analyze Examples

```python
func.strleft('StarRocks', 4)

┌────────┐
│ 'Star'  │
└────────┘
```

## SQL Syntax

```sql
STRLEFT(<str>, <len>)
```

## SQL Examples

```sql
SELECT STRLEFT('StarRocks', 4);

┌──────┐
│ Star  │
└──────┘
```
