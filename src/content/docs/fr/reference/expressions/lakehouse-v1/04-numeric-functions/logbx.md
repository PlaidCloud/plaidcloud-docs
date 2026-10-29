---
title: "LOG(b, x) (Lakehouse v1)"
description: LOG(b, x) — renvoie le logarithme en base b de x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/logbx.md
---

Renvoie le logarithme en base b de `x`. Si `x` est inférieur ou égal à 0.0E0, la fonction renvoie NULL.

## Syntaxe Analyze

```python
func.log( <b, x> )
```

## Exemples Analyze

```python
func.log(2, 65536)

┌────────────────────┐
│ func.log(2, 65536) │
├────────────────────┤
│                 16 │
└────────────────────┘
```

## Syntaxe SQL

```sql
LOG( <b, x> )
```

## Exemples SQL

```sql
SELECT LOG(2, 65536);

┌───────────────┐
│ log(2, 65536) │
├───────────────┤
│            16 │
└───────────────┘
```
