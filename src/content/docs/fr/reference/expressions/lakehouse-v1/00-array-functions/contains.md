---
title: CONTAINS (Lakehouse v1)
description: "CONTAINS : vérifie si le tableau contient un élément donné."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/contains.md
---

Vérifie si le tableau contient un élément donné.


## Syntaxe Analyze

```python
func.contains( <array>, <element> )
```

## Exemples Analyze

```python
func.contains([1, 2], 1)

┌───────────────────────────┐
│ func.contains([1, 2], 1)  │
├───────────────────────────┤
│ true                      │
└───────────────────────────┘
```

## Syntaxe SQL

```sql
CONTAINS( <array>, <element> )
```

## Alias

- [ARRAY_CONTAINS](../array-contains)

## Exemples SQL

```sql
SELECT ARRAY_CONTAINS([1, 2], 1), CONTAINS([1, 2], 1);

┌─────────────────────────────────────────────────┐
│ array_contains([1, 2], 1) │ contains([1, 2], 1) │
├───────────────────────────┼─────────────────────┤
│ true                      │ true                │
└─────────────────────────────────────────────────┘
```
