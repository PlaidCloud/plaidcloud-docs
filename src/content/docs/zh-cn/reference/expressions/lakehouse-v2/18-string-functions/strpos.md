---
title: STRPOS (Lakehouse v2)
description: STRPOS：返回子字符串首次出现的位置。是 `LOCATE` 的别名。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strpos.md
---

返回子字符串首次出现的位置。是 `LOCATE` 的别名。

## Analyze 语法

```python
func.strpos(<str>, <substr>)
```

## Analyze 示例

```python
func.strpos('hello world', 'world')

┌───┐
│ 7  │
└───┘
```

## SQL 语法

```sql
STRPOS(<str>, <substr>)
```

## SQL 示例

```sql
SELECT STRPOS('hello world', 'world');

┌───┐
│ 7  │
└───┘
```
