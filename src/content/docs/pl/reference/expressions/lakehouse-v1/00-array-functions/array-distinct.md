---
title: ARRAY_DISTINCT (Lakehouse v1)
description: ARRAY_DISTINCT — usuwa z tablicy wszystkie duplikaty i wartości NULL bez zachowania pierwotnej kolejności.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-distinct.md
---

Usuwa z tablicy wszystkie duplikaty i wartości NULL bez zachowania pierwotnej kolejności.

## Składnia Analyze

```python
func.array_distinct( <array> )
```

## Przykłady Analyze

```python
func.array_distinct([1, 2, 2, 4, 3])

┌───────────────────────────────────────┐
│ func.array_distinct([1, 2, 2, 4, 3])  │
├───────────────────────────────────────┤
│ [1,2,4,3]                             │
└───────────────────────────────────────┘
```

## Składnia SQL

```sql
ARRAY_DISTINCT( <array> )
```

## Przykłady SQL

```sql
SELECT ARRAY_DISTINCT([1, 2, 2, 4, 3]);

┌─────────────────────────────────┐
│ array_distinct([1, 2, 2, 4, 3]) │
├─────────────────────────────────┤
│ [1,2,4,3]                       │
└─────────────────────────────────┘
```
