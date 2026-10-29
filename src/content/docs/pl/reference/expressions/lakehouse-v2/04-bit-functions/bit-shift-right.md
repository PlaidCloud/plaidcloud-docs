---
title: BIT_SHIFT_RIGHT (Lakehouse v2)
description: "Użyj funkcji bitowej BIT_SHIFT_RIGHT w PlaidCloud Lakehouse. Przesuwa bity wartości liczbowej w prawo o podaną liczbę pozycji (przesunięcie arytmetyczne)."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bit-shift-right.md
---

Przesuwa bity wartości liczbowej w prawo o podaną liczbę pozycji (przesunięcie arytmetyczne).

## Składnia Analyze

```python
func.bit_shift_right(<value>, <shift>)
```

## Przykłady Analyze

```python
func.bit_shift_right(16, 2)

┌───┐
│ 4  │
└───┘
```

## Składnia SQL

```sql
BIT_SHIFT_RIGHT(<value>, <shift>)
```

## Przykłady SQL

```sql
SELECT BIT_SHIFT_RIGHT(16, 2);

┌───┐
│ 4  │
└───┘
```
