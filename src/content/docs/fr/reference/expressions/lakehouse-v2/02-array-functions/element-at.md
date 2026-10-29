---
title: "ELEMENT_AT (tableau, Lakehouse v2)"
description: ELEMENT_AT — renvoie l'élément situé à une position donnée dans un tableau (indexation à partir de 1).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/element-at.md
---

Renvoie l'élément situé à une position donnée dans un tableau (indexation à partir de 1).

## Syntaxe Analyze

```python
func.element_at([10, 20, 30], 2)
```

## Exemples Analyze

```python
func.element_at([10, 20, 30], 2)

┌────┐
│ 20 │
└────┘
```

## Syntaxe SQL

```sql
ELEMENT_AT([10, 20, 30], 2)
```

## Exemples SQL

```sql
SELECT ELEMENT_AT([10, 20, 30], 2);

┌────┐
│ 20 │
└────┘
```
