---
title: BITMAP_UNION (Lakehouse v1)
description: BITMAP_UNION conta o número de bits definidos como 1 no bitmap, executando uma operação lógica UNION.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-union.md
---

Conta o número de bits definidos como 1 no bitmap, executando uma operação lógica UNION.

## Sintaxe do Analyze

```python
func.bitmap_union( <bitmap> )
```

## Exemplos do Analyze

```python
func.bitmap_union(func.to_bitmap('1, 3, 5'))

┌──────────────────────────────────────────────┐
│ func.bitmap_union(func.to_bitmap('1, 3, 5')) │
├──────────────────────────────────────────────┤
│ 1,3,5                                        │
└──────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
BITMAP_UNION( <bitmap> )
```

## Exemplos de SQL

```sql
SELECT BITMAP_UNION(TO_BITMAP('1, 3, 5'))::String;

┌────────────────────────────────────────────┐
│ bitmap_union(to_bitmap('1, 3, 5'))::string │
├────────────────────────────────────────────┤
│ 1,3,5                                      │
└────────────────────────────────────────────┘
```
