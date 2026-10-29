---
title: EXP (Lakehouse v2)
description: EXP — renvoie e élevé à la puissance d'un nombre.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/exp.md
---

Renvoie e élevé à la puissance d'un nombre.

## Syntaxe Analyze

```python
func.exp(<x>)
```

## Exemples Analyze

```python
func.exp(1)

┌───────────────────┐
│ 2.718281828459045  │
└───────────────────┘
```

## Syntaxe SQL

```sql
EXP(<x>)
```

## Exemples SQL

```sql
SELECT EXP(1);

┌───────────────────┐
│ 2.718281828459045  │
└───────────────────┘
```
