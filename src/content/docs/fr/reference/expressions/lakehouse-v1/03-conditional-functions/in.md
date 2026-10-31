---
title: "[ NOT ] IN (Lakehouse v1)"
description: "[ NOT ] IN — vrai si une valeur est égale (ou non) à un élément d'une liste explicite."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/in.md
---

Vérifie si une valeur figure (ou non) dans une liste explicite.

## Syntaxe Analyze

```python
table.columns.in_((<value1>, <value2> ...))
```

## Exemples Analyze

```python
table.columns.in_((<value1>, <value2> ...))

┌──────────────────────────┐
│ table.column.in_((2, 3)) │
├──────────────────────────┤
│ true                     │
└──────────────────────────┘
```

## Syntaxe SQL

```sql
<value> [ NOT ] IN (<value1>, <value2> ...)
```

## Exemples SQL

```sql
SELECT 1 NOT IN (2, 3);

┌────────────────┐
│ 1 not in(2, 3) │
├────────────────┤
│ true           │
└────────────────┘
```
