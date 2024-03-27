---
title: NOT RLIKE
---

Returns 1 if the string expr doesn't match the regular expression specified by the pattern pat, 0 otherwise.

# Analyze Syntax

```python
func.
```

## Analyze Examples
```python
func.
+-----------------+
| func. |
+-----------------+
|              50 |
+-----------------+
```

## SQL Syntax

```sql
<expr> NOT RLIKE <pattern>
```

## SQL Examples

```sql
SELECT 'databend' not rlike 'd*';
+-----------------------------+
| ('databend' not rlike 'd*') |
+-----------------------------+
|                           0 |
+-----------------------------+
```