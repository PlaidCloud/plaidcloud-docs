---
title: NOT RLIKE
---

Returns 1 if the string expr doesn't match the regular expression specified by the pattern pat, 0 otherwise.

# Analyze Syntax

```python
not_(<column>.regexp_match(<pattern>))
```

## Analyze Examples
```python

With an input table of:
+-----------------+
| my_clothes      |
+-----------------+
| plaid pants     |
| plaid hat       |
| plaid shirt     |
| shoes           |
+-----------------+

not_(my_clothes.regexp_match('p*'))
+-------------------------------------+
| not_(my_clothes.regexp_match('p*')) |
+-------------------------------------+
| false                               |
| false                               |
| false                               |
| true                                |
+-------------------------------------+
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