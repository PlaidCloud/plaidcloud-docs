---
title: ARRAY_APPEND (Lakehouse v2)
description: ARRAY_APPEND — dołącza element na końcu tablicy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-append.md
---

Dołącza element na końcu tablicy.

## Składnia Analyze

```python
func.array_append([1, 2, 3], 4)
```

## Przykłady Analyze

```python
func.array_append([1, 2, 3], 4)

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```

## Składnia SQL

```sql
ARRAY_APPEND([1, 2, 3], 4)
```

## Przykłady SQL

```sql
SELECT ARRAY_APPEND([1, 2, 3], 4);

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```
