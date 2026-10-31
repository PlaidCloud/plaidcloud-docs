---
title: ABS (Lakehouse v2)
description: ABS — renvoie la valeur absolue d'un nombre.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/abs.md
---

Renvoie la valeur absolue d'un nombre.

## Syntaxe Analyze

```python
func.abs(<x>)
```

## Exemples Analyze

```python
func.abs(-5)

┌───┐
│ 5  │
└───┘
```

## Syntaxe SQL

```sql
ABS(<x>)
```

## Exemples SQL

```sql
SELECT ABS(-5);

┌───┐
│ 5  │
└───┘
```
