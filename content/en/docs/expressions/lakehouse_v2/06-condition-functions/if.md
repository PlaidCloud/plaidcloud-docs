---
title: IF
---

Returns one of two values depending on whether a condition is TRUE or FALSE.

## Analyze Syntax

```python
func.if_(get_column(table, 'score') >= 60, 'Pass', 'Fail')
```

## Analyze Examples

```python
func.if_(get_column(table, 'score') >= 60, 'Pass', 'Fail')
```

## SQL Syntax

```sql
IF(<score> >= 60, 'Pass', 'Fail')
```

## SQL Examples

```sql
SELECT name, IF(score >= 60, 'Pass', 'Fail') AS result FROM students;

┌─────────┬────────┐
│ name    │ result │
├─────────┼────────┤
│ Alice   │ Pass   │
│ Bob     │ Fail   │
│ Charlie │ Pass   │
└─────────┴────────┘
```
