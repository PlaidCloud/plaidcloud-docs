---
title: STRRIGHT
---

Returns the rightmost N characters of a string. Alias for `RIGHT`.

## Analyze Syntax

```python
func.strright(<str>, <len>)
```

## Analyze Examples

```python
func.strright('StarRocks', 5)

┌─────────┐
│ 'Rocks'  │
└─────────┘
```

## SQL Syntax

```sql
STRRIGHT(<str>, <len>)
```

## SQL Examples

```sql
SELECT STRRIGHT('StarRocks', 5);

┌───────┐
│ Rocks  │
└───────┘
```
