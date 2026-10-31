---
title: ARRAYS_ZIP (Lakehouse v1)
description: ARRAYS_ZIP — scala wiele tablic w jedną tablicę krotek.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/arrays-zip.md
---

Scala wiele tablic w jedną tablicę krotek.

## Składnia Analyze

```python
func.arrays_zip( <array1> [, ...] )
```

## Przykłady Analyze

```python
func.arrays_zip([1, 2, 3], ['a', 'b', 'c'])

┌──────────────────────────────────────────────┐
│ func.arrays_zip([1, 2, 3], ['a', 'b', 'c'])  │
├──────────────────────────────────────────────┤
│  [(1,'a'),(2,'b'),(3,'c')]                   │
└──────────────────────────────────────────────┘
```

## Składnia SQL

```sql
ARRAYS_ZIP( <array1> [, ...] )
```

## Argumenty

| Argumenty  | Opis              |
|------------|-------------------|
| `<arrayN>` | Wejściowe tablice (ARRAY). |

:::note
- Wszystkie tablice muszą mieć taką samą długość.
:::

## Zwracany typ

Array(Tuple).

## Przykłady SQL

```sql
SELECT ARRAYS_ZIP([1, 2, 3], ['a', 'b', 'c']);
┌────────────────────────────────────────┐
│ arrays_zip([1, 2, 3], ['a', 'b', 'c']) │
├────────────────────────────────────────┤
│ [(1,'a'),(2,'b'),(3,'c')]              │
└────────────────────────────────────────┘
```
