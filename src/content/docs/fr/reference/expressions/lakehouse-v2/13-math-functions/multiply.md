---
title: MULTIPLY (Lakehouse v2)
description: MULTIPLY — renvoie le produit de deux nombres.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/multiply.md
---

Renvoie le produit de deux nombres.

## Syntaxe Analyze

```python
func.multiply(<x>, <y>)
```

## Exemples Analyze

```python
func.multiply(6, 7)

┌────┐
│ 42  │
└────┘
```

## Syntaxe SQL

```sql
MULTIPLY(<x>, <y>)
```

## Exemples SQL

```sql
SELECT MULTIPLY(6, 7);

┌────┐
│ 42  │
└────┘
```
