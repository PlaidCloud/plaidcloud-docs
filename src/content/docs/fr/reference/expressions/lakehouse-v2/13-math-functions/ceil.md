---
title: CEIL (Lakehouse v2)
description: CEIL — renvoie le plus petit entier supérieur ou égal à un nombre.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/ceil.md
---

Renvoie le plus petit entier supérieur ou égal à un nombre.

## Syntaxe Analyze

```python
func.ceil(<x>)
```

## Exemples Analyze

```python
func.ceil(3.2)

┌───┐
│ 4  │
└───┘
```

## Syntaxe SQL

```sql
CEIL(<x>)
```

## Exemples SQL

```sql
SELECT CEIL(3.2);

┌───┐
│ 4  │
└───┘
```
