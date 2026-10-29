---
title: TRIM (Lakehouse v2)
description: TRIM：删除字符串开头和末尾的空白字符或指定字符。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/trim.md
---

删除字符串开头和末尾的空白字符或指定字符。

## Analyze 语法

```python
func.trim(<str>)
```

## Analyze 示例

```python
func.trim('  hello  ')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## SQL 语法

```sql
TRIM(<str>)
```

## SQL 示例

```sql
SELECT TRIM('  hello  ');

┌───────┐
│ hello  │
└───────┘
```
