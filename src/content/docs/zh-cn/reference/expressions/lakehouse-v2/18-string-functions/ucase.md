---
title: UCASE (Lakehouse v2)
description: UCASE：将字符串转换为大写。是 `UPPER` 的别名。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ucase.md
---

将字符串转换为大写。是 `UPPER` 的别名。

## Analyze 语法

```python
func.ucase(<str>)
```

## Analyze 示例

```python
func.ucase('hello')

┌─────────┐
│ 'HELLO'  │
└─────────┘
```

## SQL 语法

```sql
UCASE(<str>)
```

## SQL 示例

```sql
SELECT UCASE('hello');

┌───────┐
│ HELLO  │
└───────┘
```
