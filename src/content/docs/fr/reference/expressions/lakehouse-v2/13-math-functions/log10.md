---
title: LOG10 (Lakehouse v2)
description: LOG10 — renvoie le logarithme en base 10 d'un nombre.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/log10.md
---

Renvoie le logarithme en base 10 d'un nombre.

## Syntaxe Analyze

```python
func.log10(<x>)
```

## Exemples Analyze

```python
func.log10(1000)

┌─────┐
│ 3.0  │
└─────┘
```

## Syntaxe SQL

```sql
LOG10(<x>)
```

## Exemples SQL

```sql
SELECT LOG10(1000);

┌─────┐
│ 3.0  │
└─────┘
```
