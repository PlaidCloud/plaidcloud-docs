---
title: ARRAY_SORT (Lakehouse v1)
description: ARRAY_SORT – sortiert die Elemente des Arrays in aufsteigender Reihenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-sort.md
---

Sortiert die Elemente des Arrays in aufsteigender Reihenfolge.

## Analyze-Syntax

```sql
func.array_sort( <array>[, <order>, <nullposition>] )
```

| Parameter    | Standard    | Beschreibung                                                                                                                                   |
|--------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| order        | ASC         | Legt die Sortierreihenfolge fest: aufsteigend (ASC) oder absteigend (DESC).                                                                    |
| nullposition | NULLS FIRST | Bestimmt die Position der NULL-Werte im Sortierergebnis: am Anfang (NULLS FIRST) oder am Ende (NULLS LAST) der Sortierausgabe.                 |

## Analyze-Beispiele

```sql
func.array_sort([1, 4, 3, 2])

┌────────────────────────────────┐
│ func.array_sort([1, 4, 3, 2])  │
├────────────────────────────────┤
│ [1,2,3,4]                      │
└────────────────────────────────┘
```

## SQL-Syntax

```sql
ARRAY_SORT( <array>[, <order>, <nullposition>] )
```

| Parameter    | Standard    | Beschreibung                                                                                                                                   |
|--------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| order        | ASC         | Legt die Sortierreihenfolge fest: aufsteigend (ASC) oder absteigend (DESC).                                                                    |
| nullposition | NULLS FIRST | Bestimmt die Position der NULL-Werte im Sortierergebnis: am Anfang (NULLS FIRST) oder am Ende (NULLS LAST) der Sortierausgabe.                 |

## SQL-Beispiele

```sql
SELECT ARRAY_SORT([1, 4, 3, 2]);

┌──────────────────────────┐
│ array_sort([1, 4, 3, 2]) │
├──────────────────────────┤
│ [1,2,3,4]                │
└──────────────────────────┘
```
