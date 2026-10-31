---
title: ATAN (Lakehouse v1)
description: ATAN — renvoie l'arc tangente de x, c'est-à-dire la valeur dont la tangente est x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/atan.md
---

Renvoie l'arc tangente de `x`, c'est-à-dire la valeur dont la tangente est `x`.

## Syntaxe Analyze

```python
func.atan( <x> )
```

## Exemples Analyze

```python
func.atan(-2)

┌─────────────────────┐
│  func.atan((- 2))   │
├─────────────────────┤
│ -1.1071487177940906 │
└─────────────────────┘
```

## Syntaxe SQL

```sql
ATAN( <x> )
```

## Exemples SQL

```sql
SELECT ATAN(-2);

┌─────────────────────┐
│     atan((- 2))     │
├─────────────────────┤
│ -1.1071487177940906 │
└─────────────────────┘
```
