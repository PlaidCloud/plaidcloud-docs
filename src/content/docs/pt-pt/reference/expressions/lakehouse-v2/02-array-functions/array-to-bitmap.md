---
title: ARRAY_TO_BITMAP (Lakehouse v2)
description: ARRAY_TO_BITMAP — converte uma matriz de inteiros num bitmap.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-to-bitmap.md
---

Converte uma matriz de inteiros num bitmap.

## Sintaxe do Analyze

```python
func.array_to_bitmap([1, 2, 3])
```

## Exemplos do Analyze

```python
func.array_to_bitmap([1, 2, 3])

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxe SQL

```sql
ARRAY_TO_BITMAP([1, 2, 3])
```

## Exemplos SQL

```sql
SELECT BITMAP_TO_STRING(ARRAY_TO_BITMAP([1, 2, 3]));

┌───────┐
│ 1,2,3 │
└───────┘
```
