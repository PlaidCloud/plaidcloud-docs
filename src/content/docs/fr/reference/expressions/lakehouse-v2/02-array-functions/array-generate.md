---
title: ARRAY_GENERATE (Lakehouse v2)
description: ARRAY_GENERATE — génère un tableau de valeurs séquentielles.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-generate.md
---

Génère un tableau de valeurs séquentielles.

## Syntaxe Analyze

```python
func.array_generate(1, 5)
```

## Exemples Analyze

```python
func.array_generate(1, 5)

┌─────────────┐
│ [1,2,3,4,5] │
└─────────────┘
```

## Syntaxe SQL

```sql
ARRAY_GENERATE(1, 5)
```

## Exemples SQL

```sql
SELECT ARRAY_GENERATE(1, 5);

┌─────────────┐
│ [1,2,3,4,5] │
└─────────────┘
```
