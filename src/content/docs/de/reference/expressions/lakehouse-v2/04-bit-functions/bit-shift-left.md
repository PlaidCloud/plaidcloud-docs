---
title: BIT_SHIFT_LEFT (Lakehouse v2)
description: BIT_SHIFT_LEFT – verschiebt die Bits eines numerischen Werts um die angegebene Anzahl von Positionen nach links.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bit-shift-left.md
---

Verschiebt die Bits eines numerischen Werts um die angegebene Anzahl von Positionen nach links.

## Analyze-Syntax

```python
func.bit_shift_left(<value>, <shift>)
```

## Analyze-Beispiele

```python
func.bit_shift_left(1, 4)

┌────┐
│ 16  │
└────┘
```

## SQL-Syntax

```sql
BIT_SHIFT_LEFT(<value>, <shift>)
```

## SQL-Beispiele

```sql
SELECT BIT_SHIFT_LEFT(1, 4);

┌────┐
│ 16  │
└────┘
```
