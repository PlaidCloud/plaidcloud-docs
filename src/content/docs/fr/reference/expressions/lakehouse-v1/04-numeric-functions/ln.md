---
title: LN (Lakehouse v1)
description: LN — renvoie le logarithme népérien de x, c'est-à-dire le logarithme en base e de x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/ln.md
---

Renvoie le logarithme népérien de `x`, c'est-à-dire le logarithme en base e de `x`. Si x est inférieur ou égal à 0.0E0, la fonction renvoie NULL.

## Analyze Syntax

```python
func.ln( <x> )
```

## Analyze Examples

```python
func.ln(2)

┌────────────────────┐
│     func.ln(2)     │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```

## SQL Syntax

```sql
LN( <x> )
```

## SQL Examples

```sql
SELECT LN(2);

┌────────────────────┐
│        ln(2)       │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```
