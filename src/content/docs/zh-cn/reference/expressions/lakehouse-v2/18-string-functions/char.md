---
title: CHAR (Lakehouse v2)
description: CHAR：返回指定 ASCII 码对应的字符。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/char.md
---

返回指定 ASCII 码对应的字符。

## Analyze 语法

```python
func.char(<code>)
```

## Analyze 示例

```python
func.char(65)

┌─────┐
│ 'A'  │
└─────┘
```

## SQL 语法

```sql
CHAR(<code>)
```

## SQL 示例

```sql
SELECT CHAR(65);

┌───┐
│ A  │
└───┘
```
