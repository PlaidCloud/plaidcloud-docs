---
title: ISNULL (Lakehouse v2)
description: ISNULL — vérifie si une valeur est NULL. Renvoie 1 si elle est NULL, 0 sinon.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/isnull.md
---

Vérifie si une valeur est NULL. Renvoie 1 si elle est NULL, 0 sinon.

## Syntaxe Analyze

```python
func.isnull(<expr>)
```

## Exemples Analyze

```python
func.isnull(None)

┌───┐
│ 1  │
└───┘
```

## Syntaxe SQL

```sql
ISNULL(<expr>)
```

## Exemples SQL

```sql
SELECT ISNULL(NULL);

┌───┐
│ 1  │
└───┘
```
