---
title: "GET (Array, Lakehouse v1)"
description: GET – gibt ein Element eines Arrays anhand des Index zurück (1-basiert).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/get.md
---

Gibt ein Element eines Arrays anhand des Index zurück (1-basiert).

## Analyze-Syntax

```python
func.get( <array>, <index> )
```

## Analyze-Beispiele

```python
func.get([1, 2], 2)

┌─────────────────────┐
│ func.get([1, 2], 2) │
├─────────────────────┤
│                   2 │
└─────────────────────┘
```

## SQL-Syntax

```sql
GET( <array>, <index> )
```

## Aliasse

- [ARRAY_GET](../array-get)

## SQL-Beispiele

```sql
SELECT GET([1, 2], 2), ARRAY_GET([1, 2], 2);

┌───────────────────────────────────────┐
│ get([1, 2], 2) │ array_get([1, 2], 2) │
├────────────────┼──────────────────────┤
│              2 │                    2 │
└───────────────────────────────────────┘
```
