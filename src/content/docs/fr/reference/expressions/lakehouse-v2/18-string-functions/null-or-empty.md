---
title: NULL_OR_EMPTY (Lakehouse v2)
description: NULL_OR_EMPTY — vérifie si une chaîne est NULL ou vide. Renvoie 1 si c'est le cas, 0 sinon.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/null-or-empty.md
---

Vérifie si une chaîne est NULL ou vide. Renvoie 1 si c'est le cas, 0 sinon.

## Syntaxe Analyze

```python
func.null_or_empty(<str>)
```

## Exemples Analyze

```python
func.null_or_empty('')

┌───┐
│ 1  │
└───┘
```

## Syntaxe SQL

```sql
NULL_OR_EMPTY(<str>)
```

## Exemples SQL

```sql
SELECT NULL_OR_EMPTY('');

┌───┐
│ 1  │
└───┘
```
