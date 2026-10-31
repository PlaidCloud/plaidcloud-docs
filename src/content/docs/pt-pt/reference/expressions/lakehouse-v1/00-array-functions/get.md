---
title: "GET (matriz, Lakehouse v1)"
description: GET — devolve um elemento de uma matriz pelo índice (com base 1).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/get.md
---

Devolve um elemento de uma matriz pelo índice (com base 1).

## Sintaxe do Analyze

```python
func.get( <array>, <index> )
```

## Exemplos do Analyze

```python
func.get([1, 2], 2)

┌─────────────────────┐
│ func.get([1, 2], 2) │
├─────────────────────┤
│                   2 │
└─────────────────────┘
```

## Sintaxe SQL

```sql
GET( <array>, <index> )
```

## Alias

- [ARRAY_GET](../array-get)

## Exemplos SQL

```sql
SELECT GET([1, 2], 2), ARRAY_GET([1, 2], 2);

┌───────────────────────────────────────┐
│ get([1, 2], 2) │ array_get([1, 2], 2) │
├────────────────┼──────────────────────┤
│              2 │                    2 │
└───────────────────────────────────────┘
```
