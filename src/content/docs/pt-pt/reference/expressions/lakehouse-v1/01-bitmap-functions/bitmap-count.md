---
title: BITMAP_COUNT (Lakehouse v1)
description: BITMAP_COUNT — conta o número de bits com valor 1 no bitmap.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-count.md
---

Conta o número de bits com valor 1 no bitmap.

## Sintaxe do Analyze

```python
func.bitmap_count( <bitmap> )
```

## Exemplos do Analyze

```python
func.bitmap_count(build_bitmap([1, 4, 5]))

┌────────────────────────────────────────────┐
│ func.bitmap_count(build_bitmap([1, 4, 5])) │
├────────────────────────────────────────────┤
│                                          3 │
└────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
BITMAP_COUNT( <bitmap> )
```

## Alias

- [BITMAP_CARDINALITY](../bitmap-cardinality)

## Exemplos SQL

```sql
SELECT BITMAP_COUNT(BUILD_BITMAP([1,4,5])), BITMAP_CARDINALITY(BUILD_BITMAP([1,4,5]));

┌─────────────────────────────────────────────────────────────────────────────────────┐
│ bitmap_count(build_bitmap([1, 4, 5])) │ bitmap_cardinality(build_bitmap([1, 4, 5])) │
├───────────────────────────────────────┼─────────────────────────────────────────────┤
│                                     3 │                                           3 │
└─────────────────────────────────────────────────────────────────────────────────────┘
```
