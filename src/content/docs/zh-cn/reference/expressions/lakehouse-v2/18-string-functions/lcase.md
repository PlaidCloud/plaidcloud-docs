---
title: LCASE (Lakehouse v2)
description: LCASE：将字符串转换为小写。是 `LOWER` 的别名。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/lcase.md
---

将字符串转换为小写。是 `LOWER` 的别名。

## Analyze 语法

```python
func.lcase(<str>)
```

## Analyze 示例

```python
func.lcase('HELLO')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## SQL 语法

```sql
LCASE(<str>)
```

## SQL 示例

```sql
SELECT LCASE('HELLO');

┌───────┐
│ hello  │
└───────┘
```
