---
title: LOG10 (Lakehouse v1)
description: LOG10 — renvoie le logarithme décimal (base 10) de x. Référence.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/log10.md
---

Renvoie le logarithme décimal (base 10) de `x`. Si `x` est inférieur ou égal à 0.0E0, la fonction renvoie NULL.


## Syntaxe Analyze

```python
func.log10( <x> )
```

## Exemples Analyze

```python
func.log10(100)

┌─────────────────┐
│ func.log10(100) │
├─────────────────┤
│               2 │
└─────────────────┘
```

## Syntaxe SQL

```sql
LOG10( <x> )
```

## Exemples SQL

```sql
SELECT LOG10(100);

┌────────────┐
│ log10(100) │
├────────────┤
│          2 │
└────────────┘
```
