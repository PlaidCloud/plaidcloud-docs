---
title: FIND_IN_SET (Lakehouse v2)
description: FIND_IN_SET：返回字符串在逗号分隔列表中的位置。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/find-in-set.md
---

返回字符串在逗号分隔列表中的位置。

## Analyze 语法

```python
func.find_in_set(<str>, <strlist>)
```

## Analyze 示例

```python
func.find_in_set('b', 'a,b,c')

┌───┐
│ 2  │
└───┘
```

## SQL 语法

```sql
FIND_IN_SET(<str>, <strlist>)
```

## SQL 示例

```sql
SELECT FIND_IN_SET('b', 'a,b,c');

┌───┐
│ 2  │
└───┘
```
