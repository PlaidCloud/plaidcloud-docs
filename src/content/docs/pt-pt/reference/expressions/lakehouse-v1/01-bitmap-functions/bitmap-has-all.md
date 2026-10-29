---
title: BITMAP_HAS_ALL (Lakehouse v1)
description: BITMAP_HAS_ALL — verifica se o primeiro bitmap contém todos os bits do segundo bitmap.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-has-all.md
---

Verifica se o primeiro bitmap contém todos os bits do segundo bitmap.

## Sintaxe do Analyze

```python
func.bitmap_has_all( <bitmap1>, <bitmap2> )
```

## Exemplos do Analyze

```python
func.bitmap_has_all(build_bitmap([1, 4, 5]), build_bitmap([1, 2])) 

┌─────────────────────────────────────────────────────────────────────┐
│ func.bitmap_has_all(build_bitmap([1, 4, 5]), build_bitmap([1, 2]))  │
├─────────────────────────────────────────────────────────────────────┤
│ false                                                               │
└─────────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
BITMAP_HAS_ALL( <bitmap1>, <bitmap2> )
```

## Exemplos SQL

```sql
SELECT BITMAP_HAS_ALL(BUILD_BITMAP([1,4,5]), BUILD_BITMAP([1,2]));

┌───────────────────────────────────────────────────────────────┐
│ bitmap_has_all(build_bitmap([1, 4, 5]), build_bitmap([1, 2])) │
├───────────────────────────────────────────────────────────────┤
│ false                                                         │
└───────────────────────────────────────────────────────────────┘
```
