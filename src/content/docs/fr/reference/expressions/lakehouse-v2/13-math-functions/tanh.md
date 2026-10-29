---
title: TANH (Lakehouse v2)
description: TANH — renvoie la tangente hyperbolique d'un nombre.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/tanh.md
---

Renvoie la tangente hyperbolique d'un nombre.

## Syntaxe Analyze

```python
func.tanh(<x>)
```

## Exemples Analyze

```python
func.tanh(0)

┌─────┐
│ 0.0  │
└─────┘
```

## Syntaxe SQL

```sql
TANH(<x>)
```

## Exemples SQL

```sql
SELECT TANH(0);

┌─────┐
│ 0.0  │
└─────┘
```
