---
title: ENDS_WITH (Lakehouse v2)
description: ENDS_WITH：检查字符串是否以指定后缀结尾。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ends-with.md
---

检查字符串是否以指定后缀结尾。

## Analyze 语法

```python
func.ends_with(<str>, <suffix>)
```

## Analyze 示例

```python
func.ends_with('hello world', 'world')

┌───┐
│ 1  │
└───┘
```

## SQL 语法

```sql
ENDS_WITH(<str>, <suffix>)
```

## SQL 示例

```sql
SELECT ENDS_WITH('hello world', 'world');

┌───┐
│ 1  │
└───┘
```
