---
title: BUILD_BITMAP (Lakehouse v1)
description: "BUILD_BITMAP : convertit un tableau d'entiers positifs en une valeur BITMAP."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/build-bitmap.md
---

Convertit un tableau d'entiers positifs en une valeur BITMAP.


## Syntaxe Analyze

```python
func.build_bitmap( <expr> )
```

## Exemples Analyze

```python
func.to_string(func.build_bitmap([1, 4, 5]))

┌───────────────────────────────────────────────┐
│ func.to_string(func.build_bitmap([1, 4, 5]))  │
├───────────────────────────────────────────────┤
│ 1,4,5                                         │
└───────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
BUILD_BITMAP( <expr> )
```

## Exemples SQL

```sql
SELECT BUILD_BITMAP([1,4,5])::String;

┌─────────────────────────────────┐
│ build_bitmap([1, 4, 5])::string │
├─────────────────────────────────┤
│ 1,4,5                           │
└─────────────────────────────────┘
```
