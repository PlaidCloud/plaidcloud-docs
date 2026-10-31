---
title: BIT_SHIFT_RIGHT (Lakehouse v2)
description: "Verwenden Sie die Bitfunktion BIT_SHIFT_RIGHT in PlaidCloud Lakehouse. Verschiebt die Bits eines numerischen Werts um die angegebene Anzahl von Positionen nach rechts (arithmetisch)."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bit-shift-right.md
---

Verschiebt die Bits eines numerischen Werts um die angegebene Anzahl von Positionen nach rechts (arithmetisch).

## Analyze-Syntax

```python
func.bit_shift_right(<value>, <shift>)
```

## Analyze-Beispiele

```python
func.bit_shift_right(16, 2)

┌───┐
│ 4  │
└───┘
```

## SQL-Syntax

```sql
BIT_SHIFT_RIGHT(<value>, <shift>)
```

## SQL-Beispiele

```sql
SELECT BIT_SHIFT_RIGHT(16, 2);

┌───┐
│ 4  │
└───┘
```
