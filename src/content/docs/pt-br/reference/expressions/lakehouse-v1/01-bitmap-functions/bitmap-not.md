---
title: BITMAP_NOT (Lakehouse v1)
description: BITMAP_NOT gera um novo bitmap com os elementos do primeiro bitmap que não estão no segundo.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-not.md
---

Gera um novo bitmap com os elementos do primeiro bitmap que não estão no segundo.

## Sintaxe do Analyze

```python
func.bitmap_not( <bitmap1>, <bitmap2> )
```

## Exemplos do Analyze

```python
func.bitmap_not(func.build_bitmap([1, 4, 5]), func.cast(func.build_bitmap([5, 6, 7])), Text)

┌───────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.bitmap_not(func.build_bitmap([1, 4, 5]), func.cast(func.build_bitmap([5, 6, 7])), Text)  │
├───────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1,4                                                                                           │
└───────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
BITMAP_NOT( <bitmap1>, <bitmap2> )
```

## Aliases

- [BITMAP_AND_NOT](../bitmap-and-not)

## Exemplos de SQL

```sql
SELECT BITMAP_NOT(BUILD_BITMAP([1,4,5]), BUILD_BITMAP([5,6,7]))::String;

┌──────────────────────────────────────────────────────────────────────┐
│ bitmap_not(build_bitmap([1, 4, 5]), build_bitmap([5, 6, 7]))::string │
├──────────────────────────────────────────────────────────────────────┤
│ 1,4                                                                  │
└──────────────────────────────────────────────────────────────────────┘

SELECT BITMAP_AND_NOT(BUILD_BITMAP([1,4,5]), BUILD_BITMAP([5,6,7]))::String;

┌──────────────────────────────────────────────────────────────────────────┐
│ bitmap_and_not(build_bitmap([1, 4, 5]), build_bitmap([5, 6, 7]))::string │
├──────────────────────────────────────────────────────────────────────────┤
│ 1,4                                                                      │
└──────────────────────────────────────────────────────────────────────────┘
```
