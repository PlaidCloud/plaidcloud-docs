---
title: "GET (tableau, Lakehouse v1)"
description: "GET : renvoie un élément d'un tableau à partir de son indice (base 1)."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/get.md
---

Renvoie un élément d'un tableau à partir de son indice (base 1).

## Syntaxe Analyze

```python
func.get( <array>, <index> )
```

## Exemples Analyze

```python
func.get([1, 2], 2)

┌─────────────────────┐
│ func.get([1, 2], 2) │
├─────────────────────┤
│                   2 │
└─────────────────────┘
```

## Syntaxe SQL

```sql
GET( <array>, <index> )
```

## Alias

- [ARRAY_GET](../array-get)

## Exemples SQL

```sql
SELECT GET([1, 2], 2), ARRAY_GET([1, 2], 2);

┌───────────────────────────────────────┐
│ get([1, 2], 2) │ array_get([1, 2], 2) │
├────────────────┼──────────────────────┤
│              2 │                    2 │
└───────────────────────────────────────┘
```
