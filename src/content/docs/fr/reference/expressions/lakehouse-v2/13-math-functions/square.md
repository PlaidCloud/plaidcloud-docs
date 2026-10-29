---
title: SQUARE (Lakehouse v2)
description: SQUARE — renvoie le carré d'un nombre.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/square.md
---

Renvoie le carré d'un nombre.

## Syntaxe Analyze

```python
func.square(<x>)
```

## Exemples Analyze

```python
func.square(7)

┌────┐
│ 49  │
└────┘
```

## Syntaxe SQL

```sql
SQUARE(<x>)
```

## Exemples SQL

```sql
SELECT SQUARE(7);

┌────┐
│ 49  │
└────┘
```
