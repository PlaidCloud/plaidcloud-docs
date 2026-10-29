---
title: FLOOR (Lakehouse v2)
description: FLOOR — renvoie le plus grand entier inférieur ou égal à un nombre.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/floor.md
---

Renvoie le plus grand entier inférieur ou égal à un nombre.

## Syntaxe Analyze

```python
func.floor(<x>)
```

## Exemples Analyze

```python
func.floor(3.7)

┌───┐
│ 3  │
└───┘
```

## Syntaxe SQL

```sql
FLOOR(<x>)
```

## Exemples SQL

```sql
SELECT FLOOR(3.7);

┌───┐
│ 3  │
└───┘
```
