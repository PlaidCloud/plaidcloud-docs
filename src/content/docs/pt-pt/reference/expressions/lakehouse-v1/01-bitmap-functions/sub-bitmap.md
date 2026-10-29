---
title: SUB_BITMAP (Lakehouse v1)
description: SUB_BITMAP — gera um sub-bitmap do bitmap de origem, a partir do índice inicial, com um tamanho especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/sub-bitmap.md
---

Gera um sub-bitmap do bitmap de origem, a partir do índice inicial, com um tamanho especificado.

## Sintaxe do Analyze

```python
func.sub_bitmap( <bitmap>, <start>, <size> )
```

## Exemplos do Analyze

```python
func.sub_bitmap(func.build_bitmap([1, 2, 3, 4, 5]), 1, 3)

┌───────────────────────────────────────────────────────────┐
│ func.sub_bitmap(func.build_bitmap([1, 2, 3, 4, 5]), 1, 3) │
├───────────────────────────────────────────────────────────┤
│ 2,3,4                                                     │
└───────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
SUB_BITMAP( <bitmap>, <start>, <size> )
```

## Exemplos SQL

```sql
SELECT SUB_BITMAP(BUILD_BITMAP([1, 2, 3, 4, 5]), 1, 3)::String;

┌─────────────────────────────────────────────────────────┐
│ sub_bitmap(build_bitmap([1, 2, 3, 4, 5]), 1, 3)::string │
├─────────────────────────────────────────────────────────┤
│ 2,3,4                                                   │
└─────────────────────────────────────────────────────────┘
```
