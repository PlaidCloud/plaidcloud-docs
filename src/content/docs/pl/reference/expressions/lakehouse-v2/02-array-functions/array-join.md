---
title: ARRAY_JOIN (Lakehouse v2)
description: ARRAY_JOIN — Łączy elementy tablicy w ciąg znaków przy użyciu separatora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-join.md
---

Łączy elementy tablicy w ciąg znaków przy użyciu separatora.

## Składnia Analyze

```python
func.array_join([1,2,3], '-')
```

## Przykłady Analyze

```python
func.array_join(['a', 'b', 'c'], '-')

┌─────────┐
│ 'a-b-c' │
└─────────┘
```

## Składnia SQL

```sql
ARRAY_JOIN([1,2,3], '-')
```

## Przykłady SQL

```sql
SELECT ARRAY_JOIN(['a', 'b', 'c'], '-');

┌───────┐
│ a-b-c │
└───────┘
```
