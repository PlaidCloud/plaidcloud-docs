---
title: POSITIVE (Lakehouse v2)
description: POSITIVE — renvoie la valeur inchangée (plus unaire).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/positive.md
---

Renvoie la valeur inchangée (plus unaire).

## Syntaxe Analyze

```python
func.positive(<x>)
```

## Exemples Analyze

```python
func.positive(-5)

┌────┐
│ -5  │
└────┘
```

## Syntaxe SQL

```sql
POSITIVE(<x>)
```

## Exemples SQL

```sql
SELECT POSITIVE(-5);

┌────┐
│ -5  │
└────┘
```
