---
title: LOG2 (Lakehouse v1)
description: LOG2 — renvoie le logarithme en base 2 de x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/log2.md
---

Renvoie le logarithme en base 2 de `x`. Si `x` est inférieur ou égal à 0.0E0, la fonction renvoie NULL.

## Syntaxe Analyze

```python
func.log2( <x> )
```

## Exemples Analyze

```python
func.log2(65536)

┌──────────────────┐
│ func.log2(65536) │
├──────────────────┤
│               16 │
└──────────────────┘
```

## Syntaxe SQL

```sql
LOG2( <x> )
```

## Exemples SQL

```sql
SELECT LOG2(65536);

┌─────────────┐
│ log2(65536) │
├─────────────┤
│          16 │
└─────────────┘
```
