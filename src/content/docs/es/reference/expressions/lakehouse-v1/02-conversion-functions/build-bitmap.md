---
title: BUILD_BITMAP (Lakehouse v1)
description: BUILD_BITMAP — convierte un arreglo de enteros positivos en un valor BITMAP.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/build-bitmap.md
---

Convierte un arreglo de enteros positivos en un valor BITMAP.


## Sintaxis de Analyze

```python
func.build_bitmap( <expr> )
```

## Ejemplos de Analyze

```python
func.to_string(func.build_bitmap([1, 4, 5]))

┌───────────────────────────────────────────────┐
│ func.to_string(func.build_bitmap([1, 4, 5]))  │
├───────────────────────────────────────────────┤
│ 1,4,5                                         │
└───────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
BUILD_BITMAP( <expr> )
```

## Ejemplos de SQL

```sql
SELECT BUILD_BITMAP([1,4,5])::String;

┌─────────────────────────────────┐
│ build_bitmap([1, 4, 5])::string │
├─────────────────────────────────┤
│ 1,4,5                           │
└─────────────────────────────────┘
```
