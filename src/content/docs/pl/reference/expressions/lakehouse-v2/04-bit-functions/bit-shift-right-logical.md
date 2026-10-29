---
title: BIT_SHIFT_RIGHT_LOGICAL (Lakehouse v2)
description: "Użyj funkcji bitowej BIT_SHIFT_RIGHT_LOGICAL w PlaidCloud Lakehouse. Przesuwa bity wartości liczbowej w prawo o podaną liczbę pozycji."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bit-shift-right-logical.md
---

Przesuwa bity wartości liczbowej w prawo o podaną liczbę pozycji (przesunięcie logiczne).

## Składnia Analyze

```python
func.bit_shift_right_logical(<value>, <shift>)
```

## Przykłady Analyze

```python
func.bit_shift_right_logical(16, 2)

┌───┐
│ 4  │
└───┘
```

## Składnia SQL

```sql
BIT_SHIFT_RIGHT_LOGICAL(<value>, <shift>)
```

## Przykłady SQL

```sql
SELECT BIT_SHIFT_RIGHT_LOGICAL(16, 2);

┌───┐
│ 4  │
└───┘
```
