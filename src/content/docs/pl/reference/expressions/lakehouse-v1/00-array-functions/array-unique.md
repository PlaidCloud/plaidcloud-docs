---
title: ARRAY_UNIQUE (Lakehouse v1)
description: ARRAY_UNIQUE — zlicza unikatowe elementy tablicy (z wyjątkiem NULL).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-unique.md
---

Zlicza unikatowe elementy tablicy (z wyjątkiem NULL).

## Składnia Analyze

```python
func.array_unique( <array> )
```

## Przykłady Analyze

```python
func.array_unique([1, 2, 3, 3, 4])

┌─────────────────────────────────────┐
│ func.array_unique([1, 2, 3, 3, 4])  │
├─────────────────────────────────────┤
│                                   4 │
└─────────────────────────────────────┘
```

## Składnia SQL

```sql
ARRAY_UNIQUE( <array> )
```

## Przykłady SQL

```sql
SELECT ARRAY_UNIQUE([1, 2, 3, 3, 4]);

┌───────────────────────────────┐
│ array_unique([1, 2, 3, 3, 4]) │
├───────────────────────────────┤
│                             4 │
└───────────────────────────────┘
```
