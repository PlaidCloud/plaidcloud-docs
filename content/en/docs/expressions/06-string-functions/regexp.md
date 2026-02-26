---
title: REGEXP
---

Returns `true` if the string `<expr>` matches the regular expression specified by the `<pattern>`, `false` otherwise.

# Analyze Syntax

```python
<column>.regexp_match(<pattern>)
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

my_clothes.regexp_match('p*')
+-------------------------------+
| my_clothes.regexp_match('p*') |
+-------------------------------+
| true                          |
| true                          |
| true                          |
| false                         |
+-------------------------------+
```

## SQL Syntax

```sql
<expr> REGEXP <pattern>
```

## Aliases

- [RLIKE](rlike)

## SQL Examples

```sql
SELECT 'databend' REGEXP 'd*', 'databend' RLIKE 'd*';

┌────────────────────────────────────────────────────┐
│ ('databend' regexp 'd*') │ ('databend' rlike 'd*') │
├──────────────────────────┼─────────────────────────┤
│ true                     │ true                    │
└────────────────────────────────────────────────────┘
```