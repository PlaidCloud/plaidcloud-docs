---
title: BIT_SHIFT_RIGHT (Lakehouse v2)
description: "PlaidCloud Lakehouse で BIT_SHIFT_RIGHT ビット関数を使用します。数値のビットを指定した桁数だけ右にシフトします（算術シフト）。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bit-shift-right.md
---

数値のビットを指定した桁数だけ右にシフトします（算術シフト）。

## Analyzeの構文

```python
func.bit_shift_right(<value>, <shift>)
```

## Analyzeの例

```python
func.bit_shift_right(16, 2)

┌───┐
│ 4  │
└───┘
```

## SQLの構文

```sql
BIT_SHIFT_RIGHT(<value>, <shift>)
```

## SQLの例

```sql
SELECT BIT_SHIFT_RIGHT(16, 2);

┌───┐
│ 4  │
└───┘
```
