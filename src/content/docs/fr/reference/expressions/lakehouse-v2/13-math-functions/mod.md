---
title: MOD (Lakehouse v2)
description: MOD — renvoie le reste de la division de deux nombres.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/mod.md
---

Renvoie le reste de la division de deux nombres.

## Syntaxe Analyze

```python
func.mod(<x>, <y>)
```

## Exemples Analyze

```python
func.mod(10, 3)

┌───┐
│ 1  │
└───┘
```

## Syntaxe SQL

```sql
MOD(<x>, <y>)
```

## Exemples SQL

```sql
SELECT MOD(10, 3);

┌───┐
│ 1  │
└───┘
```
