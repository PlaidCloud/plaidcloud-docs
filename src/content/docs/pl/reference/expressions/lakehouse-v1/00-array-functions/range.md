---
title: RANGE (Lakehouse v1)
description: RANGE — zwraca tablicę zebraną z przedziału [start, end).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/range.md
---

Zwraca tablicę zebraną z przedziału [start, end).

## Składnia Analyze

```python
func.range( <start>, <end> )
```

## Przykłady Analyze

```python
func.range(1, 5)

┌────────────────────┐
│  func.range(1, 5)  │
├────────────────────┤
│ [1,2,3,4]          │
└────────────────────┘
```

## Składnia SQL

```sql
RANGE( <start>, <end> )
```

## Przykłady SQL

```sql
SELECT RANGE(1, 5);

┌───────────────┐
│  range(1, 5)  │
├───────────────┤
│ [1,2,3,4]     │
└───────────────┘
```
