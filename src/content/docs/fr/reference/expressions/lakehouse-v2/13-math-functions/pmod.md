---
title: PMOD (Lakehouse v2)
description: PMOD — renvoie le modulo positif de la division de deux nombres.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/pmod.md
---

Renvoie le modulo positif de la division de deux nombres.

## Syntaxe Analyze

```python
func.pmod(<x>, <y>)
```

## Exemples Analyze

```python
func.pmod(-10, 3)

┌───┐
│ 2  │
└───┘
```

## Syntaxe SQL

```sql
PMOD(<x>, <y>)
```

## Exemples SQL

```sql
SELECT PMOD(-10, 3);

┌───┐
│ 2  │
└───┘
```
