---
title: CBRT (Lakehouse v2)
description: CBRT — renvoie la racine cubique d'un nombre.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cbrt.md
---

Renvoie la racine cubique d'un nombre.

## Syntaxe Analyze

```python
func.cbrt(<x>)
```

## Exemples Analyze

```python
func.cbrt(27)

┌─────┐
│ 3.0  │
└─────┘
```

## Syntaxe SQL

```sql
CBRT(<x>)
```

## Exemples SQL

```sql
SELECT CBRT(27);

┌─────┐
│ 3.0  │
└─────┘
```
