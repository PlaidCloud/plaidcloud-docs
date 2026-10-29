---
title: BITMAP_SUBSET_LIMIT (Lakehouse v1)
description: BITMAP_SUBSET_LIMIT — gera um sub-bitmap do bitmap de origem, começando num intervalo a partir do valor inicial, com um limite de tamanho.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-subset-limit.md
---

Gera um sub-bitmap do bitmap de origem, começando num intervalo a partir do valor inicial, com um limite de tamanho.

## Sintaxe do Analyze

```python
func.bitmap_subset_limit( <bitmap>, <start>, <limit> )
```

## Exemplos do Analyze

```python
func.bitmap_subset_limit(func.build_bitmap([1, 4, 5]), 2, 2)

┌──────────────────────────────────────────────────────────────┐
│ func.bitmap_subset_limit(func.build_bitmap([1, 4, 5]), 2, 2) │
├──────────────────────────────────────────────────────────────┤
│ 4,5                                                          │
└──────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
BITMAP_SUBSET_LIMIT( <bitmap>, <start>, <limit> )
```

## Exemplos SQL

```sql
SELECT BITMAP_SUBSET_LIMIT(BUILD_BITMAP([1,4,5]), 2, 2)::String;

┌────────────────────────────────────────────────────────────┐
│ bitmap_subset_limit(build_bitmap([1, 4, 5]), 2, 2)::string │
├────────────────────────────────────────────────────────────┤
│ 4,5                                                        │
└────────────────────────────────────────────────────────────┘
```
