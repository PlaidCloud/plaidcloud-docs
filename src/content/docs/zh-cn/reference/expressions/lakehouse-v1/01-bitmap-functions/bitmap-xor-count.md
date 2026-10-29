---
title: BITMAP_XOR_COUNT (Lakehouse v1)
description: BITMAP_XOR_COUNT：通过执行逻辑 XOR 运算，统计位图中值为 1 的位数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-xor-count.md
---

通过执行逻辑 XOR（异或）运算，统计位图中值为 1 的位数。

## Analyze 语法

```python
func.bitmap_xor_count( <bitmap> )
```

## Analyze 示例

```python
func.bitmap_xor_count(func.to_bitmap('1, 3, 5'))

┌──────────────────────────────────────────────────┐
│ func.bitmap_xor_count(func.to_bitmap('1, 3, 5')) │
├──────────────────────────────────────────────────┤
│                                                3 │
└──────────────────────────────────────────────────┘
```

## SQL 语法

```sql
BITMAP_XOR_COUNT( <bitmap> )
```

## SQL 示例

```sql
SELECT BITMAP_XOR_COUNT(TO_BITMAP('1, 3, 5'));

┌────────────────────────────────────────┐
│ bitmap_xor_count(to_bitmap('1, 3, 5')) │
├────────────────────────────────────────┤
│                                      3 │
└────────────────────────────────────────┘
```
