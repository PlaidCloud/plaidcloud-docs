---
title: SM3 (Lakehouse v2)
description: SM3 — renvoie le hachage SM3 d'une chaîne.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/sm3.md
---

Renvoie le hachage SM3 d'une chaîne.

## Syntaxe Analyze

```python
func.sm3(<str>)
```

## Exemples Analyze

```python
func.sm3('hello')

┌───────────────┐
│ 'becbbfaa...'  │
└───────────────┘
```

## Syntaxe SQL

```sql
SM3(<str>)
```

## Exemples SQL

```sql
SELECT SM3('hello');

┌──────────────────────────────────────────────────────────────────┐
│ becbbfaae6548b8bf0cfcad5a27183cd1be6093b1cceccc303d9c61d0a645268  │
└──────────────────────────────────────────────────────────────────┘
```
