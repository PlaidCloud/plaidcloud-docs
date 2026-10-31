---
title: BITMAP_XOR_COUNT (Lakehouse v1)
description: BITMAP_XOR_COUNT conta o número de bits definidos como 1 no bitmap, executando uma operação lógica XOR.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-xor-count.md
---

Conta o número de bits definidos como 1 no bitmap, executando uma operação lógica XOR (OR exclusivo).

## Sintaxe do Analyze

```python
func.bitmap_xor_count( <bitmap> )
```

## Exemplos do Analyze

```python
func.bitmap_xor_count(func.to_bitmap('1, 3, 5'))

┌──────────────────────────────────────────────────┐
│ func.bitmap_xor_count(func.to_bitmap('1, 3, 5')) │
├──────────────────────────────────────────────────┤
│                                                3 │
└──────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
BITMAP_XOR_COUNT( <bitmap> )
```

## Exemplos de SQL

```sql
SELECT BITMAP_XOR_COUNT(TO_BITMAP('1, 3, 5'));

┌────────────────────────────────────────┐
│ bitmap_xor_count(to_bitmap('1, 3, 5')) │
├────────────────────────────────────────┤
│                                      3 │
└────────────────────────────────────────┘
```
