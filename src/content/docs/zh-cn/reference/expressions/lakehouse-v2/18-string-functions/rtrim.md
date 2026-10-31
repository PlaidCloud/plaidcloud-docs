---
title: RTRIM (Lakehouse v2)
description: RTRIM：删除字符串末尾的空白字符或指定字符。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/rtrim.md
---

删除字符串末尾的空白字符或指定字符。

## Analyze 语法

```python
func.rtrim(<str>)
```

## Analyze 示例

```python
func.rtrim('hello   ')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## SQL 语法

```sql
RTRIM(<str>)
```

## SQL 示例

```sql
SELECT RTRIM('hello   ');

┌───────┐
│ hello  │
└───────┘
```
