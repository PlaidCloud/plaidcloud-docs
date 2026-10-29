---
title: ATAN (Lakehouse v2)
description: ATAN — renvoie l'arc tangente d'un nombre en radians.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/atan.md
---

Renvoie l'arc tangente d'un nombre en radians.

## Syntaxe Analyze

```python
func.atan(<x>)
```

## Exemples Analyze

```python
func.atan(1)

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```

## Syntaxe SQL

```sql
ATAN(<x>)
```

## Exemples SQL

```sql
SELECT ATAN(1);

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```
