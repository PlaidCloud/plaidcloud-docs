---
title: BIT_SHIFT_LEFT (Lakehouse v2)
description: BIT_SHIFT_LEFT — przesuwa bity wartości liczbowej w lewo o podaną liczbę pozycji.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bit-shift-left.md
---

Przesuwa bity wartości liczbowej w lewo o podaną liczbę pozycji.

## Składnia Analyze

```python
func.bit_shift_left(<value>, <shift>)
```

## Przykłady Analyze

```python
func.bit_shift_left(1, 4)

┌────┐
│ 16  │
└────┘
```

## Składnia SQL

```sql
BIT_SHIFT_LEFT(<value>, <shift>)
```

## Przykłady SQL

```sql
SELECT BIT_SHIFT_LEFT(1, 4);

┌────┐
│ 16  │
└────┘
```
