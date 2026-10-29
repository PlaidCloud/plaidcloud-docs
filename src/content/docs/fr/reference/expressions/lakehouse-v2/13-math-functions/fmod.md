---
title: FMOD (Lakehouse v2)
description: FMOD — renvoie le reste à virgule flottante de la division de deux nombres.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/fmod.md
---

Renvoie le reste à virgule flottante de la division de deux nombres.

## Syntaxe Analyze

```python
func.fmod(<x>, <y>)
```

## Exemples Analyze

```python
func.fmod(10.5, 3.0)

┌─────┐
│ 1.5  │
└─────┘
```

## Syntaxe SQL

```sql
FMOD(<x>, <y>)
```

## Exemples SQL

```sql
SELECT FMOD(10.5, 3.0);

┌─────┐
│ 1.5  │
└─────┘
```
