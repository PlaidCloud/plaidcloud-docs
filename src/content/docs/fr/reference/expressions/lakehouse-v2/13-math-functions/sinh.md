---
title: SINH (Lakehouse v2)
description: SINH — renvoie le sinus hyperbolique d'un nombre.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sinh.md
---

Renvoie le sinus hyperbolique d'un nombre.

## Syntaxe Analyze

```python
func.sinh(<x>)
```

## Exemples Analyze

```python
func.sinh(0)

┌─────┐
│ 0.0  │
└─────┘
```

## Syntaxe SQL

```sql
SINH(<x>)
```

## Exemples SQL

```sql
SELECT SINH(0);

┌─────┐
│ 0.0  │
└─────┘
```
