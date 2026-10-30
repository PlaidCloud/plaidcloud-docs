---
title: ARRAY_SORT (Lakehouse v1)
description: ARRAY_SORT — sortuje elementy tablicy w kolejności rosnącej.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-sort.md
---

Sortuje elementy tablicy w kolejności rosnącej.

## Składnia Analyze

```sql
func.array_sort( <array>[, <order>, <nullposition>] )
```

| Parametr | Domyślnie | Opis |
|--------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| order | ASC | Określa kolejność sortowania: rosnącą (ASC) lub malejącą (DESC). |
| nullposition | NULLS FIRST | Określa położenie wartości NULL w wyniku sortowania: na początku (NULLS FIRST) lub na końcu (NULLS LAST). |

## Przykłady Analyze

```sql
func.array_sort([1, 4, 3, 2])

┌────────────────────────────────┐
│ func.array_sort([1, 4, 3, 2])  │
├────────────────────────────────┤
│ [1,2,3,4]                      │
└────────────────────────────────┘
```

## Składnia SQL

```sql
ARRAY_SORT( <array>[, <order>, <nullposition>] )
```

| Parametr | Domyślnie | Opis |
|--------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| order | ASC | Określa kolejność sortowania: rosnącą (ASC) lub malejącą (DESC). |
| nullposition | NULLS FIRST | Określa położenie wartości NULL w wyniku sortowania: na początku (NULLS FIRST) lub na końcu (NULLS LAST). |

## Przykłady SQL

```sql
SELECT ARRAY_SORT([1, 4, 3, 2]);

┌──────────────────────────┐
│ array_sort([1, 4, 3, 2]) │
├──────────────────────────┤
│ [1,2,3,4]                │
└──────────────────────────┘
```
