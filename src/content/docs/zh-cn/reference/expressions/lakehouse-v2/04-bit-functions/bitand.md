---
title: BITAND (Lakehouse v2)
description: BITAND：返回两个数值的按位与结果。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitand.md
---

返回两个数值的按位与结果。

## Analyze 语法

```python
func.bitand(<x>, <y>)
```

## Analyze 示例

```python
func.bitand(12, 10)

┌───┐
│ 8  │
└───┘
```

## SQL 语法

```sql
BITAND(<x>, <y>)
```

## SQL 示例

```sql
SELECT BITAND(12, 10);

┌───┐
│ 8  │
└───┘
```
