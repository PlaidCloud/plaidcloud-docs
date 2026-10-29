---
title: COSH (Lakehouse v2)
description: COSH — renvoie le cosinus hyperbolique d'un nombre.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cosh.md
---

Renvoie le cosinus hyperbolique d'un nombre.

## Syntaxe Analyze

```python
func.cosh(<x>)
```

## Exemples Analyze

```python
func.cosh(0)

┌─────┐
│ 1.0  │
└─────┘
```

## Syntaxe SQL

```sql
COSH(<x>)
```

## Exemples SQL

```sql
SELECT COSH(0);

┌─────┐
│ 1.0  │
└─────┘
```
