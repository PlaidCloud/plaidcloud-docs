---
title: "GET (Array, Lakehouse v1)"
description: GET — devuelve un elemento de un arreglo según su índice (base 1).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/get.md
---

Devuelve un elemento de un arreglo según su índice (base 1).

## Sintaxis de Analyze

```python
func.get( <array>, <index> )
```

## Ejemplos de Analyze

```python
func.get([1, 2], 2)

┌─────────────────────┐
│ func.get([1, 2], 2) │
├─────────────────────┤
│                   2 │
└─────────────────────┘
```

## Sintaxis de SQL

```sql
GET( <array>, <index> )
```

## Alias

- [ARRAY_GET](../array-get)

## Ejemplos de SQL

```sql
SELECT GET([1, 2], 2), ARRAY_GET([1, 2], 2);

┌───────────────────────────────────────┐
│ get([1, 2], 2) │ array_get([1, 2], 2) │
├────────────────┼──────────────────────┤
│              2 │                    2 │
└───────────────────────────────────────┘
```
