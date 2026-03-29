---
title: VAR_POP
---

Returns the population variance. Alias for `VARIANCE_POP`.

## Analyze Syntax

```python
func.var_pop(get_column(table, 'score'))
```

## Analyze Examples

```python
func.var_pop(get_column(table, 'score'))

┌────────┐
│ 234.72 │
└────────┘
```

## SQL Syntax

```sql
VAR_POP(<score>)
```

## SQL Examples

```sql
SELECT VAR_POP(score) FROM test_results;

┌────────┐
│ 234.72 │
└────────┘
```
