---
title: ARRAY_FLATTEN (Lakehouse v1)
description: ARRAY_FLATTEN — spłaszcza zagnieżdżone tablice, przekształcając je w tablicę jednopoziomową.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-flatten.md
---

Spłaszcza zagnieżdżone tablice, przekształcając je w tablicę jednopoziomową.

## Składnia Analyze

```python
func.array_flatten( <array> )
```

## Przykłady Analyze

```python
func.array_flatten([[1, 2], [3, 4, 5]]) 

┌──────────────────────────────────────────┐
│ func.array_flatten([[1, 2], [3, 4, 5]])  │
├──────────────────────────────────────────┤
│ [1,2,3,4,5]                              │
└──────────────────────────────────────────┘
```

## Składnia SQL

```sql
ARRAY_FLATTEN( <array> )
```

## Przykłady SQL

```sql
SELECT ARRAY_FLATTEN([[1,2], [3,4,5]]);

┌────────────────────────────────────┐
│ array_flatten([[1, 2], [3, 4, 5]]) │
├────────────────────────────────────┤
│ [1,2,3,4,5]                        │
└────────────────────────────────────┘
```
