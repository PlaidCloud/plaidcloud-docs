---
title: ISNOTNULL (Lakehouse v2)
description: ISNOTNULL — vérifie si une valeur n'est pas NULL. Renvoie 1 si elle n'est pas NULL, 0 sinon.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/isnotnull.md
---

Vérifie si une valeur n'est pas NULL. Renvoie 1 si elle n'est pas NULL, 0 sinon.

## Syntaxe Analyze

```python
func.isnotnull(<expr>)
```

## Exemples Analyze

```python
func.isnotnull(1)

┌───┐
│ 1  │
└───┘
```

## Syntaxe SQL

```sql
ISNOTNULL(<expr>)
```

## Exemples SQL

```sql
SELECT ISNOTNULL(1);

┌───┐
│ 1  │
└───┘
```
