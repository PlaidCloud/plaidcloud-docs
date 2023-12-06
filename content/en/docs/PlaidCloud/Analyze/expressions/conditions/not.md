---
title: not_
slug: not
weight: 4.0
description: The PostgreSQL NOT condition (also called the NOT Operator) is used to negate a condition in a SELECT, INSERT, UPDATE, or DELETE statement
date: 2022-01-25T07:39:53
---

The PostgreSQL NOT condition (also called the NOT Operator) is used to negate a condition in a SELECT, INSERT, UPDATE, or DELETE statement

## Syntax
```python
not_(value)
```

## Examples
```python
not_(and_(table.VALUE_FC==0.0, table.VALUE_LC==0.0))
```
```python
not_(or_(get_column(table, 'GL Account').startswith('7'), get_column(table, 'GL Account').startswith('8')))
```
