---
title: CONV (Lakehouse v2)
description: CONV — 将数值从一种进制转换为另一种进制。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/conv.md
---

将数值从一种进制转换为另一种进制。

## Analyze 语法

```python
func.conv(<num>, <from_base>, <to_base>)
```

## Analyze 示例

```python
func.conv('ff', 16, 10)

┌───────┐
│ '255'  │
└───────┘
```

## SQL 语法

```sql
CONV(<num>, <from_base>, <to_base>)
```

## SQL 示例

```sql
SELECT CONV('ff', 16, 10);

┌─────┐
│ 255  │
└─────┘
```
