---
title: BIT_SHIFT_RIGHT_LOGICAL (Lakehouse v2)
description: "在 PlaidCloud Lakehouse 中使用 BIT_SHIFT_RIGHT_LOGICAL 位函数。将数值的二进制位向右移动指定的位数。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bit-shift-right-logical.md
---

将数值的二进制位向右移动指定的位数（逻辑移位）。

## Analyze 语法

```python
func.bit_shift_right_logical(<value>, <shift>)
```

## Analyze 示例

```python
func.bit_shift_right_logical(16, 2)

┌───┐
│ 4  │
└───┘
```

## SQL 语法

```sql
BIT_SHIFT_RIGHT_LOGICAL(<value>, <shift>)
```

## SQL 示例

```sql
SELECT BIT_SHIFT_RIGHT_LOGICAL(16, 2);

┌───┐
│ 4  │
└───┘
```
