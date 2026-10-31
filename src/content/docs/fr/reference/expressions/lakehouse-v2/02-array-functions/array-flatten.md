---
title: ARRAY_FLATTEN (Lakehouse v2)
description: ARRAY_FLATTEN — aplatit des tableaux imbriqués en un tableau à un seul niveau.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-flatten.md
---

Aplatit des tableaux imbriqués en un tableau à un seul niveau.

## Syntaxe Analyze

```python
func.array_flatten([[1,2],[3,4]])
```

## Exemples Analyze

```python
func.array_flatten([[1, 2], [3, 4]])

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```

## Syntaxe SQL

```sql
ARRAY_FLATTEN([[1,2],[3,4]])
```

## Exemples SQL

```sql
SELECT ARRAY_FLATTEN([[1, 2], [3, 4]]);

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```
