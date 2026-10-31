---
title: CBRT (Lakehouse v1)
description: CBRT — renvoie la racine cubique d'un nombre positif ou nul x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/cbrt.md
---

Renvoie la racine cubique d'un nombre positif ou nul `x`.

## Syntaxe Analyze

```python
func.cbrt( <x> )
```

## Exemples Analyze

```python
func.cbrt(27)

┌───────────────┐
│ func.cbrt(27) │
├───────────────┤
│             3 │
└───────────────┘
```

## Syntaxe SQL

```sql
CBRT( <x> )
```

## Exemples SQL

```sql
SELECT CBRT(27);

┌──────────┐
│ cbrt(27) │
├──────────┤
│        3 │
└──────────┘
```
