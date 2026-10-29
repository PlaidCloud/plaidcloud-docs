---
title: OCT (Lakehouse v1)
description: OCT renvoie la représentation sous forme de chaîne de la valeur octale de N.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/oct.md
---

Renvoie la représentation sous forme de chaîne de la valeur octale de N.

## Syntaxe Analyze

```python
func.oct(<expr>)
```

## Exemples Analyze

```python
func.oct(12)
┌─────────────────┐
│ func.oct(12)    │
├─────────────────┤
│ 014             │
└─────────────────┘
```

## Syntaxe SQL

```sql
OCT(<expr>)
```

## Exemples SQL

```sql
SELECT OCT(12);
┌─────────┐
│ OCT(12) │
├─────────┤
│ 014     │
└─────────┘
```
