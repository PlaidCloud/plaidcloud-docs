---
title: BUILD_BITMAP (Lakehouse v1)
description: BUILD_BITMAP — konwertuje tablicę dodatnich liczb całkowitych na wartość BITMAP.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/build-bitmap.md
---

Konwertuje tablicę dodatnich liczb całkowitych na wartość BITMAP.


## Składnia Analyze

```python
func.build_bitmap( <expr> )
```

## Przykłady Analyze

```python
func.to_string(func.build_bitmap([1, 4, 5]))

┌───────────────────────────────────────────────┐
│ func.to_string(func.build_bitmap([1, 4, 5]))  │
├───────────────────────────────────────────────┤
│ 1,4,5                                         │
└───────────────────────────────────────────────┘
```

## Składnia SQL

```sql
BUILD_BITMAP( <expr> )
```

## Przykłady SQL

```sql
SELECT BUILD_BITMAP([1,4,5])::String;

┌─────────────────────────────────┐
│ build_bitmap([1, 4, 5])::string │
├─────────────────────────────────┤
│ 1,4,5                           │
└─────────────────────────────────┘
```
