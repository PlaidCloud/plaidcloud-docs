---
title: CEILING (Lakehouse v2)
description: CEILING — renvoie le plus petit entier supérieur ou égal à un nombre. Alias de `CEIL`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/ceiling.md
---

Renvoie le plus petit entier supérieur ou égal à un nombre. Alias de `CEIL`.

## Syntaxe Analyze

```python
func.ceiling(<x>)
```

## Exemples Analyze

```python
func.ceiling(3.2)

┌───┐
│ 4  │
└───┘
```

## Syntaxe SQL

```sql
CEILING(<x>)
```

## Exemples SQL

```sql
SELECT CEILING(3.2);

┌───┐
│ 4  │
└───┘
```
