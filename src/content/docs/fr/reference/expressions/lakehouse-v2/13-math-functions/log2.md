---
title: LOG2 (Lakehouse v2)
description: LOG2 — renvoie le logarithme en base 2 d'un nombre.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/log2.md
---

Renvoie le logarithme en base 2 d'un nombre.

## Syntaxe Analyze

```python
func.log2(<x>)
```

## Exemples Analyze

```python
func.log2(8)

┌─────┐
│ 3.0  │
└─────┘
```

## Syntaxe SQL

```sql
LOG2(<x>)
```

## Exemples SQL

```sql
SELECT LOG2(8);

┌─────┐
│ 3.0  │
└─────┘
```
