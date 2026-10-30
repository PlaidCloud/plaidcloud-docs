---
title: LTRIM (Lakehouse v2)
description: LTRIM：删除字符串开头的空白字符或指定字符。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ltrim.md
---

删除字符串开头的空白字符或指定字符。

## Analyze 语法

```python
func.ltrim(<str>)
```

## Analyze 示例

```python
func.ltrim('   hello')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## SQL 语法

```sql
LTRIM(<str>)
```

## SQL 示例

```sql
SELECT LTRIM('   hello');

┌───────┐
│ hello  │
└───────┘
```
