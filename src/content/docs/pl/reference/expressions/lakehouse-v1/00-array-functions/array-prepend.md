---
title: ARRAY_PREPEND (Lakehouse v1)
description: ARRAY_PREPEND — dodaje element na początku tablicy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-prepend.md
---

Dodaje element na początku tablicy.

## Składnia Analyze

```python
func.array_prepend( <element>, <array> )
```

## Przykłady Analyze

```python
func.array_prepend(1, [3, 4])

┌────────────────────────────────┐
│ func.array_prepend(1, [3, 4])  │
├────────────────────────────────┤
│ [1,3,4]                        │
└────────────────────────────────┘
```

## Składnia SQL

```sql
ARRAY_PREPEND( <element>, <array> )
```

## Przykłady SQL

```sql
SELECT ARRAY_PREPEND(1, [3, 4]);

┌──────────────────────────┐
│ array_prepend(1, [3, 4]) │
├──────────────────────────┤
│ [1,3,4]                  │
└──────────────────────────┘
```
