---
title: NOT REGEXP
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
<expr> NOT REGEXP <pattern>
```

## SQL Examples

```sql
SELECT 'databend' NOT REGEXP 'd*';
+------------------------------+
| ('databend' not regexp 'd*') |
+------------------------------+
|                            0 |
+------------------------------+
```