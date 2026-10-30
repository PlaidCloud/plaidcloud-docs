---
title: STARTS_WITH (Lakehouse v2)
description: STARTS_WITH：检查字符串是否以指定前缀开头。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/starts-with.md
---

检查字符串是否以指定前缀开头。

## Analyze 语法

```python
func.starts_with(<str>, <prefix>)
```

## Analyze 示例

```python
func.starts_with('StarRocks', 'Star')

┌───┐
│ 1  │
└───┘
```

## SQL 语法

```sql
STARTS_WITH(<str>, <prefix>)
```

## SQL 示例

```sql
SELECT STARTS_WITH('StarRocks', 'Star');

┌───┐
│ 1  │
└───┘
```
