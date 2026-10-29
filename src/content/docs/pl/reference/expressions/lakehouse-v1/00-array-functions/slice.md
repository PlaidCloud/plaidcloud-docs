---
title: SLICE (Lakehouse v1)
description: SLICE — wyodrębnia fragment tablicy według indeksu (liczonego od 1).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/slice.md
---

Wyodrębnia fragment tablicy według indeksu (liczonego od 1).

## Składnia Analyze

```python
func.slice( <array>, <start>[, <end>] )
```

## Przykłady Analyze

```python
func.slice([1, 21, 32, 4], 2, 3)

┌──────────────────────────────────┐
│ func.slice([1, 21, 32, 4], 2, 3) │
├──────────────────────────────────┤
│ [21,32]                          │ 
└──────────────────────────────────┘
```

## Składnia SQL

```sql
SLICE( <array>, <start>[, <end>] )
```

## Aliasy

- [ARRAY_SLICE](../array-slice)

## Przykłady SQL

```sql
SELECT ARRAY_SLICE([1, 21, 32, 4], 2, 3), SLICE([1, 21, 32, 4], 2, 3);

┌─────────────────────────────────────────────────────────────────┐
│ array_slice([1, 21, 32, 4], 2, 3) │ slice([1, 21, 32, 4], 2, 3) │
├───────────────────────────────────┼─────────────────────────────┤
│ [21,32]                           │ [21,32]                     │
└─────────────────────────────────────────────────────────────────┘
```
