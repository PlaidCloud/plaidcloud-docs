---
title: BITMAP_INTERSECT (Lakehouse v1)
description: BITMAP_INTERSECT — conta o número de bits com valor 1 no bitmap através de uma operação lógica INTERSECT.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-intersect.md
---

Conta o número de bits com valor 1 no bitmap através de uma operação lógica INTERSECT.

## Sintaxe do Analyze

```python
func.bitmap_intersect( <bitmap> )
```

## Exemplos do Analyze

```python
func.bitmap_intersect(func.to_bitmap('1, 3, 5'))

┌──────────────────────────────────────────────────┐
│ func.bitmap_intersect(func.to_bitmap('1, 3, 5')) │
├──────────────────────────────────────────────────┤
│ 1,3,5                                            │
└──────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
BITMAP_INTERSECT( <bitmap> )
```

## Exemplos SQL

```sql
SELECT BITMAP_INTERSECT(TO_BITMAP('1, 3, 5'))::String;

┌────────────────────────────────────────────────┐
│ bitmap_intersect(to_bitmap('1, 3, 5'))::string │
├────────────────────────────────────────────────┤
│ 1,3,5                                          │
└────────────────────────────────────────────────┘
```
