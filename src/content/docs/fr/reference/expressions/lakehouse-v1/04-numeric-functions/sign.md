---
title: SIGN (Lakehouse v1)
description: SIGN — renvoie le signe de l'argument sous la forme -1, 0 ou 1, selon que x est négatif, nul ou positif.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/sign.md
---

Renvoie le signe de l'argument sous la forme -1, 0 ou 1, selon que `x` est négatif, nul ou positif, ou NULL si l'argument est NULL.

## Syntaxe Analyze

```python
func.sign( <x> )
```

## Exemples Analyze

```python
func.sign(0)

┌──────────────┐
│ func.sign(0) │
├──────────────┤
│            0 │
└──────────────┘
```

## Syntaxe SQL

```sql
SIGN( <x> )
```

## Exemples SQL

```sql
SELECT SIGN(0);

┌─────────┐
│ sign(0) │
├─────────┤
│       0 │
└─────────┘
```
