---
title: TAN (Lakehouse v2)
description: TAN — renvoie la tangente d'un nombre en radians.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/tan.md
---

Renvoie la tangente d'un nombre en radians.

## Syntaxe Analyze

```python
func.tan(<x>)
```

## Exemples Analyze

```python
func.tan(0)

┌─────┐
│ 0.0  │
└─────┘
```

## Syntaxe SQL

```sql
TAN(<x>)
```

## Exemples SQL

```sql
SELECT TAN(0);

┌─────┐
│ 0.0  │
└─────┘
```
