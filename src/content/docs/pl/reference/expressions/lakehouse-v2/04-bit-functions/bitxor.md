---
title: BITXOR (Lakehouse v2)
description: BITXOR — zwraca wynik bitowej operacji XOR na dwóch wartościach liczbowych.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitxor.md
---

Zwraca wynik bitowej operacji XOR na dwóch wartościach liczbowych.

## Składnia Analyze

```python
func.bitxor(<x>, <y>)
```

## Przykłady Analyze

```python
func.bitxor(12, 10)

┌───┐
│ 6  │
└───┘
```

## Składnia SQL

```sql
BITXOR(<x>, <y>)
```

## Przykłady SQL

```sql
SELECT BITXOR(12, 10);

┌───┐
│ 6  │
└───┘
```
