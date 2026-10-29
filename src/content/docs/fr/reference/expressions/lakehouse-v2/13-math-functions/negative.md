---
title: NEGATIVE (Lakehouse v2)
description: NEGATIVE — renvoie l'opposé d'un nombre.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/negative.md
---

Renvoie l'opposé d'un nombre.

## Syntaxe Analyze

```python
func.negative(<x>)
```

## Exemples Analyze

```python
func.negative(5)

┌────┐
│ -5  │
└────┘
```

## Syntaxe SQL

```sql
NEGATIVE(<x>)
```

## Exemples SQL

```sql
SELECT NEGATIVE(5);

┌────┐
│ -5  │
└────┘
```
