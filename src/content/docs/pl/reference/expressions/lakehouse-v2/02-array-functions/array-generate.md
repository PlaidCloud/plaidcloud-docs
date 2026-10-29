---
title: ARRAY_GENERATE (Lakehouse v2)
description: ARRAY_GENERATE — generuje tablicę kolejnych wartości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-generate.md
---

Generuje tablicę kolejnych wartości.

## Składnia Analyze

```python
func.array_generate(1, 5)
```

## Przykłady Analyze

```python
func.array_generate(1, 5)

┌─────────────┐
│ [1,2,3,4,5] │
└─────────────┘
```

## Składnia SQL

```sql
ARRAY_GENERATE(1, 5)
```

## Przykłady SQL

```sql
SELECT ARRAY_GENERATE(1, 5);

┌─────────────┐
│ [1,2,3,4,5] │
└─────────────┘
```
