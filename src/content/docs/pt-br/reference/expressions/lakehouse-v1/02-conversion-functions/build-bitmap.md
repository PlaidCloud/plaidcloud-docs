---
title: BUILD_BITMAP (Lakehouse v1)
description: BUILD_BITMAP converte um array de inteiros positivos em um valor BITMAP.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/build-bitmap.md
---

Converte um array de inteiros positivos em um valor BITMAP.


## Sintaxe do Analyze

```python
func.build_bitmap( <expr> )
```

## Exemplos do Analyze

```python
func.to_string(func.build_bitmap([1, 4, 5]))

┌───────────────────────────────────────────────┐
│ func.to_string(func.build_bitmap([1, 4, 5]))  │
├───────────────────────────────────────────────┤
│ 1,4,5                                         │
└───────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
BUILD_BITMAP( <expr> )
```

## Exemplos de SQL

```sql
SELECT BUILD_BITMAP([1,4,5])::String;

┌─────────────────────────────────┐
│ build_bitmap([1, 4, 5])::string │
├─────────────────────────────────┤
│ 1,4,5                           │
└─────────────────────────────────┘
```
