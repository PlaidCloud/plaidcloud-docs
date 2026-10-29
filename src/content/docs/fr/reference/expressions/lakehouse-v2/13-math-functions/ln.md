---
title: LN (Lakehouse v2)
description: LN — renvoie le logarithme népérien d'un nombre.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/ln.md
---

Renvoie le logarithme népérien d'un nombre.

## Syntaxe Analyze

```python
func.ln(<x>)
```

## Exemples Analyze

```python
func.ln(2.718281828459045)

┌─────┐
│ 1.0  │
└─────┘
```

## Syntaxe SQL

```sql
LN(<x>)
```

## Exemples SQL

```sql
SELECT LN(EXP(1));

┌─────┐
│ 1.0  │
└─────┘
```
