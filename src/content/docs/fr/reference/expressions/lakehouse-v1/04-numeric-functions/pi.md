---
title: PI (Lakehouse v1)
description: PI — renvoie la valeur de π sous forme de nombre à virgule flottante.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/pi.md
---

Renvoie la valeur de π sous forme de nombre à virgule flottante.

## Syntaxe Analyze

```python
func.pi()
```

## Exemples Analyze

```python
func.pi()

┌───────────────────┐
│     func.pi()     │
├───────────────────┤
│ 3.141592653589793 │
└───────────────────┘
```

## Syntaxe SQL

```sql
PI()
```

## Exemples SQL

```sql
SELECT PI();

┌───────────────────┐
│        pi()       │
├───────────────────┤
│ 3.141592653589793 │
└───────────────────┘
```
