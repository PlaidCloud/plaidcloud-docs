---
title: SIGN (Lakehouse v2)
description: "SIGN — renvoie le signe d'un nombre : -1, 0 ou 1."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sign.md
---

Renvoie le signe d'un nombre : -1, 0 ou 1.

## Syntaxe Analyze

```python
func.sign(<x>)
```

## Exemples Analyze

```python
func.sign(-42)

┌────┐
│ -1  │
└────┘
```

## Syntaxe SQL

```sql
SIGN(<x>)
```

## Exemples SQL

```sql
SELECT SIGN(-42);

┌────┐
│ -1  │
└────┘
```
