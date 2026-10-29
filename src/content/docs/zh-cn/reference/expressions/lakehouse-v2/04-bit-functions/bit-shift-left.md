---
title: BIT_SHIFT_LEFT (Lakehouse v2)
description: BIT_SHIFT_LEFT：将数值的二进制位向左移动指定的位数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bit-shift-left.md
---

将数值的二进制位向左移动指定的位数。

## Analyze 语法

```python
func.bit_shift_left(<value>, <shift>)
```

## Analyze 示例

```python
func.bit_shift_left(1, 4)

┌────┐
│ 16  │
└────┘
```

## SQL 语法

```sql
BIT_SHIFT_LEFT(<value>, <shift>)
```

## SQL 示例

```sql
SELECT BIT_SHIFT_LEFT(1, 4);

┌────┐
│ 16  │
└────┘
```
