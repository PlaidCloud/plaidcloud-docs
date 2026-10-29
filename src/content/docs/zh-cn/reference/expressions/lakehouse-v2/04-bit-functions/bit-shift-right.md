---
title: BIT_SHIFT_RIGHT (Lakehouse v2)
description: "在 PlaidCloud Lakehouse 中使用 BIT_SHIFT_RIGHT 位函数。将数值的二进制位向右移动指定的位数（算术移位）。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bit-shift-right.md
---

将数值的二进制位向右移动指定的位数（算术移位）。

## Analyze 语法

```python
func.bit_shift_right(<value>, <shift>)
```

## Analyze 示例

```python
func.bit_shift_right(16, 2)

┌───┐
│ 4  │
└───┘
```

## SQL 语法

```sql
BIT_SHIFT_RIGHT(<value>, <shift>)
```

## SQL 示例

```sql
SELECT BIT_SHIFT_RIGHT(16, 2);

┌───┐
│ 4  │
└───┘
```
