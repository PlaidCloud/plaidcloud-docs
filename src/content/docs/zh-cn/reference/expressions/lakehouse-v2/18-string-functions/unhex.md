---
title: UNHEX (Lakehouse v2)
description: UNHEX：将十六进制字符串转换为字符字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/unhex.md
---

将十六进制字符串转换为字符字符串。

## Analyze 语法

```python
func.unhex(<hex_str>)
```

## Analyze 示例

```python
func.unhex('48656C6C6F')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## SQL 语法

```sql
UNHEX(<hex_str>)
```

## SQL 示例

```sql
SELECT UNHEX('48656C6C6F');

┌───────┐
│ Hello  │
└───────┘
```
