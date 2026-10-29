---
title: BITXOR (Lakehouse v2)
description: BITXOR：返回两个数值的按位异或结果。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitxor.md
---

返回两个数值的按位异或结果。

## Analyze 语法

```python
func.bitxor(<x>, <y>)
```

## Analyze 示例

```python
func.bitxor(12, 10)

┌───┐
│ 6  │
└───┘
```

## SQL 语法

```sql
BITXOR(<x>, <y>)
```

## SQL 示例

```sql
SELECT BITXOR(12, 10);

┌───┐
│ 6  │
└───┘
```
