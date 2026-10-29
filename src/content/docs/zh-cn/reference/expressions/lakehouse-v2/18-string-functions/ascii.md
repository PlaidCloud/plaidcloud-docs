---
title: ASCII (Lakehouse v2)
description: ASCII：返回字符串首个字符的 ASCII 码。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ascii.md
---

返回字符串首个字符的 ASCII 码。

## Analyze 语法

```python
func.ascii(<str>)
```

## Analyze 示例

```python
func.ascii('A')

┌────┐
│ 65  │
└────┘
```

## SQL 语法

```sql
ASCII(<str>)
```

## SQL 示例

```sql
SELECT ASCII('A');

┌────┐
│ 65  │
└────┘
```
