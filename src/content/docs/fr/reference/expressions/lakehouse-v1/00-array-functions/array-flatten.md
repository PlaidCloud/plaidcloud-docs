---
title: ARRAY_FLATTEN (Lakehouse v1)
description: "ARRAY_FLATTEN : aplatit des tableaux imbriqués pour les convertir en un tableau à un seul niveau."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-flatten.md
---

Aplatit des tableaux imbriqués pour les convertir en un tableau à un seul niveau.

## Syntaxe Analyze

```python
func.array_flatten( <array> )
```

## Exemples Analyze

```python
func.array_flatten([[1, 2], [3, 4, 5]]) 

┌──────────────────────────────────────────┐
│ func.array_flatten([[1, 2], [3, 4, 5]])  │
├──────────────────────────────────────────┤
│ [1,2,3,4,5]                              │
└──────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
ARRAY_FLATTEN( <array> )
```

## Exemples SQL

```sql
SELECT ARRAY_FLATTEN([[1,2], [3,4,5]]);

┌────────────────────────────────────┐
│ array_flatten([[1, 2], [3, 4, 5]]) │
├────────────────────────────────────┤
│ [1,2,3,4,5]                        │
└────────────────────────────────────┘
```
