---
title: DIVIDE (Lakehouse v2)
description: DIVIDE — renvoie le résultat de la division d'un nombre par un autre.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/divide.md
---

Renvoie le résultat de la division d'un nombre par un autre.

## Syntaxe Analyze

```python
func.divide(<x>, <y>)
```

## Exemples Analyze

```python
func.divide(10, 3)

┌────────────────────┐
│ 3.3333333333333335  │
└────────────────────┘
```

## Syntaxe SQL

```sql
DIVIDE(<x>, <y>)
```

## Exemples SQL

```sql
SELECT DIVIDE(10, 3);

┌────────────────────┐
│ 3.3333333333333335  │
└────────────────────┘
```
