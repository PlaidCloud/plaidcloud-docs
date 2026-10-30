---
title: ARRAY_REPEAT (Lakehouse v2)
description: ARRAY_REPEAT — tworzy tablicę zawierającą wskazany element powtórzony N razy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-repeat.md
---

Tworzy tablicę zawierającą wskazany element powtórzony N razy.

## Składnia Analyze

```python
func.array_repeat('x', 3)
```

## Przykłady Analyze

```python
func.array_repeat('x', 3)

┌───────────────┐
│ ['x','x','x'] │
└───────────────┘
```

## Składnia SQL

```sql
ARRAY_REPEAT('x', 3)
```

## Przykłady SQL

```sql
SELECT ARRAY_REPEAT('x', 3);

┌───────────────┐
│ ["x","x","x"] │
└───────────────┘
```
