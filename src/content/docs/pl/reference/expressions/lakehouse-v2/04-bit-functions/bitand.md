---
title: BITAND (Lakehouse v2)
description: BITAND — zwraca wynik bitowej operacji AND na dwóch wartościach liczbowych.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitand.md
---

Zwraca wynik bitowej operacji AND na dwóch wartościach liczbowych.

## Składnia Analyze

```python
func.bitand(<x>, <y>)
```

## Przykłady Analyze

```python
func.bitand(12, 10)

┌───┐
│ 8  │
└───┘
```

## Składnia SQL

```sql
BITAND(<x>, <y>)
```

## Przykłady SQL

```sql
SELECT BITAND(12, 10);

┌───┐
│ 8  │
└───┘
```
