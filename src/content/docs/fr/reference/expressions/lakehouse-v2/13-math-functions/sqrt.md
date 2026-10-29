---
title: SQRT (Lakehouse v2)
description: SQRT — renvoie la racine carrée d'un nombre.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sqrt.md
---

Renvoie la racine carrée d'un nombre.

## Syntaxe Analyze

```python
func.sqrt(<x>)
```

## Exemples Analyze

```python
func.sqrt(144)

┌──────┐
│ 12.0  │
└──────┘
```

## Syntaxe SQL

```sql
SQRT(<x>)
```

## Exemples SQL

```sql
SELECT SQRT(144);

┌──────┐
│ 12.0  │
└──────┘
```
