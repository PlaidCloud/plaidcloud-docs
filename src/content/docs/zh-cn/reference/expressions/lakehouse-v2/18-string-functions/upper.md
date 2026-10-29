---
title: UPPER (Lakehouse v2)
description: UPPER：将字符串转换为大写。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/upper.md
---

将字符串转换为大写。

## Analyze 语法

```python
func.upper(<str>)
```

## Analyze 示例

```python
func.upper('hello')

┌─────────┐
│ 'HELLO'  │
└─────────┘
```

## SQL 语法

```sql
UPPER(<str>)
```

## SQL 示例

```sql
SELECT UPPER('hello');

┌───────┐
│ HELLO  │
└───────┘
```
