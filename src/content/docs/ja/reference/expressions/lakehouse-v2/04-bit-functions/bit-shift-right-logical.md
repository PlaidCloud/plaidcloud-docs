---
title: BIT_SHIFT_RIGHT_LOGICAL (Lakehouse v2)
description: "PlaidCloud Lakehouse で BIT_SHIFT_RIGHT_LOGICAL ビット関数を使用します。数値のビットを指定した桁数だけ右にシフトします。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bit-shift-right-logical.md
---

数値のビットを指定した桁数だけ右にシフトします（論理シフト）。

## Analyzeの構文

```python
func.bit_shift_right_logical(<value>, <shift>)
```

## Analyzeの例

```python
func.bit_shift_right_logical(16, 2)

┌───┐
│ 4  │
└───┘
```

## SQLの構文

```sql
BIT_SHIFT_RIGHT_LOGICAL(<value>, <shift>)
```

## SQLの例

```sql
SELECT BIT_SHIFT_RIGHT_LOGICAL(16, 2);

┌───┐
│ 4  │
└───┘
```
