---
title: SIN (Lakehouse v2)
description: SIN — renvoie le sinus d'un nombre en radians.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sin.md
---

Renvoie le sinus d'un nombre en radians.

## Syntaxe Analyze

```python
func.sin(<x>)
```

## Exemples Analyze

```python
func.sin(0)

┌─────┐
│ 0.0  │
└─────┘
```

## Syntaxe SQL

```sql
SIN(<x>)
```

## Exemples SQL

```sql
SELECT SIN(0);

┌─────┐
│ 0.0  │
└─────┘
```
