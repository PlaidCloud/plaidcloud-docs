---
title: GREATEST (Lakehouse v1)
description: GREATEST — renvoie la valeur maximale d'un ensemble de valeurs.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/greatest.md
---

Renvoie la valeur maximale d'un ensemble de valeurs.

## Syntaxe Analyze

```python
func.greatest(<value1>, <value2> ...)
```

## Exemples Analyze

```python
func.greatest((5, 9, 4))

┌──────────────────────────┐
│ func.greatest((5, 9, 4)) │
├──────────────────────────┤
│                        9 │
└──────────────────────────┘
```

## Syntaxe SQL

```sql
GREATEST(<value1>, <value2> ...)
```

## Exemples SQL

```sql
SELECT GREATEST(5, 9, 4);

┌───────────────────┐
│ greatest(5, 9, 4) │
├───────────────────┤
│                 9 │
└───────────────────┘
```
