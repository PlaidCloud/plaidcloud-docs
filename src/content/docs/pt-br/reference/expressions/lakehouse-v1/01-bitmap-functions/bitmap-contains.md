---
title: BITMAP_CONTAINS (Lakehouse v1)
description: BITMAP_CONTAINS verifica se o bitmap contém um valor específico.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-contains.md
---

Verifica se o bitmap contém um valor específico.


## Sintaxe do Analyze

```python
func.bitmap_contains( <bitmap>, <value> )
```

## Exemplos do Analyze

```python
func.bitmap_contains(build_bitmap([1, 4, 5]), 1)

┌───────────────────────────────────────────────────┐
│ func.bitmap_contains(build_bitmap([1, 4, 5]), 1)  │
├───────────────────────────────────────────────────┤
│ true                                              │
└───────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
BITMAP_CONTAINS( <bitmap>, <value> )
```

## Exemplos de SQL

```sql
SELECT BITMAP_CONTAINS(BUILD_BITMAP([1,4,5]), 1);

┌─────────────────────────────────────────────┐
│ bitmap_contains(build_bitmap([1, 4, 5]), 1) │
├─────────────────────────────────────────────┤
│ true                                        │
└─────────────────────────────────────────────┘
```
