---
title: ARRAY_TRANSFORM (Lakehouse v1)
description: "ARRAY_TRANSFORM : renvoie un tableau résultant de l'application de la fonction lambda à chaque élément du tableau d'entrée."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-transform.md
---

Renvoie un tableau résultant de l'application de la fonction lambda à chaque élément du tableau d'entrée.

## Syntaxe Analyze

```python
func.array_transform( <array>, <lambda> )
```

## Exemples Analyze

```python
func.array_transform([1, 2, 3], x -> (x + 1))

┌───────────────────────────────────────────────┐
│ func.array_transform([1, 2, 3], x -> (x + 1)) │
├───────────────────────────────────────────────┤
│ [2,3,4]                                       │
└───────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
ARRAY_TRANSFORM( <array>, <lambda> )
```

## Alias

- [ARRAY_APPLY](../array-apply)

## Exemples SQL

```sql
SELECT ARRAY_TRANSFORM([1, 2, 3], x -> x + 1);

┌──────────────────────────────────────────┐
│ array_transform([1, 2, 3], x -> (x + 1)) │
├──────────────────────────────────────────┤
│ [2,3,4]                                  │
└──────────────────────────────────────────┘
```
