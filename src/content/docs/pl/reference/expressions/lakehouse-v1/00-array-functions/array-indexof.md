---
title: ARRAY_INDEXOF (Lakehouse v1)
description: ARRAY_INDEXOF — zwraca indeks (liczony od 1) elementu, jeśli tablica go zawiera.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-indexof.md
---

Zwraca indeks (liczony od 1) elementu, jeśli tablica go zawiera.

## Składnia Analyze

```python
func.array_indexof( <array>, <element> )
```

## Przykłady Analyze

```python
func.array_indexof([1, 2, 9], 9)

┌───────────────────────────────────┐
│ func.array_indexof([1, 2, 9], 9)  │
├───────────────────────────────────┤
│                                 3 │
└───────────────────────────────────┘
```

## Składnia SQL

```sql
ARRAY_INDEXOF( <array>, <element> )
```

## Przykłady SQL

```sql
SELECT ARRAY_INDEXOF([1, 2, 9], 9);

┌─────────────────────────────┐
│ array_indexof([1, 2, 9], 9) │
├─────────────────────────────┤
│                           3 │
└─────────────────────────────┘
```
