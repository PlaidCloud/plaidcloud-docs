---
title: BIT_SHIFT_RIGHT_LOGICAL (Lakehouse v2)
description: "Verwenden Sie die Bitfunktion BIT_SHIFT_RIGHT_LOGICAL in PlaidCloud Lakehouse. Verschiebt die Bits eines numerischen Werts um die angegebene Anzahl von Positionen nach rechts."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bit-shift-right-logical.md
---

Verschiebt die Bits eines numerischen Werts um die angegebene Anzahl von Positionen nach rechts (logisch).

## Analyze-Syntax

```python
func.bit_shift_right_logical(<value>, <shift>)
```

## Analyze-Beispiele

```python
func.bit_shift_right_logical(16, 2)

┌───┐
│ 4  │
└───┘
```

## SQL-Syntax

```sql
BIT_SHIFT_RIGHT_LOGICAL(<value>, <shift>)
```

## SQL-Beispiele

```sql
SELECT BIT_SHIFT_RIGHT_LOGICAL(16, 2);

┌───┐
│ 4  │
└───┘
```
