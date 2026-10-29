---
title: LOG(x) (Lakehouse v1)
description: LOG(x) — renvoie le logarithme népérien de x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/logx.md
---

Renvoie le logarithme népérien de `x`. Si x est inférieur ou égal à 0.0E0, la fonction renvoie NULL.

## Syntaxe Analyze

```python
 func.log( <x> )
```

## Exemples Analyze

```python
 func.log(2)

┌────────────────────┐
│    func.log(2)     │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```

## Syntaxe SQL

```sql
LOG( <x> )
```

## Exemples SQL

```sql
SELECT LOG(2);

┌────────────────────┐
│       log(2)       │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```
