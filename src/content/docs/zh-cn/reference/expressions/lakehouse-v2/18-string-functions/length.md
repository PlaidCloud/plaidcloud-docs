---
title: LENGTH (Lakehouse v2)
description: LENGTH：返回字符串的字节长度。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/length.md
---

返回字符串的字节长度。

## Analyze 语法

```python
func.length(<str>)
```

## Analyze 示例

```python
func.length('hello')

┌───┐
│ 5  │
└───┘
```

## SQL 语法

```sql
LENGTH(<str>)
```

## SQL 示例

```sql
SELECT LENGTH('hello');

┌───┐
│ 5  │
└───┘
```
