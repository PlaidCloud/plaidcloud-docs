---
title: ARRAY_REPEAT (Lakehouse v2)
description: ARRAY_REPEAT — crée un tableau contenant un élément donné répété N fois.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-repeat.md
---

Crée un tableau contenant un élément donné répété N fois.

## Syntaxe Analyze

```python
func.array_repeat('x', 3)
```

## Exemples Analyze

```python
func.array_repeat('x', 3)

┌───────────────┐
│ ['x','x','x'] │
└───────────────┘
```

## Syntaxe SQL

```sql
ARRAY_REPEAT('x', 3)
```

## Exemples SQL

```sql
SELECT ARRAY_REPEAT('x', 3);

┌───────────────┐
│ ["x","x","x"] │
└───────────────┘
```
