---
title: ARRAY_LENGTH (Lakehouse v1)
description: ARRAY_LENGTH — zwraca długość tablicy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-length.md
---

Zwraca długość tablicy.

## Składnia Analyze

```python
func.array_length( <array> )
```

## Przykłady Analyze

```python
func.array_length([1, 2])

┌────────────────────────────┐
│ func.array_length([1, 2])  │
├────────────────────────────┤
│                          2 │
└────────────────────────────┘
```

## Składnia SQL

```sql
ARRAY_LENGTH( <array> )
```

## Przykłady SQL

```sql
SELECT ARRAY_LENGTH([1, 2]);

┌──────────────────────┐
│ array_length([1, 2]) │
├──────────────────────┤
│                    2 │
└──────────────────────┘
```
