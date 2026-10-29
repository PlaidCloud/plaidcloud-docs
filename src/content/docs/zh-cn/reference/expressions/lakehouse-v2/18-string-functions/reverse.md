---
title: "REVERSE (String, Lakehouse v2)"
description: REVERSE：反转字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/reverse.md
---

反转字符串。

## Analyze 语法

```python
func.reverse(<str>)
```

## Analyze 示例

```python
func.reverse('hello')

┌─────────┐
│ 'olleh'  │
└─────────┘
```

## SQL 语法

```sql
REVERSE(<str>)
```

## SQL 示例

```sql
SELECT REVERSE('hello');

┌───────┐
│ olleh  │
└───────┘
```
