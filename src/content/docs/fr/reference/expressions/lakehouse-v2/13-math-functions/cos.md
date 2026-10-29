---
title: COS (Lakehouse v2)
description: COS — renvoie le cosinus d'un nombre en radians.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cos.md
---

Renvoie le cosinus d'un nombre en radians.

## Syntaxe Analyze

```python
func.cos(<x>)
```

## Exemples Analyze

```python
func.cos(0)

┌─────┐
│ 1.0  │
└─────┘
```

## Syntaxe SQL

```sql
COS(<x>)
```

## Exemples SQL

```sql
SELECT COS(0);

┌─────┐
│ 1.0  │
└─────┘
```
