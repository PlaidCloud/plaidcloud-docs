---
title: ARRAY_LENGTH (Lakehouse v1)
description: "ARRAY_LENGTH : renvoie la longueur d'un tableau."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-length.md
---

Renvoie la longueur d'un tableau.

## Syntaxe Analyze

```python
func.array_length( <array> )
```

## Exemples Analyze

```python
func.array_length([1, 2])

┌────────────────────────────┐
│ func.array_length([1, 2])  │
├────────────────────────────┤
│                          2 │
└────────────────────────────┘
```

## Syntaxe SQL

```sql
ARRAY_LENGTH( <array> )
```

## Exemples SQL

```sql
SELECT ARRAY_LENGTH([1, 2]);

┌──────────────────────┐
│ array_length([1, 2]) │
├──────────────────────┤
│                    2 │
└──────────────────────┘
```
