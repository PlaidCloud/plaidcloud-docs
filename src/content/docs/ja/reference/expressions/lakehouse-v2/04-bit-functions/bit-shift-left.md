---
title: BIT_SHIFT_LEFT (Lakehouse v2)
description: BIT_SHIFT_LEFT — 数値のビットを指定した桁数だけ左にシフトします。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bit-shift-left.md
---

数値のビットを指定した桁数だけ左にシフトします。

## Analyzeの構文

```python
func.bit_shift_left(<value>, <shift>)
```

## Analyzeの例

```python
func.bit_shift_left(1, 4)

┌────┐
│ 16  │
└────┘
```

## SQLの構文

```sql
BIT_SHIFT_LEFT(<value>, <shift>)
```

## SQLの例

```sql
SELECT BIT_SHIFT_LEFT(1, 4);

┌────┐
│ 16  │
└────┘
```
