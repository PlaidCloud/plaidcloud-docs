---
title: ABS (Lakehouse v1)
description: ABS — renvoie la valeur absolue de x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/abs.md
---

Renvoie la valeur absolue de `x`.

## Syntaxe Analyze

```python
func.abs( <x> )
```

## Exemples Analyze

```python
func.abs((- 5))

┌─────────────────┐
│ func.abs((- 5)) │
├─────────────────┤
│               5 │
└─────────────────┘
```

## Syntaxe SQL

```sql
ABS( <x> )
```

## Exemples SQL

```sql
SELECT ABS(-5);

┌────────────┐
│ abs((- 5)) │
├────────────┤
│          5 │
└────────────┘
```
