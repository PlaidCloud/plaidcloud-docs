---
title: COT (Lakehouse v2)
description: COT — renvoie la cotangente d'un nombre en radians.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cot.md
---

Renvoie la cotangente d'un nombre en radians.

## Syntaxe Analyze

```python
func.cot(<x>)
```

## Exemples Analyze

```python
func.cot(1)

┌────────────────────┐
│ 0.6420926159343306  │
└────────────────────┘
```

## Syntaxe SQL

```sql
COT(<x>)
```

## Exemples SQL

```sql
SELECT COT(1);

┌────────────────────┐
│ 0.6420926159343306  │
└────────────────────┘
```
