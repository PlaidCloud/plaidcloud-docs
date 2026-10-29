---
title: LOWER (Lakehouse v2)
description: LOWER：将字符串转换为小写。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/lower.md
---

将字符串转换为小写。

## Analyze 语法

```python
func.lower(<str>)
```

## Analyze 示例

```python
func.lower('HELLO')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## SQL 语法

```sql
LOWER(<str>)
```

## SQL 示例

```sql
SELECT LOWER('HELLO');

┌───────┐
│ hello  │
└───────┘
```
